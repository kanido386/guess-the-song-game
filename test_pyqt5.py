# PyQt 入門，用 Python 寫第一支 GUI
# https://zhung.com.tw/article/pyqt入門用python寫第一支gui/

from sys import flags
from typing import Text
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import vlc
import os
import time

import test as ui

class Main(QMainWindow, ui.Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

    self.instance = vlc.Instance()
    self.player = self.instance.media_player_new()
    self.cwd = os.getcwd()
    # self.dir = '../'
    # self.file = 'test.mp3'
    # self.media = self.instance.media_new(os.path.join(self.dir, self.file))
    # self.player.set_media(self.media)
    self.dir = None
    self.file = None
    self.media = None
    self.song_length = None
    
    self.timer = QTimer(self)
    # self.timer.timeout.connect(self.update_func)
    self.timer.timeout.connect(self.on_timer)
    # TODO:
    self.i = 0
    
    # PyQt - QSlider Widget & Signal
    # https://www.tutorialspoint.com/pyqt/pyqt_qslider_widget_signal.htm
    self.horizontalSlider_2.sliderPressed.connect(self.progress_slider)
    
    self.horizontalSlider.valueChanged.connect(self.volume_slider)
    self.horizontalSlider.setMinimum(0)
    self.horizontalSlider.setMaximum(200)
    # FIXME:
    self.volume = 100
    self.horizontalSlider.setValue(self.volume)

    self.horizontalSlider_2.setEnabled(False)
    self.pushButton_5.setEnabled(False)
    self.pushButton_2.setEnabled(False)

    # How to pass arguments to functions by the click of button in PyQt?
    # https://stackoverflow.com/questions/6784084/how-to-pass-arguments-to-functions-by-the-click-of-button-in-pyqt
    self.pushButton_4.clicked.connect(self.get_file_and_set_audio)
    self.pushButton_5.clicked.connect(lambda: self.toggle_play_pause())
    self.pushButton_2.clicked.connect(lambda: self.stop())
    self.pushButton_3.clicked.connect(lambda: self.toggle_mute_unmute())


  def progress_slider(self):

    progress = self.horizontalSlider_2.value() / self.song_length
    self.player.set_position(progress)
    self.i = int(self.horizontalSlider_2.value() // 1000)
    print(self.i)
    self.label.setText(str(self.i))
    print(f'test: {self.player.get_position()}')


  def volume_slider(self):

    self.volume = self.horizontalSlider.value()
    self.player.audio_set_volume(self.volume)



  def on_timer(self):

    self.i += 1
    self.label.setText(str(self.i))

    # vlc.State
    # http://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.State-class.html
    if self.player.get_state() == vlc.State.Playing:
      self.song_length = self.player.get_length()
      # print(length)
      # https://www.tutorialspoint.com/pyqt/pyqt_qslider_widget_signal.htm
      self.horizontalSlider_2.setMinimum(0)
      self.horizontalSlider_2.setMaximum(self.song_length)
      time = self.player.get_time()
      # print(time)
      self.horizontalSlider_2.setValue(time)

      self.player.audio_set_volume(self.volume)



  def update_func(self):
    # TODO:
    self.i += 1
    self.label.setText(str(self.i))



  def get_file_and_set_audio(self):

    # TODO:
    self.i = 0
    
    fname = QFileDialog.getOpenFileName(self, 'Open file', self.cwd, "Audio files (*.mp3 *.wav)")
    file_path = fname[0]
    self.media = self.instance.media_new(file_path)
    # FIXME:
    playurl = 'https://r2---sn-u4h-un5e.googlevideo.com/videoplayback?expire=1621868420&ei=I2urYK7jOsb2rQSlgLDACw&ip=61.64.1.190&id=o-AOeGt3evf0T1WAtlSGNjR0sT4rgDgfWGzdrKKbDiC9TP&itag=18&source=youtube&requiressl=yes&mh=Ec&mm=31%2C29&mn=sn-u4h-un5e%2Csn-u4o-u2xs&ms=au%2Crdu&mv=m&mvi=2&pl=24&initcwndbps=1318750&vprv=1&mime=video%2Fmp4&ns=TAdc378vImyFE-zgGPsv3oEF&gir=yes&clen=4945865&ratebypass=yes&dur=226.092&lmt=1575105455899496&mt=1621846606&fvip=2&fexp=24001373%2C24007246&beids=9466585&c=WEB&txp=5531432&n=OTo8vGKXLiPd8Mdf&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgJTEVnKfjnoyP6Ks9xq5KOpLDqCdcCdPelO2BuD0k0eECIA50XOeyeWOSxxmIYt9hAi9u9ilu15CNom6NAT5D9QCo&sig=AOq0QJ8wRQIgOx7rUrlo335XQYlIeEBSkkeCSxu15klpvfRdNL0RlVcCIQCOMAYQ7WWS8VpHQ7LFozYgAfJqsLoj4sXivhYwTd0sjw=='
    self.player.set_mrl(playurl, ':no-video')
    # self.player.set_media(self.media)

    song_name = file_path.split('/')[-1].split('.')[0]
    # self.label.setText(song_name)
    # TODO:
    self.label.setText(str(self.i))

    time.sleep(0.3)

    self.horizontalSlider_2.setEnabled(True)
    self.pushButton_5.setEnabled(True)
    self.pushButton_2.setEnabled(True)

    self.toggle_play_pause()



  # PyQt5 Signal / Slot 機制入門
  # https://jimmylab.wordpress.com/2018/07/12/pyqt5-signal-slot/
  def toggle_play_pause(self):
    print(self.player.get_state())
    # TODO: very messy
    if self.player.get_state() == vlc.State.Stopped:
      # 按 Stop 後再按 Play
      self.pushButton_5.setText('Pause')
      self.player.play()
      self.timer.start(1000)
      time.sleep(0.3)
      progress = self.horizontalSlider_2.value() / self.song_length
      print(f'why? {progress}')
      self.player.set_position(progress)
      self.i = int(self.horizontalSlider_2.value() // 1000)
      print(self.i)
      self.label.setText(str(self.i))
      print(f'test: {self.player.get_position()}')
    elif self.pushButton_5.text() == 'Play':
      self.pushButton_5.setText('Pause')
      self.player.play()
      self.timer.start(1000)
    else:
      self.pushButton_5.setText('Play')
      self.player.pause()
      self.timer.stop()


  def stop(self):
    self.player.stop()
    self.pushButton_5.setText('Play')
    self.timer.stop()
    # TODO:
    self.i = 0
    self.label.setText(str(self.i))
    self.horizontalSlider_2.setValue(0)


  def toggle_mute_unmute(self):
    if self.pushButton_3.text() == 'Mute':
      self.pushButton_3.setText('Unmute')
      self.player.audio_set_mute(True)
    else:
      self.pushButton_3.setText('Mute')
      self.player.audio_set_mute(False)


if __name__ == '__main__':
  import sys
  app = QtWidgets.QApplication(sys.argv)
  window = Main()
  window.show()
  sys.exit(app.exec_())