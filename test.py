# # import speech_recognition as sr
# # import pyautogui as autogui
# # import time

# # HOTWORDS = ["asistan", "uyan"]
# # EXITWORDS = ["çık", "çıkış", "kapat"]

# # def simulate_win_j():
# #     autogui.keyDown("win")
# #     autogui.press("j")
# #     time.sleep(1)
# #     autogui.keyUp("win")

# # def listen_for_hotword():
# #     recognizer = sr.Recognizer()
# #     mic = sr.Microphone()

# #     print("🎙️ Dinleniyor...")

# #     with mic as source:
# #         recognizer.adjust_for_ambient_noise(source)

# #         while True:
# #             try:
# #                 audio = recognizer.listen(source, timeout=5)
# #                 text = recognizer.recognize_google(audio, language="tr-TR").lower()
# #                 print(f"🗣️ Duyulan: {text}")

# #                 if any(word in text for word in EXITWORDS):
# #                     print("🛑 Çıkış komutu verildi.")
# #                     break

# #                 if any(word in text for word in HOTWORDS):
# #                     print("✅ Hotword algılandı. Win + J tetikleniyor...")
# #                     import pyautogui as autogui
# #                     autogui.keyDown("win")
# #                     autogui.press("j")
# #                     time.sleep(2)
# #                     autogui.keyUp("win")

# #             except sr.WaitTimeoutError:
# #                 print("⌛ Zaman aşımı...")

# #             except sr.UnknownValueError:
# #                 print("🤷 Konuşma anlaşılamadı.")

# #             except sr.RequestError as e:
# #                 print(f"❌ API hatası: {e}")
# #                 break

# # if __name__ == "__main__":
# #     listen_for_hotword()

# import sqlite3

# c = sqlite3.connect('Zen.db')
# cursor = c.cursor()

 
# query = "Doğaç Üni"
# # İlk harfi büyük yapmak
# query_capitalized = query.title()

# print(query_capitalized)

# # Veritabanı sorgusu
# cursor.execute("SELECT name, mobile_no FROM contacts WHERE name = ? COLLATE NOCASE", (query_capitalized,))

# results = cursor.fetchall()

# if results:
#     for name, mobile_no in results:
#         print(f"{name} = {mobile_no}")
# else:
#     print("No match found.")


# import re

# query = "Doğaç'ın"
# query = re.sub(r"(yi|yı|yu|yü|i|ı|u|ü|mi|mı|mu|mü|ni|nı|nu|nü|ya|ye|i|de|den|e|a|ın|in)$", "", query, flags=re.IGNORECASE)
# query = query.strip(" '\"")
# print(query)


import os
import sqlite3

# komut = "chrome.exe"
# os.system('start '+ komut)
# conn = sqlite3.connect('Zen.db')
# c = conn.cursor()

# app_name = "discord"
# c.execute("SELECT path FROM sys_command WHERE name=?", (app_name,))
# result = c.fetchall()
# print(result[0] [0])
# os.startfile(result[0][0])

from hugchat import hugchat

def chatBot(komut):
    user_input = komut.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    return response

chatBot("saat kaç")
