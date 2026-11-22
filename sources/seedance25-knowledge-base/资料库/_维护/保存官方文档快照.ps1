$ErrorActionPreference = 'Stop'
$taskRoot = 'D:/seedance2.5提示词及结构'
$taskOutput = Join-Path $taskRoot '资料库/03_官方参考'
[void][System.IO.Directory]::CreateDirectory($taskOutput)
$taskUtf8 = [System.Text.UTF8Encoding]::new($false)
$taskOfficialSources = @(
    @{ id='O001'; name='即梦Seedance2.5使用手册'; url='https://bytedance.larkoffice.com/wiki/RXh5ww6EqighMdkVTMccm2d4n7e' },
    @{ id='O002'; name='小云雀Seedance2.5手册'; url='https://bytedance.larkoffice.com/wiki/W5tHwoZIDi12dbk2z3KcFkuUnsf' },
    @{ id='O003'; name='Seedance2.5提示词撰写指南'; url='https://bytedance.larkoffice.com/docx/OsiUdR1OxoDqvnxsK8LczYx7nPd' }
)
$taskSnapshots = @()
foreach ($taskSource in $taskOfficialSources) {
    $taskFetchLines = & lark-cli.cmd docs +fetch --doc $taskSource.url --doc-format markdown --as user
    if ($LASTEXITCODE -ne 0) { throw "Document fetch failed: $($taskSource.id)" }
    $taskFetchResult = ($taskFetchLines -join "`n") | ConvertFrom-Json
    if ($taskFetchResult.ok -ne $true) { throw "Document returned no successful envelope: $($taskSource.id)" }
    $taskDocument = $taskFetchResult.data.document
    $taskBaseName = "$($taskSource.id)_$($taskSource.name)_r$($taskDocument.revision_id)"
    $taskContentPath = Join-Path $taskOutput ($taskBaseName + '.md')
    $taskDataPath = Join-Path $taskOutput ($taskBaseName + '.json')
    if (Test-Path -LiteralPath $taskContentPath) {
        if (-not [string]::Equals([System.IO.File]::ReadAllText($taskContentPath), $taskDocument.content, [System.StringComparison]::Ordinal)) { throw 'Existing snapshot differs; do not overwrite.' }
    } else {
        [System.IO.File]::WriteAllText($taskContentPath, $taskDocument.content, $taskUtf8)
    }
    if (-not (Test-Path -LiteralPath $taskDataPath)) {
        [System.IO.File]::WriteAllText($taskDataPath, ($taskDocument | ConvertTo-Json -Depth 60), $taskUtf8)
    }
    $taskSnapshots += [pscustomobject][ordered]@{
        id=$taskSource.id
        name=$taskSource.name
        source_url=$taskSource.url
        captured_date='2026-10-09'
        document_id=$taskDocument.document_id
        revision_id=$taskDocument.revision_id
        markdown_file=($taskBaseName + '.md')
        document_json_file=($taskBaseName + '.json')
        utf16_length=$taskDocument.content.Length
        sha256=(Get-FileHash -LiteralPath $taskContentPath -Algorithm SHA256).Hash.ToLowerInvariant()
        media_note='仅保存文档正文与接口返回的引用信息，未下载或观看嵌入的视频、图片等媒体。'
    }
}
$taskSnapshotManifest = Join-Path $taskOutput '快照清单_2026-10-09.json'
if (Test-Path -LiteralPath $taskSnapshotManifest) { throw 'Snapshot manifest already exists; review before updating.' }
[System.IO.File]::WriteAllText($taskSnapshotManifest, ($taskSnapshots | ConvertTo-Json -Depth 6), $taskUtf8)
$taskSnapshots | Select-Object id,revision_id,utf16_length,markdown_file | ConvertTo-Json -Depth 3
