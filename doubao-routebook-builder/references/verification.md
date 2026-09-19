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

- [ ] 输入已读全、画像已确认
- [ ] 8 板块（或按画像裁剪后）齐全，章节编号连续
- [ ] 地图真实经纬度、城市方位正确、图例清晰
- [ ] 每个景点/酒店/交通/体验有真实可访问图片（禁防盗链直链）
- [ ] 所有价格当地货币+人民币换算，标注汇率基准日与来源
- [ ] 商务数据有核实状态标注
- [ ] shot.py lint 0（桌面+移动）
- [ ] embed 无 missing/warnings、<5MB
- [ ] present_files 已交付
