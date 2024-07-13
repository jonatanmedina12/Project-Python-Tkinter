import tkinter as tk


def barra_menu(root):
    barra_men = tk.Menu(root)
    root.config(menu=barra_men, width=300, height=300)

    menu_inicio = tk.Menu(barra_men, tearoff=0)
    barra_men.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear Registro en DB')
    menu_inicio.add_command(label='Eliminar Registro en DB')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_men.add_cascade(label='Consultas')
    barra_men.add_cascade(label='configuración')
    barra_men.add_cascade(label='Ayuda')


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__()
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
        self.config(width=480, height=320)
        self.campo_pelicula()

    def campo_pelicula(self):
        self.label_nombre = tk.Label(self, text='Nombre:')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text='Duración:')
        self.label_duracion.config(font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text='Genero:')
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.mi_generacion = tk.StringVar()
        self.entry_generacion = tk.Entry(self, textvariable=self.mi_generacion)
        self.entry_generacion.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_generacion.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

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
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_generacion.set('')
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_generacion.config(state='disabled')

        self.button_guardar.config(state='disabled')
        self.button_cancelar.config(state='disabled')

    def guardar_datos(self):
        self.deshabilitar_campos()
