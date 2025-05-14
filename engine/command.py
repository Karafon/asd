from gtts import gTTS
import os
import pygame
import time
from pydub import AudioSegment
from pydub.utils import which
import speech_recognition as sr
import eel

# ffmpeg yolunu belirtin
AudioSegment.ffmpeg = which(r"C:\ffmpeg\bin\ffmpeg.exe")

def speak(string):
    string = str(string)

    if not string.strip():  # Eğer metin boşsa veya sadece boşluklardan oluşuyorsa
        print("Konuşmadı.")
        return  # Boş metin verilirse, işlem yapılmaz.

    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)

    
    sound = AudioSegment.from_mp3(file)
    sound = sound.speedup(playback_speed=1.28)  # Hızı artır
    sound.export(file, format="mp3")

    eel.DisplayMassage(string)

    
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()
    os.remove(file)




def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        eel.DisplayMassage("Dinliyorum...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=20, phrase_time_limit=15)
        print("Ses kaydedildi...")
        

    try:
        print("Anlamaya çalışılıyor...")
        eel.DisplayMassage("Anlamaya çalışılıyor...")
        
        # Ses tanıma işlemi
        komut = r.recognize_google(audio, language="tr-TR")
        print(f"Komut: {komut}")
        eel.DisplayMassage(komut)        
        time.sleep(2)
        

    
    except Exception as e:
        print(f"Diğer hata: {e}")
        return "hatalı"  # Diğer tüm hatalar için 'hatalı' döndür
    
    # Komut başarılıysa küçük harfe çevir
    return komut.lower()

@eel.expose    
def allCommands(message=1):

    if message == 1:
        komut = take_command()
        print(komut)
        eel.senderText(komut)
    else:
        komut = message
        eel.senderText(komut)


    try:
        if " aç" in komut:
            from engine.features import openCommand
            openCommand(komut)

        elif " youtube'da" in komut:
            from engine.features import YoutubeArat
            YoutubeArat(komut)


        elif "mesaj gönder" in komut or "ara" in komut or "görüntülü ara" in komut:
            from engine.features import findContact, whatsApp, sendMessage, makeCall
            message = ""
            contact_no, name = findContact(komut)
            if(contact_no != 0):
                speak("Ne ile işlem yapmak istersiniz? Whatsapp mı? Telefon mu?")
                tercih = take_command()
                print(tercih)

                if "telefon" in tercih:
                    if "mesaj gönder" in komut:
                        speak("Ne mesajı göndermek istersiniz?")
                        message = take_command()
                        sendMessage(message, contact_no, name)
                    elif "ara" in komut:
                        makeCall(name, contact_no)
                    else:
                        speak("Lütfen tekrar deneyin.")
                elif "whatsapp" in tercih:
                    message = ""
                    if "mesaj gönder" in komut:
                        message = "mesaj"
                        speak("Ne mesajı göndermek istersiniz?")
                        komut = take_command()

                    elif "ara" in komut:
                        message = "ara"
                    else:
                        message = "görüntülü ara"


                    whatsApp(contact_no, komut, message, name)




            else:
                print("Açılmadı.")
        else:
            from engine.features import chatBot
            chatBot(komut)
    except:
        print("Bir hata oluştu.")
    
    

        eel.ShowHood()