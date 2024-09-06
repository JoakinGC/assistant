import webbrowser
import pyttsx3

def buscar_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Buscando {query} en Google...")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
