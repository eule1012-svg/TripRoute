# 验证与交付规范（verification）

## 一、运行环境判定

- SystemPrompt `Computer OS` 为 Windows/Mac → 本地电脑；其他 → 云电脑
- 云电脑：图片必须内嵌（Base64），交付 `_embed.html`
- 本地电脑：图片相对路径 `assets/`，交付原 HTML + 提醒"连目录一起发送"

## 二、自检（每次修改后必跑）

使用 html Skill 的 `scripts/shot.py`（**禁止**用 artifacts-preview 等其它校验，防 Debug 螺旋）：

```bash
python3 /home/user/.doubao/agent_mode/workspace/.skills/html/scripts/shot.py <html_path>   # 桌面+移动
```

- 看报告次序：先 lint（`consoleErrors` 优先）→ Read 截图视觉核对 → 有疑点再针对性裁剪查看
- 逐项核对：地图城市方位、每日卡片（行程第一行/图片第二行）、行前包 2×2、预算条无重叠、表格移动端横向滚动、导航不溢出、图片比例正常
- lint 有报错按对应 Hint 修复后重跑；`responsiveChartIssues` 触发时核对移动截图

## 三、内嵌（云电脑交付前）

```bash
python3 /home/user/.doubao/agent_mode/workspace/.skills/html/scripts/embed.py <html_path>
```

- 产物：同目录 `<原文件名>_embed.html`；改动只改原 HTML，改完重跑 embed
- 检查输出：`missing: []` 且 `warnings: []`；产物 <5MB（图片超重先跑 `scripts/compress_images.py`）
- 内嵌版也要跑一次 shot.py 自检

## 四、交付

- 用 present_files 交付唯一 HTML 文件（交付内嵌版，不额外附一套"以防万一"）
- 交付说明必须写明：核实范围、未核实/待确认项、汇率基准日、图片来源处理方式（下载→压缩→本地化）
- 最终回复 ≤300 字、≤8 行

## 五、多产物补充（按用户要求）

- 报价表：按用户模板样式（如【HMA20260903】你好北京 xlsx），sheet Skill 建飞书在线表交付
- 飞书文档备份 / zip 打包：按用户要求执行（lark-doc / lark-drive Skill）
- 所有交付物路径在回复中列出

## 六、回归检查清单（交付前逐项过）

### 基础检查
- [ ] 输入已读全、画像已确认（商务考察需求已深入追问：行业、方向、目标）
- [ ] 8 板块（或按画像裁剪后）齐全，章节编号连续
- [ ] 所有价格当地货币+人民币换算，标注汇率基准日与来源
- [ ] 商务数据有核实状态标注（已核实/待现场确认/未核实）
- [ ] shot.py consoleErrors 为空（桌面+移动）
- [ ] shot.py resourceErrors 为空（无加载失败资源）
- [ ] 内嵌版无 missing/warnings、<5MB
- [ ] present_files 已交付

### 图片验证（用户必查项）
- [ ] **Hero 头图是真实风景大图**（禁 SVG 插画/几何图冒充）
- [ ] **每日行程中所有提到的景点/餐饮/酒店都配了真实图片**（无占位符）
- [ ] 每张图片内容与描述匹配（无张冠李戴）
- [ ] 图片清晰完整、无水印、非占位图
- [ ] 所有图片正常显示（resourceErrors 为空）
- [ ] 图片比例正确（object-fit:cover，无拉伸变形）
- [ ] 无重复图片滥用（同一张图用在不同景点处）

### 地图验证（用户必查项）
- [ ] **使用真实地图底图**（Leaflet + 高德瓦片），非纯 SVG 手绘示意图
- [ ] **所有城市/景点都有真实经纬度坐标**（已搜索验证，非凭记忆编造）
- [ ] **城市标记在真实地图底图上位置准确**，与实际地理位置一致
- [ ] 路线线型清晰区分（国际航班金色虚线、包车绿色实线、返程绿色点线）
- [ ] 地图瓦片正常加载（无空白、无裂图、无超时错误）
- [ ] 点击城市标记能跳转到对应日行程卡片
- [ ] 地图 attribution 正确标注

### 商务考察验证（用户必查项）
- [ ] 商务考察板块包含：市场概览、政策/税费、资质要求、落地路径、行程安排
- [ ] 行程中安排了具体的考察动作（市场走访、拜访机构等）
- [ ] 每项数据标注核实状态
- [ ] 考察目标明确（用户想了解什么、最终达成什么结果）
