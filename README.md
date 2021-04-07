# guess-the-song-game

### 靈感來源
[三個麻瓜](https://www.youtube.com/channel/UC-Es7ozDeMMPy9_jH6uL5TA) - [另類猜歌九宮格](https://www.youtube.com/watch?v=hhlk5GABq64)

### To-do
- [ ] （youtube_agent.py）拆分成幾個小部分，主要任務是讓使用者拿到影片網址
- [ ] （test_kkbox_open_api.py）Normalize 音檔的聲音大小
- [x] 試試 pafy & vlc 這兩個套件（參考[這篇的最佳回答](https://stackoverflow.com/questions/49354232/how-to-stream-audio-from-a-youtube-url-in-python-without-download)）
- [x] 試用 chinese-word-to-emoji 相關現成套件（試過了 techkang/zh2emoji，可惜不符合我的需求）
- [ ] 研究怎麼 reverse 音檔（也許 pysox 可以做到，如果要用這個套件的話，記得在底下加上安裝說明）

### 實作相關
- [x] 用 YouTube Data API 抓 YouTube 影片的網址
- [x] 用「YouTube 轉 mp3」的相關套件抓歌曲音檔
- [x] 想抓「某某」歌 => 用「某某 lyrics」當關鍵詞搜尋 YouTube => 找最相關的影片當作目標 => 請套件做他該做的事情
- [x] 用 API 或爬蟲抓取 KKBOX 排行榜的歌名

### 遊戲模式
- [ ] 同時播放**多首**歌，讓玩家猜出現在播放的是哪幾首歌
- [ ] 歌詞用純 **emoji** 的方式來顯示，讓玩家依據秀出來的「歌詞 emoji」，猜出這是哪首歌（chinese-word-to-emoji）
- [ ] 用**倒轉**的方式播歌來讓玩家猜
- [ ] 播**間奏**讓玩家猜是哪首歌
- [ ] （發揮創意中）

### 安裝子套件
```
pip install -r requirements.txt
```