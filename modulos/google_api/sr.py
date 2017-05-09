# Load packages
import pyaudio
import speech_recognition as sr
import sphinxbase
import pocketsphinx

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

r = sr.Recognizer()
with sr.AudioFile('microphone-results.wav') as source:
    audio = r.record(source) # read the entire audio file

try:
    print("You said " +  r.recognize_sphinx(audio))
except LookupError:         # speech is unintelligible
    print("Could not understand audio")
