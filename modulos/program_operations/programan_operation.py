import os
import subprocess
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def abrir_programa(nombre_programa):
    try:
        subprocess.Popen(nombre_programa)
        speak(f"{nombre_programa} abierto.")
    except FileNotFoundError:
        speak(f"No se encontró el programa {nombre_programa}.")

def cerrar_ventana_especifica(nombre_programa):
    try:
        os.system(f"taskkill /f /im {nombre_programa}.exe")
        speak(f"{nombre_programa} cerrado.")
    except Exception as e:
        speak(f"Hubo un error al cerrar {nombre_programa}: {str(e)}")

def encontrar_programa(nombre_programa):
    programas = {
        "notepad": "notepad.exe",
        "calculadora": "calc.exe",
        "paint": "mspaint.exe",
    }
    return programas.get(nombre_programa.lower())
