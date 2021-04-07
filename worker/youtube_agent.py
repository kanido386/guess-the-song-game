# -*- coding: utf-8 -*-

from googleapiclient.discovery import build
import credentials

class YoutubeAgent(object):

  def __init__(self, tracks):
    youTubeApiKey = credentials.youtube['api_key']
    youtube = build('youtube', 'v3', developerKey=youTubeApiKey)
    
    for artist, song in tracks:
      request = youtube.search().list(
        part='snippet',
        q=f'{artist} {song} lyrics',
        type='video'
      )
      response = request.execute()
      # The video that is most relevant to the search query
      firstVideo = response['items'][0]
      videoId = firstVideo['id']['videoId']
      videoUrl = f'https://www.youtube.com/watch?v={videoId}'
      print(f'{artist} - {song}')
      print('影片網址:', videoUrl)
      print('==============================')