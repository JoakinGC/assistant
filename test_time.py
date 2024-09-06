import sys
import os
import time
from modulos.time_control.time_control import TaskTimer
from modulos.services.services import AgendaTareaService


def test_task_timer():
    agenda_tarea_service = AgendaTareaService()
    task_timer = TaskTimer(agenda_tarea_service)

    print("Iniciando tarea...")
    task_timer.start_task()
    time.sleep(5)  
    print("Comenzando tarea...")
    task_timer.begin_task()
    time.sleep(40)  
    print("Pausando tarea...")
    task_timer.pause_task()
    time.sleep(10)  
    print("Finalizando tarea...")
    task_timer.end_task(1, 1)

if __name__ == "__main__":
    test_task_timer()