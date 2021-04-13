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