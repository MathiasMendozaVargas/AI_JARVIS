import os
import speech_recognition as sr

listener = sr.Recognizer()
listener.dynamic_energy_threshold = False
listener.energy_threshold = 600

try:
    with sr.Microphone() as source:
        print("Listening")
        voice = listener.listen(source, timeout=3)
        command = listener.recognize_google(voice)
        print(command)
        if command:
            command = command.lower()
            print("You said: {}".format(command))
            if 'hey jarvis' in command or 'jarvis' in command or 'hey darby' in command:
                print("hello")

except:
    pass