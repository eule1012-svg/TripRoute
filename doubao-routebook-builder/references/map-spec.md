# 真实地图制作规范（map-spec）

路线总览中的地图**优先使用真实地图底图**（Leaflet + 高德/OSM 瓦片），在真实地理底图上标注城市节点和路线。SVG 手绘示意图仅作为离线备选方案。

## 一、城市坐标获取（强制）

1. 用搜索验证每个城市的经纬度（高德/百度/谷歌同源的公开坐标即可，如 time-ok.com、latlong.info、维基）。**不得凭记忆编坐标**。
2. 记录各城市参考经纬度（每次按实际目的地核实）：
   - 北京 39.90°N / 116.41°E
   - 乌兰巴托 47.89°N/106.91°E、特日勒吉 48.05°N/107.45°E、成吉思汗雕像 47.80°N/107.20°E
   - 越南：河内 21.03°N/105.85°E、岘港 16.07°N/108.22°E、胡志明 10.82°N/106.63°E
   - 老挝：琅勃拉邦 19.89°N/102.14°E、万荣 18.93°N/102.45°E、万象 17.97°N/102.60°E

## 二、真实地图方案（首选，Leaflet + 高德瓦片）

### 2.1 引入 Leaflet

```html
<!-- head 中 -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />

<!-- body 底部 -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
```

### 2.2 地图容器

```html
<div id="realmap" style="height:520px;border-radius:10px;z-index:1"></div>
```

### 2.3 初始化地图 + 高德瓦片（国内访问优先）

```javascript
var map = L.map('realmap', {
  center: [中心纬度, 中心经度],
  zoom: 5,
  scrollWheelZoom: false  // 防止页面滚动被地图劫持
});

// 高德瓦片（国内访问稳定）
L.tileLayer('https://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}', {
  subdomains: ['1', '2', '3', '4'],
  attribution: '&copy; 高德地图 AutoNavi',
  maxZoom: 18
}).addTo(map);
```

> 注意：OSM 国际源（tile.openstreetmap.org）在国内/云电脑环境常加载超时，**优先用高德瓦片**。

### 2.4 添加城市标记 + 标签

```javascript
var cities = [
  { name: '乌兰巴托', lat: 47.89, lng: 106.91, day: 1, color: '#0E7C76', desc: 'D1·D4-D6 · 首都' },
  { name: '特日勒吉', lat: 48.05, lng: 107.45, day: 2, color: '#5C7A2E', desc: 'D2-D3 · 国家公园' }
];

cities.forEach(function(city) {
  // 圆形标记
  var marker = L.circleMarker([city.lat, city.lng], {
    radius: 10,
    fillColor: city.color,
    color: '#fff',
    weight: 3,
    fillOpacity: 0.9
  }).addTo(map);
  marker.bindPopup('<b>' + city.name + '</b><br>' + city.desc);
  // 点击跳转到对应日
  marker.on('click', function() {
    var card = document.querySelectorAll('.day-card')[city.day - 1];
    if (card) card.scrollIntoView({behavior: 'smooth', block: 'center'});
  });
  // 永久标签
  L.tooltip({
    permanent: true, direction: 'bottom', offset: [0, -12], className: 'city-label'
  }).setLatLng([city.lat, city.lng]).setContent(
    '<b>' + city.name + '</b><br><span style="font-size:11px">' + city.desc + '</span>'
  ).addTo(map);
});
```

### 2.5 绘制路线

```javascript
// 国际航班（金色虚线）
L.polyline([
  [39.90, 116.41],  // 北京
  [47.89, 106.91]   // 乌兰巴托
], { color: '#C08A2D', weight: 3, dashArray: '9,7' }).addTo(map);

// 境内包车（绿色实线）
L.polyline([
  [47.89, 106.91],  // 乌兰巴托
  [48.05, 107.45]   // 特日勒吉
], { color: '#0E7C76', weight: 3 }).addTo(map);

// 返程（绿色点线，半透明）
L.polyline([...], { color: '#0E7C76', weight: 2.5, dashArray: '5,7', opacity: 0.7 }).addTo(map);
```

### 2.6 自适应缩放

```javascript
var group = L.featureGroup(cities.map(function(c) {
  return L.marker([c.lat, c.lng]);
}));
map.fitBounds(group.getBounds().pad(0.1));
```

### 2.7 标签样式

```css
.leaflet-popup-content-wrapper { border-radius: 10px; }
.leaflet-container { font-family: var(--font-sans); }
.city-label {
  background: transparent; border: none; box-shadow: none;
  font-size: 13px; font-weight: 600; color: #1E3836;
  text-shadow: 0 1px 2px #fff;
}
.city-label::before { display: none; }
```

## 三、SVG 手绘方案（备选，仅离线场景用）

如果无法加载在线瓦片（纯离线交付），可用 SVG 手绘示意图：

- 按真实经纬度线性投影计算 x/y
- 国家色块淡色半透明
- 路线用不同线型区分（国际航班金色虚线、包车绿色实线、返程绿色点线）
- 图注标注关键城市坐标，注明"示意图"

## 四、渲染验证（用户验收必查）

- **截图检查地图瓦片正常加载**：无空白、无裂图、无 `ERR_TIMED_OUT` 错误
- **城市标记位置正确**：在真实地图底图上位置准确，与实际地理位置一致
- **路线线型正确**：国际航班（金色虚线）、包车（绿色实线）、返程（绿色点线）
- **标签可读**：城市名+副标题清晰，不重叠
- **点击交互正常**：点城市标记能跳转到对应日卡片
- **移动端可用**：地图容器高度合适，不溢出，手指可拖动缩放
- **地图 attribution 正确**：footer 标注"地图 © 高德地图 AutoNavi"

## 五、常见坑

- OSM 国际源在国内/云电脑环境加载超时 → **必须用高德瓦片**
- `scrollWheelZoom: false` 必须设，否则页面滚动时会被地图劫持
- 城市标签 `permanent: true` 才会常显，否则 hover 才出现
- `fitBounds` 前要确保所有 marker 已添加，否则缩放范围不对
