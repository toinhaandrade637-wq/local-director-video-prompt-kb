// 全量复核：台账与源重算逐条比对 + 事件唯一性 + 现行 8 页清点
// 稳定版迁自 tmp_batch3_out/_一次性脚本/_audit_full_1105.js（2026-11-07 入口化 P1-11）
// 修复：①退役 K 页路径段→现行 8 页清点 ②事件 b 后缀 regex 误报重号
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const BASE = path.resolve('D:/higgsfield.ai画布/02_完整提示词数据包');
const DIRS = ['THE_LAST_GARDEN', '5_MINUTES', 'DAYLIGHT_SAVING_TIME', 'SIDE_BY_SIDE', 'FOOL_S_GOLD', 'S_KOU', 'THE_SEVENTH_LOOP', 'THE_WRONG_GURDIAN'];

// 1) 源重算
const srcRows = [];
for (const d of DIRS) {
  if (!/^[A-Z0-9_]{2,60}$/.test(d)) throw new Error('非法目录名 ' + d);
  const dir = path.resolve(BASE, d);
  if (!dir.startsWith(BASE + path.sep)) throw new Error('越界 ' + d);
  const jl = fs.readdirSync(dir).filter(f => f.endsWith('.jsonl'));
  const seen = new Map();
  for (const f of jl) {
    for (const line of fs.readFileSync(path.join(dir, f), 'utf8').split('\n')) {
      if (!line.trim()) continue;
      let x; try { x = JSON.parse(line); } catch (e) { continue; }
      const p = x.prompt || x.p || (x.job && x.job.params && x.job.params.prompt) || '';
      if (!p) continue;
      if (!seen.has(p)) seen.set(p, true);
    }
  }
  let i = 0;
  for (const p of seen.keys()) {
    i++;
    srcRows.push(d + '|' + i + '|' + crypto.createHash('sha256').update(p, 'utf8').digest('hex').slice(0, 8) + '|' + p.length);
  }
}
const srcMap = new Map(srcRows.map(s => [s.split('|')[0] + '|' + s.split('|')[1], s]));

// 2) 台账比对
const lp = 'D:/higgsfield.ai画布/06_知识库/维护/逐字阅读台账_T3_33-40.jsonl';
const rows = fs.readFileSync(lp, 'utf8').split('\n').filter(x => x.trim()).map(l => JSON.parse(l));
let mismatch = 0, readTrue = 0;
const byProj = {};
for (const r of rows) {
  const key = r.project + '|' + r.idx;
  const s = srcMap.get(key);
  if (!s) { mismatch++; console.log('台账有而源无:', key); continue; }
  if (s !== r.project + '|' + r.idx + '|' + r.sha8 + '|' + r.len) { mismatch++; if (mismatch < 5) console.log('指纹不符:', key, '台账', r.sha8 + '/' + r.len, '源', s); }
  if (r.read) { readTrue++; byProj[r.project] = (byProj[r.project] || 0) + 1; }
}
const ledgerKeys = new Set(rows.map(r => r.project + '|' + r.idx));
let missing = 0;
for (const s of srcRows) { const k = s.split('|')[0] + '|' + s.split('|')[1]; if (!ledgerKeys.has(k)) { missing++; if (missing < 5) console.log('源有而台账缺:', k); } }
console.log('源重算唯一条数:', srcRows.length, '| 台账行数:', rows.length, '| 指纹/长度不符:', mismatch, '| 源有台账缺:', missing);
console.log('read=true 合计:', readTrue, JSON.stringify(byProj));

// 3) 事件唯一性（b 后缀入键：E169 与 E169b 不算重号）
const ev = fs.readFileSync('D:/higgsfield.ai画布/06_知识库/维护/事件记录.md', 'utf8');
const evNums = [...ev.matchAll(/\| E(\d+)(b?)( \d)? ·/g)].map(m => m[1] + m[2] + (m[3] ? m[3].trim() : ''));
const seen = new Map(); let dupEv = 0;
for (const n of evNums) { if (seen.has(n)) { dupEv++; console.log('事件重号: E' + n); } seen.set(n, 1); }
console.log('事件 E 号:', evNums.length, '个（物理行 ' + (ev.match(/^\| \d{4}-/gm) || []).length + '，fused row E231/E232 同行）, 重号:', dupEv);

// 4) 现行 8 页清点（退役 K 页路径已废，改列现行语义命名页）
const KDIR = 'D:/higgsfield.ai画布/06_知识库/现行知识';
for (const tr of ['视频', '生图', '通用']) {
  for (const f of fs.readdirSync(path.join(KDIR, tr)).filter(f => f.endsWith('.md')).sort()) {
    const t = fs.readFileSync(path.join(KDIR, tr, f), 'utf8');
    const secs = (t.match(/^## [^\n]*(收官蒸馏|重组落地)[^\n]*/gm) || []).length;
    const lines = t.split('\n').length;
    console.log(tr + '/' + f + ': ' + lines + ' 行, 蒸馏节 ' + secs + ' 个');
  }
}
