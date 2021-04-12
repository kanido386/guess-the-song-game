from worker.youtube_agent import YoutubeAgent
import webbrowser

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

      # print(f'{artist} - {song}: {videoUrl}')
      # pytube = PytubeAgent(artist, song, videoUrl)
      # pytube.run()


  def get_tracks_from_txt(self):
    # TODO: 改成讀 txt 檔
    return [('王藍茵', '惡作劇'), ('bruno mars', 'when i was your man')]


if __name__ == '__main__':
  SongDownloader()