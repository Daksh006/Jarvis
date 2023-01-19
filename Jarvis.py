from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Started The Jarvis : Wait For Few Seconds More")
from Main import MainTaskExecution
from Main import Shutdown
import datetime
import requests
from bs4 import BeautifulSoup
import speedtest_cli


def MainExecution():
    Speak("Hello Sir")
    Speak("I'm Jarvis, I'm Ready To Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        elif "whatsapp message" in Data or "message" in Data:
            pass

        elif "shut down"  in Data or "close down" in Data or "power off" in Data :
            Speak("Are You sure you want to shutdown")
            Reply = Shutdown()

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)

        elif "the time" in  Data or 'what is the time'  in Data or 'could you please tell the time' in Data:
                          strTime = datetime.datetime.now().strftime("%I:%M %p")
                          print(f"\n\tIt is {strTime}")
                          Speak(f"Sir the time is {strTime}")
                          pass

        elif "temperature" in Data:
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            Speak(f"currect{search} is {temp}")
        
        elif "weather" in Data:
            search = "weather in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            Speak(f"currect{search} is {temp}")

        elif "speedtest" in Data:
            wifi = speedtest_cli.Speedtest()
            upload_net = wifi.upload()/1048576
            download_net = wifi.download()/1048576
            print("Wifi Upload Speed is", upload_net)
            print("Wifi download speed is ",download_net)
            Speak(f"Wifi download speed is {download_net}")
            Speak(f"Wifi Upload speed is {upload_net}")
        
        elif "youtube" in Data:
            from Features.SearchNow import searchYoutube
            searchYoutube(Data)

        elif "wikipedia" in Data:
            from Features.SearchNow import searchWikipedia
            searchWikipedia(Data)

        elif "google" in Data:
            from Features.SearchNow import searchGoogle
            searchGoogle(Data)

        elif "sleep" in Data:
            Speak("Ok sir , You can me call anytime")
            break 




                          
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
    else:
        pass

ClapDetect()

