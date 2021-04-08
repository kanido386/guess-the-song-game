from worker.kkbox_agent import KkboxAgent
from worker.youtube_agent import YoutubeAgent

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
    youtube = YoutubeAgent(self.temp_list)
    # youtube.print_song_list()
    self.song_list = youtube.get_song_list()
    # print(self.song_list)


if __name__ == '__main__':
  Main()