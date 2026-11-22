// count_blocks.js — 块频统计固定口径工具（E140 来源可溯审判 P1-5）
// 口径：读指定 JSONL（支持 {jid,m,p} 与 {job_id,model,prompt} 双 schema）→ 按 jid/job_id 去重 →
//       对每条提示词逐行匹配行首 ALL-CAPS 块头（≥5 字符，正则固定如下）→ 计数。
// 用法：node count_blocks.js <jsonl路径...>   （多文件合并统计）
// 输出：块头 ×次数，降序。K 页 ×N 一律以本脚本输出为准，禁止手记。
const fs = require('fs');
const files = process.argv.slice(2);
if (!files.length) { console.log('用法: node count_blocks.js <jsonl...>'); process.exit(1); }
const seen = new Set();
const prompts = [];
for (const f of files) {
  for (const l of fs.readFileSync(f, 'utf8').split('\n')) {
    if (!l.trim()) continue;
    try {
      const x = JSON.parse(l);
      const id = x.jid || x.job_id || x.id || null;
      const p = x.p || x.prompt || '';
      if (id && seen.has(id)) continue;
      if (id) seen.add(id);
      if (p) prompts.push(p);
    } catch (e) {}
  }
}
const heads = {};
for (const p of prompts) {
  for (const line of p.split('\n')) {
    const m = line.match(/^([A-Z][A-Z0-9 &/'"().,\-—:]{4,60})(?=\s*(?::|—|-|$))/);
    if (m) {
      const h = m[1].trim().replace(/\s+/g, ' ');
      if (h.length >= 5) heads[h] = (heads[h] || 0) + 1;
    }
  }
}
console.log('语料: ' + files.length + ' 文件 / ' + prompts.length + ' 条唯一提示词');
const sorted = Object.entries(heads).sort((a, b) => b[1] - a[1]);
for (const [h, n] of sorted.slice(0, 60)) console.log(String(n).padStart(6) + '×  ' + h);
console.log('（块型总数: ' + sorted.length + '）');
