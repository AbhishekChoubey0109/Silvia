import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from gtts import gTTS
from playsound import playsound
import os
import random


listener = sr.Recognizer()


def talk(text):
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save("speak.mp3")
    playsound("speak.mp3", True)
    os.remove("speak.mp3")


talk('Hi Abhishek,I am Silvia, what can I do for you?')

def take_command():
    try:
        with sr.Microphone() as source:

            print('Listening...')
            listener.adjust_for_ambient_noise(source, duration=0.2)
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language='en')
            command = command.lower()
            print("Did you say "+command)
    except:
        pass
    return command


def run_silvia():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        item = command.replace('what is', '')
        info = wikipedia.summary(item, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'thank you' in command:
        talk('Okay Thank You Abhishek ')
    else:
        talk('Please say the command again.')
    greetings = ["hello silvia", "ok silvia", "hi silvia", "hey silvia","silvia"]
    greetings_rep = ["hi! i am your Assistant! , how can i help you?", "Ohh..!, so its my turn to help you out!",
                     "i am glad to serve!, so what's my task?"]

    if command in greetings:
        rep = random.choice(greetings_rep)
        talk(rep)


while True:
    run_silvia()