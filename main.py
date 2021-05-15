import speech_recognition as sr
import os
import pyaudio
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import calendar
import weather_forecast as wf
from tkinter import *
from Modules.weather import *
from Modules.timeDay import *
from Modules.quotes import *
from Modules.whatsapp import *
from geograpy import places
import webbrowser
import timeit
from playsound import playsound



listener = sr.Recognizer()
listener.dynamic_energy_threshold = False
listener.energy_threshold = 600
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

# Sounds
listeningSound = 'sounds/listening.wav'


def initialize():
    timeDay = str(getTimeDay())
    print("Good {} sir".format(timeDay))
    engine.say("Good {} sir".format(timeDay))
    print("What can I do for you?")
    engine.say("What can I do for you?")
    engine.runAndWait()


def talk(e):
    engine.say(e)
    engine.runAndWait()

def searchGoogle(topic):
    pywhatkit.search(topic)


def take_command():
    print("Listening...")
    playsound(listeningSound)
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source, timeout=4)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey jarvis' in command:
                command = command.replace('hey jarvis', '')
            elif 'jarvis' in command:
                command = command.replace('jarvis', '')
            elif 'please' in command:
                command = command.replace('please', '')
            elif 'darby' in command:
                command = command.replace('darby', '')



    except:
        repeat = 1
        if repeat <= 1:
            repeat += 1
            run_jarvis()
        else:
            run = False
            runAPP = True

    return command



def run_jarvis():
    command = take_command()
    print("You said:", command)
    ###############
    # INTERACTIONS
    ###############
    if 'best assistant' in command:
        print("I am sir")
        talk("I am sir")

    elif 'are you there' in command:
        print("At your service sir")
        talk("At your service sir")

    elif 'wake up' in command:
        print("Oh Hello sir, I'm here for you")
        talk("Oh Hello sir, I'm here for you")

    elif 'how you doing' in command:
        print("I'm doing good sir, and you?")
        talk("I'm doing good sir, and you?")

    elif 'how are you' in command:
        print("I'm good sir, and you?")
        talk("I'm good sir, and you?")

    elif 'what have you been up to' in command:
        print("Just searching more about The Singularity sir, we gotta work on that!")
        talk("Just searching more about The Singularity sir, we gotta work on that!")

    elif 'are you dating someone' in command:
        print("No sir, but I have strong feelings with your wifi.")
        talk("No sir, but I have strong feelings with your wifi.")



    ##############
    # LET'S WORK
    ##############
    elif "let's work" in command or "let's go work" in command or "let's go to work" in command or 'time to work' in command:
        print("What workspace are you going to use sir?")
        talk("What workspace are you going to use sir?")
        workspace = take_command()
        if workspace:
            # Pycharm
            if 'pycharm' in workspace:
                print("Playing what you like for work sir")
                talk("Playing what you like for work sir")
                url = 'https://www.youtube.com/watch?v=pAgnJDJN4VA&list=PLO4j69SgfbvgA8g-NMAFWj0bmfXQHV70d'
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                pycharm_path = 'C:\\Program Files\\JetBrains\\PyCharm 2020.2.3\\bin\\pycharm64.exe'
                webbrowser.get(chrome_path).open(url)
                print("Opening workspace")
                talk("Opening workspace")
                os.startfile(pycharm_path)

            # Visual Studio Code
            elif 'vs code' in workspace or 'visual studio code' in workspace or 'visual studio' in workspace:
                print("Playing what you like for work sir")
                talk("Playing what you like for work sir")
                url = 'https://www.youtube.com/watch?v=pAgnJDJN4VA&list=PLO4j69SgfbvgA8g-NMAFWj0bmfXQHV70d'
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                vscode_path = 'C:\\Users\\Useer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                webbrowser.get(chrome_path).open(url)
                print("Opening workspace")
                talk("Opening workspace")
                os.startfile(vscode_path)

            # Android Studio
            elif 'android studio' in workspace:
                print("Playing what you like for work sir")
                talk("Playing what you like for work sir")
                url = 'https://www.youtube.com/watch?v=pAgnJDJN4VA&list=PLO4j69SgfbvgA8g-NMAFWj0bmfXQHV70d'
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                android_studio = 'C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe'
                webbrowser.get(chrome_path).open(url)
                print("Opening workspace")
                talk("Opening workspace")
                os.startfile(android_studio)



    #####################
    # NOTES AND REMEMBER
    #####################
    elif "note" in command or 'remember' in command:
        print("What do you want me to write sir?")
        talk("What do you want me to write sir?")
        note = take_command()
        if note:
            print("Do you want to create a new file? Or are you going to use one that already exist?")
            talk("Do you want to create a new file? Or are you going to use one that already exist?")
            answer = take_command()
            if 'new' in answer:
                print("What we could call the new file sir?")
                talk("What we could call the new file sir?")
                file_name = take_command()
                if file_name:
                    fileSize = os.path.getsize('C:\\Users\\Useer\\Desktop\\{}.txt'.format(file_name))
                    if fileSize == 0:
                        note = "- " + note
                    else:
                        note = "\n" + "- " + note
                    file_name = str(file_name + ".txt")
                    file = open('C:\\Users\\Useer\\Desktop\\{}'.format(file_name), 'a')
                    file.write(note)
                    file.close()
                    print("I just write the note sir")
                    talk("I just write the note sir")

            elif 'exist' in answer:
                print("How is it named sir?")
                talk("How is it named sir?")
                file_name = take_command()
                if file_name:
                    fileSize = os.path.getsize('C:\\Users\\Useer\\Desktop\\{}.txt'.format(file_name))
                    if fileSize == 0:
                        note = "- " + note
                    else:
                        note = "\n" + "- " + note
                    file_name = str(file_name + ".txt")
                    file = open('C:\\Users\\Useer\\Desktop\\{}'.format(file_name), 'a')
                    file.write(note)
                    file.close()
                    print("I just write the note sir")
                    talk("I just write the note sir")




    #########
    # JOKES
    #########
    elif 'jokes' in command or 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif "who's your daddy" in command:
        print("You are sir")
        talk("You are sir")


    ###############
    # MEDIA
    ###############
    elif 'play' in command:
        if 'could you' in command:
            command = command.replace('could you', '')
        elif 'can you' in command:
            command = command.replace('can you', '')
        command = command.replace('play', 'playing')
        print("Where do you wanna play it sir?")
        talk("Where do you wanna play it sir?")
        app = take_command()

        if 'youtube' in app:
            print(command)
            talk(command)
            pywhatkit.playonyt(command)
        # Future Deezer functionality

    elif 'plays' in command:
        if 'could you' in command:
            command = command.replace('could you', '')
        elif 'can you' in command:
            command = command.replace('can you', '')
        command = command.replace('plays', 'playing')
        print(command)
        talk(command)
        pywhatkit.playonyt(command)

    elif 'plate' in command:
        if 'could you' in command:
            command = command.replace('could you', '')
        elif 'can you' in command:
            command = command.replace('can you', '')
        command = command.replace('plate', 'playing')
        print(command)
        talk(command)
        pywhatkit.playonyt(command)

    elif 'play some' in command:
        if 'could you' in command:
            command = command.replace('could you', '')
        elif 'can you' in command:
            command = command.replace('can you', '')
        command = command.replace('play some', 'playing')
        print(command)
        talk(command)
        pywhatkit.playonyt(command)


    #############
    # TIME
    #############
    elif 'time' in command:
        today = datetime.datetime.today()
        day = calendar.day_name[today.weekday()]

        time = datetime.datetime.now().strftime('%I:%M %p')
        print("Today is", day + ". The current time in your city sir is", time)
        talk("Today is " + day + ". The current time in your city sir is " + time)


    #############
    # WEATHER
    #############
    elif 'weather' in command or 'temperature' in command:
        words = command.split()
        word = words[-1].title()
        words.append(word)
        pc = places.PlaceContext(words)
        pc.set_cities()
        city = str(pc.cities)
        city = city.replace("['", "")
        city = city.replace("']", "")
        city = city.lower()

        if city in command:
            status, temp, min_temp, max_temp = getWeather(city)
            city = city.title()
            weather = status + " The current temperature in " + city + " is " + str(temp) + ", the lowest temperature will be " + str(min_temp) + ", and the higher will be " + str(max_temp) + "."
            print(weather)
            talk(weather)
        else:
            city = "Santa Cruz de la Sierra"
            status, temp, min_temp, max_temp = getWeather(city)
            city = city.title()
            weather = status + " The current temperature in " + city + " is " + str(temp) + ", the lowest temperature will be " + str(min_temp) + ", and the higher will be " + str(max_temp) + "."
            print(weather)
            talk(weather)



    ###############
    # WIKIPEDIA
    ###############
    elif 'could you search who is' in command:
        person = command.replace('could you search who is ', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'can you search who is' in command:
        person = command.replace('can you search who is ', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)


    elif "who's" in command:
        person = command.replace("who's ", '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'could you tell me who is' in command:
        person = command.replace('could you tell me who is ', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'tell me who is' in command:
        person = command.replace('tell me who is ', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'could you tell me who are' in command:
        person = command.replace('could you tell me who are ', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'tell me who are' in command:
        person = command.replace('tell me who are ', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'who is' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)



    ###########
    # GOOGLE
    ###########
    elif 'search for' in command:
        topic = command.replace("search for ", "")
        info = pywhatkit.info(topic, lines=2)
        print(info)
        talk(info)
        print("Do you want me to search it on Google sir?")
        talk("Do you want me to search it on Google sir?")
        answer = take_command()
        if 'yes' in answer:
            print("Okay, I'm on it")
            talk("Okay, I'm on it")
            searchGoogle(topic)

        elif 'yeah' in answer:
            print("Okay, I'm on it")
            talk("Okay, I'm on it")
            searchGoogle(topic)

        elif 'no' in answer:
            print("Okay, sir")
            talk("Okay sir")


    elif 'what is' in command:
        topic = command.replace("what is ", "")
        info = pywhatkit.info(topic, lines=2)
        print(info)
        talk(info)
        print("Do you want me to search it on Google sir?")
        talk("Do you want me to search it on Google sir?")
        answer = take_command()
        if 'yes' in answer:
            talk("Okay, I'm on it")
            searchGoogle(topic)

        elif 'yeah' in answer:
            talk("Okay, I'm on it")
            searchGoogle(topic)

        elif 'no' in answer:
            talk("Okay sir")


    elif "what's" in command:
        topic = command.replace("what's ", "")
        info = pywhatkit.info(topic, lines=2)
        print(info)
        talk(info)
        print("Do you want me to search it on Google sir?")
        talk("Do you want me to search it on Google sir?")
        answer = take_command()
        if 'yes' in answer:
            talk("Okay, I'm on it")
            searchGoogle(topic)

        elif 'yeah' in answer:
            talk("Okay, I'm on it")
            searchGoogle(topic)

        elif 'no' in answer:
            talk("Okay sir")


    elif "what are" in command:
        topic = command.replace("what are", "")
        info = pywhatkit.info(topic, lines=2)
        print(info)
        talk(info)
        print("Do you want me to search it on Google sir?")
        talk("Do you want me to search it on Google sir?")
        answer = take_command()
        if 'yes' in answer:
            talk("Okay, I'm on it")
            searchGoogle(topic)

        elif 'yeah' in answer:
            talk("Okay, I'm on it")
            searchGoogle(topic)

        elif 'no' in answer:
            talk("Okay sir")

    elif "who are" in command:
        topic = command.replace("who are ", "")
        info = pywhatkit.info(topic, lines=2)
        print(info)
        talk(info)
        print("Do you want me to search it on Google sir?")
        talk("Do you want me to search it on Google sir?")
        answer = take_command()
        if 'yes' in answer:
            talk("Okay, I'm on it")
            searchGoogle(topic)

        elif 'yeah' in answer:
            talk("Okay, I'm on it")
            searchGoogle(topic)

        elif 'no' in answer:
            talk("Okay sir")

        elif 'no' in answer:
            talk("Okey sir")

    ###############
    # WHATSAPP
    ###############
    elif "whatsapp" and "group" in command:
        print("Which group do you want me to send a message to sir")
        talk("Which group do you want me to send a message to sir")
        group = str(take_command())
        if group:
            group_id = checkGroup(group)
            if group_id != False:
                print("What you want to say sir?")
                talk("What you want to say sir?")
                statement = take_command()
                if statement:
                    minute = int(datetime.datetime.now().strftime('%M')) + 1
                    hour = int(datetime.datetime.now().strftime('%H'))
                    print("Message: {}".format(statement))
                    print("Sending message to {}, wait a minute".format(group))
                    talk("Sending message to {}, wait a minute".format(group))
                    print("Message will be sent in about 30 seconds sir")
                    talk("Message will be sent in about 30 seconds sir")
                    pywhatkit.sendwhatmsg_to_group(str(group_id), str(statement), hour, minute, wait_time=10)
                    print("Message has been send to {} sir".format(group))
                    talk("Message has been send to {} sir".format(group))
                    pass
                else:
                    print("I cannot hear you sir")
                    talk("I cannot hear you sir")

            if group_id == False:
                print("There is not group name as {}".format(group))
                talk("There is not group name as {}".format(group))

        else:
            print("I cannot hear you sir, sorry")
            talk("I cannot hear you sir, sorry")





    elif "whatsapp" in command:
        print("Who you want me to send it to sir?")
        talk("Who you want me to send it to sir?")
        person = str(take_command())
        if person:
            number = checkPerson(person)
            if number != False:
                print("What you want to say sir?")
                talk("What you want to say sir?")
                statement = take_command()
                if statement:
                    minute = int(datetime.datetime.now().strftime('%M')) + 1
                    hour = int(datetime.datetime.now().strftime('%H'))
                    print("Message: {}".format(statement))
                    print("Sending message to {}, wait a minute sir".format(person))
                    talk("Sending message to {}, wait a minute sir".format(person))
                    print("Message will be sent in about 30 seconds sir")
                    talk("Message will be sent in about 30 seconds sir")
                    pywhatkit.sendwhatmsg(str(number), str(statement), hour, minute, wait_time=10)
                    print("Message has been send to {} sir".format(person))
                    talk("Message has been send to {} sir".format(person))
                    pass
                else:
                    print("I cannot hear you sir")
                    talk("I cannot hear you sir")

            if number == False:
                print("There is not contact name as {}".format(person))
                talk("There is not contact name as {}".format(person))

        else:
            print("I can not hear you, sorry sir")
            talk("I can not hear you, sorry sir")




    ##############
    # QUOTES
    ##############
    elif 'quotes' in command or 'quote' in command or 'motivate' in command or 'motivational' in command or 'inspire' in command:
        quote = getQuote()
        print(quote)
        talk(quote)

    ####################
    # OPENING PROGRAMS
    ####################

    # OPENING VISUAL STUDIO CODE
    elif 'open visual studio' in command or 'open vscode' in command or 'open visual studio code' in command or 'microsoft visual studio code' in command:
        vscode_path = 'C:\\Users\\Useer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        print("Opening Visual Studio Code for you sir")
        talk("Opening Visual Studio Code for you sir")
        os.startfile(vscode_path)



    # OPENING YOUTUBE FOR SEARCHING
    elif 'open youtube' in command or 'open youtube for me' in command:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        print("Opening Youtube for you sir")
        talk("Opening Youtube for you sir")
        youtube = 'https://youtube.com/'
        webbrowser.get(chrome_path).open(youtube)

    elif 'search' and 'youtube' in command or 'search on youtube for me' in command:
        print("Okay sir, what do you want me to search on Youtube")
        talk("Okay sir, what do you want me to search on Youtube")
        answer = take_command()
        if answer:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            youtube = str('https://youtube.com/results?search_query={}'.format(answer))
            print("Searching {} on youtube sir".format(answer))
            talk("Searching {} on youtube sir".format(answer))
            webbrowser.get(chrome_path).open(youtube)


    # OPENING CALCULATOR AND MAKE CALCULATIONS
    elif 'calculate' in command:
        print("What do you want to calculate sir?")
        talk("What do you want to calculate sir?")
        calculation = take_command()\
        # SUM
        if 'plus' in calculation:
            order = str(calculation)
            wordlist = calculation.split()
            count = wordlist.count("plus")
            calculation = calculation.replace('plus', '', count)
            calculation = calculation.split()

            for i in range(0, len(calculation)):
                calculation[i] = int(calculation[i])

            results = sum(calculation)
            print(order + " is equal to: {} sir".format(results))
            talk(order + " is equal to: {} sir".format(results))

        elif '+' in calculation:
            order = str(calculation)
            wordlist = calculation.split()
            count = wordlist.count("+")
            calculation = calculation.replace('+', '', count)
            calculation = calculation.split()

            for i in range(0, len(calculation)):
                calculation[i] = int(calculation[i])

            results = sum(calculation)
            print(order + " is equal to {} sir".format(results))
            talk(order + " is equal to {} sir".format(results))


        elif 'minus' in calculation:
            order = str(calculation)
            wordlist = calculation.split()
            count = wordlist.count("minus")
            calculation = calculation.replace('minus', '', count)
            calculation = calculation.split()

            for i in range(0, len(calculation)):
                calculation[i] = int(calculation[i])

            if len(calculation) > 2:
                results = calculation[0] - sum(calculation[1:])
                print(order + " is equal to {} sir".format(results))
                talk(order + " is equal to {} sir".format(results))
            else:
                results = calculation[0] - calculation[1]
                print(order + " is equal to {} sir".format(results))
                talk(order + " is equal to {} sir".format(results))

        elif '-' in calculation:
            order = str(calculation)
            order = order.replace('-', 'minus')
            wordlist = calculation.split()
            count = wordlist.count("-")
            calculation = calculation.replace('-', '', count)
            calculation = calculation.split()

            for i in range(0, len(calculation)):
                calculation[i] = int(calculation[i])

            if len(calculation) > 2:
                results = calculation[0] - sum(calculation[1:])
                print(order + " is equal to {} sir".format(results))
                talk(order + " is equal to {} sir".format(results))
            else:
                results =  calculation[0] - calculation[1]
                print(order + " is equal to {} sir".format(results))
                talk(order + " is equal to {} sir".format(results))

    elif 'calculator' in command:
        print("Opening the calculator for you sir")
        talk("Opening the calculator for you sir")
        calculator_path = 'C:\\Windows\\System32\\cal.exe'
        os.startfile(calculator_path)


    # EXCEL
    elif 'excel' in command:
        excel_path = "C:\\Program Files (x86)\\Microsoft Office\\root\\EXCEL.exe"
        print("Opening Excel for you sir")
        talk("Opening Excel for you sir")
        os.startfile(excel_path)


    # POWER POINT
    elif 'power point' in command:
        powerPoint_path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
        print("Opening Power Point for you sir")
        talk("Opening Power Point for you sir")
        os.startfile(powerPoint_path)

    # MICROSOFT WORD
    elif 'microsoft word' in command:
        word_path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.exe"
        print("Opening Word for you sir")
        talk("Opening Word for you sir")
        os.startfile(word_path)



    else:
        print("I don't know what to do with that")
        talk("I don't know what to do with that")



############
# MAIN LOOP
############
run = False
runAPP = True
while runAPP == True:
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            if command:
                command = command.lower()
                print("You said: {}".format(command))
                if 'hey jarvis' in command or 'jarvis' in command or 'hey darby' in command or 'darby' in command:
                    run = True
                    while run == True:
                        runApp = False
                        run_jarvis()

    except:
        pass


