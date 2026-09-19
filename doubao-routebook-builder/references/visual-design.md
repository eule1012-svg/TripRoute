# 视觉设计规范（visual-design）

## 默认配色（浅色系，越南/老挝实践验证；用户点名深色或其他色系才改）

| Token | 值 | 用途 |
|---|---|---|
| `--paper` | `#F8F6F1` | 页面暖纸白背景 |
| `--card` | `#FFFFFF` | 卡片背景 |
| `--teal` | `#0E7C76` | 主色·湄公河青绿（导航、标题、强调） |
| `--teal-deep` | `#0A524E` | 深青（表头、深色强调） |
| `--gold` | `#C08A2D` | 佛塔金（国际航班线、品牌点缀） |
| `--coral` | `#DD6848` | 越南日落珊瑚（直飞亮点、万荣等） |
| `--ink` | `#243331` | 正文 |
| `--ink-soft` | `#5A6E6B` | 次要文字 |
| `--line` | `#E4E0D6` | 边框 |
| `--paper-2` | `#EDF1EC` | 浅色块背景（进度条底等） |
| `--teal-tint` | `#E7F1EE` | 浅青底（表头、hover） |

- 换目的地主题时，用 oklch 在同 hue 轴上派生（固定 hue 调 lightness/chroma），不凭空造 hex。
- 禁大块深色背景（用户已明确嫌"配色太重"）；禁渐变滥用、毛玻璃、粒子网。

## 字体

- 标题/展示：Noto Serif SC（`--font-serif`），正文：Noto Sans SC（`--font-sans`）
- 加载走镜像 `https://miaoda.feishu.cn/fonts/css2?family=Noto+Serif+SC:wght@400;600;700;900&family=Noto+Sans+SC:wght@300;400;500;700&display=swap`（禁直连 Google Fonts）
- 每个 font-family 带完整系统回退栈
- 数据表格数字开 `font-variant-numeric:tabular-nums`

## 组件规范

- **禁 emoji**：所有图标用内联 SVG（`<svg viewBox="0 0 24 24">`），建立风格连贯的图标语言（城市点、交通、标签徽章）
- 标签徽章（`.tag`）：圆角小胶囊，不同主题不同底色（商务=青、自然=绿、文化=金、网红=珊瑚）
- 卡片统一圆角 `--radius`（10–14px）+ 细边框 + 极轻阴影（`rgba(0,0,0,.05)`），禁 glow border
- 章节标题：`sec-num`（衬线大字 01/02…）+ `sec-title` + `sec-rule`（分隔线）+ `sec-sub`（一句话导语）
- 时间轴：grid 三列（时间/轴/内容）像素对齐，圆点居中列 `justify-self:center`，轴线 `calc()` 推导；文字不得与轴线/图标重叠
- 双环图/占比图：用内联 SVG 环形（`stroke-dasharray`），禁 canvas 依赖
- 进度条/阅读进度条：顶部 `#progress` 固定细条

## 图片呈现

- 宽高比：Banner/大图 16:9，卡片图 4:3，竖版内容 3:4；禁止拉伸变形（用 `object-fit:cover` + `aspect-ratio`）
- 所有具象内容（人物、景点、酒店、交通工具）必须真实图片，禁 SVG/CSS 几何冒充
- 图片下方统一 `figcaption` 说明

## 动效红线

- 最多 1–2 个动效锚点；禁全站 fade-in-up、数字 counter、粒子背景
- `prefers-reduced-motion: reduce` 时禁用所有动效
- 展开/收起卡片、灯箱属于响应交互，允许 150–250ms 过渡
