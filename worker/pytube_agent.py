# -*- coding: utf-8 -*-

import os
import time
import librosa
from scipy.io.wavfile import write
from pytube import YouTube

# Turn off the warning "PySoundFile failed. Trying audioread instead."
import warnings
warnings.filterwarnings('ignore')

class PytubeAgent(object):
  ''' 下載 YouTube 影片音檔 '''

  def __init__(self, artist_name, song_name, video_url):
    self.filepath = './Audio'
    self.artist_name = artist_name
    self.song_name = song_name
    self.video_url = video_url


  def run(self):
    self.create_audio_folder()
    # TODO: 有重複的就不要再下載了
    self.download()
    self.convert_and_write_file()


  def create_audio_folder(self):
    if not os.path.exists(self.filepath):
      os.mkdir(self.filepath)


  def download(self):
    print(f'{self.artist_name} - {self.song_name}')
    print('（下載中）')

    YouTube(self.video_url) \
      .streams \
      .filter(adaptive=True, only_audio=True) \
      .order_by('abr') \
      .last() \
      .download(output_path=self.filepath, filename='temp')
    

  def convert_and_write_file(self):
    print('（轉檔中）')

    y, sr = librosa.load(f'{self.filepath}/temp.webm')
    y = librosa.util.normalize(y)
    
    if os.path.exists(f'{self.filepath}/temp.webm'):
      os.remove(f'{self.filepath}/temp.webm')
    else:
      print('The file does not exist')

    write(f'{self.filepath}/{self.song_name}.wav', sr, y)
    print('（完成）')
    print('檔案路徑為:', os.path.abspath(f'{self.filepath}/{self.song_name}.wav'))
    print('===================================')