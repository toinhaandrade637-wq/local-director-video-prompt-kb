$ErrorActionPreference='Stop'
$taskRoot='D:/seedance2.5提示词及结构'
$taskReadDir=Join-Path $taskRoot '资料库/03_官方参考/在线研读_2026-10-15'
$taskUtf8=[System.Text.UTF8Encoding]::new($false)
[void][System.IO.Directory]::CreateDirectory($taskReadDir)
$taskSources=@(
    @{id='O001';name='即梦使用手册';url='https://bytedance.larkoffice.com/wiki/RXh5ww6EqighMdkVTMccm2d4n7e'},
    @{id='O002';name='小云雀手册';url='https://bytedance.larkoffice.com/wiki/W5tHwoZIDi12dbk2z3KcFkuUnsf'},
    @{id='O003';name='提示词撰写指南';url='https://bytedance.larkoffice.com/docx/OsiUdR1OxoDqvnxsK8LczYx7nPd'},
    @{id='O004';name='企业级业务场景实践指南';url='https://bytedance.larkoffice.com/wiki/Tyi1woQAgiZlkhkWGnYcF2Cun3e'}
)
function Save-ReadFile([string]$Path,[string]$Text){
    if(Test-Path -LiteralPath $Path){
        if(-not [string]::Equals([System.IO.File]::ReadAllText($Path),$Text,[System.StringComparison]::Ordinal)){throw "Existing read artifact differs: $Path"}
    }else{[System.IO.File]::WriteAllText($Path,$Text,$taskUtf8)}
}
$taskManifest=@()
foreach($taskSource in $taskSources){
    $taskResponseLines=& lark-cli.cmd docs +fetch --doc $taskSource.url --doc-format markdown --as user
    if($LASTEXITCODE -ne 0){throw "Online fetch failed: $($taskSource.id)"}
    $taskResponse=($taskResponseLines -join "`n")|ConvertFrom-Json
    if($taskResponse.ok -ne $true){throw 'No successful document envelope.'}
    $taskDoc=$taskResponse.data.document
    $taskRaw=[string]$taskDoc.content
    if([string]::IsNullOrWhiteSpace($taskRaw)){throw 'Empty body.'}
    $taskBase="$($taskSource.id)_r$($taskDoc.revision_id)"
    Save-ReadFile (Join-Path $taskReadDir ($taskBase+'_正文.md')) $taskRaw
    Save-ReadFile (Join-Path $taskReadDir ($taskBase+'_文档.json')) ($taskDoc|ConvertTo-Json -Depth 80)

    # 只移除排版与媒体属性；保留正文、表格文字、代码内容、链接名与提示词占位符。
    # 先去实际HTML排版，最后解码实体，避免将&lt;主体&gt;等文本占位符当标签删除。
    $taskMediaCount=[regex]::Matches($taskRaw,'(?is)<(?:img|source|whiteboard)\b[^>]*>').Count
    $taskClean=[regex]::Replace($taskRaw,'(?is)<cite\b[^>]*>.*?</cite>',[System.Text.RegularExpressions.MatchEvaluator]{param($taskMatch)
        $taskTitle=[regex]::Match($taskMatch.Value,'title="([^"]*)"').Groups[1].Value
        $taskId=[regex]::Match($taskMatch.Value,'doc-id="([^"]*)"').Groups[1].Value
        return "[引用文档：$taskTitle；ID：$taskId]"
    })
    $taskClean=[regex]::Replace($taskClean,'(?is)<(?:img|source|whiteboard)\b[^>]*>','[媒体占位：按用户要求不观看]')
    $taskClean=[regex]::Replace($taskClean,'(?is)<a\b[^>]*href="([^"]*)"[^>]*>','[链接：$1]')
    $taskClean=[regex]::Replace($taskClean,'(?is)<h([1-6])\b[^>]*>',[System.Text.RegularExpressions.MatchEvaluator]{param($taskMatch) return "`n"+('#'*[int]$taskMatch.Groups[1].Value)+' '})
    $taskClean=[regex]::Replace($taskClean,'(?is)<br\s*/?>|</(?:p|div|li|tr|pre|code|h[1-6]|title|callout|grid|column|figure)>',"`n")
    $taskClean=[regex]::Replace($taskClean,'(?is)</(?:td|th)>'," | `n")
    $taskClean=[regex]::Replace($taskClean,'(?is)</?(?:p|div|b|i|u|strong|em|span|li|ol|ul|table|thead|tbody|tfoot|tr|td|th|colgroup|col|pre|code|callout|grid|column|figure|title|a|s|strike|sup|sub|source|img|whiteboard)\b[^>]*>','')
    $taskClean=[System.Net.WebUtility]::HtmlDecode($taskClean)
    $taskClean=[regex]::Replace($taskClean,"[ \t]+`r?`n","`n")
    $taskClean=[regex]::Replace($taskClean,"(?:`r?`n){4,}","`n`n`n")
    Save-ReadFile (Join-Path $taskReadDir ($taskBase+'_可读全文.txt')) $taskClean
    $taskUnresolved=[regex]::Matches($taskClean,'(?i)<(?:synced_reference|sheet|bitable|excerpt|fragment)\b').Count
    $taskChunks=@();$taskStart=0;$taskIndex=1;$taskRejoin=[System.Text.StringBuilder]::new()
    while($taskStart -lt $taskClean.Length){
        $taskLength=[Math]::Min(7000,$taskClean.Length-$taskStart)
        if($taskStart+$taskLength -lt $taskClean.Length){
            $taskBreak=$taskClean.LastIndexOf("`n",$taskStart+$taskLength-1,$taskLength)
            if($taskBreak -gt $taskStart+3500){$taskLength=$taskBreak-$taskStart+1}
        }
        $taskChunk=$taskClean.Substring($taskStart,$taskLength)
        $taskChunkName=('{0}_阅读{1:D2}.txt' -f $taskBase,$taskIndex)
        Save-ReadFile (Join-Path $taskReadDir $taskChunkName) $taskChunk
        [void]$taskRejoin.Append($taskChunk)
        $taskChunks += [pscustomobject]@{file=$taskChunkName;start_utf16=$taskStart;end_utf16_exclusive=$taskStart+$taskLength;length=$taskLength}
        $taskStart+=$taskLength;$taskIndex++
    }
    if(-not [string]::Equals($taskClean,$taskRejoin.ToString(),[System.StringComparison]::Ordinal)){throw 'Read chunks lost content.'}
    $taskManifest += [pscustomobject]@{id=$taskSource.id;name=$taskSource.name;url=$taskSource.url;online_checked_date='2026-10-15';document_id=$taskDoc.document_id;revision_id=$taskDoc.revision_id;raw_utf16_length=$taskRaw.Length;readable_utf16_length=$taskClean.Length;raw_sha256=(Get-FileHash -LiteralPath (Join-Path $taskReadDir ($taskBase+'_正文.md')) -Algorithm SHA256).Hash.ToLowerInvariant();readable_sha256=(Get-FileHash -LiteralPath (Join-Path $taskReadDir ($taskBase+'_可读全文.txt')) -Algorithm SHA256).Hash.ToLowerInvariant();media_placeholders=$taskMediaCount;unresolved_embedded_text_markers=$taskUnresolved;chunk_reconstruction_verified=$true;chunks=$taskChunks}
}
Save-ReadFile (Join-Path $taskReadDir '在线获取与分块清单.json') ($taskManifest|ConvertTo-Json -Depth 8)
$taskManifest|Select-Object id,revision_id,raw_utf16_length,readable_utf16_length,media_placeholders,unresolved_embedded_text_markers,@{n='chunks';e={$_.chunks.Count}}|ConvertTo-Json
