import os
from shlex import quote
import sqlite3
import struct
import subprocess
import time
import webbrowser
import re
from playsound3 import playsound
import eel
import pvporcupine
import pyaudio
import pyautogui
from engine.config import Assistant_Name
from engine.command import speak
import pywhatkit as kit
import speech_recognition as sr
from hugchat import hugchat
from engine.helper import remove_words, yt_terimi_ayiklama

# opening sound function

conn = sqlite3.connect('Zen.db')
cursor = conn.cursor()

@eel.expose
def play_opening_sound():
    opening = r"C:\Users\hasan\Desktop\Zen\www\assets\audio\Opening.mp3"
    playsound(opening)

def openCommand(komut):
    
    komut = komut.replace(Assistant_Name, "")
    komut = komut.replace("aç", "")
    komut = komut.lower()

    app_name = komut.strip()

    if app_name != "":

        try:

            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak(app_name + " açılıyor")
                eel.receiverText(app_name + " açılıyor")
                os.startfile(results[0][0])

            elif len(results) == 0:
                cursor.execute(
                    'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak(app_name + " açılıyor")
                    eel.receiverText(app_name + " açılıyor")
                    webbrowser.open(results[0][0])

                else:
                    speak(komut + " açılıyor")
                    eel.receiverText(app_name + " açılıyor")
                    try:
                        os.system('start '+ app_name)
                    except:
                        speak("Bulunamadı")
        except:
            speak("Bir hata oluştu")



def YoutubeArat(komut):
    arma_terimi = yt_terimi_ayiklama(komut)
    speak(arma_terimi + " Youtube'da oynatılıyor")
    kit.playonyt(arma_terimi)

def hotword():
    HOTWORDS = ["asistan", "uyan"]
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio, language="tr-TR").lower()
                



                if any(word in text for word in HOTWORDS):
                    import pyautogui as autogui
                    autogui.keyDown("win")
                    autogui.press("j")
                    time.sleep(2)
                    autogui.keyUp("win")


                    


            except Exception as e:
                print(f"Devam ediyor...")


def findContact(query):
    words_to_remove = ['ara', 'gönder', 'mesaj', 'wahtsapp', 'görüntülü', 'arama', 'video', 'ara', 'arama yap', 'arama yap', 'ara']
    query = re.sub(r"(yi|yı|yu|yü|i|ı|u|ü|mi|mı|mu|mü|ni|nı|nu|nü)$", "", query.strip(" '\""), flags=re.IGNORECASE)
    query = remove_words(query, words_to_remove)
    query = re.sub(r"(yi|yı|yu|yü|i|ı|u|ü|mi|mı|mu|mü|ni|nı|nu|nü|ya|ye|i|de|den|e|a|ın|in)$", "", query, flags=re.IGNORECASE)
    query = query.strip(" '\"")


    try:
        query = query.strip().lower()
        query_capitalized = query.title()

        # SQL sorgusu düzeltildi, parametreler doğru şekilde verildi
        cursor.execute("""
            SELECT mobile_no 
            FROM contacts 
            WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?
        """, ('%' + query + '%', '%' + query_capitalized + '%'))

        results = cursor.fetchall()
        if results:
            mobile_number_str = str(results[0][0])
            if not mobile_number_str.startswith('+90'):
                mobile_number_str = '+90' + mobile_number_str

            return mobile_number_str, query
        else:
            speak('No match found in contacts.')
            return 0, 0
    except Exception as e:
        print(f"Error: {e}")
        speak('An error occurred while searching.')
        return 0, 0
    

def whatsApp(mobile_no, message, flag, name):

    if flag == 'mesaj':
        target_tab = 12
        jarvis_message = "mesaj "+name+ " adlı kişiye gönderildi"

    elif flag == 'ara':
        target_tab = 7
        message = ''
        jarvis_message = name + "aranıyor"

    else:
        target_tab = 6
        message = ''
        jarvis_message = name+ "ile görüntülü konuşma başlatılıyor"

    # Encode the message for URL
    message = message.strip("'\"")  # hem tek hem çift tırnakları temizler
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')   
    speak(jarvis_message)

# chat bot hugface
def chatBot(komut):
    user_input = komut.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response


# android autamation


def makeCall(name, mobileNo):
    mobileNo =mobileNo.replace(" ", "")
    speak(name+" aranıyor")
    komut = 'adb -s 192.168.1.64:5555 shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(komut)


def sendMessage(message, mobileNo, name):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("mesaj gönderiliyor")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open sms app
    tapEvents(136, 2220)
    #start chat
    tapEvents(819, 2192)
    # search mobile no
    adbInput(mobileNo)
    #tap on name
    tapEvents(601, 574)
    # tap on input
    tapEvents(375, 2190)
    #message
    adbInput(message)
    #send
    tapEvents(957, 1397)
    speak("Mesaj başarıyla "+name+" kişisine gönderildi")