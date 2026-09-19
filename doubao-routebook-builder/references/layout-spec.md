# 板块结构与排版规范（layout-spec）

HTML 路书固定 8 大板块（按画像裁剪，见 SKILL.md 板块路由）。所有板块共用一套 CSS 类（模板已内置，见 `assets/routebook-template.html`）。

## 全局结构

```
<body>
  <div id="progress">          ← 阅读进度条（固定顶部）
  <nav> 品牌 + 8 个锚点链接     ← 桌面全显；移动端 overflow-x 滚动、flex:none
  <main>
    <section id="route">01 路线总览
    <section id="days">02 每日行程
    <section id="highlights">03 必体验
    <section id="biz">04 商务考察专题（可选）
    <section id="stay">05 住宿
    <section id="budget">06 预算
    <section id="prep">07 行前信息包
    <section id="booking">08 预订入口汇总
  <footer>
  <div id="lightbox">           ← 图片灯箱
</body>
```

每个板块结构：`<div class="sec-head"><span class="sec-num">NN</span><h2 class="sec-title">…</h2></div><hr class="sec-rule"><p class="sec-sub">一句话导语</p>`。

## 各板块内容规范

### 01 路线总览
- **大地图（全宽）**：`<div class="route-wrap">` 单列布局——地图 `<div class="map-card">` 全宽在上，城市节点 `<div class="route-side" id="cityList">` 网格在下方（桌面 4 列、移动 2 列）。地图 SVG 制作见 `references/map-spec.md`。
- 城市节点卡（JS 渲染 `.city-chip`）：名称 + 停留天数/日段 + 交通方式图例，点击跳转对应日卡片。
- 总览表 `.ov-table`（包在 `.table-scroll` 内，移动端横向滚动）：天 / 日期 / 行程 / 交通方式 / 时长 / 夜宿，15 行逐日列出。

### 02 每日行程
- 顶部筛选条 `#dayFilter`：全部 + 按标签筛选（商务/自然/文化/网红体验/交通/自由日/海边…）；"全部展开/收起"按钮。
- 每日一张 `.day-card`（可展开，默认全部展开）：
  - `.day-head`：D 编号 + 日期 + 主题 + 标签徽章（点击展开/收起，含 aria-expanded、Enter/空格键盘支持）
  - `.day-cols`（**单列**：行程第一行、图片第二行）：
    - 时间线：上午/下午/傍晚/晚上 4 段，每段 时间+内容（含交通、价格当地货币+人民币换算）
    - `.day-imgs`：图片 grid（2 列），`figure > img + figcaption`；图片 `aspect-ratio:4/3`（单图或三图首张 16:9）；点击图片打开灯箱
  - 底部住宿行：名称 + 价格区间 + 评分
- 卡片 `data-tags` 属性供筛选；`data-day` 供地图/必体验跳转。

### 03 必体验（TOP N）
- `.hl-card` 网格卡片：真实图 + 名称 + 一句话亮点 + 价格 + 建议日，`data-jump` 点击展开并跳转对应日。

### 04 商务考察专题（仅考察类诉求）
- 考察背景：行业生态速览（市场格局、头部玩家、最新动态）
- 对标图/表：如支付通道对标（本国既有接口 ↔ 目标国龙头）
- 落地路径时间轴（grid 三列：时间/轴/内容）：注册 → 开户 → 实缴 → 签支付商户 → 联调上线
- 费用测算表：按最低实缴标准测算具体金额（含代理费、规费、实缴资本），标注币种+人民币
- 真实性核验状态表：每项数据标注 已核实/待现场确认/未核实 + 依据来源
- 行业常识与风险提示框（`.warn`）

### 05 住宿
- 策略说明条：住宿策略 + 分配（如 70% 混住青旅 + 30% 特色酒店），配双圆环/环形图
- 特色酒店卡片：外观图 + 房间图 + 名称 + 核心亮点 + 真实价格 + 预订渠道
- 青旅卡片：外观 + 房间实拍 + 混住说明 + 评分（Hostelworld/Booking 等）+ 价格 + 预订渠道

### 06 预算
- 预算条 `.budget-line`（grid 三栏：名称 / 进度条 / 金额区间+占比；**禁悬浮 min/max 标签**，防重叠）
- 人均红线仪表 + 严控后区间
- 省钱 tips（直飞省时、淡季住海景、门票做减法、提前抢促销、混合住宿…）
- 所有金额：当地货币为主 + 人民币括号换算，标注汇率基准日

### 07 行前信息包
- `.prep-grid` **2×2 网格**（桌面两列、移动单列）四张卡：
  1. 签证（网址、费用、时效、停留期、口岸提醒）
  2. 11 月天气速查（城市/白天/夜间/降雨/适合度 表格，`.weather-table` 包 `.table-scroll`）+ 穿衣建议
  3. 货币与支付（汇率、银联/云闪付可用性、现金需求）
  4. 电源与杂项（插头标准、常用 APP、无人机/设备规定）
- 行前包固定 4 卡（签证/天气/货币/电源），保持 2×2；不添加额外核实卡。

### 08 预订入口汇总
- `.book-table`：项目 / 官方/常用入口 / 网址（`<code>` 展示域名）

## 响应式底线（必须实现）
- 桌面 1440 宽：8 板块完整两栏/三栏网格
- 移动 390 宽：所有 grid 变单列或 2 列（chips、day-imgs 2 列）；宽表格 `.table-scroll` 横向滚动（min-width:480px）；导航横向滚动；正文 ≥12px
- 图片按 `aspect-ratio` 固定比例，禁止拉伸变形

## 表格规范（硬性）
- 多列表格必须 `table-layout:fixed` + `<colgroup>` 每列显式宽度合计 100%（防止中文逐字折行撑爆行高）
- 移动端所有宽表包 `.table-scroll{overflow-x:auto}`
