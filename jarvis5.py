#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import wikipedia
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
from playsound import playsound


def speak(audioString):
    """Convert text to speech and play it."""
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    playsound("audio.mp3")
    os.remove("audio.mp3")

def recordAudio():
    """Capture audio from the microphone and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("Sorry, the speech service is down.")
    
    return data

def jarvis(data):
    """Respond to user queries."""
    if "how are you" in data:
        speak("I am fine")

    elif "what time is it" in data:
        speak(ctime())

    elif "where is" in data:
        data = data.split(" ")
        location = " ".join(data[2:])  # Join the remaining parts of the command
        speak(f"Hold on, I will show you where {location} is.")
        os.system(f"chromium-browser https://www.google.nl/maps/place/{location}/&")

    elif 'wikipedia' in data:
        speak('Searching Wikipedia...')
        query = data.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'search in browser' in data:
        speak("What should I search?")
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print('Say something!')
            audio = recognizer.listen(source)
            print("Done")
        try:
            search_query = recognizer.recognize_google(audio)
            print(f"Google thinks you said: {search_query}")
            os.system(f"chromium-browser https://www.google.com/search?q={search_query}")
        except sr.UnknownValueError:
            print("Could not understand audio")
            speak("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("Sorry, the speech service is down.")

def main():
    """Main function to run the assistant."""
    time.sleep(2)
    speak("Hi Jarvis, what can I do for you?")
    while True:
        try:
            data = recordAudio()
            jarvis(data)
        except KeyboardInterrupt:
            print("Program exited by user")
            break

if __name__ == "__main__":
    main()

