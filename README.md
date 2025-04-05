# 📚 StanCode 101 Python Projects - 王奐鈞 Jay

> 課程成果總覽 | SC101: Programming Methodology  
> Instructor: Jerry Liao

本倉庫整理了我在 SC101 課程中完成的四個核心 Python 專案，每一個專案都結合了圖形界面、資料處理、模擬與爬蟲技術，展現了我在初階程式設計與邏輯思維的學習成果。

---

## 📦 專案目錄

| 作業代號 | 專案名稱                | 技術主題                     |
|----------|-------------------------|------------------------------|
| A1       | Bouncing Ball           | 動畫模擬、物理重力、滑鼠事件 |
| A2       | Breakout Game           | 遊戲開發、碰撞偵測、物件導向 |
| A3       | Ghost Removal           | 影像處理、色彩距離、影像合成 |
| A4       | Baby Names Visualization | 資料視覺化、Tkinter GUI、爬蟲 |

---

## 🎾 A1 - Bouncing Ball

> 模擬一顆小球在畫面中水平移動並受到重力影響，每次落地反彈高度逐漸減小，點擊最多三次後不再啟動。

### 💡 功能亮點
- 模擬重力與彈跳能量耗損
- 點擊觸發動畫，每次重置起點
- 限制最多3次彈跳動畫

### ▶️ 執行方式

```bash
pip install campy
python bouncing_ball.py
```

---

## 🧱 A2 - Breakout Game

> 改編自經典打磚塊遊戲，玩家控制滑鼠平台反彈小球擊破磚塊，球落出畫面會失去一次生命，磚塊全部擊破則獲勝。

### 💡 功能亮點
- 滑鼠控制平台左右移動
- 小球碰牆、自動反彈
- 擁有 3 條命，球掉出畫面會重置
- 磚塊顏色依層次區分，撞擊後消除
- 完整物件導向設計，邏輯與畫面分離

### ▶️ 執行方式

```bash
pip install campy
python breakout.py
```

---

## 👻 A3 - Ghost Removal (StanCodoshop)

> 將多張相同場景照片中的「動態物體」（例如行人、車輛）消除，保留背景生成乾淨的合成圖。

### 💡 功能亮點
- 逐像素計算所有影像的平均 RGB 值
- 選擇顏色距離最小的像素，合成乾淨背景
- 運用簡易圖像處理邏輯實現幽靈去除效果

### ▶️ 執行方式

```bash
pip install pillow
python stanCodoshop.py images/
```

---

## 👶 A4 - Baby Names Visualization & Web Crawler

> 透過 GUI 圖形介面觀察美國嬰兒名字隨時間變化的排名趨勢，並結合網頁爬蟲抓取 SSA 統計資料。

### 💡 功能亮點
- 可輸入多個名字觀察排名變化趨勢
- 使用 Tkinter 圖形介面，顯示折線圖
- 支援模糊搜尋、排名標註、資料爬取
- 爬取 SSA 官網統計，計算前 200 名總人數

### ▶️ 執行方式

#### GUI 視覺化系統

```bash
python babygraphics.py
```

#### SSA 統計資料爬蟲

```bash
pip install requests beautifulsoup4
python webcrawler.py
```

