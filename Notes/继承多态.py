class audiofile():
    def __init__(self,filename):
        if not filename.endswith(self.ext):#就是下面的ext,ext和下面class是同级的
            raise Exception('未知的文件格式')
        name='存在'
        self.filename=filename
class mp3file(audiofile):
    def __init__(self, filename):
        super().__init__(filename)
    ext='mp3'
    def play(self):
        print('播放{}'.format(self.filename))
class wavfile(audiofile):
    ext='wav'
    def play(self):
        print('wav文件{}'.format(self.filename))
class oggfile(audiofile):
    ext='ogg'
    def play(self):
        print('ogg音频：{}'.format(self.filename))

ogg=oggfile('one.ogg')
ogg.play()
mp3=mp3file('two.mp3')
mp3.play()