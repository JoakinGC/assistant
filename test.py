from modulos.services.services import TaskService, SubtareaService, AgendaService, AgendaTareaService, EventoService, RecordatorioService
from datetime import datetime, time
from modulos.time_control.time_control import TaskTimer

def test_agenda_tarea_service():
    agenda_tarea_service = AgendaTareaService()
    task_timer = TaskTimer(agenda_tarea_service=agenda_tarea_service)
    


test_agenda_tarea_service()