from worker.kkbox_agent import KkboxAgent
from worker.youtube_agent import YoutubeAgent
from worker.pytube_agent import PytubeAgent

class Main(object):

  def __init__(self):
    self.temp_list = None
    self.song_list = None

    self.run()


  def run(self):
    kkbox = KkboxAgent()
    # TODO: it shows KkboxAgent's main goal
    self.temp_list = kkbox.get_tracks()
    # print(self.temp_list)
    youtube = YoutubeAgent(self.temp_list, 'data.txt')
    # youtube.print_song_list()
    self.song_list = youtube.get_song_list()
    # print(self.song_list)
    
    for artist, song, videoUrl in self.song_list:
      # print(f'{artist} - {song}: {videoUrl}')
      pytube = PytubeAgent(artist, song, videoUrl)
      pytube.run()


if __name__ == '__main__':
  Main()