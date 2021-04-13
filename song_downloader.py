from worker.youtube_agent import YoutubeAgent
import webbrowser
import os
import librosa
from scipy.io.wavfile import write
import numpy as np

# Turn off the warning "PySoundFile failed. Trying audioread instead."
import warnings
warnings.filterwarnings('ignore')

class SongDownloader(object):

  def __init__(self):
    self.temp_list = None   # [('artist1', 'song1'), ('artist2', 'song2'), ...]
    self.song_list = None

    self.run()


  def run(self):
    self.temp_list = self.get_tracks_from_txt()
    youtube = YoutubeAgent(self.temp_list, 'song.txt')
    # youtube.print_song_list()
    self.song_list = youtube.get_song_list()
    # print(self.song_list)
    
    for artist, song, videoUrl in self.song_list:
      temp = videoUrl.split('youtube')
      newUrl = f'{temp[0]}youtubeto{temp[1]}'
      webbrowser.open(newUrl)

    # TODO: 比較 normalize 前後的音質差別
    do_normalize = input('要標準化音檔的音量大小嗎(y/n)？ ')
    if do_normalize == 'y':
      download_folder = '../../Downloads'
      mp3_files = [item for item in os.listdir(download_folder) if '.mp3' in item]
      print(mp3_files)
      for item in mp3_files:
        current_file = f'{download_folder}/{item}'
        # TODO: 會不會有些下載的音檔是 mono？
        y, sr = librosa.load(current_file, mono=False)
        left, right = y
        left = librosa.util.normalize(left)
        right = librosa.util.normalize(right)
        # https://stackoverflow.com/questions/3637350/how-to-write-stereo-wav-files-in-python
        y = np.vstack((left, right))
        write(current_file, sr, y.T)
    else:
      print('fine.')


  def get_tracks_from_txt(self):
    song_list = []

    with open('input.txt', 'r') as f:
      content = f.readlines()
      content = [x.strip() for x in content]
      for item in content:
        artist, song = item.split(' - ')
        song_list.append((artist, song))

    # return [('王藍茵', '惡作劇'), ('bruno mars', 'when i was your man')]
    return song_list


if __name__ == '__main__':
  SongDownloader()