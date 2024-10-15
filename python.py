import tkinter as tk
from tkinter import messagebox
import json
import os

# Archivo JSON donde se almacenarán los jugadores registrados
archivo_jugadores = "jugadores.json"
usuario_actual = None  # Para llevar el control del usuario que ha iniciado sesión

# Función para salir del programa
def salir():
    ventana.quit()

# Función para cargar los jugadores del archivo JSON
def cargar_jugadores():
    if os.path.exists(archivo_jugadores):
        with open(archivo_jugadores, "r") as archivo:
            return json.load(archivo)
    else:
        return {}

# Función para guardar los jugadores en el archivo JSON
def guardar_jugadores(jugadores):
    with open(archivo_jugadores, "w") as archivo:
        json.dump(jugadores, archivo)

# Función para mostrar el formulario de ingreso (usuario y contraseña)
def mostrar_ingresar():
    limpiar_ventana()

    # Etiquetas y campos de entrada
    etiqueta_usuario = tk.Label(ventana, text="Usuario:", font=("Helvetica", 14), width=15)
    etiqueta_usuario.pack(padx=10, pady=5, anchor='center')

    entrada_usuario = tk.Entry(ventana, font=("Helvetica", 14), width=20)
    entrada_usuario.pack(padx=10, pady=5, anchor='center')

    etiqueta_contraseña = tk.Label(ventana, text="Contraseña:", font=("Helvetica", 14), width=15)
    etiqueta_contraseña.pack(padx=10, pady=5, anchor='center')

    entrada_contraseña = tk.Entry(ventana, show="*", font=("Helvetica", 14), width=20)
    entrada_contraseña.pack(padx=10, pady=5, anchor='center')

    # Función para validar los datos de ingreso
    def enviar_datos():
        global usuario_actual
        usuario = entrada_usuario.get()
        contraseña = entrada_contraseña.get()
        jugadores = cargar_jugadores()

        if usuario in jugadores and jugadores[usuario] == contraseña:
            messagebox.showinfo("Ingreso", "¡Ingreso exitoso!")
            usuario_actual = usuario
            limpiar_ventana()
            mostrar_menu_principal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    # Botón para enviar las credenciales
    boton_ingresar = tk.Button(ventana, text="Iniciar Sesión", font=("Helvetica", 14), command=enviar_datos, width=15)
    boton_ingresar.pack(padx=10, pady=10, anchor='center')


def mostrar_registrar():
    limpiar_ventana()

    # Etiquetas y campos de entrada
    etiqueta_usuario = tk.Label(ventana, text="Usuario:", font=("Helvetica", 14), width=15)
    etiqueta_usuario.pack(padx=10, pady=5, anchor='center')

    entrada_usuario = tk.Entry(ventana, font=("Helvetica", 14), width=20)
    entrada_usuario.pack(padx=10, pady=5, anchor='center')

    etiqueta_contraseña = tk.Label(ventana, text="Contraseña:", font=("Helvetica", 14), width=15)
    etiqueta_contraseña.pack(padx=10, pady=5, anchor='center')

    entrada_contraseña = tk.Entry(ventana, show="*", font=("Helvetica", 14), width=20)
    entrada_contraseña.pack(padx=10, pady=5, anchor='center')

    # Función para registrar un nuevo usuario
    def registrar_usuario():
        global usuario_actual
        usuario = entrada_usuario.get()
        contraseña = entrada_contraseña.get()
        jugadores = cargar_jugadores()

        if usuario in jugadores:
            messagebox.showerror("Error", "El usuario ya está registrado.")
        else:
            jugadores[usuario] = contraseña
            guardar_jugadores(jugadores)
            usuario_actual = entrada_usuario.get()
            messagebox.showinfo("Registro", f"Usuario {usuario} registrado con éxito.")
            limpiar_ventana()
            mostrar_menu_principal()

    # Botón para registrar nuevo usuario
    boton_registro = tk.Button(ventana, text="Registro", font=("Helvetica", 14), command=registrar_usuario, width=15)
    boton_registro.pack(padx=10, pady=10, anchor='center')
    # enviar_datos()

# Función para mostrar las opciones de dificultad del juego
def mostrar_jugar():
    limpiar_ventana()

    etiqueta = tk.Label(ventana, text="Selecciona la dificultad:", font=("Helvetica", 14))
    etiqueta.pack(padx=10, pady=10, anchor='center')

    # Funciones para las dificultades
    def elegir_dificultad(dificultad):
        messagebox.showinfo("Dificultad seleccionada", f"Has elegido la dificultad {dificultad}")
        limpiar_ventana()
        mostrar_menu_principal()

    # Botones de dificultad
    boton_facil = tk.Button(ventana, text="Fácil", font=("Helvetica", 14), command=lambda: elegir_dificultad("Fácil"))
    boton_facil.pack(padx=10, pady=5, anchor='center')

    boton_normal = tk.Button(ventana, text="Normal", font=("Helvetica", 14), command=lambda: elegir_dificultad("Normal"))
    boton_normal.pack(padx=10, pady=5, anchor='center')

    boton_intermedio = tk.Button(ventana, text="Intermedio", font=("Helvetica", 14), command=lambda: elegir_dificultad("Intermedio"))
    boton_intermedio.pack(padx=10, pady=5, anchor='center')

# Función para limpiar todos los widgets actuales en la ventana
def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.pack_forget()

# Función para mostrar el menú principal
def mostrar_menu_principal():
    limpiar_ventana()

    # Etiqueta de bienvenida
    etiqueta_bienvenida = tk.Label(ventana, text=f"Bienvenido {usuario_actual}" if usuario_actual else "Bienvenido al Juego", font=("Helvetica", 18))
    etiqueta_bienvenida.pack(pady=20, anchor='center')

    # Botón para Ingresar (solo si no ha iniciado sesión)
    if not usuario_actual:
        boton_ingresar = tk.Button(ventana, text="Iniciar Sesión", font=("Helvetica", 14), command=mostrar_ingresar, width=15)
        boton_ingresar.pack(pady=10, anchor='center')  

    # Botón para Registrar (solo si no ha iniciado sesión)
    if not usuario_actual:
        boton_registrar = tk.Button(ventana, text="Registrarse", font=("Helvetica", 14), command=mostrar_registrar, width=15)
        boton_registrar.pack(pady=10, anchor='center')  


    # Botón para Jugar (solo visible si ha iniciado sesión)
    if usuario_actual:
        mostrar_jugar()
        # boton_jugar = tk.Button(ventana, text="Seleccionar Dificultad", font=("Helvetica", 14), command=mostrar_jugar, width=15)
        # boton_jugar.pack(pady=10, anchor='center')

    # Botón para Cerrar sesión (solo visible si ha iniciado sesión)
    if usuario_actual:
        boton_cerrar_sesion = tk.Button(ventana, text="Cerrar sesión", font=("Helvetica", 14), command=cerrar_sesion, width=15)
        boton_cerrar_sesion.pack(pady=10, anchor='center')

    # Botón para Salir
    boton_salir = tk.Button(ventana, text="Salir", font=("Helvetica", 14), command=salir, width=15)
    boton_salir.pack(pady=10, anchor='center')

# Función para cerrar la sesión
def cerrar_sesion():
    global usuario_actual
    usuario_actual = None
    limpiar_ventana()
    mostrar_menu_principal()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menú Principal")
ventana.geometry("600x400")  # Tamaño de la ventana principal

# Mostrar el menú principal al iniciar
mostrar_menu_principal()

# Ejecutar la ventana
ventana.mainloop()
