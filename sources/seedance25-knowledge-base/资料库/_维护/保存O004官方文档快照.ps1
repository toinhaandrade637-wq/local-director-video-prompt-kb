$ErrorActionPreference='Stop'
$taskRoot='D:/seedance2.5提示词及结构'
$taskDirectory=Join-Path $taskRoot '资料库/03_官方参考'
$taskSourceUrl='https://bytedance.larkoffice.com/wiki/Tyi1woQAgiZlkhkWGnYcF2Cun3e'
$taskUtf8=[System.Text.UTF8Encoding]::new($false)
$taskResultLines=& lark-cli.cmd docs +fetch --doc $taskSourceUrl --doc-format markdown --as user
if($LASTEXITCODE -ne 0){throw 'Feishu read failed.'}
$taskResult=($taskResultLines -join "`n")|ConvertFrom-Json
if($taskResult.ok -ne $true){throw 'Document response not successful.'}
$taskDocument=$taskResult.data.document
if([string]::IsNullOrWhiteSpace($taskDocument.content)){throw 'Empty document body.'}
$taskTitle=[regex]::Match($taskDocument.content,'(?s)^<title>(.*?)</title>').Groups[1].Value
$taskBaseName="O004_Seedance2.5官方综合文档_r$($taskDocument.revision_id)"
[void][System.IO.Directory]::CreateDirectory($taskDirectory)
function Save-NewOfficialText([string]$Name,[string]$Content){
    $taskPath=Join-Path $taskDirectory $Name
    if(Test-Path -LiteralPath $taskPath){
        if(-not [string]::Equals([System.IO.File]::ReadAllText($taskPath),$Content,[System.StringComparison]::Ordinal)){throw "Existing snapshot differs: $Name"}
    }else{[System.IO.File]::WriteAllText($taskPath,$Content,$taskUtf8)}
    return (Get-FileHash -LiteralPath $taskPath -Algorithm SHA256).Hash.ToLowerInvariant()
}
$taskContentHash=Save-NewOfficialText ($taskBaseName+'.md') $taskDocument.content
$taskDataHash=Save-NewOfficialText ($taskBaseName+'.json') ($taskDocument|ConvertTo-Json -Depth 80)
$taskManifest=[ordered]@{
    id='O004'
    document_title=$taskTitle
    archive_label='Seedance 2.5 官方综合文档（归档描述名）'
    source_url=$taskSourceUrl
    captured_date='2026-10-15'
    document_id=$taskDocument.document_id
    revision_id=$taskDocument.revision_id
    markdown_file=$taskBaseName+'.md'
    document_json_file=$taskBaseName+'.json'
    utf16_length=$taskDocument.content.Length
    sha256=$taskContentHash
    document_json_sha256=$taskDataHash
    read_scope='正文全文与接口返回的引用信息；当前仅浏览目录和开头，未逐项研究全部案例。'
    media_note='未批量下载或观看文档内嵌的图片、音频和视频。'
}
$taskManifestHash=Save-NewOfficialText '快照清单_2026-10-15_O004.json' ($taskManifest|ConvertTo-Json -Depth 5)
[pscustomobject]@{id='O004';document_id=$taskDocument.document_id;revision_id=$taskDocument.revision_id;content_length=$taskDocument.content.Length;markdown_file=$taskBaseName+'.md';opening=$taskDocument.content.Substring(0,[Math]::Min(700,$taskDocument.content.Length));sha256=$taskContentHash}|ConvertTo-Json -Depth 3
