from Catalogo.model.conexion_db import ConexionDB
from tkinter import messagebox


def crear_tabla():
    conexion = ConexionDB()

    sql = ''' 
        CREATE TABLE  IF NOT EXISTS  peliculas(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(150),
            Duracion VARCHAR(20),
            Genero VARCHAR(100)
        )
    '''

    try:
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Asegúrate de que los cambios se confirmen
        print("Tabla 'peliculas' creada exitosamente.")
    except Exception as e:
        titulo = 'Ya existe la tabla'
        mensaje = 'lA TABLA YA CREADA'
        messagebox.showwarning(titulo, mensaje)

        print(f"Error al crear la tabla: {e}")
    finally:
        conexion.cerrar_Conexion()


def borrar_tabla():
    conexion = ConexionDB()

    sql = '''
        DROP TABLE IF EXISTS peliculas
    '''

    try:
        titulo = 'Borrar Registro'
        mensaje = 'Se borro la tabla correctamente'
        messagebox.showinfo(titulo, mensaje)
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Asegúrate de que los cambios se confirmen
        print("Tabla 'peliculas' eliminada exitosamente.")
    except Exception as e:
        titulo = 'Borrar Registro'
        mensaje = 'No existe la tabla'
        messagebox.showwarning(titulo, mensaje)
        print(f"Error al eliminar la tabla: {e}")
    finally:
        conexion.cerrar_Conexion()
