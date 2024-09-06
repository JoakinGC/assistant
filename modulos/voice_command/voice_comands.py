import datetime
import speech_recognition as sr
import pyttsx3
import time
from datetime import datetime, timedelta
from threading import Thread
from modulos.services.task.task_service import TaskService
from modulos.services.services import AgendaService, AgendaTareaService
from modulos.time_control.time_control import TaskTimer
from utils.regular_expression import patron_url
from modulos.program_operations.program_operations import abrir_programa, cerrar_ventana_especifica, speak, encontrar_programa
from modulos.search.openGoogle import buscar_google
from modulos.webScrapping.searchInforWeb import obtener_info_web
from modulos.api_huggi.api import ChatAPI
from modulos.note_operations.note_operations import anotar_en_bloc_de_notas  
from modulos.webScrapping.weather_scraper import WeatherScraper
from modulos.google_calendar.google_calendar import add_event_to_calendar, list_upcoming_events

assist_name = "alexis"
chat_api = ChatAPI()
tarea_seleccionada = None
task_timer = None
agenda_service = AgendaService()
agenda_tarea_service = AgendaTareaService()
task_service = TaskService()

sinonimos = {
    "abrir": ["abre", "abrí", "abri", "abrir"],
    "cerrar": ["cierra", "cerrá", "cerra", "cerrar"],
    "anotar": ["nota", "notar", "anotar", "anota"],
    "dime la hora": ["que hora es", "que hora es?", "qué hora es", "¿qué hora es?", "qué hora es?", "dime la hora"],
    "dime todas las tareas": ["dime todas las tareas"],
    "agrega una tarea": ["agrega una tarea", "agrega nueva tarea", "agrega nueva tarea"],
}

num_palabras = {
    "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
    "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20
}

def convertir_palabra_a_numero(palabra):
    return num_palabras.get(palabra, None)

def normalizar_comando(comando):
    palabras = comando.split()
    comando_normalizado = []

    for palabra in palabras:
        encontrado = False
        for key, values in sinonimos.items():
            if palabra in values:
                comando_normalizado.append(key)
                encontrado = True
                break
        if not encontrado:
            comando_normalizado.append(palabra)
    
    return " ".join(comando_normalizado)

def reconocer_comando():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-ES")
        print(f"Comando reconocido: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("No se pudo entender el comando")
        return ""
    except sr.RequestError:
        print("Error al comunicarse con el servicio de reconocimiento de voz")
        return ""

def escuchar_y_ejecutar():
    while True:
        comando = reconocer_comando()
        if comando and assist_name.lower() in comando.lower():
            comando = comando.replace(assist_name, "").strip()
            comando = normalizar_comando(comando.strip())
            
            if "abrir chat" in comando:
                Thread(target=abrir_chat_interface).start()
            elif "cerrar chat" in comando:
                cerrar_chat_interface()
            elif "anotar" in comando:
                Thread(target=anotar_en_bloc_de_notas).start()
            elif "cerrar" in comando:
                nombre_programa = comando.replace("cerrar ", "").strip()
                nombre_programa = encontrar_programa(nombre_programa)
                if nombre_programa:
                    cerrar_ventana_especifica(nombre_programa)
            elif "abrir" in comando:
                nombre_programa = comando.replace("abrir ", "").strip()
                nombre_programa = encontrar_programa(nombre_programa)
                if nombre_programa:
                    abrir_programa(nombre_programa)
            elif "busca" in comando or "buscar" in comando:
                buscar = comando.replace("buscar", "").replace("busca", "").strip()
                Thread(target=buscar_google, args=(buscar,)).start()
            elif "dime la hora" in comando.lower():
                local_time = datetime.now().strftime("%H:%M:%S")
                speak(f"La hora es {local_time}")
            elif patron_url.search(comando):
                link = patron_url.search(comando).group(0)
                result = obtener_info_web(link)
                print(result)
                speak(f"Resultado de la búsqueda: {result}")
            elif "dime las noticias de hoy" in comando.lower():
                result = obtener_info_web("https://www.elpais.com")
                print(result)
                speak(f"Las noticias de hoy son: {result}")
            elif "dime el clima de hoy" in comando:
                obtener_clima_ubicacion("Alicante")
            elif "dime todas las tareas" in comando:
                todas_las_tareas()
            elif "agrega una tarea" in comando:
                agregar_nueva_tarea()
            elif "iniciar tarea" in comando:
                iniciar_tarea()
            elif "haz la rutina de nuevo" in comando:
                generar_rutina()
            elif "agregar evento" in comando:
                speak("¿Cuál es el título del evento?")
                summary = reconocer_comando()
                speak("¿Cuál es la descripción del evento?")
                description = reconocer_comando()
                speak("¿Cuál es la fecha y hora de inicio? Diga en formato 'AAAA-MM-DD HH:MM'")
                start_time_str = reconocer_comando()
                start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
                speak("¿Cuál es la fecha y hora de finalización? Diga en formato 'AAAA-MM-DD HH:MM'")
                end_time_str = reconocer_comando()
                end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
                add_event_to_calendar(summary, description, start_time, end_time)
            elif "dime los próximos eventos" in comando:
                list_upcoming_events()
            else:
                messages = [{"role": "user", "content": comando}]
                chat_api.speak_response(messages)

        time.sleep(1)

def obtener_clima_ubicacion(ubicacion):
    weather_scraper = WeatherScraper(city=ubicacion)
    weather_info = weather_scraper.get_weather()
    if weather_info:
        speak(f"El clima de hoy en {weather_scraper.city} es: {weather_info}")
        print(f"El clima de hoy en {weather_scraper.city} es: {weather_info}")
    else:
        speak("No se pudo obtener la información del clima.")

def todas_las_tareas():
    task_service = TaskService()
    todas_las_tareas = task_service.get_tareas()

    fecha_actual = datetime.now()
    speak(f"Las tareas de hoy, {fecha_actual.day}, son: ")
    for tarea in todas_las_tareas:
        speak(f"{tarea.nombre}, descripcion: {tarea.descripcion}, tiempo estimado: {tarea.tiempo_estimado}")
                
    speak("Esas son todas las tareas de hoy")
    return todas_las_tareas  # Devolver las tareas para su uso en la rutina

def abrir_chat_interface():
    import tkinter as tk
    from modulos.chat_assinst.asistnWithModules import ChatInterface

    global chat_window
    if chat_window is None:
        root = tk.Tk()
        root.title("Chatbot Interface")
        chat_window = ChatInterface(root)
        root.mainloop()

def cerrar_chat_interface():
    global chat_window
    if chat_window:
        chat_window.master.destroy()
        chat_window = None

def agregar_nueva_tarea():
    global tarea_seleccionada
    speak("¿Cuál es el nombre de la tarea?")
    nombre_tarea = reconocer_comando()

    speak("¿Cuál es la descripción de la tarea?")
    descripcion_tarea = reconocer_comando()

    speak("¿Cuánto tiempo estimas que tomará esta tarea en minutos?")
    tiempo_estimado_tarea = int(reconocer_comando())

    tarea_seleccionada = task_service.create_tarea(nombre_tarea, descripcion_tarea, tiempo_estimado_tarea)

def iniciar_tarea():
    global tarea_seleccionada, task_timer
    if tarea_seleccionada:
        agenda = agenda_service.create_agenda(datetime.now(), "Agenda para tareas")
        task_timer = TaskTimer(agenda_tarea_service)
        task_timer.start_task(agenda.id, tarea_seleccionada.id)
        speak(f"Tarea {tarea_seleccionada.nombre} iniciada.")
    else:
        speak("No hay tarea seleccionada.")

def generar_rutina():
    speak("Generando rutina para hoy")
    tareas = todas_las_tareas()
    rutina = "Tareas para hoy:\n"
    for tarea in tareas:
        rutina += f"- {tarea.nombre}: {tarea.descripcion}, Tiempo estimado: {tarea.tiempo_estimado} minutos\n"
    speak("Rutina generada. Aquí está:")
    print(rutina)
    speak(rutina)
    anotar_en_bloc_de_notas(rutina)

if __name__ == "__main__":
    escuchar_y_ejecutar()
