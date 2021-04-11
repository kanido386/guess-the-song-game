# -*- coding: utf-8 -*-

# https://developers.google.com/youtube/v3/docs/search/list
from googleapiclient.discovery import build

import credentials

youTubeApiKey = credentials.youtube['api_key']
youtube = build('youtube', 'v3', developerKey=youTubeApiKey)

print('==============================')
print('     輸入「stop」來結束程式')
print('==============================')

while True:
  query = input('請輸入歌曲名稱: ')
  if query == 'stop':
    break
  artist_name = input('誰的歌？ ')
  if artist_name == 'stop':
    break
  
  request = youtube.search().list(
    part='snippet',
    q=f'{artist_name} {query} lyrics',
    type='video'
  )
  response = request.execute()

  # # Print video url & title of the five most relevant videos
  # for item in response['items']:
  #   videoId = item['id']['videoId']
  #   print(f'https://www.youtube.com/watch?v={videoId}')
  #   print(item['snippet']['title'])
  #   print('-----')

  # The video that is most relevant to the search query
  firstVideo = response['items'][0]

  videoId = firstVideo['id']['videoId']
  videoUrl = f'https://www.youtube.com/watch?v={videoId}'
  print('影片網址:', videoUrl)
  print('==============================')