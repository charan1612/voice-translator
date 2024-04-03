from flask import Flask, render_template, request, jsonify
import googletrans
import gtts
import pygame
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', languages=googletrans.LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    translate_text = data['text']
    target_language = data['language']

    translator = googletrans.Translator()
    translated_text = translator.translate(translate_text, dest=target_language).text

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    audio_filename = f"static/voice_{timestamp}.mp3"

    converted_audio = gtts.gTTS(translated_text, lang=target_language)
    converted_audio.save(audio_filename)
    
    pygame.mixer.init()
    pygame.mixer.music.load(audio_filename)
    pygame.mixer.music.play()

    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
