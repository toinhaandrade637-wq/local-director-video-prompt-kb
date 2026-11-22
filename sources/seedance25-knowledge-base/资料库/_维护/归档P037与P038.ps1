$ErrorActionPreference='Stop'
$taskRoot='D:/seedance2.5提示词及结构'
$taskSession='D:/CodexData/.codex/sessions/2026/10/08/rollout-2026-10-08T20-53-04-01a11b93-0d5d-72b0-9a10-5b9fa386a1a1.jsonl'
$taskUtf8=[System.Text.UTF8Encoding]::new($false)
$taskFound=@();$taskLine=0
foreach($taskJson in (Get-Content -LiteralPath $taskSession -Encoding UTF8)){
    $taskLine++;$taskRecord=$taskJson|ConvertFrom-Json
    if($taskRecord.type -ne 'response_item' -or $taskRecord.payload.role -ne 'user'){continue}
    $taskText=($taskRecord.payload.content|Where-Object{$_.type -eq 'input_text' -or $_.type -eq 'text'}|ForEach-Object{$_.text}) -join "`n"
    if($taskText.StartsWith('生成一支30秒、写实电影质感、原生英语同步对白的双人剧情短片。') -and $taskText.Contains('AI默认把对白处理成A说完→B说完')){$taskFound += [pscustomobject]@{line=$taskLine;text=$taskText}}
}
if($taskFound.Count -ne 1){throw 'Expected exactly one source user message.'}
$taskSource=$taskFound[0];$taskOriginal=$taskSource.text
$taskSecond=$taskOriginal.IndexOf('生成一支30秒、写实电影质感、原生同步对白的家庭剧情短片。',[System.StringComparison]::Ordinal)
$taskAnalysis=$taskOriginal.IndexOf('AI默认把对白处理成A说完→B说完',[System.StringComparison]::Ordinal)
if($taskSecond -le 0 -or $taskAnalysis -le $taskSecond){throw 'Invalid source boundaries.'}
function Save-ExactDialogueArchive([string]$RelativePath,[string]$Content){
    $taskAbsolute=[System.IO.Path]::GetFullPath((Join-Path $taskRoot $RelativePath))
    $taskPrefix=[System.IO.Path]::GetFullPath($taskRoot).TrimEnd([char[]]@('\','/'))+[System.IO.Path]::DirectorySeparatorChar
    if(-not $taskAbsolute.StartsWith($taskPrefix,[System.StringComparison]::OrdinalIgnoreCase)){throw 'Path outside project.'}
    [void][System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($taskAbsolute))
    if(Test-Path -LiteralPath $taskAbsolute){if(-not [string]::Equals([System.IO.File]::ReadAllText($taskAbsolute),$Content,[System.StringComparison]::Ordinal)){throw "Existing archive differs: $RelativePath"}}
    else{[System.IO.File]::WriteAllText($taskAbsolute,$Content,$taskUtf8)}
    return (Get-FileHash -LiteralPath $taskAbsolute -Algorithm SHA256).Hash.ToLowerInvariant()
}
$taskRawPath='资料库/00_完整原始消息/用户新增案例原始消息_2026-10-13_双人对白与表演节拍.txt'
$taskRawHash=Save-ExactDialogueArchive $taskRawPath $taskOriginal
$taskSpecs=@(
    @{id='P037';title='冬日街边双人对话_抢话与启动失败';start=0;end=$taskSecond},
    @{id='P038';title='后院门廊夫妻争吵_镜内情绪与听者反应';start=$taskSecond;end=$taskAnalysis}
)
$taskEntries=@();$taskJoined=[System.Text.StringBuilder]::new()
foreach($taskSpec in $taskSpecs){
    $taskContent=$taskOriginal.Substring($taskSpec.start,$taskSpec.end-$taskSpec.start)
    $taskPath="资料库/01_用户提示词原文/$($taskSpec.id)_$($taskSpec.title).txt"
    $taskHash=Save-ExactDialogueArchive $taskPath $taskContent
    [void]$taskJoined.Append([System.IO.File]::ReadAllText((Join-Path $taskRoot $taskPath)))
    $taskEntries += [ordered]@{id=$taskSpec.id;title=$taskSpec.title;path=$taskPath;source_start_utf16=$taskSpec.start;source_end_utf16_exclusive=$taskSpec.end;utf16_length=$taskContent.Length;sha256_utf8=$taskHash;validation='新增对白表演研究样本，附用户结构分析；本条生成结果未单独说明。'}
}
$taskAnalysisPath='资料库/00_完整原始消息/用户结构补充_2026-10-13_镜内表演节拍与抢话.txt'
$taskAnalysisText=$taskOriginal.Substring($taskAnalysis)
$taskAnalysisHash=Save-ExactDialogueArchive $taskAnalysisPath $taskAnalysisText
[void]$taskJoined.Append([System.IO.File]::ReadAllText((Join-Path $taskRoot $taskAnalysisPath)))
if(-not [string]::Equals($taskOriginal,$taskJoined.ToString(),[System.StringComparison]::Ordinal)){throw 'Reconstruction failed.'}
$taskManifest=[ordered]@{schema_version=1;archived_date='2026-10-13';thread_id='01a11b93-0d5d-72b0-9a10-5b9fa386a1a1';source_user_record_line=$taskSource.line;original_message=@{path=$taskRawPath;utf16_length=$taskOriginal.Length;sha256_utf8=$taskRawHash};fidelity='两条提示词与用户末尾结构分析分别作连续切片，字词、标点、反斜杠和台词原样保留。';reconstruction_verified=$true;cases=$taskEntries;user_analysis=@{path=$taskAnalysisPath;source_start_utf16=$taskAnalysis;source_end_utf16_exclusive=$taskOriginal.Length;sha256_utf8=$taskAnalysisHash}}
$taskManifestPath='资料库/归档清单_2026-10-13_P037-P038.json'
$taskManifestHash=Save-ExactDialogueArchive $taskManifestPath ($taskManifest|ConvertTo-Json -Depth 7)
[pscustomobject]@{case_count=2;user_analysis_saved=$true;source_length=$taskOriginal.Length;exact_reconstruction=$true;manifest=$taskManifestPath}|ConvertTo-Json
