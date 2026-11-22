$ErrorActionPreference='Stop'
$taskRoot='D:/seedance2.5提示词及结构'
$taskSession='D:/CodexData/.codex/sessions/2026/10/08/rollout-2026-10-08T20-53-04-01a11b93-0d5d-72b0-9a10-5b9fa386a1a1.jsonl'
$taskUtf8=[System.Text.UTF8Encoding]::new($false)
$taskPrefixText='【优秀的现实主义导演，深谙侯孝贤叙事风格】'
$taskFound=@();$taskLine=0
foreach($taskJson in (Get-Content -LiteralPath $taskSession -Encoding UTF8)){
    $taskLine++;$taskRecord=$taskJson|ConvertFrom-Json
    if($taskRecord.type -ne 'response_item' -or $taskRecord.payload.role -ne 'user'){continue}
    $taskText=($taskRecord.payload.content|Where-Object{$_.type -eq 'input_text' -or $_.type -eq 'text'}|ForEach-Object{$_.text}) -join "`n"
    if($taskText.StartsWith($taskPrefixText) -and $taskText.Contains('bān-hue-tông') -and $taskText.Contains('[audios: 2]')){$taskFound += [pscustomobject]@{line=$taskLine;text=$taskText}}
}
if($taskFound.Count -ne 1){throw "Expected one source, found $($taskFound.Count)."}
$taskSource=$taskFound[0];$taskOriginal=$taskSource.text
$taskBoundaries=[regex]::Matches($taskOriginal,[regex]::Escape($taskPrefixText))
if($taskBoundaries.Count -ne 5 -or $taskBoundaries[0].Index -ne 0){throw 'Unexpected case boundaries.'}
function Save-ExactReferenceDialogue([string]$Relative,[string]$Content){
    $taskAbsolute=[System.IO.Path]::GetFullPath((Join-Path $taskRoot $Relative))
    $taskSafePrefix=[System.IO.Path]::GetFullPath($taskRoot).TrimEnd([char[]]@('\','/'))+[System.IO.Path]::DirectorySeparatorChar
    if(-not $taskAbsolute.StartsWith($taskSafePrefix,[System.StringComparison]::OrdinalIgnoreCase)){throw 'Path outside project.'}
    [void][System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($taskAbsolute))
    if(Test-Path -LiteralPath $taskAbsolute){if(-not [string]::Equals([System.IO.File]::ReadAllText($taskAbsolute),$Content,[System.StringComparison]::Ordinal)){throw "Existing archive differs: $Relative"}}
    else{[System.IO.File]::WriteAllText($taskAbsolute,$Content,$taskUtf8)}
    return (Get-FileHash -LiteralPath $taskAbsolute -Algorithm SHA256).Hash.ToLowerInvariant()
}
$taskTitles=@('对岸约定拉钩_花括号引用首版','万花筒争夺与归还_五镜','对岸约定拉钩_纯编号与资源标记版','打赌激将与起身反应_六镜','对岸约定拉钩_再次提供')
$taskRawPath='资料库/00_完整原始消息/用户新增案例原始消息_2026-10-18_对岸对白与构图参考.txt'
$taskRawHash=Save-ExactReferenceDialogue $taskRawPath $taskOriginal
$taskCases=@();$taskJoined=[System.Text.StringBuilder]::new()
for($taskI=0;$taskI -lt 5;$taskI++){
    $taskStart=$taskBoundaries[$taskI].Index;$taskEnd=if($taskI -lt 4){$taskBoundaries[$taskI+1].Index}else{$taskOriginal.Length}
    $taskContent=$taskOriginal.Substring($taskStart,$taskEnd-$taskStart)
    $taskId='P{0:D3}' -f (44+$taskI)
    $taskPath="资料库/01_用户提示词原文/$($taskId)_$($taskTitles[$taskI]).txt"
    $taskHash=Save-ExactReferenceDialogue $taskPath $taskContent
    [void]$taskJoined.Append([System.IO.File]::ReadAllText((Join-Path $taskRoot $taskPath)))
    $taskCases += [ordered]@{id=$taskId;title=$taskTitles[$taskI];path=$taskPath;source_start_utf16=$taskStart;source_end_utf16_exclusive=$taskEnd;utf16_length=$taskContent.Length;sha256_utf8=$taskHash;validation='新增参考驱动对白结构样本，未单独确认生成结果。';reference_availability='只有文字引用与部分资源数量/角色标签，未提供所指图像音频本体。';logical_group=if($taskI -in @(0,2,4)){'对岸约定拉钩，同一逻辑片段的引用形式/重复出现分别保留'}elseif($taskI -eq 1){'万花筒争夺与归还'}else{'打赌激将与反应'}}
}
if(-not [string]::Equals($taskOriginal,$taskJoined.ToString(),[System.StringComparison]::Ordinal)){throw 'Exact reconstruction failed.'}
$taskManifest=[ordered]@{schema_version=1;archived_date='2026-10-18';thread_id='01a11b93-0d5d-72b0-9a10-5b9fa386a1a1';source_user_record_line=$taskSource.line;original_message=@{path=$taskRawPath;utf16_length=$taskOriginal.Length;sha256_utf8=$taskRawHash};fidelity='按五次出现连续切片，保留重复版本、台词汉字、罗马字拼音、资产标记、空格与标点，不校正语言或图号。';reconstruction_verified=$true;cases=$taskCases}
$taskManifestPath='资料库/归档清单_2026-10-18_P044-P048.json'
$taskManifestHash=Save-ExactReferenceDialogue $taskManifestPath ($taskManifest|ConvertTo-Json -Depth 7)
[pscustomobject]@{cases=5;logical_groups=3;source_length=$taskOriginal.Length;exact_reconstruction=$true;manifest=$taskManifestPath}|ConvertTo-Json
