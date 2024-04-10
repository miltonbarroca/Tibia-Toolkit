import os
from pydub import AudioSegment
from pydub.playback import play

AudioSegment.converter = os.path.abspath("C:/Program Files/ffmpeg/ffmpeg.exe")

def play_sound():     
    sound = AudioSegment.from_wav("sound/evacuation_alarm.wav")
    play(sound)
