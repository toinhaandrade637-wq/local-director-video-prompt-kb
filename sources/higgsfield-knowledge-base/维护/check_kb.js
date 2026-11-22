const fs = require('fs');
const path = require('path');
const KB_ROOT = path.resolve(__dirname, '..');
const SAFE = (root, ...segs) => {
  for (const s of segs) {
    if (typeof s !== 'string' || s.includes('/') || s.includes('\\') || s.includes('..')) throw new Error('unsafe: ' + s);
  }
  const t = path.resolve(root, ...segs);
  if (!t.startsWith(root + path.sep)) throw new Error('escape: ' + t);
  return t;
};
let fails = [];
const chk = (name, cond, detail) => { console.log((cond ? '✅' : '❌'), name, detail || ''); if (!cond) fails.push(name); };

// 1. 现行知识方法页状态头（知识树 v2：视频/生图/通用 语义命名，2026-11-05 E230）
const kbDir = SAFE(KB_ROOT, '现行知识');
const ROUTES = ['按任务查.md', '按问题查.md'];
const TRACKS = ['视频', '生图', '通用'];
for (const tr of TRACKS) chk('轨道目录 ' + tr + ' 在位', fs.existsSync(SAFE(kbDir, tr)));
const pages = [];
for (const tr of TRACKS) {
  for (const f of fs.readdirSync(SAFE(kbDir, tr))) {
    if (f.endsWith('.md')) pages.push(tr + '/' + f);
  }
}
chk('双入口路由文件在位', ROUTES.every(r => fs.existsSync(SAFE(kbDir, r))));
chk('工作流程在位', fs.existsSync(SAFE(KB_ROOT, '维护', '工作流程.md')));
chk('来源登记在位', fs.existsSync(SAFE(KB_ROOT, '维护', '来源登记.md')));
chk('待验证问题在位', fs.existsSync(SAFE(KB_ROOT, '维护', '待验证问题.md')));
chk('验证报告在位', fs.existsSync(SAFE(KB_ROOT, '维护', '验证报告.md')));
chk('U+FFFD 清单在位', fs.existsSync(SAFE(KB_ROOT, '维护', 'U+FFFD污染清单.json')));
let rbad = 0;
for (const d of ['skills' + path.sep + 'hf-video-prompt' + path.sep + 'references', 'skills' + path.sep + 'hf-image-prompt' + path.sep + 'references']) {
  const dd = path.join(KB_ROOT, d);
  if (!fs.existsSync(dd)) continue;
  for (const f of fs.readdirSync(dd)) {
    const txt = fs.readFileSync(path.join(dd, f), 'utf8');
    for (const m of txt.matchAll(/\]\(([^)#]+?\.md)\)/g)) {
      if (!fs.existsSync(path.resolve(path.dirname(path.join(dd, f)), m[1]))) rbad++;
    }
  }
}
chk('references 链接可达（真解析）', rbad === 0, String(rbad));
for (const p of pages) {
  const txt = fs.readFileSync(SAFE(kbDir, ...p.split('/')), 'utf8');
  chk(p + ' 状态头', />\s*\*\*状态\*\*/.test(txt) || /\| .*状态/.test(txt.slice(0, 500)), '缺 状态/更新/依据 头');
  chk(p + ' 证据分层', /\*\*证据分层\*\*/.test(txt), '缺证据分层图例');
  chk(p + ' 复审到期', /复审到期/.test(txt), '缺复审到期');
  chk(p + ' 依据标注', /\[实测|\[官方|\[案例|\[用户经验|实测|依据项目/.test(txt), '结论未分层标记');
  chk(p + ' 待验证清单', /待验证/.test(txt), '无生长点');
  chk(p + ' 页头更新日期', /\*\*更新\*\*：20\d\d-\d\d/.test(txt), '页头更新日期缺失或格式错');
  const orphan = (txt.match(/\[案例\](?![^\[]*?[A-Za-z\u4e00-\u9fff])/g) || []).length;
  chk(p + ' [案例] 带项目名', orphan === 0, orphan + ' 条裸 [案例] 无项目名');
}

// 2. 三方一致：现行知识目录 vs 索引.md vs index.json
const ix = fs.readFileSync(SAFE(kbDir, '索引.md'), 'utf8');
const idx = JSON.parse(fs.readFileSync(SAFE(KB_ROOT, 'index.json'), 'utf8'));
const indexedIds = idx.knowledge_pages.map(p => p.id);
for (const p of pages) {
  const fname = p.split('/').pop();
  chk('索引.md 含 ' + fname, ix.includes(fname));
  const ent = idx.knowledge_pages.find(x => x.path === '现行知识/' + p);
  chk('index.json 含 ' + fname, !!ent);
}

// 3. 事件记录有本日条目（每次变更后追加）
const ev = fs.readFileSync(SAFE(KB_ROOT, '维护', '事件记录.md'), 'utf8');
const evCount = (ev.match(/^\| E/gm) || []).length + (ev.match(/^\| \d{4}-/gm) || []).length;
chk('事件记录非空', evCount > 0, String(evCount) + ' 条');

// 4. 资料库指针存在且覆盖
const reg = fs.readFileSync(SAFE(KB_ROOT, '资料库指针.md'), 'utf8');
const regCount = (reg.match(/higgsfield\.ai/g) || []).length;
chk('资料库指针 覆盖 78 项目', regCount >= 78, String(regCount) + ' 个链接');

// 5. 研究记录与现行知识分离（现行知识正文不引用深读笔记作为正文依据）
for (const p of pages) {
  const txt = fs.readFileSync(SAFE(kbDir, ...p.split('/')), 'utf8');
  if (/深读笔记/.test(txt)) fail_suggest(p);
}
function fail_suggest(p) { console.log('⚠️', p, '正文提及深读笔记——应改为引用研究记录路径或直接给结论'); }

// 6. 事件记录完整（深读进度体系已作废移档，E143）
const evPath = SAFE(KB_ROOT, '维护', '事件记录.md');
const evCount2 = (fs.readFileSync(evPath, 'utf8').match(/^\| \d{4}-/gm) || []).length;
chk('事件记录非空', evCount2 > 0, String(evCount2) + ' 条');
chk('旧体系已清档（深读进度不在维护区）', !fs.existsSync(SAFE(KB_ROOT, '维护', '深读进度.md')));

console.log('\n' + (fails.length === 0 ? '★★★ check_kb 通过（' + pages.length + ' 方法页）★★★' : '❌ 失败 ' + fails.length + ' 项: ' + fails.join(' | ')));
if (fails.length > 0) process.exit(1);
