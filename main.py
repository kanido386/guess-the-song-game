from worker.kkbox_agent import KkboxAgent

class Main(object):

  def __init__(self):
    self.temp_list = None

    self.run()


  def run(self):
    kkbox = KkboxAgent()
    # TODO: it shows KkboxAgent's main goal
    self.temp_list = kkbox.get_tracks()
    print(self.temp_list)


if __name__ == '__main__':
  Main()