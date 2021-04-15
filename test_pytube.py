# -*- coding: utf-8 -*-

# https://github.com/pytube/pytube
from pytube import YouTube

import os
import time
import librosa
from scipy.io.wavfile import write
import numpy as np

# Turn off the warning "PySoundFile failed. Trying audioread instead."
import warnings
warnings.filterwarnings('ignore')

print('==============================')
print('     輸入「stop」來結束程式')
print('==============================')

while True:

  filepath = './Audio'
  video_url = input('輸入影片網址: ')
  if video_url == 'stop':
    break
  song_name = input('輸入歌名: ')
  if song_name == 'stop':
    break

  time.sleep(1)

  print('（下載中）')

  if not os.path.exists(filepath):
    os.mkdir(filepath)

  YouTube(video_url) \
    .streams \
    .filter(adaptive=True, only_audio=True) \
    .order_by('abr') \
    .last() \
    .download(output_path=filepath, filename='temp')

  print('（轉檔中）')

  y, sr = librosa.load(f'{filepath}/temp.webm', mono=False, sr=None)
  if y.shape[0] == 2:
    # stereo
    left, right = y
    left = librosa.util.normalize(left) * 0.5
    right = librosa.util.normalize(right) * 0.5
    # https://stackoverflow.com/questions/3637350/how-to-write-stereo-wav-files-in-python
    y = np.vstack((left, right))
    write(f'{filepath}/{song_name}.wav', sr, y.T)
  else:
    # mono
    y = librosa.util.normalize(y) * 0.5
    write(f'{filepath}/{song_name}.wav', sr, y)

  # ==============================

  # old version

  # y, sr = librosa.load(f'{filepath}/temp.webm')
  # y = librosa.util.normalize(y)

  # write(f'{filepath}/{song_name}.wav', sr, y)

  # ==============================

  # remove webm file
  if os.path.exists(f'{filepath}/temp.webm'):
    os.remove(f'{filepath}/temp.webm')
  else:
    print('The file does not exist')

  print('（完成）')
  
  time.sleep(1)
  
  print('檔案路徑為:', os.path.abspath(f'{filepath}/{song_name}.wav'))
  print('==============================')

  time.sleep(3)