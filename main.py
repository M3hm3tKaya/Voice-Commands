import speech_recognition as sr
import pyaudio
import time
import keyboard
import pyautogui
import os

rec = sr.Recognizer()
durum = ""
while True:
    with sr.Microphone() as source:
        try:
            rec.adjust_for_ambient_noise(source)
            print("ses alınıyor")
            data = rec.listen(source,phrase_time_limit=3)
            print("konuşma bitti")

            text = rec.recognize_google(data, language="tr").lower()
            print(text)
            if text.find("ekran") != -1:
                screen_shot1 = pyautogui.screenshot()
                screen_shot1.save("sss.png")
            if text.find("disney") != -1:
                durum = "disney"
                keyboard.press_and_release("windows+r")
                time.sleep(0.2)
                keyboard.write("https://www.disneyplus.com/tr-tr/home")
                time.sleep(0.1)
                keyboard.press_and_release("enter")
            if durum == "disney" and text.find("değiştir") != -1:
                keyboard.press_and_release("f5")
                time.sleep(3)
                for x in range(9):
                    time.sleep(0.1)
                    keyboard.press_and_release("tab")
                time.sleep(0.2)
                keyboard.press_and_release("enter")
                time.sleep(0.1)
                keyboard.press_and_release("tab")
                time.sleep(0.1)
                keyboard.press_and_release("enter")
            else:
                continue

        except:
            continue