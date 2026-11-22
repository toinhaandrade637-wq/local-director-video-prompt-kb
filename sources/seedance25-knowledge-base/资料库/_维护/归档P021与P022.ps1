$ErrorActionPreference = 'Stop'
$taskRoot = 'D:/seedance2.5提示词及结构'
$taskSession = 'D:/CodexData/.codex/sessions/2026/10/08/rollout-2026-10-08T20-53-04-01a11b93-0d5d-72b0-9a10-5b9fa386a1a1.jsonl'
$taskUtf8 = [System.Text.UTF8Encoding]::new($false)
$taskSources = @()
$taskLine = 0
foreach ($taskJson in (Get-Content -LiteralPath $taskSession -Encoding UTF8)) {
    $taskLine++
    $taskRecord = $taskJson | ConvertFrom-Json
    if ($taskRecord.type -ne 'response_item' -or $taskRecord.payload.role -ne 'user') { continue }
    $taskText = ($taskRecord.payload.content | Where-Object { $_.type -eq 'input_text' -or $_.type -eq 'text' } | ForEach-Object { $_.text }) -join "`n"
    if ($taskText.StartsWith('参考图统一引用：**图片1**') -and $taskText.Contains('MULTIVERSE LUNGE')) {
        $taskSources += [pscustomobject]@{line=$taskLine; text=$taskText}
    }
}
if ($taskSources.Count -ne 1) { throw "Expected one original new case message, got $($taskSources.Count)." }
$taskSource = $taskSources[0]
$taskOriginal = $taskSource.text
$taskBoundary = $taskOriginal.IndexOf('整体为一条喜剧式的', [System.StringComparison]::Ordinal)
if ($taskBoundary -le 0) { throw 'Case boundary not found.' }
function Save-ExactNewArchive([string]$RelativePath, [string]$Content) {
    $taskDestination = [System.IO.Path]::GetFullPath((Join-Path $taskRoot $RelativePath))
    $taskPrefix = [System.IO.Path]::GetFullPath($taskRoot).TrimEnd([char[]]@('\','/')) + [System.IO.Path]::DirectorySeparatorChar
    if (-not $taskDestination.StartsWith($taskPrefix, [System.StringComparison]::OrdinalIgnoreCase)) { throw 'Path leaves workspace.' }
    [void][System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($taskDestination))
    if (Test-Path -LiteralPath $taskDestination) {
        if (-not [string]::Equals([System.IO.File]::ReadAllText($taskDestination), $Content, [System.StringComparison]::Ordinal)) { throw 'Existing archive differs; refusing overwrite.' }
    } else { [System.IO.File]::WriteAllText($taskDestination, $Content, $taskUtf8) }
    return (Get-FileHash -LiteralPath $taskDestination -Algorithm SHA256).Hash.ToLowerInvariant()
}
$taskRawPath = '资料库/00_完整原始消息/用户新增案例原始消息_2026-10-10_足球与风格穿越.txt'
$taskRawHash = Save-ExactNewArchive $taskRawPath $taskOriginal
$taskCaseSpecs = @(
    @{id='P021'; title='男孩足球_四镜与速度切换'; start=0; end=$taskBoundary},
    @{id='P022'; title='MULTIVERSE_LUNGE_双主体环绕与媒介变化'; start=$taskBoundary; end=$taskOriginal.Length}
)
$taskEntries = @()
$taskRebuilt = [System.Text.StringBuilder]::new()
foreach ($taskSpec in $taskCaseSpecs) {
    $taskSlice = $taskOriginal.Substring($taskSpec.start, $taskSpec.end-$taskSpec.start)
    $taskPath = "资料库/01_用户提示词原文/$($taskSpec.id)_$($taskSpec.title).txt"
    $taskHash = Save-ExactNewArchive $taskPath $taskSlice
    [void]$taskRebuilt.Append([System.IO.File]::ReadAllText((Join-Path $taskRoot $taskPath)))
    $taskEntries += [ordered]@{
        id=$taskSpec.id; title=$taskSpec.title; path=$taskPath
        source_start_utf16=$taskSpec.start; source_end_utf16_exclusive=$taskSpec.end
        utf16_length=$taskSlice.Length; sha256_utf8=$taskHash
        validation='用户于2026-10-10新增提供的结构案例；本条生成结果未被单独说明或附视频。'
    }
}
if (-not [string]::Equals($taskRebuilt.ToString(),$taskOriginal,[System.StringComparison]::Ordinal)) { throw 'Exact reconstruction failed.' }
$taskManifest = [ordered]@{
    schema_version=1; archived_date='2026-10-10'; thread_id='01a11b93-0d5d-72b0-9a10-5b9fa386a1a1'
    source_user_record_line=$taskSource.line
    original_message=@{path=$taskRawPath; utf16_length=$taskOriginal.Length; sha256_utf8=$taskRawHash}
    fidelity='原始用户消息连续切片；未清理标点、反斜杠、占位符或文字；所有媒介条目保留。'
    reconstruction_verified=$true; cases=$taskEntries
}
$taskManifestPath = '资料库/归档清单_2026-10-10_P021-P022.json'
$taskManifestHash = Save-ExactNewArchive $taskManifestPath ($taskManifest | ConvertTo-Json -Depth 7)
[pscustomobject]@{cases=2; original_utf16_length=$taskOriginal.Length; exact_reconstruction=$true; manifest=$taskManifestPath} | ConvertTo-Json
