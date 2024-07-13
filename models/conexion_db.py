import sqlite3
import os


class ConexionDB:
    def __init__(self):
        # Obtener la ruta absoluta al directorio del archivo de base de datos
        self.db_path = os.path.join(os.path.dirname(__file__), '..', 'DataBase', 'peliculas.db')
        self.db_path = os.path.abspath(self.db_path)

        # Crear el directorio si no existe
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        self.conexion = sqlite3.connect(self.db_path)  # Nombre de la base de datos
        self.cursor = self.conexion.cursor()

    def cerrar_Conexion(self):
        self.conexion.close()