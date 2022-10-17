
from tabnanny import filename_only
from typing import final
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import requests, json
import pyaudio
from playsound import playsound
from datetime import datetime as dt
import streamlit as st


class VirtualAssitent():



    def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            with st.sidebar:
                code = st.code("I am listening...")
                time.sleep(3)
                code.empty()
                
            audio = r.listen(source)
        data = ""
        try:
            data = r.recognize_google(audio)
            
        
        except sr.UnknownValueError:
            print("Google Speech Recognition did not understand audio")
        except sr.RequestError as e:
            print("Request Failed; {0}".format(e))
        
        return data


    def respond(audioString):
        with st.sidebar:
            code = st.code(audioString)
        tts = gTTS(text=audioString, lang='en')
        tts.save("speech.mp3")
        file = "speech.mp3"
        audio_file = open('speech.mp3', 'rb')
        audio_bytes = audio_file.read()
        audio = st.audio(audio_bytes, format="audio/mp3", start_time=0)
        time.sleep(2)
        #audio.empty()
        #code.empty()

    @classmethod
    def digital_assistant(cls,data):

        if "hey" in data:
            cls.respond("Yes Ser, How Can I Help You.")
            time.sleep(3)
            listening = True


        if "articule" in data:
            cls.respond("I was feeling good, but then, I found in google that Queen Isabelle past away. Rest in Peace.")
            time.sleep(9)
            listening = True

        if "you know me" in data:
            cls.respond("Ofcourse I know you. \nYou are my creator,\nand Iam greatfull of that, Wise George")
            time.sleep(9)
            listening = True

        
        if "how are you" in data:
            cls.respond("So so, not good at all.")
            time.sleep(3)
            listening = True

        if "what time is it" in data:
            cls.respond(ctime())
            time.sleep(9)
            listening = True

        
        #Song
        if "play a song" in data:
            cls.respond("A song you love...")
            os.system("rocknroll.mp3")
            listening = True

        #Where
        if "where is" in data:
            listening = True
            data = data.split(" ")
            location_url = "https://www.google.com/maps/place/" + str(data[2])
            cls.respond("Hold on George, I will show you where " + data[2] + " is.")
            maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
            os.system(maps_arg)


        #Weather
        if "what is the weather in" in data:
            listening = True
            api_key = "Your_API_key"
            weather_url = "http://api.openweathermap.org/data/2.5/weather?"
            data = data.split(" ")
            location = str(data[5])
            url = weather_url + "appid=" + api_key + "&q=" + location 
            js = requests.get(url).json() 
            if js["cod"] != "404": 
                weather = js["main"] 
                temp = weather["temp"] 
                hum = weather["humidity"] 
                desc = js["weather"][0]["description"]
                resp_string = " The temperature in Kelvin is " + str(temp) + " The humidity is " + str(hum) + " and The weather description is "+ str(desc)
                cls.respond(resp_string)
            else: 
                cls.respond("City Not Found") 
            
        #ShutDown
        if "shut down the computer" in data:
            cls.respond("Shuting Down the Computer...\nYes or Not")
            time.sleep(6)
            listening = True
            if "yes" in data:
                os.system('shutdown -s')
            else:
                cls.respond("Ok you can continue working")

        #CleanConsole
        if "clean the console" in data:
            cls.respond("Cleaning Console...")
            os.system('cls')
            time.sleep(5)
            listening = True
        
        if "play a song" in data:
            while True:
                initial_Time = dt.now()
                os.system("rocknroll.mp3")
                time.sleep(1)
                os.kill()
                final_time = dt.now()
                if final_time.second >=10:
                    break

        else:
            print("....")
            time.sleep(2)
            listening = True

        return listening


# time.sleep(2)
# print("Conversation Started")
# respond("Hi George, Iam Anne your AI, \nMy Current Version is 0.2.4,\n What can I do for you?")
# time.sleep(8)


# listening = True
# while listening == True:
#     data = listen()
#     listening = digital_assistant(data)



                
# if __name__ == "__main__":
    
#     VirtualAssitent.listening()