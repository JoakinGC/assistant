from modulos.database.connection import create_connection, close_connection
from modulos.database.models import Tarea, Subtarea, Agenda

class TareaRepository:
    def __init__(self):
        self.connection = create_connection()

    def get_all_tareas(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Tarea")
            rows = cursor.fetchall()
            tareas = [Tarea(*row) for row in rows]
            return tareas
        except Exception as e:
            print(f"Error: '{e}'")
            return []
        finally:
            cursor.close()
            close_connection(self.connection)

    def add_tarea(self, tarea):
        try:
            cursor = self.connection.cursor()
            sql = "INSERT INTO Tarea (nombre, descripcion, tiempo_estimado) VALUES (%s, %s, %s)"
            val = (tarea.nombre, tarea.descripcion, tarea.tiempo_estimado)
            cursor.execute(sql, val)
            self.connection.commit()
        except Exception as e:
            print(f"Error: '{e}'")
        finally:
            cursor.close()
            close_connection(self.connection)

# Implement similar repositories for Subtarea and Agenda
