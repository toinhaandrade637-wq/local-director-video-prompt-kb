$ErrorActionPreference = 'Stop'
$taskRoot = 'D:/seedance2.5提示词及结构'
$taskSession = 'D:/CodexData/.codex/sessions/2026/10/08/rollout-2026-10-08T20-53-04-01a11b93-0d5d-72b0-9a10-5b9fa386a1a1.jsonl'
$taskUtf8 = [System.Text.UTF8Encoding]::new($false)

function Save-ExactArchiveText([string]$RelativePath, [string]$Content) {
    $taskDestination = [System.IO.Path]::GetFullPath((Join-Path $taskRoot $RelativePath))
    $taskRootPrefix = [System.IO.Path]::GetFullPath($taskRoot).TrimEnd([char[]]@('\','/')) + [System.IO.Path]::DirectorySeparatorChar
    if (-not $taskDestination.StartsWith($taskRootPrefix, [System.StringComparison]::OrdinalIgnoreCase)) { throw 'Archive path leaves project.' }
    [void][System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($taskDestination))
    if ([System.IO.File]::Exists($taskDestination)) {
        if (-not [string]::Equals([System.IO.File]::ReadAllText($taskDestination), $Content, [System.StringComparison]::Ordinal)) {
            throw "Existing archive differs; refusing to overwrite: $RelativePath"
        }
    } else {
        [System.IO.File]::WriteAllText($taskDestination, $Content, $taskUtf8)
    }
    return (Get-FileHash -LiteralPath $taskDestination -Algorithm SHA256).Hash.ToLowerInvariant()
}

$taskUserRecords = [System.Collections.Generic.List[object]]::new()
$taskLine = 0
foreach ($taskJsonLine in (Get-Content -LiteralPath $taskSession -Encoding UTF8)) {
    $taskLine++
    $taskRecord = $taskJsonLine | ConvertFrom-Json
    if ($taskRecord.type -ne 'response_item' -or $taskRecord.payload.role -ne 'user') { continue }
    $taskText = ($taskRecord.payload.content | Where-Object { $_.type -eq 'input_text' -or $_.type -eq 'text' } | ForEach-Object { $_.text }) -join "`n"
    $taskUserRecords.Add([pscustomobject]@{ line = $taskLine; text = $taskText })
}
$taskSourceCandidates = @($taskUserRecords | Where-Object { $_.text.Length -gt 50000 -and $_.text.StartsWith('[https://bytedance.larkoffice.com/wiki/RXh5ww6EqighMdkVTMccm2d4n7e]') })
if ($taskSourceCandidates.Count -ne 1) { throw 'Expected exactly one original user case message.' }
$taskSource = $taskSourceCandidates[0]
$taskOriginal = $taskSource.text
$taskRawPath = '资料库/00_完整原始消息/用户案例原始消息_2026-10-08.txt'
$taskRawHash = Save-ExactArchiveText $taskRawPath $taskOriginal

$taskTitles = @(
    '跳格子与踢球_首次提供',
    '母子街道转熔岩火山_三镜版本',
    '母子街道转秋日山谷_连续行走版本',
    '跳格子与踢球_再次提供',
    '酒馆对峙_蛇老板与相骨',
    '雪熊传奇介绍_三十秒一镜到底',
    '丰兔传奇介绍_三十秒一镜到底',
    '水面分流与巨塔攀爬',
    '606宿舍争执与老年曾亮',
    '黑白出租车_连续长镜头',
    '芦苇单手对抗_首次提供',
    '芦苇睁眼拔剑与剑面倒影',
    '闭眼火焰剑与怪物',
    '芦苇鸟妖近身缠斗与挑飞长刀',
    '芦苇单手对抗_再次提供',
    '凉亭鸟妖跃起与正面冲击',
    '浩铭举枪与发现小女孩',
    '披萨店接单与制作_英文原文',
    '披萨出炉与父子交接_英文原文'
)
$taskBoundaryPattern = '图1:|\[STYLE LOCK\]|【基础设定】|场景参考 \{\{|风格：高清CG电影|东方奇幻电影动画|15秒东方奇幻动作短片|【o秒|Action comedy vibe and timings\.'
$taskBoundaries = [regex]::Matches($taskOriginal, $taskBoundaryPattern)
if ($taskBoundaries.Count -ne $taskTitles.Count) { throw "Unexpected case count: $($taskBoundaries.Count)" }
$taskPrefix = $taskOriginal.Substring(0, $taskBoundaries[0].Index)
$taskPrefixHash = Save-ExactArchiveText '资料库/00_完整原始消息/用户案例原始消息_前言与官方链接.txt' $taskPrefix
$taskReconstruction = [System.Text.StringBuilder]::new()
[void]$taskReconstruction.Append($taskPrefix)
$taskCaseEntries = @()
for ($taskIndex = 0; $taskIndex -lt $taskTitles.Count; $taskIndex++) {
    $taskStart = $taskBoundaries[$taskIndex].Index
    $taskEnd = if ($taskIndex + 1 -lt $taskBoundaries.Count) { $taskBoundaries[$taskIndex + 1].Index } else { $taskOriginal.Length }
    $taskCaseText = $taskOriginal.Substring($taskStart, $taskEnd - $taskStart)
    $taskId = 'P{0:D3}' -f ($taskIndex + 1)
    $taskCasePath = "资料库/01_用户提示词原文/$($taskId)_$($taskTitles[$taskIndex]).txt"
    $taskCaseHash = Save-ExactArchiveText $taskCasePath $taskCaseText
    [void]$taskReconstruction.Append($taskCaseText)
    $taskCaseEntries += [ordered]@{
        id = $taskId
        title = $taskTitles[$taskIndex]
        path = $taskCasePath
        source_start_utf16 = $taskStart
        source_end_utf16_exclusive = $taskEnd
        utf16_length = $taskCaseText.Length
        sha256_utf8 = $taskCaseHash
        validation = '用户明确确认此前提供的提示词均经实际验证效果不错；未附对应生成视频'
    }
}
if (-not [string]::Equals($taskReconstruction.ToString(), $taskOriginal, [System.StringComparison]::Ordinal)) { throw 'Lossless reconstruction check failed.' }
if (-not [string]::Equals([System.IO.File]::ReadAllText((Join-Path $taskRoot $taskRawPath)), $taskOriginal, [System.StringComparison]::Ordinal)) { throw 'Saved original does not match source.' }

$taskSupplementFilters = @(
    @{ Name='用户确认_案例均已验证_2026-10-08.txt'; Start='继续他们这些官方当参考，我给你的这些提示词都是验证过得不错的提示词' },
    @{ Name='用户要求_原文分开存档与通用结构_2026-10-09.txt'; Start='像这些的的和之前给到的那些的提示词原文' }
)
$taskSupplementEntries = @()
foreach ($taskFilter in $taskSupplementFilters) {
    $taskMatches = @($taskUserRecords | Where-Object { $_.text.StartsWith($taskFilter.Start) })
    if ($taskMatches.Count -ne 1) { throw "Cannot identify supplement: $($taskFilter.Name)" }
    $taskSupplementPath = '资料库/00_完整原始消息/' + $taskFilter.Name
    $taskSupplementHash = Save-ExactArchiveText $taskSupplementPath $taskMatches[0].text
    $taskSupplementEntries += @{ path=$taskSupplementPath; source_line=$taskMatches[0].line; sha256_utf8=$taskSupplementHash }
}

$taskImageSource = 'D:/微信图片_20260916155111_322_1.jpg'
$taskImageRelative = '资料库/02_图片原件/P020_一镜到底第一期_25秒日剧自然表演.jpg'
$taskImageTarget = Join-Path $taskRoot $taskImageRelative
[void][System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($taskImageTarget))
$taskImageSourceHash = (Get-FileHash -LiteralPath $taskImageSource -Algorithm SHA256).Hash.ToLowerInvariant()
if (-not [System.IO.File]::Exists($taskImageTarget)) { Copy-Item -LiteralPath $taskImageSource -Destination $taskImageTarget }
$taskImageSavedHash = (Get-FileHash -LiteralPath $taskImageTarget -Algorithm SHA256).Hash.ToLowerInvariant()
if ($taskImageSourceHash -ne $taskImageSavedHash) { throw 'Original image and archive image differ.' }

$taskManifest = [ordered]@{
    schema_version = 1
    archived_date = '2026-10-09'
    thread_id = '01a11b93-0d5d-72b0-9a10-5b9fa386a1a1'
    source_user_record_line = $taskSource.line
    original_message = @{ path=$taskRawPath; utf16_length=$taskOriginal.Length; sha256_utf8=$taskRawHash }
    prefix = @{ path='资料库/00_完整原始消息/用户案例原始消息_前言与官方链接.txt'; sha256_utf8=$taskPrefixHash }
    fidelity = '只从本聊天用户原始消息提取；不改字、不解码HTML实体、不删除反斜杠、不统一标点、不去重。按原文起点连续切片，片尾保留原始分隔标点。'
    reconstruction_verified = $true
    cases = $taskCaseEntries
    supplements = $taskSupplementEntries
    image = @{ id='P020'; path=$taskImageRelative; original_source=$taskImageSource; sha256=$taskImageSavedHash; byte_copy_verified=$true; validation='用户提供的结构参考长图；尚未单独确认此图案例的生成验证状态' }
}
$taskManifestPath = Join-Path $taskRoot '资料库/归档清单.json'
if ([System.IO.File]::Exists($taskManifestPath)) { throw 'Manifest already exists; review before a second archival run.' }
[System.IO.File]::WriteAllText($taskManifestPath, ($taskManifest | ConvertTo-Json -Depth 8), $taskUtf8)
[pscustomobject]@{
    case_count = $taskCaseEntries.Count
    original_utf16_length = $taskOriginal.Length
    reconstruction_verified = $true
    original_sha256 = $taskRawHash
    image_copy_verified = $true
    image_bytes = (Get-Item -LiteralPath $taskImageTarget).Length
    manifest = $taskManifestPath
} | ConvertTo-Json
