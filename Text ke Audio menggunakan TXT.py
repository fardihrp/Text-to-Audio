from gtts import gTTS
import os

file=open('text.txt')
text=file.read()

language='id'
ubah= gTTS(text=text, lang=language)
ubah.save("audio.mp3")
os.system("audio.mp3")
