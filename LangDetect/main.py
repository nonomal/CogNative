import speech_recognition as sr
from langdetect import detect

r = sr.Recognizer()

try:
    source = sr.AudioFile('C:/Users/Jonathan/Documents/Study/CSCE483/code/repo/CogNative/CogNative/backend/LangDetect/BillMaher22.wav')
except:
    print("Cannot open file")
    
with source as audio_file:
    audio_cont = r.record(audio_file)
try:
    text = r.recognize_google(audio_cont)
    print("You said: {}".format(text))
    print("Lang: " + detect(text))
except:
    print("Sorry, the langurage cannot be identified. \n")

