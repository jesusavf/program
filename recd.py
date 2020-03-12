import speech_recognition as sr
from os import path
from pydub import AudioSegment
song = AudioSegment.from_mp3("jjj.mp3")
song.export("mashupd.wav", format="wav")
filename = "mashupd.wav"

r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data, language="es-US")
    print(text)