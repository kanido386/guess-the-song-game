# -*- coding: utf-8 -*-

# https://www.learncodewithmike.com/2020/02/python-kkbox-open-api.html

import requests
import credentials

def get_access_token():
  
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

  access_token = requests.post(url, headers=headers, data=data)
  return access_token.json()['access_token']


# https://docs-en.kkbox.codes/#get-/charts
def get_chart_playlists():  # TODO:
  
  access_token = get_access_token()

  url = 'https://api.kkbox.com/v1.1/charts'

  headers = {
    'accept': 'application/json',
    'authorization': f'Bearer {access_token}'
  }

  params = {
    'territory': 'TW',    # Allowed: HK, JP, MY, SG, TW
    'offset': 0,
    'limit': 30
  }

  response = requests.get(url, headers=headers, params=params)
  result = response.json()["data"]
  for item in result:
    print(item['id'], item['title'])
    print('==============================')


# https://docs-en.kkbox.codes/#get-/charts/{playlist_id}/tracks
def get_tracks_of_chart_playlist(playlist_id):  # TODO:

  access_token = get_access_token()

  url = f'https://api.kkbox.com/v1.1/charts/{playlist_id}/tracks'

  headers = {
    'accept': 'application/json',
    'authorization': f'Bearer {access_token}'
  }

  params = {
    'territory': 'TW',    # Allowed: HK, JP, MY, SG, TW
    'offset': 0,
    'limit': 30
  }

  response = requests.get(url, headers=headers, params=params)
  result = response.json()["data"]
  for item in result:
    # print(item)
    print(get_cleaner_name(item['album']['artist']['name']))
    print(get_cleaner_name(item['name']))
    print('==============================')


def get_cleaner_name(name):   # TODO:

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


# get_chart_playlists()
get_tracks_of_chart_playlist('HZsJnXizzAH64_DrMp')  # TODO: