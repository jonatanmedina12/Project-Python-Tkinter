from models.conexion_db import ConexionDB

from tkinter import messagebox


def crear_tabla():
    conexion = ConexionDB()

    sql = ''' 
        CREATE TABLE IF NOT EXISTS peliculas (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(150),
            Duracion VARCHAR(20),
            Genero VARCHAR(100)
        )
    '''

    try:
        titulo = "Se creo la tabla"
        mensaje = "Se creo la tabla correctamente "
        messagebox.showinfo(titulo,mensaje)
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Asegúrate de que los cambios se confirmen
        print("Tabla 'peliculas' creada exitosamente.")
    except Exception as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        conexion.cerrar_Conexion()


def borrar_tabla():
    conexion = ConexionDB()

    sql = '''
        DROP TABLE IF EXISTS peliculas
    '''

    try:
        titulo = "Se borro la tabla"
        mensaje = "Se borro la tabla correctamente "
        messagebox.showinfo(titulo,mensaje)
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Asegúrate de que los cambios se confirmen
        print("Tabla 'peliculas' eliminada exitosamente.")
    except Exception as e:
        print(f"Error al eliminar la tabla: {e}")
    finally:
        conexion.cerrar_Conexion()
