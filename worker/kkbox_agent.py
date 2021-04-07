# -*- coding: utf-8 -*-

import requests
import credentials

class KkboxAgent(object):

  def __init__(self):
    self.access_token = None

    self.init_access_token()


  def init_access_token(self):

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
  #   ''' For testing '''
  #   return self.access_token