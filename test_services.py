from datetime import datetime, time
from modulos.services.services import TaskService, SubtareaService, AgendaService, AgendaTareaService, EventoService, RecordatorioService

def test_task_service():
    task_service = TaskService()
    task_service.create_tarea("Test Task", "This is a test task", 2.5)
    tareas = task_service.get_tareas()
    for tarea in tareas:
        print(tarea.__dict__)

def test_subtarea_service():
    subtarea_service = SubtareaService()
    subtarea_service.create_subtarea(1, "Test Subtask", "This is a test subtask", 1.5)
    subtareas = subtarea_service.get_subtareas()
    for subtarea in subtareas:
        print(subtarea.__dict__)

def test_agenda_service():
    agenda_service = AgendaService()
    agenda_service.create_agenda(datetime.now().date(), "Daily agenda")
    agendas = agenda_service.get_agendas()
    for agenda in agendas:
        print(agenda.__dict__)

def test_agenda_tarea_service():
    agenda_tarea_service = AgendaTareaService()
    agenda_tarea_service.create_agenda_tarea(1, 1, time(9, 0), time(10, 0), False, 60, 45, 15)
    agenda_tareas = agenda_tarea_service.get_agenda_tareas()
    for agenda_tarea in agenda_tareas:
        print(agenda_tarea.__dict__)

def test_evento_service():
    evento_service = EventoService()
    evento_service.create_evento(1, "Meeting", "Team meeting", time(11, 0), time(12, 0))
    eventos = evento_service.get_eventos()
    for evento in eventos:
        print(evento.__dict__)

def test_recordatorio_service():
    recordatorio_service = RecordatorioService()
    recordatorio_service.create_recordatorio("Test Reminder", "This is a test reminder", datetime.now().date(), time(8, 0), 1)
    recordatorios = recordatorio_service.get_recordatorios()
    for recordatorio in recordatorios:
        print(recordatorio.__dict__)

if __name__ == "__main__":
    test_task_service()
    test_subtarea_service()
    test_agenda_service()
    test_agenda_tarea_service()
    test_evento_service()
    test_recordatorio_service()
