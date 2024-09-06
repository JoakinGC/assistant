import time
import psutil
import ctypes
import subprocess

def main():
    # Preguntar al usuario el tiempo en minutos durante el cual bloquear las aplicaciones
    while True:
        try:
            block_time_minutes = int(input("Introduce el tiempo en minutos para bloquear las aplicaciones no deseadas: "))
            if block_time_minutes <= 0:
                print("Por favor, introduce un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

    block_time_seconds = block_time_minutes * 60

    # Lista de nombres de procesos a bloquear
    blocked_apps = ["CalculatorApp.exe"]

    start_time = time.time()

    while time.time() - start_time < block_time_seconds:
        # Obtener la lista de procesos en ejecución
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                process_name = proc.info['name']
                if process_name in blocked_apps:
                    # Terminar el proceso
                    psutil.Process(proc.info['pid']).terminate()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        time.sleep(1)  # Esperar un segundo antes de la próxima comprobación

    # Mostrar una alerta en Windows
    ctypes.windll.user32.MessageBoxW(0, "El tiempo de bloqueo ha finalizado.", "Alerta", 1)

if __name__ == "__main__":
    main()
