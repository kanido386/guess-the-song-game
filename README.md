# guess-the-song-game

### 靈感來源
[三個麻瓜](https://www.youtube.com/channel/UC-Es7ozDeMMPy9_jH6uL5TA) - [另類猜歌九宮格](https://www.youtube.com/watch?v=hhlk5GABq64)

### 實作相關
- [ ] 用 YouTube Data API 抓 YouTube 影片的網址
- [x] 用「YouTube 轉 mp3」的相關套件抓歌曲音檔
- [ ] 想抓「某某」歌 => 用「某某 歌詞」當關鍵詞搜尋 YouTube => 找觀看次數最高且 title 有「歌詞」的影片當作目標 => 請套件做他該做的事情
- [ ] 用 API 或爬蟲抓取 KKBOX 排行榜的歌名

### 遊戲模式
- [ ] 同時播放**多首**歌，讓玩家猜出現在播放的是哪幾首歌
- [ ] 歌詞用純 **emoji** 的方式來顯示，讓玩家依據秀出來的「歌詞 emoji」，猜出這是哪首歌
- [ ] 用**倒轉**的方式播歌來讓玩家猜
- [ ] 播**間奏**讓玩家猜是哪首歌
- [ ] （發揮創意中）

### 安裝子套件
```
pip install -r requirements.txt
```