class TaskService:
    def __init__(self):
        self.tareas = []

    def create_tarea(self, nombre, descripcion, tiempo_estimado):
        tarea = {
            "id": len(self.tareas) + 1,
            "nombre": nombre,
            "descripcion": descripcion,
            "tiempo_estimado": tiempo_estimado,
            "estado": "pendiente"
        }
        self.tareas.append(tarea)
        return tarea

    def get_tareas(self):
        return self.tareas

    def get_tarea_por_nombre(self, nombre):
        for tarea in self.tareas:
            if tarea["nombre"].lower() == nombre.lower():
                return tarea
        return None

    def iniciar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea["id"] == id_tarea:
                tarea["estado"] = "en progreso"
                return tarea
        return None

    def finalizar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea["id"] == id_tarea:
                tarea["estado"] = "completada"
                return tarea
        return None
