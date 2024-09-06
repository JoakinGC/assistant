class AgendaService:
    def __init__(self):
        self.agendas = []

    def create_agenda(self, fecha, descripcion):
        agenda = {
            "id": len(self.agendas) + 1,
            "fecha": fecha,
            "descripcion": descripcion,
            "tareas": []
        }
        self.agendas.append(agenda)
        return agenda

    def get_agenda_by_date(self, date):
        for agenda in self.agendas:
            if agenda["fecha"].date() == date.date():
                return agenda
        return None


class AgendaTareaService:
    def start_task(self, id_agenda, id_tarea, tiempo_estimado):
        agenda = self.get_agenda_by_id(id_agenda)
        if agenda:
            tarea = {"id_tarea": id_tarea, "tiempo_estimado": tiempo_estimado, "estado": "en progreso"}
            agenda["tareas"].append(tarea)
            return tarea
        return None

    def get_agenda_by_id(self, id_agenda):
        for agenda in AgendaService().agendas:
            if agenda["id"] == id_agenda:
                return agenda
        return None

    def finalizar_tarea(self, id_agenda, id_tarea):
        agenda = self.get_agenda_by_id(id_agenda)
        if agenda:
            for tarea in agenda["tareas"]:
                if tarea["id_tarea"] == id_tarea:
                    tarea["estado"] = "completada"
                    return tarea
        return None
