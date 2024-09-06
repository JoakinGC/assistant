from datetime import datetime, timedelta
import time

class TaskTimer:
    def __init__(self, agenda_tarea_service):
        self.agenda_tarea_service = agenda_tarea_service
        self.running = False
        self.task_id = None

    def start_task(self, id_agenda, id_tarea):
        self.task_id = id_tarea
        self.running = True
        self.start_time = datetime.now()
        self.agenda_tarea_service.start_task(id_agenda, id_tarea, self.start_time)

    def stop_task(self, id_agenda, id_tarea):
        if self.running and self.task_id == id_tarea:
            end_time = datetime.now()
            tiempo_total = end_time - self.start_time
            self.agenda_tarea_service.finalizar_tarea(id_agenda, id_tarea)
            self.running = False
            return tiempo_total
        return None

    def get_time_spent(self):
        if self.running:
            return datetime.now() - self.start_time
        return timedelta(0)
