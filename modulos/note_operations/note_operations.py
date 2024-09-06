import os
import pyttsx3

def anotar_en_bloc_de_notas(texto):
    with open("nota.txt", "a") as archivo:
        archivo.write(texto + "\n")
    os.startfile("nota.txt")
    speak("Texto anotado en el bloc de notas.")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
