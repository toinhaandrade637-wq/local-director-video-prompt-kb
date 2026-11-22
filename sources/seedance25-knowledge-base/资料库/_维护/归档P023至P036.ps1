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
    if ($taskText.StartsWith('制作一支 30 秒、16:9 横屏') -and $taskText.Contains('SCENE BACKGROUND')) { $taskSources += [pscustomobject]@{line=$taskLine;text=$taskText} }
}
if ($taskSources.Count -ne 1) { throw "Expected one user source, got $($taskSources.Count)." }
$taskSource = $taskSources[0]
$taskOriginal = $taskSource.text
function Save-ExactBatchText([string]$RelativePath,[string]$Content) {
    $taskDestination = [System.IO.Path]::GetFullPath((Join-Path $taskRoot $RelativePath))
    $taskPrefix = [System.IO.Path]::GetFullPath($taskRoot).TrimEnd([char[]]@('\','/')) + [System.IO.Path]::DirectorySeparatorChar
    if (-not $taskDestination.StartsWith($taskPrefix,[System.StringComparison]::OrdinalIgnoreCase)) { throw 'Path outside workspace.' }
    [void][System.IO.Directory]::CreateDirectory([System.IO.Path]::GetDirectoryName($taskDestination))
    if (Test-Path -LiteralPath $taskDestination) {
        if (-not [string]::Equals([System.IO.File]::ReadAllText($taskDestination),$Content,[System.StringComparison]::Ordinal)) { throw "Existing archive differs: $RelativePath" }
    } else { [System.IO.File]::WriteAllText($taskDestination,$Content,$taskUtf8) }
    return (Get-FileHash -LiteralPath $taskDestination -Algorithm SHA256).Hash.ToLowerInvariant()
}
$taskSpecs = @(
    @{id='P023';title='日本校园饮料广告_较劲到好感';marker='制作一支 30 秒、16:9 横屏'},
    @{id='P024';title='绿色西装独轮车_参考职责与完整下坡';marker='[REFERENCE CONTROL]'},
    @{id='P025';title='卧室女子与猫_电话与门铃_英文原文';marker='Create a 30-second ultra-realistic'},
    @{id='P026';title='九十年代试镜_单机位情绪递进_英文原文';marker='30-second hyperrealistic SCREEN TEST film'},
    @{id='P027';title='城堡三人密谋_对白反应与烛光_英文原文';marker='SCENE BACKGROUND'},
    @{id='P028';title='高空机舱现金打斗_全局设计_英文原文';marker='Style: 8K large-format photoreal action cinema'},
    @{id='P029';title='四人女团MV_电影与记者画质_英文原文';marker='SCENE CONTEXT: A four-member'},
    @{id='P030';title='竹林剑修与禅师_十五镜_待完善';marker='8K 3D CG写实，PBR物理材质'},
    @{id='P031';title='曼哈顿时停_手持与FPV连续演变_英文原文';marker='ONE CONTINUOUS SHOT — NO CUTS'},
    @{id='P032';title='樱花草原割草_三阶段_逻辑待优化';marker='顶级院线级真人实拍东方玄幻特效电影质感'},
    @{id='P033';title='掌击与灵体剥离_颠倒城市两镜';marker='镜头01｜0:00—0:09｜击中与灵体剥离'},
    @{id='P034';title='冰封遗迹斜向法阵_十五秒蓄力';marker='【全局·画质设定】'},
    @{id='P035';title='九天云海十段组合技_逻辑与效果待优化';marker='镜头贴地跟拍与FPV贴背交错'},
    @{id='P036';title='韩剧雨天错投快递_初次心动';marker='韩剧氛围感，户外白天下雨天'}
)
$taskSearchFrom = 0
foreach ($taskSpec in $taskSpecs) {
    $taskStart = $taskOriginal.IndexOf($taskSpec.marker,$taskSearchFrom,[System.StringComparison]::Ordinal)
    if ($taskStart -lt 0) { throw "Missing boundary: $($taskSpec.id)" }
    if ($taskSpec.id -eq 'P026') {
        $taskOpeningPrefix = "A\`n"
        if ($taskStart -ge $taskOpeningPrefix.Length -and $taskOriginal.Substring($taskStart-$taskOpeningPrefix.Length,$taskOpeningPrefix.Length) -eq $taskOpeningPrefix) { $taskStart -= $taskOpeningPrefix.Length }
    }
    if ($taskSpec.id -eq 'P035') { $taskStart = $taskOriginal.LastIndexOf('【SSS级一句话总合成】',$taskStart,[System.StringComparison]::Ordinal) }
    $taskSpec.start = $taskStart
    $taskSearchFrom = $taskStart + $taskSpec.marker.Length
}
if ($taskSpecs[0].start -ne 0) { throw 'Source prefix would be lost.' }
$taskRawPath = '资料库/00_完整原始消息/用户新增案例原始消息_2026-10-13_十四例与补充意见.txt'
$taskRawHash = Save-ExactBatchText $taskRawPath $taskOriginal
$taskEntries = @()
$taskRebuilt = [System.Text.StringBuilder]::new()
$taskFeedback = @{
    P024='像这个提示词他就是可以是不单单是用视频替换因为其实也已经描述非常清楚的环境啊运动的，可以是直接完善成文生，或者是参考人物场景道具参考生成了'
    P030='像这种的但是还是需要有完善的地方'
    P032='像这种的就是感觉但是战斗逻辑和等等的这些都是很乱的还是有优化的空间'
    P035='这个也是战斗逻辑和施展的这些等等的多杂但是效果还是不太行逻辑有些差'
}
for ($taskIndex=0; $taskIndex -lt $taskSpecs.Count; $taskIndex++) {
    $taskSpec=$taskSpecs[$taskIndex]
    $taskEnd=if($taskIndex+1 -lt $taskSpecs.Count){$taskSpecs[$taskIndex+1].start}else{$taskOriginal.Length}
    if($taskEnd -le $taskSpec.start){throw 'Invalid ordered slice.'}
    $taskSlice=$taskOriginal.Substring($taskSpec.start,$taskEnd-$taskSpec.start)
    $taskCasePath="资料库/01_用户提示词原文/$($taskSpec.id)_$($taskSpec.title).txt"
    $taskHash=Save-ExactBatchText $taskCasePath $taskSlice
    [void]$taskRebuilt.Append([System.IO.File]::ReadAllText((Join-Path $taskRoot $taskCasePath)))
    $taskStatus=switch($taskSpec.id){
        'P030' {'用户指出仍需完善，未具体确认生成效果'}
        'P032' {'用户明确指出战斗逻辑混乱、仍有优化空间'}
        'P035' {'用户明确指出战斗与施展杂乱、效果不太行、逻辑较差'}
        default {'新增研究样本；未单独确认该条生成结果，不继承此前19条的验证状态'}
    }
    $taskEntry=[ordered]@{id=$taskSpec.id;title=$taskSpec.title;path=$taskCasePath;source_start_utf16=$taskSpec.start;source_end_utf16_exclusive=$taskEnd;utf16_length=$taskSlice.Length;sha256_utf8=$taskHash;validation=$taskStatus}
    if($taskFeedback.ContainsKey($taskSpec.id)){
        $taskQuote=$taskFeedback[$taskSpec.id]
        $taskQuotePosition=$taskSlice.IndexOf($taskQuote,[System.StringComparison]::Ordinal)
        if($taskQuotePosition -lt 0){throw "Feedback quote missing: $($taskSpec.id)"}
        $taskEntry.user_feedback_quote=$taskQuote
        $taskEntry.feedback_start_utf16_in_source=$taskSpec.start+$taskQuotePosition
    }
    $taskEntries += $taskEntry
}
if(-not [string]::Equals($taskOriginal,$taskRebuilt.ToString(),[System.StringComparison]::Ordinal)){throw 'Exact reconstruction failed.'}
$taskManifest=[ordered]@{schema_version=1;archived_date='2026-10-13';thread_id='01a11b93-0d5d-72b0-9a10-5b9fa386a1a1';source_user_record_line=$taskSource.line;original_message=@{path=$taskRawPath;utf16_length=$taskOriginal.Length;sha256_utf8=$taskRawHash};fidelity='连续切片保存原文；用户插入的评价和连接标点也保留在原位置。原文字词、语言、反斜杠、HTML实体与占位引用不修订。';reconstruction_verified=$true;cases=$taskEntries}
$taskManifestPath='资料库/归档清单_2026-10-13_P023-P036.json'
$taskManifestHash=Save-ExactBatchText $taskManifestPath ($taskManifest|ConvertTo-Json -Depth 8)
[pscustomobject]@{cases=$taskEntries.Count;first_id='P023';last_id='P036';original_utf16_length=$taskOriginal.Length;exact_reconstruction=$true;manifest=$taskManifestPath}|ConvertTo-Json
