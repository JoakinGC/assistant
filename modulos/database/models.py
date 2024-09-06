class Tarea:
    def __init__(self, idTarea, nombre, descripcion, tiempo_estimado):
        self.idTarea = idTarea
        self.nombre = nombre
        self.descripcion = descripcion
        self.tiempo_estimado = tiempo_estimado

class Subtarea:
    def __init__(self, idSubtarea, idTarea, nombre, descripcion, tiempo_estimado):
        self.idSubtarea = idSubtarea
        self.idTarea = idTarea
        self.nombre = nombre
        self.descripcion = descripcion
        self.tiempo_estimado = tiempo_estimado

class Agenda:
    def __init__(self, idAgenda, fecha):
        self.idAgenda = idAgenda
        self.fecha = fecha
