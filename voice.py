import requests
import API
import pygame
import time


def text_to_speech(text, api_key, voice_id="pNInz6obpgDQGcFmaJgB"):
    url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }

    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        },
        "model_id": "eleven_multilingual_v1"
    }

    response = requests.post(url.format(voice_id=voice_id), json=data, headers=headers)

    if response.status_code == 200:
        with open("output.mp3", "wb") as f:
            f.write(response.content)

        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)

        pygame.mixer.quit()

    else:
        print(f"Error: {response.status_code}, {response.text}")

