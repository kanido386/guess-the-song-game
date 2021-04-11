# -*- coding: utf-8 -*-

import requests
import credentials

class KkboxAgent(object):
  ''' 抓取 KKBOX 排行榜的歌名 '''

  def __init__(self):
    self.access_token = None
    self.chart_playlists = []
    self.playlist_id = None
    self.playlist_title = None
    self.tracks = []

    self.init_access_token()
    self.init_chart_playlists()
    self.print_chart_playlists_and_ask()
    self.init_tracks_of_chart_playlist()
    # self.print_tracks()


  def init_access_token(self):
    ''' Init access token for future use '''

    url = 'https://account.kkbox.com/oauth2/token'

    headers = {
      'Host': 'account.kkbox.com',
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
      'grant_type': 'client_credentials',
      'client_id': credentials.kkbox['client_id'],
      'client_secret': credentials.kkbox['client_secret']
    }

    self.access_token = requests.post(url, headers=headers, data=data).json()['access_token']


  # def get_access_token(self):
  #   ''' (for testing) '''
  #   return self.access_token


  def init_chart_playlists(self):
    ''' Init chart playlists '''

    url = 'https://api.kkbox.com/v1.1/charts'

    headers = {
      'accept': 'application/json',
      'authorization': f'Bearer {self.access_token}'
    }

    params = {
      'territory': 'TW',    # Allowed: HK, JP, MY, SG, TW
      'offset': 0,
      'limit': 30
    }

    response = requests.get(url, headers=headers, params=params)
    result = response.json()["data"]
    for item in result:
      self.chart_playlists.append((item['id'], item['title']))


  def print_chart_playlists_and_ask(self):
    ''' Print chart playlists and ask user choose one from the list '''

    for i, (_id, title) in enumerate(self.chart_playlists):
      print(f'{i:>2}: {title}')

    print('===================================')
    print('從上面選一個吧！')
    the_id = int(input(f'請輸入數字：'))
    self.playlist_id = self.chart_playlists[the_id][0]
    self.playlist_title = self.chart_playlists[the_id][1]
    print(f'您選了【{self.playlist_title}】！')
    print('===================================')


  def init_tracks_of_chart_playlist(self):
    ''' Init tracks of the chosen chart playlist '''

    url = f'https://api.kkbox.com/v1.1/charts/{self.playlist_id}/tracks'

    headers = {
      'accept': 'application/json',
      'authorization': f'Bearer {self.access_token}'
    }

    params = {
      'territory': 'TW',    # Allowed: HK, JP, MY, SG, TW
      'offset': 0,
      'limit': 5            # TODO: modify this
    }

    response = requests.get(url, headers=headers, params=params)
    result = response.json()["data"]
    for item in result:
      # print(item)
      artist = self.get_cleaner_name(item['album']['artist']['name'])
      song = self.get_cleaner_name(item['name'])
      self.tracks.append((artist, song))
      # print(artist)
      # print(song)
      # print('==============================')


  # def print_tracks(self):
  #   ''' (for testing) '''
  #   for artist, song in self.tracks:
  #     print(artist)
  #     print(song)
  #     print('==============================')
  #   # print(self.tracks)


  def get_tracks(self):
    ''' The most important part of this module '''
    return self.tracks


  @staticmethod
  def get_cleaner_name(name):
    '''
    For example:
    turn
    "想見你想見你想見你 (Miss You 3000) - 電視劇<想見你>片尾曲"
    to
    "想見你想見你想見你"
    '''

    cleaner_name = name

    # turn
    # "想見你想見你想見你 (Miss You 3000) - 電視劇<想見你>片尾曲"
    # to
    # "想見你想見你想見你 (Miss You 3000)"
    cleaner_name = cleaner_name.split(' -')[0]

    # turn
    # "想見你想見你想見你 (Miss You 3000)"
    # to
    # "想見你想見你想見你"
    cleaner_name = cleaner_name.split(' (')[0]

    return cleaner_name