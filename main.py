from threading import Thread
from modulos.voice_command.voice_commands import escuchar_y_ejecutar
import time
from modulos.icon.mostra_gif import mostrar_gif

if __name__ == "__main__":
    thread_icon = Thread(target=mostrar_gif)
    thread_icon.daemon = True
    thread_escuchar = Thread(target=escuchar_y_ejecutar)
    thread_escuchar.daemon = True
    thread_escuchar.start()
    thread_icon.start()

    while True:
        time.sleep(1)
