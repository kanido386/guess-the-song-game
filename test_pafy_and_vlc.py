# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/49354232/how-to-stream-audio-from-a-youtube-url-in-python-without-download

import pafy
import vlc
from time import sleep



# https://stackoverflow.com/questions/57623123/control-vlc-player-using-python-vlc-module
# TODO: 包成 class，也許可結合 keyboard，讓使用者能夠暫停、換一首歌之類的操作
# https://www.daniweb.com/programming/tutorials/523626/creating-a-gui-wrapper-for-vlc-media-player-in-python-wxpython
# TODO: 用個 GUI 介面，讓整個操作更方便！



''' Get correct / best URL from youtube using pafy '''
# url = 'https://www.youtube.com/watch?v=pM9zZinLvkA'
# TODO: 下面的連結會有 bug（因為喜歡不喜歡數都是0，待修，跟pafy有關，也許可發PR）
# url = 'https://www.youtube.com/watch?v=MUXF1RHzVbU'
url = 'https://www.youtube.com/watch?v=vjTKB65XXKM'
video = pafy.new(url)
best = video.getbest()
playurl = best.url
print(playurl)



''' Use VLC to play it (multiple ways can do this) '''
# https://www.geeksforgeeks.org/vlc-module-in-python-an-introduction/
# media = vlc.MediaPlayer(playurl)
# media.play()
# TODO: can also play local file! (this project may use this)
# player = vlc.MediaPlayer('../test.mp3')   # relative path
# print(player.play())

# https://stackoverflow.com/questions/49354232/how-to-stream-audio-from-a-youtube-url-in-python-without-download
# Instance = vlc.Instance()
# player = Instance.media_player_new()
# Media = Instance.media_new(playurl)
# Media.get_mrl()
# player.set_media(Media)
# player.play()

# https://forum.videolan.org/viewtopic.php?t=150336
audioPlayer = vlc.MediaPlayer(vlc.Instance())
# audioPlayer.set_mrl(playurl)
audioPlayer.set_mrl(playurl, ':no-video')
audioPlayer.play()



''' To play the song, need to add dummy loop '''
# https://stackoverflow.com/questions/43272532/python-vlc-wont-start-the-player/57583062#57583062
sleep(5)    # Or however long you expect it to take to open vlc
while audioPlayer.is_playing():
  sleep(1)