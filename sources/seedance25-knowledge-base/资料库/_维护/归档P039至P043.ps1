$ErrorActionPreference='Stop'
$taskRoot='D:/seedance2.5提示词及结构'
$taskSession='D:/CodexData/.codex/sessions/2026/10/08/rollout-2026-10-08T20-53-04-01a11b93-0d5d-72b0-9a10-5b9fa386a1a1.jsonl'
$taskUtf8=[System.Text.UTF8Encoding]::new($false)
$taskFound=@();$taskLine=0
foreach($taskJson in (Get-Content -LiteralPath $taskSession -Encoding UTF8)){
    $taskLine++;$taskRecord=$taskJson|ConvertFrom-Json
    if($taskRecord.type -ne 'response_item' -or $taskRecord.payload.role -ne 'user'){continue}
    $taskText=($taskRecord.payload.content|Where-Object{$_.type -eq 'input_text' -or $_.type -eq 'text'}|ForEach-Object{$_.text}) -join "`n"
    if($taskText.StartsWith('图1:环境') -and $taskText.Contains('主角的鼓') -and $taskText.Contains('Get the brain out.')){$taskFound += [pscustomobject]@{line=$taskLine;text=$taskText}}
}
if($taskFound.Count -ne 1){throw "Expected one source, found $($taskFound.Count)."}
$taskSource=$taskFound[0];$taskOriginal=$taskSource.text
function Save-ExactDocumentaryArchive([string]$Relative,[string]$Content){
    $taskAbsolute=[System.IO.Path]::GetFullPath((Join-Path $taskRoot $Relative))
    $taskPrefix=[System.IO.Path]::GetFullPath($taskRoot).TrimEnd([char[]]@('\','/'))+[System.IO.Path]::DirectorySeparatorChar
    if(-not $taskAbsolute.StartsWith($taskPrefix,[System.StringComparison]::OrdinalIgnoreCase)){throw 'Path outside project.'}
    [void][System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($taskAbsolute))
    if(Test-Path -LiteralPath $taskAbsolute){if(-not [string]::Equals([System.IO.File]::ReadAllText($taskAbsolute),$Content,[System.StringComparison]::Ordinal)){throw "Existing archive differs: $Relative"}}
    else{[System.IO.File]::WriteAllText($taskAbsolute,$Content,$taskUtf8)}
    return (Get-FileHash -LiteralPath $taskAbsolute -Algorithm SHA256).Hash.ToLowerInvariant()
}
$taskSpecs=@(
    @{id='P039';title='日出男孩奔跑敲鼓_五镜纪录片';marker='图1:环境'},
    @{id='P040';title='草原狩猎_起跑放箭与追摇承接';marker="图1:人物`n`n图2:弓箭武器"},
    @{id='P041';title='男孩被架离圣地并关入黑屋';marker="图1:大环境`n`n图2:部落众人"},
    @{id='P042';title='五女采摘闻嗅分享蘑菇';marker="图1:大环境`n`n图2:女人们"},
    @{id='P043';title='拾荒者围观病者与转向Echo_简式分镜';marker='{{Image 2}} Tǀaru病重'}
)
$taskSearch=0
foreach($taskSpec in $taskSpecs){$taskPos=$taskOriginal.IndexOf($taskSpec.marker,$taskSearch,[System.StringComparison]::Ordinal);if($taskPos -lt 0){throw "Missing boundary: $($taskSpec.id)"};$taskSpec.start=$taskPos;$taskSearch=$taskPos+$taskSpec.marker.Length}
if($taskSpecs[0].start -ne 0){throw 'Unexpected prefix.'}
$taskRawPath='资料库/00_完整原始消息/用户新增案例原始消息_2026-10-18_五段纪录片观察.txt'
$taskRawHash=Save-ExactDocumentaryArchive $taskRawPath $taskOriginal
$taskCases=@();$taskJoined=[System.Text.StringBuilder]::new()
for($taskI=0;$taskI -lt $taskSpecs.Count;$taskI++){
    $taskSpec=$taskSpecs[$taskI];$taskEnd=if($taskI+1 -lt $taskSpecs.Count){$taskSpecs[$taskI+1].start}else{$taskOriginal.Length}
    $taskContent=$taskOriginal.Substring($taskSpec.start,$taskEnd-$taskSpec.start)
    $taskPath="资料库/01_用户提示词原文/$($taskSpec.id)_$($taskSpec.title).txt"
    $taskHash=Save-ExactDocumentaryArchive $taskPath $taskContent
    [void]$taskJoined.Append([System.IO.File]::ReadAllText((Join-Path $taskRoot $taskPath)))
    $taskCases += [ordered]@{id=$taskSpec.id;title=$taskSpec.title;path=$taskPath;source_start_utf16=$taskSpec.start;source_end_utf16_exclusive=$taskEnd;utf16_length=$taskContent.Length;sha256_utf8=$taskHash;validation='2026-10-18新增结构样本，未单独确认生成结果；所指参考资产未随本批提供。'}
}
if(-not [string]::Equals($taskOriginal,$taskJoined.ToString(),[System.StringComparison]::Ordinal)){throw 'Exact reconstruction failed.'}
$taskManifest=[ordered]@{schema_version=1;archived_date='2026-10-18';thread_id='01a11b93-0d5d-72b0-9a10-5b9fa386a1a1';source_user_record_line=$taskSource.line;original_message=@{path=$taskRawPath;utf16_length=$taskOriginal.Length;sha256_utf8=$taskRawHash};fidelity='连续切片保存五段原文，保留引用、改稿说明、标点、反斜杠及末尾用户用语，不修改图号或时间。';reconstruction_verified=$true;cases=$taskCases}
$taskManifestPath='资料库/归档清单_2026-10-18_P039-P043.json'
$taskManifestHash=Save-ExactDocumentaryArchive $taskManifestPath ($taskManifest|ConvertTo-Json -Depth 7)
[pscustomobject]@{cases=5;source_length=$taskOriginal.Length;exact_reconstruction=$true;manifest=$taskManifestPath}|ConvertTo-Json
