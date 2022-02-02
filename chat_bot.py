import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def talkbot():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                talk(command)
    except():
        pass
    return command


def run_command():
    command = talkbot()
    # print(command)
    if "play" in command:
        song = command.replace('play', '')
        print(' playing...')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)

        talk('time is ' + time)
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'single' in command:
        print('I am in relationship with google')
        talk('I am in relationship with google')
    elif 'marry' in command:
        print('No, i can not marry with you because i love google')
        talk('no i can not marry with you because i love google')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'krishna' in command:
        print('krishna is my boss he is genius he is my god he is super hero')
        talk('Krishna is my boss he is genius he is my god he is super hero')
    elif 'vikas' in command:
        print('vikas is Mota he is fatty ,he is a donkey and monkey both ha ha ha')
        talk('vikas is Mota he is fatty ,he is a donkey and monkey both ha ha ha')
    else:
        print('i could not understand , please say it again')
        talk('i could not understand , please say it again')


while True:
    run_command()
