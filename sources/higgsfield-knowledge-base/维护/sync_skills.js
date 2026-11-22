// references 同步：现行知识 → skills（复制+自动三层链接改写；禁手改 references）
// 03/04 为拼接同步：官方依据页 + T3 追补流页 合并重建（幂等，防重复追加）
const fs = require('fs');
const KB = 'D:/higgsfield.ai画布/06_知识库/';
const toRef = t => t.split('../../维护/').join('../../../维护/').split('../../研究记录/').join('../../../研究记录/').split('(../视频/').join('(./');
const FILES = [
  ['现行知识/视频/01-提示词结构.md', 'skills/hf-video-prompt/references/01-提示词结构.md'],
  ['现行知识/视频/02-参考分工.md', 'skills/hf-video-prompt/references/02-参考分工.md'],
  ['现行知识/视频/05-多主体调度.md', 'skills/hf-video-prompt/references/05-多主体调度.md'],
  ['现行知识/视频/06-VFX与合成.md', 'skills/hf-video-prompt/references/06-VFX与合成.md'],
  ['现行知识/视频/07-声音与音频.md', 'skills/hf-video-prompt/references/07-声音与音频.md'],
  ['现行知识/生图/01-生图提示词方法.md', 'skills/hf-image-prompt/references/01-生图提示词方法.md'],
  ['现行知识/生图/02-质感与后期.md', 'skills/hf-image-prompt/references/02-质感与后期.md'],
  ['现行知识/通用/01-色彩与HEX.md', 'skills/hf-image-prompt/references/03-色彩与HEX.md'],
  ['现行知识/通用/02-模型手册.md', 'skills/hf-image-prompt/references/04-模型手册.md'],
  ['现行知识/通用/03-术语表.md', 'skills/hf-image-prompt/references/05-术语表.md'],
];
// [官方依据页, T3 追补流页, 目标 references]
const MERGED = [
  ['现行知识/视频/03-运镜与空间.md', '现行知识/视频/03-镜头语言.md', 'skills/hf-video-prompt/references/03-运镜与空间.md'],
  ['现行知识/视频/04-动作与打戏.md', '现行知识/视频/04-动作与表演.md', 'skills/hf-video-prompt/references/04-动作与打戏.md'],
];
let n = 0;
for (const [src, dst] of FILES) {
  const s = KB + src;
  if (!fs.existsSync(s)) { console.log('缺源跳过: ' + src); continue; }
  fs.writeFileSync(KB + dst, toRef(fs.readFileSync(s, 'utf8')));
  n++;
}
for (const [official, stream, dst] of MERGED) {
  const so = KB + official, ss = KB + stream;
  if (!fs.existsSync(so) || !fs.existsSync(ss)) { console.log('缺源跳过: ' + official + ' / ' + stream); continue; }
  const body = fs.readFileSync(so, 'utf8').trimEnd() + '\n\n---\n\n# T3 追补流（逐项收割实证，自 E863 起）\n\n' + fs.readFileSync(ss, 'utf8').trimStart();
  fs.writeFileSync(KB + dst, toRef(body));
  n++;
}
console.log('同步+三层改写 ' + n + '/' + (FILES.length + MERGED.length));
