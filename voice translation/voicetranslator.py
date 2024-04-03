import googletrans
import speech_recognition as sr
import gtts
import pygame

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("speak now...")
    voice = recognizer.listen(source)
    print("Recognizing...")
    listen = recognizer.recognize_google(voice, language="en")
    print("Input Audio:",listen)

translator = googletrans.Translator()
translate = translator.translate(listen, dest="hi")
print("Translated Text:",translate.text)

converted_audio = gtts.gTTS(translate.text, lang="hi")
converted_audio.save("hello.mp3")
print("Translated Audio:")
pygame.init()
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
