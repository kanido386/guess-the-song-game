# -*- coding: utf-8 -*-

import json
from googleapiclient.discovery import build
import credentials

class YoutubeAgent(object):

  def __init__(self, tracks):
    self.youtube = None
    self.tracks = tracks
    self.song_list = []

    self.init_youtube()
    self.init_song_list()
    self.save_song_list()


  def init_youtube(self):
    youTubeApiKey = credentials.youtube['api_key']
    self.youtube = build('youtube', 'v3', developerKey=youTubeApiKey)


  def init_song_list(self):
    # TODO: 拆成讀檔的 init ＆ 從 YouTube 抓的版本
    for artist, song in self.tracks:
      request = self.youtube.search().list(
        part='snippet',
        q=f'{artist} {song} lyrics',
        type='video'
      )
      response = request.execute()
      # The video that is most relevant to the search query
      firstVideo = response['items'][0]
      videoId = firstVideo['id']['videoId']
      videoUrl = f'https://www.youtube.com/watch?v={videoId}'
      self.song_list.append((artist, song, videoUrl))
      # 邊處理邊印出，讓使用者有被回饋的感覺！
      print(f'{artist} - {song}')
      print('影片網址:', videoUrl)
      print('==============================')


  def print_song_list(self):
    for artist, song, videoUrl in self.song_list:
      print(f'{artist} - {song}')
      print('影片網址:', videoUrl)
      print('==============================')


  def get_song_list(self):
    return self.song_list


  def save_song_list(self):
    # TODO: 以第一個為主來當作參考資料（畢竟是 list）
    # https://pythonexamples.org/python-list-to-json/
    # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
    with open('data.txt', 'w', encoding='utf-8') as outfile:
      # http://litaotju.github.io/python/2016/06/28/python-json-dump-utf/
      json.dump(self.song_list, outfile, ensure_ascii=False)

    # TODO: 用下面的 list 來判別有無重複
    test = [f'{item[0]} - {item[1]}' for item in self.song_list]
    print(test)