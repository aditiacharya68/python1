import os
from gtts import gTTS, tts
tts=gTTS('HEllO')
tts.save ('HELLO.mp3')
os.system("start Aditi.mp3")