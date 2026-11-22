// 全维度审查 v2：13 维度只读体检矩阵（不改任何文件）
// 稳定版迁自 tmp_batch3_out/_一次性脚本/_kb_fullaudit_v2_1105.js（2026-11-07 入口化，P1-11）
const fs = require('fs');
const path = require('path');
const KB = 'D:/higgsfield.ai画布/06_知识库/';
const WS = 'D:/higgsfield.ai画布/';
const J = p => path.join(KB, p);
const toRefX = t => t.split("../../维护/").join("../../../维护/").split("../../研究记录/").join("../../../研究记录/").split("(../视频/").join("(./");
const ok = [];
const bad = [];
const chk = (name, cond, detail) => { (cond ? ok : bad).push(name + (detail ? '｜' + detail : '')); };
const rd = p => { try { return fs.readFileSync(p, 'utf8'); } catch (e) { return null; } };

// 1 语料台账
const led = rd(WS + '06_知识库/维护/逐字阅读台账_T3_33-40.jsonl') || rd(J('维护/逐字阅读台账_T3_33-40.jsonl'));
let rows = [], readN = 0;
if (led) { rows = led.split('\n').filter(x => x.trim()).map(l => { try { return JSON.parse(l); } catch (e) { return null; } }).filter(Boolean); readN = rows.filter(r => r.read).length; }
chk('台账 1,496 行', rows.length === 1496, '实际 ' + rows.length);
chk('台账 read=1,496（T3 #33-40 八项目战役满员）', readN === 1496, '实际 ' + readN);
const dump = rd(WS + 'tmp_batch3_out/_verbatim_dst.txt');
const dstCount = dump ? (dump.match(/^◆◆ DST #/gm) || []).length : 0;
chk('DST 转储 235 条', dstCount === 235, '实际 ' + dstCount);

// 2 事件链（fused row 口径：E231/E232 同物理行，物理行数=逻辑号数-1）
const ev = rd(J('维护/事件记录.md')) || '';
const evRows = (ev.match(/^\| \d{4}-/gm) || []).length;
const e232 = (ev.match(/\| E232 /g) || []).length, e230 = (ev.match(/\| E230 /g) || []).length;
chk('事件物理行 ' + evRows + '（fused row E231/E232 同行，逻辑号=物理行+1）', evRows > 0 && e230 === 1 && e232 === 1, '物理行 ' + evRows);

// 3 来源登记
const src = rd(J('维护/来源登记.md')) || '';
const s43 = (src.match(/\| S43 \|/g) || []).length, s42 = (src.match(/\| S42 \|/g) || []).length;
chk('来源 S42/S43 各 1', s42 === 1 && s43 === 1, 'S42=' + s42 + ' S43=' + s43);

// 4 现行知识 12 页结构
const tracks = ['现行知识/视频', '现行知识/生图', '现行知识/通用'];
let pages = [];
for (const tr of tracks) for (const f of fs.readdirSync(J(tr))) if (f.endsWith('.md')) pages.push(tr + '/' + f);
chk('方法页 12 页', pages.length === 12, pages.map(p => p.split('/')[1]).join(','));
let headFail = [], linkFail = [];
for (const p of pages) {
  const t = rd(J(p)) || '';
  const fname = p.split('/').pop();
  if (!/\*\*状态\*\*/.test(t) || !/\*\*更新\*\*：20\d\d-\d\d/.test(t) || !/复审到期/.test(t)) headFail.push(fname + ':头');
  if (!/\*\*证据分层\*\*/.test(t) && !/证据分层\*\*：/.test(t) && !/证据分层/.test(t)) headFail.push(fname + ':分层');
  if (!/待验证/.test(t)) headFail.push(fname + ':待验证');
  if (/视频轨\/|生图轨\//.test(t)) { headFail.push(fname + ':旧路径'); }
  const bare = (t.match(/\[案例\](?![^\[]*?[A-Za-z\u4e00-\u9fff])/g) || []).length;
  if (bare) headFail.push(fname + ':裸案例' + bare);
  for (const m of t.matchAll(/\]\(([^)#]+?\.md)\)/g)) {
    const lp = m[1];
    if (lp.includes('http')) continue;
    const target = path.resolve(J(p), '..', lp);
    if (!fs.existsSync(target)) linkFail.push(fname + '→' + lp);
  }
}
chk('页结构（头/分层/待验证/无旧路径/无裸案例）', headFail.length === 0, headFail.join(',') || '全过');
chk('页内相对链接全部可达', linkFail.length === 0, linkFail.join(',') || '0 断链');

// 5 skills 果实层
const refs = [['现行知识/视频/01-提示词结构.md', 'skills/hf-video-prompt/references/01-提示词结构.md'], ['现行知识/视频/02-参考分工.md', 'skills/hf-video-prompt/references/02-参考分工.md'], ['现行知识/视频/03-运镜与空间.md', 'skills/hf-video-prompt/references/03-运镜与空间.md'], ['现行知识/视频/04-动作与打戏.md', 'skills/hf-video-prompt/references/04-动作与打戏.md'], ['现行知识/视频/05-多主体调度.md', 'skills/hf-video-prompt/references/05-多主体调度.md'], ['现行知识/视频/06-VFX与合成.md', 'skills/hf-video-prompt/references/06-VFX与合成.md'], ['现行知识/视频/07-声音与音频.md', 'skills/hf-video-prompt/references/07-声音与音频.md'], ['现行知识/生图/01-生图提示词方法.md', 'skills/hf-image-prompt/references/01-生图提示词方法.md'], ['现行知识/生图/02-质感与后期.md', 'skills/hf-image-prompt/references/02-质感与后期.md'], ['现行知识/通用/01-色彩与HEX.md', 'skills/hf-image-prompt/references/03-色彩与HEX.md'], ['现行知识/通用/02-模型手册.md', 'skills/hf-image-prompt/references/04-模型手册.md'], ['现行知识/通用/03-术语表.md', 'skills/hf-image-prompt/references/05-术语表.md']];
let syncBad = 0;
for (const [a, b] of refs) { const x = rd(J(a)), y = rd(J(b)); const exp = x ? toRefX(x) : ''; if (!x || !y || y !== exp) syncBad++; }
chk('skills 2 SKILL + references 12/12 与树干逐字一致', syncBad === 0 && fs.existsSync(J('skills/hf-video-prompt/SKILL.md')) && fs.existsSync(J('skills/hf-image-prompt/SKILL.md')) && fs.existsSync(J('维护/sync_skills.js')), '不一致 ' + syncBad);

// 6 路由与机器目录
const ix = rd(J('现行知识/索引.md')) || '';
const idxRaw = rd(J('index.json'));
let idxOK = false, idxPaths = 0;
try { const idx = JSON.parse(idxRaw); idxPaths = idx.knowledge_pages.filter(p => fs.existsSync(J(p.path))).length; idxOK = idx.version === '0.2.0' && idxPaths === 12; } catch (e) { }
chk('index.json v0.2.0 且 12 路径全部存在', idxOK, '存在 ' + idxPaths + '/12');
let routeBad = [];
for (const rel of ['现行知识/索引.md', '现行知识/按任务查.md', '现行知识/按问题查.md']) {
  const t = rd(J(rel)) || '';
  for (const m of t.matchAll(/\]\(([^)#]+?\.md)\)/g)) {
    const target = path.resolve(J(rel), '..', m[1]);
    if (!fs.existsSync(target)) routeBad.push(rel.split('/').pop() + '→' + m[1]);
  }
  if (/视频轨\/|生图轨\//.test(t)) routeBad.push(rel + ':旧路径');
}
chk('路由三件链接可达且无旧路径', routeBad.length === 0, routeBad.join(',') || '0 断链');
chk('索引含 skills 果实层', ix.includes('hf-video-prompt') && ix.includes('hf-image-prompt'));

// 7 宪法/入口/清单
const bp = rd(J('知识库建设蓝图.md')) || '', agents = rd(J('AGENTS.md')) || '', readme = rd(J('README.md')) || '';
const html = rd(J('流程图.html')) || '', qd = rd(J('维护/知识库完善总清单.md')) || '';
chk('蓝图现行纯净+历史已外迁', bp.includes('现行定稿：2026-11-05') && bp.includes('_archive_历史档案/建设蓝图_历史档案') && !bp.includes('# ⛔ 历史档案'));
chk('AGENTS/README 含 v2 通告且无旧路径', agents.includes('知识树 v2') && readme.includes('知识树 v2') && !/视频轨\/|生图轨\//.test(agents + readme));
chk('流程图节点语义化', html.includes('生图/01') && !/K09|K10|K11/.test(html));
chk('完善总清单 A-E 五节+三战役✅', /## A\.|## B\.|## C\.|## D\.|## E\./.test(qd) && qd.includes('7L 收官'));

// 8 研究记录/页面史
chk('页面史存档 2 份', fs.existsSync(J('研究记录/页面史_旧版_运镜与空间_2026-11-05.md')) && fs.existsSync(J('研究记录/页面史_旧版_质感与后期_2026-11-05.md')));
const t3 = rd(WS + '06_知识库/研究记录/T3批量_33-40.md') || rd(J('研究记录/T3批量_33-40.md')) || '';
chk('研究记录含 7L 收官轮', t3.includes('7L') || t3.includes('THE_SEVENTH_LOOP'));

// 9 实践记录
chk('实践记录/任务索引 在位', fs.existsSync(J('实践记录/任务索引.md')));

// 10 记忆层
const mem = rd('C:/Users/26430/.zcode/cli/memories/projects/higgsfield.ai-2f12b5825e8c1965/memory/knowledge-base-pattern.md') || '';
chk('记忆含知识树 v2 落地记录', mem.includes('知识树 v2 重组落地'));

// 11 范本提取区（只读）
chk('两范本提取区在位', fs.existsSync(WS + '_ref_kb_extract/imagegen') && fs.existsSync(WS + '_ref_kb_extract/seedance25'));

// 12 维护工具
chk('维护工具三件在位', fs.existsSync(J('维护/check_kb.js')) && fs.existsSync(J('维护/sync_skills.js')) && fs.existsSync(J('维护/工作流程.md')));

// 13 待验证/验证报告
chk('待验证问题+验证报告在位', fs.existsSync(J('维护/待验证问题.md')) && fs.existsSync(J('维护/验证报告.md')));

console.log('=== 全维度审查矩阵 ===');
for (const l of ok) console.log('✅ ' + l);
for (const l of bad) console.log('❌ ' + l);
console.log('=== ' + ok.length + ' 过 / ' + bad.length + ' 不过 ===');
