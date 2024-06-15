class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Not recoginze file format!")
        self.filename = filename
    

class MP3File(AudioFile):
    ext='mp3'
    def __init__(self, filename):
        super().__init__(filename)
        
    def play(self):
        print(f"Play {self.filename} as mp3.")

class WavFile(AudioFile):
    ext='wav'
    def __init__(self, filename):
        super().__init__(filename)
    
    def play(self):
        print(f"Play {self.filename} as wav.")

class FlacFile:
    ext='flac'
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Not recoginze file format!")
        self.filename = filename
        
    def play(self):
        print(f"Play {self.filename} as flac.")

a = MP3File('music.mp3')
a.play()

b = WavFile('music.wav')
b.play()

#c = MP3File('music.wav')
#c.play()

d = FlacFile('music.flac')
d.play()