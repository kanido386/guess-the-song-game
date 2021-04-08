# -*- coding: utf-8 -*-

from googleapiclient.discovery import build
import credentials

class YoutubeAgent(object):

  def __init__(self, tracks):
    self.youtube = None
    self.tracks = tracks
    self.song_list = []

    self.init_youtube()
    self.init_song_list()


  def init_youtube(self):
    youTubeApiKey = credentials.youtube['api_key']
    self.youtube = build('youtube', 'v3', developerKey=youTubeApiKey)


  def init_song_list(self):
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