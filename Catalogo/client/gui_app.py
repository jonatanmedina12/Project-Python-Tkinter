import tkinter as tk
<<<<<<< Updated upstream
=======
from tkinter import ttk
from models.pelicula_dao import crear_tabla, borrar_tabla, pelicula_tabla, guardar_datos, listar_datos, editar, eliminar
from tkinter import messagebox
>>>>>>> Stashed changes

from ttkthemes import ThemedStyle

def barra_menu(root):
    barra_men = tk.Menu(root)
    root.config(menu=barra_men, width=800, height=600)

    menu_inicio = tk.Menu(barra_men, tearoff=0)
    barra_men.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear Registro en DB')
    menu_inicio.add_command(label='Eliminar Registro en DB')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_men.add_cascade(label='Consultas')
    barra_men.add_cascade(label='Configuración')
    barra_men.add_cascade(label='Ayuda')


class Frame(tk.Frame):
    def __init__(self, root=None):
<<<<<<< Updated upstream
        super().__init__()
=======
        super().__init__(root)
        self.genero_pelicula = None
        self.duracion_pelicula = None
        self.nombre_pelicula = None
        self.id_pelicula = None
        self.scroll = None
        self.lista_peliculas = None
        self.button_editar = None
        self.button_eliminar = None
        self.tabla = None
>>>>>>> Stashed changes
        self.mi_generacion = None
        self.mi_duracion = None
        self.mi_nombre = None
        self.button_cancelar = None
        self.button_guardar = None
        self.button_nuevo = None
        self.entry_generacion = None
        self.entry_duracion = None
        self.entry_nombre = None
        self.label_duracion = None
        self.label_genero = None
        self.label_nombre = None
        self.root = root
        self.pack()
        self.config(width=800, height=600)

        # Aplicar el estilo
        style = ThemedStyle(root)
        style.set_theme("arc")  # Puedes probar otros temas como "plastik", "radiance", "clearlooks"

        self.campo_pelicula()

    def campo_pelicula(self):
        self.label_nombre = ttk.Label(self, text='Nombre:')
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.label_duracion = ttk.Label(self, text='Duración:')
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.label_genero = ttk.Label(self, text='Género:')
        self.label_genero.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.mi_nombre = tk.StringVar()
        self.entry_nombre = ttk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, state='disabled')
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.mi_duracion = tk.StringVar()
        self.entry_duracion = ttk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50, state='disabled')
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.mi_generacion = tk.StringVar()
        self.entry_generacion = ttk.Entry(self, textvariable=self.mi_generacion)
        self.entry_generacion.config(width=50, state='disabled')
        self.entry_generacion.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

<<<<<<< Updated upstream
        self.button_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.button_nuevo.config(width=20, font=('Arial', 12), fg='#DAD5D6', bg='#158645', cursor='hand2',
                                 activebackground='#35BD6F')
        self.button_nuevo.grid(row=4, column=0, padx=10, pady=10)

        self.button_guardar = tk.Button(self, text="Guardar",command=self.guardar_datos)
        self.button_guardar.config(width=20, font=('Arial', 12), fg='#DAD5D6', bg='#1658A2', cursor='hand2',
                                   activebackground='#3586DF')
        self.button_guardar.grid(row=4, column=1, padx=10, pady=10)

        self.button_cancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar_campos)
        self.button_cancelar.config(width=20, font=('Arial', 12), fg='#DAD5D6', bg='#BD152E', cursor='hand2',
                                    activebackground='#E15370')
        self.button_cancelar.grid(row=4, column=2, padx=10, pady=10)
=======
        self.button_nuevo = ttk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.button_nuevo.grid(row=3, column=0, padx=10, pady=10)

        self.button_guardar = ttk.Button(self, text="Guardar", command=self.guardar_datos)
        self.button_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.button_cancelar = ttk.Button(self, text="Cancelar", command=self.deshabilitar_campos)
        self.button_cancelar.grid(row=3, column=2, padx=10, pady=10)
>>>>>>> Stashed changes

        self.deshabilitar_campos()

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_generacion.set('')
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_generacion.config(state='normal')

        self.button_guardar.config(state='normal')
        self.button_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.id_pelicula = None

        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_generacion.set('')
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_generacion.config(state='disabled')

        self.button_guardar.config(state='disabled')
        self.button_cancelar.config(state='disabled')

    def guardar_datos(self):
        pelicula = pelicula_tabla(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_generacion.get()
        )
        if self.id_pelicula is not None:
            editar(pelicula, self.id_pelicula)
        else:
            guardar_datos(pelicula)

        self.tabla_peliculas()
        self.deshabilitar_campos()
<<<<<<< Updated upstream
=======

    def tabla_peliculas(self):
        self.lista_peliculas = listar_datos()

        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Duración', 'Género'))
        self.tabla.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=3, sticky='ns')
        self.tabla.config(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACIÓN')
        self.tabla.heading('#3', text='GÉNERO')

        for item in self.lista_peliculas:
            self.tabla.insert('', 'end', text=item[0], values=(item[1], item[2], item[3]))

        self.button_editar = ttk.Button(self, text="Editar", command=self.editar_campos)
        self.button_editar.grid(row=5, column=0, padx=10, pady=10)

        self.button_eliminar = ttk.Button(self, text="Eliminar", command=self.eliminar_datos)
        self.button_eliminar.grid(row=5, column=1, padx=10, pady=10)

    def editar_campos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][2]

            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_generacion.insert(0, self.genero_pelicula)
        except Exception as e:
            messagebox.showinfo("Sin datos seleccionados", "Sin datos seleccionados")
            print(e)

    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_pelicula)
            self.tabla_peliculas()
            self.id_pelicula = None
        except Exception as e:
            messagebox.showinfo("Sin datos seleccionados", "Sin datos seleccionados")
            print(e)
>>>>>>> Stashed changes
