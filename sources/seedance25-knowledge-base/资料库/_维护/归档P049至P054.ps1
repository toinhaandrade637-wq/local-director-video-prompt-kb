$ErrorActionPreference='Stop'
$taskRoot='D:/seedance2.5提示词及结构'
$taskSession='D:/CodexData/.codex/sessions/2026/10/08/rollout-2026-10-08T20-53-04-01a11b93-0d5d-72b0-9a10-5b9fa386a1a1.jsonl'
$taskUtf8=[System.Text.UTF8Encoding]::new($false)
$taskFound=@();$taskLine=0
foreach($taskJson in (Get-Content -LiteralPath $taskSession -Encoding UTF8)){
    $taskLine++;$taskRecord=$taskJson|ConvertFrom-Json
    if($taskRecord.type -ne 'response_item' -or $taskRecord.payload.role -ne 'user'){continue}
    $taskText=($taskRecord.payload.content|Where-Object{$_.type -eq 'input_text' -or $_.type -eq 'text'}|ForEach-Object{$_.text}) -join "`n"
    if($taskText.StartsWith('16:9，超低机位的微观纪录片视角') -and $taskText.Contains('SHEPHERD THE SHEPHERD')){$taskFound += [pscustomobject]@{line=$taskLine;text=$taskText}}
}
if($taskFound.Count -ne 1){throw 'Expected exactly one source user message.'}
$taskSource=$taskFound[0];$taskOriginal=$taskSource.text
$taskAnalysisStart=$taskOriginal.IndexOf('这几个经查有说的的我觉得有的',[System.StringComparison]::Ordinal)
if($taskAnalysisStart -le 0){throw 'User analysis boundary missing.'}
$taskSpecs=@(
    @{id='P049';title='蚂蚁搬运透明硬糖_微观纪录片';marker='16:9，超低机位的微观纪录片视角'},
    @{id='P050';title='实验基地观察与糖果化反转';marker='写实电影画面，极度真实的实拍质感，16:9，纪录片式运镜'},
    @{id='P051';title='发布会声明_记者一镜到底';marker='16:9，严格一镜到底，真实发布会现场的手持记者拍摄质感'},
    @{id='P052';title='美术馆到桶厂_逐区域遮挡转场';marker='16:9，真实纪录片质感，一镜到底，无BGM，仅保留美术馆的低声交谈'},
    @{id='P053';title='女孩捏起黄色硬糖_贴地微距';marker='写实电影画面，16:9，极度真实可信的手持纪录片质感，一镜到底'},
    @{id='P054';title='美术馆群像讨论_说者与画作细节'}
)
$taskSpecs[5].marker='真实写实的现代白色美术馆，16:9，一镜到底，低饱和'
$taskSearch=0
foreach($taskSpec in $taskSpecs){$taskStart=$taskOriginal.IndexOf($taskSpec.marker,$taskSearch,[System.StringComparison]::Ordinal);if($taskStart -lt 0 -or $taskStart -ge $taskAnalysisStart){throw "Case boundary missing: $($taskSpec.id)"};$taskSpec.start=$taskStart;$taskSearch=$taskStart+$taskSpec.marker.Length}
if($taskSpecs[0].start -ne 0){throw 'Unexpected prefix.'}
function Save-ExactCandyArchive([string]$Relative,[string]$Content){
    $taskAbsolute=[System.IO.Path]::GetFullPath((Join-Path $taskRoot $Relative))
    $taskPrefix=[System.IO.Path]::GetFullPath($taskRoot).TrimEnd([char[]]@('\','/'))+[System.IO.Path]::DirectorySeparatorChar
    if(-not $taskAbsolute.StartsWith($taskPrefix,[System.StringComparison]::OrdinalIgnoreCase)){throw 'Path outside project.'}
    [void][System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($taskAbsolute))
    if(Test-Path -LiteralPath $taskAbsolute){if(-not [string]::Equals([System.IO.File]::ReadAllText($taskAbsolute),$Content,[System.StringComparison]::Ordinal)){throw "Existing archive differs: $Relative"}}
    else{[System.IO.File]::WriteAllText($taskAbsolute,$Content,$taskUtf8)}
    return (Get-FileHash -LiteralPath $taskAbsolute -Algorithm SHA256).Hash.ToLowerInvariant()
}
$taskRawPath='资料库/00_完整原始消息/用户新增案例原始消息_2026-10-19_糖果世界六例与写作经验.txt'
$taskRawHash=Save-ExactCandyArchive $taskRawPath $taskOriginal
$taskEntries=@();$taskJoined=[System.Text.StringBuilder]::new()
for($taskI=0;$taskI -lt 6;$taskI++){
    $taskSpec=$taskSpecs[$taskI];$taskEnd=if($taskI -lt 5){$taskSpecs[$taskI+1].start}else{$taskAnalysisStart}
    $taskContent=$taskOriginal.Substring($taskSpec.start,$taskEnd-$taskSpec.start)
    $taskPath="资料库/01_用户提示词原文/$($taskSpec.id)_$($taskSpec.title).txt"
    $taskHash=Save-ExactCandyArchive $taskPath $taskContent
    [void]$taskJoined.Append([System.IO.File]::ReadAllText((Join-Path $taskRoot $taskPath)))
    $taskEntries += [ordered]@{id=$taskSpec.id;title=$taskSpec.title;path=$taskPath;source_start_utf16=$taskSpec.start;source_end_utf16_exclusive=$taskEnd;utf16_length=$taskContent.Length;sha256_utf8=$taskHash;validation='新增文字样本；用户另述部分写法的个人实用经验，未提供本批生成视频或逐例验证记录。';reference_availability='文中所指首尾图、画作局部与此前世界观仅按文字分析，未随本批提供相关图像或视频本体。'}
}
$taskAnalysisPath='资料库/00_完整原始消息/用户写作经验_2026-10-19_代入感材质与一致性强调.txt'
$taskAnalysis=$taskOriginal.Substring($taskAnalysisStart)
$taskAnalysisHash=Save-ExactCandyArchive $taskAnalysisPath $taskAnalysis
[void]$taskJoined.Append([System.IO.File]::ReadAllText((Join-Path $taskRoot $taskAnalysisPath)))
if(-not [string]::Equals($taskOriginal,$taskJoined.ToString(),[System.StringComparison]::Ordinal)){throw 'Exact reconstruction failed.'}
$taskManifest=[ordered]@{schema_version=1;archived_date='2026-10-19';thread_id='01a11b93-0d5d-72b0-9a10-5b9fa386a1a1';source_user_record_line=$taskSource.line;original_message=@{path=$taskRawPath;utf16_length=$taskOriginal.Length;sha256_utf8=$taskRawHash};fidelity='六条提示词与用户写作经验作连续切片，保留错字、引用、重复引句、英文台词与标点，不校正物理或画作描述。';reconstruction_verified=$true;cases=$taskEntries;user_analysis=@{path=$taskAnalysisPath;source_start_utf16=$taskAnalysisStart;source_end_utf16_exclusive=$taskOriginal.Length;sha256_utf8=$taskAnalysisHash}}
$taskManifestPath='资料库/归档清单_2026-10-19_P049-P054.json'
$taskManifestHash=Save-ExactCandyArchive $taskManifestPath ($taskManifest|ConvertTo-Json -Depth 7)
[pscustomobject]@{cases=6;user_analysis_saved=$true;source_length=$taskOriginal.Length;exact_reconstruction=$true;manifest=$taskManifestPath}|ConvertTo-Json
