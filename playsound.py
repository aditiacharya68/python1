from gtts import gTTS
from playsound import playsound
audio = 'speech.mp3'

sp = gTTS(text = "I am alive" )

sp.save(audio)
playsound(audio)

