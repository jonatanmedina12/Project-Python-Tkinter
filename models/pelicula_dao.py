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
        messagebox.showinfo(titulo, mensaje)
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
        messagebox.showinfo(titulo, mensaje)
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Asegúrate de que los cambios se confirmen
        print("Tabla 'peliculas' eliminada exitosamente.")
    except Exception as e:
        print(f"Error al eliminar la tabla: {e}")
    finally:
        conexion.cerrar_Conexion()


class pelicula_tabla:
    def __init__(self, nombre, duracion, genero):
        self.id_ = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'película[{self.nombre},{self.duracion},{self.genero}]'


def guardar_datos(pelicula):
    conexion = ConexionDB()

    sql = f"""
    INSERT INTO peliculas (Nombre, Duracion, Genero)
    VALUES ('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')
    """

    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Asegúrate de que los cambios se confirmen
        messagebox.showinfo("Datos guardados", "Los datos de la película se guardaron correctamente")
    except Exception as e:
        messagebox.showinfo("Error la tabla no existe", "Error la tabla no existe")

        print(f"Error al guardar los datos: {e}")
    finally:
        conexion.cerrar_Conexion()


def listar_datos():
    conexion = ConexionDB()
    lista_peliculas = []
    sql = '''
        SELECT * FROM peliculas order by  1 desc 
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Asegúrate de que los cambios se confirmen
        lista_peliculas = conexion.cursor.fetchall()
        print(lista_peliculas)
    except Exception as e:
        messagebox.showinfo("Error la tabla no existe", "Error la tabla no existe")

        print(f"Error al guardar los datos: {e}")
    finally:
        conexion.cerrar_Conexion()

    return lista_peliculas


def editar(pelicula, id_):
    conexion = ConexionDB()
    sql = f"""
        UPDATE peliculas set Nombre ='{pelicula.nombre}' , Duracion  = '{pelicula.duracion}', Genero='{pelicula.genero}'
        where Id ={id_}
    """
    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Asegúrate de que los cambios se confirmen
        messagebox.showinfo("Actualización completa", "Actualización completa")

    except Exception as e:
        messagebox.showinfo("Error la tabla no existe", "Error la tabla no existe")
        print(f"Error al guardar los datos: {e}")
    finally:
        conexion.cerrar_Conexion()


def eliminar(id_):
    conexion = ConexionDB()

    sql =f'DELETE FROM peliculas where Id ={id_}'

    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Asegúrate de que los cambios se confirmen
        messagebox.showinfo("Eliminación completa", "Eliminación completa")

    except Exception as e:
        messagebox.showinfo("Error la tabla no existe", "Error la tabla no existe")
        print(f"Error al guardar los datos: {e}")
    finally:
        conexion.cerrar_Conexion()

