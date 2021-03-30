# -*- coding: utf-8 -*-

import requests
import credentials


# https://www.learncodewithmike.com/2020/02/python-kkbox-open-api.html
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



print(get_access_token())