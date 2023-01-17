import math
import os
import time
import webbrowser
import pyautogui
import speech_recognition as sr
import datetime
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")





language = "en"
pesquisa = ""
r = sr.Recognizer()


def pc_talk(ole):
    speak.Speak(ole)


while True:
    with sr.Microphone() as source:
        pc_talk("Say hello to start")
        audio_text = r.listen(source)
        try:
            command = (r.recognize_google(audio_text))
            oi = str(command).lower()
        except:
            print("No mic")
    if "hello" in oi:
        while True:
            pesquisa = ""
            link = ""
            city = ""
            word = ""
            pc_talk("Hello, what you want to do?")
            with sr.Microphone() as source:
                print("talk")
                audio_text = r.listen(source)
                print("Time over")
            try:
                command = (r.recognize_google(audio_text))
                new_command = str(command).lower()
                print(new_command)

            except:
                print("Erro Audio")

            if "open" in new_command or "start" in new_command:
                split_command_open = new_command.split()
                search = ""
                b = 0
                for a in split_command_open:
                    if a == " ":
                        split_command_open.pop(b)
                        b = b + 1
                if "open" in new_command:
                    index_open = split_command_open.index("open")
                if "start" in new_command:
                    index_open = split_command_open.index("start")
                for i in range(index_open + 1, len(split_command_open)):
                    search = search + split_command_open[i]
                link = "www." + search + ".com"
                webbrowser.open(link)

            if "play " in new_command or "music" in new_command:
                split_command = new_command.split()
                if "play" in new_command:
                    index_play = int(split_command.index("play"))
                if "music" in new_command:
                    index_play = int(split_command.index("music"))
                for i in range(index_play + 1, len(split_command)):
                    word = split_command[i]
                    pesquisa = pesquisa + "+" + word
                print(pesquisa)

                link = "www.youtube.com/results?search_query=" + pesquisa
                webbrowser.open(link)
                time.sleep(5)
                pyautogui.click(533, 325)

            if "what is" in new_command or "give me the meaning of" in new_command:
                split_command = new_command.split()
                if "what is" in new_command:
                    index_wiki = int(split_command.index("is"))
                if "give me the meaning of" in new_command:
                    index_wiki = int(split_command.index("of"))
                for i in range(index_wiki + 1, len(split_command)):
                    word = split_command[i]
                    if len(word) > 2:
                        pesquisa = pesquisa + "_" + word
                print(pesquisa)
                link = "https://en.wikipedia.org/wiki/" + pesquisa
                webbrowser.open(link)

            if "search" in new_command or "look for" in new_command or "google" in new_command:
                split_command = new_command.split()
                if "search" in new_command:
                    index_pesquisa = int(split_command.index("search"))
                if "look for" in new_command:
                    index_pesquisa = int(split_command.index("for"))
                if "google" in new_command:
                    index_pesquisa = int(split_command.index("google"))
                for i in range(index_pesquisa + 1, len(split_command)):
                    word = split_command[i]
                    pesquisa = pesquisa + word
                print(pesquisa)
                link = "https://www.google.com/search?q=" + pesquisa
                webbrowser.open(link)

            if "weather in" in new_command:
                split_command = new_command.split()
                index_weather = int(split_command.index("in"))
                city = split_command[index_weather + 1]
                webbrowser.open("https://www.weather-forecast.com/locations/" + city + "/forecasts/latest")

            if "hours" in new_command or "time" in new_command:
                now = datetime.datetime.now()
                actual_date = (
                        str(now.day) + "/" + str(now.month) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(
                    now.minute) + ":" + str(now.second))
                pc_talk(actual_date)

            if "what's" in new_command or "give me" in new_command or "tell me" in new_command or "whats" in new_command:
                split_command_math = new_command.split()
                if "+" in new_command:
                    plus_index = split_command_math.index("+")
                    n1 = int(split_command_math[plus_index - 1])
                    n2 = int(split_command_math[plus_index + 1])
                    pc_talk(n1 + n2)
                if "-" in new_command:
                    minus_index = split_command_math.index("-")
                    n1 = int(split_command_math[minus_index - 1])
                    n2 = int(split_command_math[minus_index + 1])
                    pc_talk(n1 - n2)
                if "*" in new_command:
                    multi_index = split_command_math.index("*")
                    n1 = int(split_command_math[multi_index - 1])
                    n2 = int(split_command_math[multi_index + 1])
                    pc_talk(n1 * n2)
                if "/" in new_command:
                    div_index = split_command_math.index("/")
                    n1 = int(split_command_math[div_index - 1])
                    n2 = int(split_command_math[div_index + 1])
                    pc_talk(n1 / n2)
                if "factorial of" in new_command:
                    fact_index = split_command_math.index("factorial")
                    n1 = int(split_command_math[fact_index + 1])
                    pc_talk(math.factorial(n1))
                if "square root of" in new_command:
                    square_index = split_command_math.index("root")
                    n1 = int(split_command_math[square_index + 2])
                    pc_talk(pow(n1, 1 / 2))
                if "cube root of" in new_command or "cubic root of" in new_command:
                    cube_index = split_command_math.index("root")
                    n1 = int(split_command_math[cube_index + 2])
                    pc_talk(pow(n1, 1 / 3))
                if " sine of" in new_command:
                    sin_index = split_command_math.index("sine")
                    n1 = int(split_command_math[sin_index + 2])
                    pc_talk(math.sin(math.radians(n1)))
                if "cosine of" in new_command:
                    cos_index = split_command_math.index("cosine")
                    n1 = int(split_command_math[cos_index + 2])
                    pc_talk(math.cos(math.radians(n1)))
                if "tangent of" in new_command:
                    tan_index = split_command_math.index("tangent")
                    n1 = int(split_command_math[tan_index + 2])
                    pc_talk(math.tan(math.radians(n1)))

            if "close" in new_command:
                os.system("taskkill /F /IM chrome.exe")

            if "nothing" in new_command or "exit" in new_command:
                break
            else:
                print("nothing to open")
