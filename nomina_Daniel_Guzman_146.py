# Fase_2_Abstracción y Diseño
# Daniel_Alberto_Guzman_Afanassieva_146
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import os

# Clase para gestionar empleados y calcular nómina
class GestionEmpleados:
    def __init__(self, identificacion, nombre, genero, cargo, dias, valor_dia):
        self.identificacion = identificacion
        self.nombre = nombre
        self.genero = genero
        self.cargo = cargo
        self.dias = dias
        self.valor_dia = valor_dia
        self.fecha = datetime.now().strftime("%Y-%m-%d")
        self.total = 0

# Método para calcular la nómina total a pagar
    def calcularNomina(self):
        self.total = self.dias * self.valor_dia
        return self.total

# Diccionario para asignar valores de día según el cargo
valores_cargo = {
    "Servicios Generales": 40000,
    "Administrativo": 50000,
    "Electricista": 60000,
    "Mecánico": 80000,
    "Soldador": 90000
}

# Variable global para almacenar el empleado guardado
empleado_guardado = None
archivo = "Empleado.json"

# Función para validar el login
def validar_login():
    if entry_password.get() == "4682":
        ventana_login.destroy()
        ventana_registro()
    else:
        messagebox.showerror("Error", "Contraseña incorrecta")

# Función para actualizar el valor del día según el cargo seleccionado
def actualizar_valor_dia(*args):
    cargo = cargo_var.get()
    if cargo in valores_cargo:
        valor_dia_var.set(valores_cargo[cargo])

# Función para validar los campos de entrada
def validar_campos():
    if not entry_id.get() or not entry_nombre.get() or not entry_dias.get():
        return False
    if not entry_dias.get().isdigit():
        return False
    return True

# Función para guardar los datos del empleado en un archivo JSON
def guardar_datos():
    global empleado_guardado

    if not validar_campos():
        messagebox.showerror("Error", "Datos inválidos")
        return

# Crear instancia de empleado con los datos ingresados
    empleado_guardado = GestionEmpleados(
        entry_id.get(),
        entry_nombre.get(),
        genero_var.get(),
        cargo_var.get(),
        int(entry_dias.get()),
        valores_cargo[cargo_var.get()],
    )

    guardar_archivo(empleado_guardado)
    messagebox.showinfo("Éxito", "Datos guardados correctamente")

# Función para guardar el empleado en un archivo JSON
def guardar_archivo(emp):
    data = []
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            data = json.load(f)

    data.append(emp.__dict__)

    with open(archivo, "w") as f:
        json.dump(data, f, indent=4)

# Función para mostrar el reporte de nómina
def mostrar_reporte():
    if empleado_guardado is None:
        messagebox.showwarning("Atención", "Primero guarda datos")
        return

    total = empleado_guardado.calcularNomina()

    ventana = tk.Toplevel()
    ventana.title("Reporte de nomina")

# Crear el texto del reporte con los datos del empleado y el total a pagar
    texto = f"""
IDENTIFICACION: {empleado_guardado.identificacion}
NOMBRE COMPLETO: {empleado_guardado.nombre}
CARGO: {empleado_guardado.cargo}
DIAS TRABAJADOS: {empleado_guardado.dias}
VALOR DIA: ${empleado_guardado.valor_dia}
FECHA: {empleado_guardado.fecha}

TOTAL A PAGAR: ${total}
"""

    tk.Label(ventana, text=texto, font=("Arial", 11)).pack(padx=20, pady=20)

# Función para salir de la aplicación
def salir():
    if messagebox.askyesno("Salir", "¿Deseas salir?"):
        root.quit()

root = tk.Tk()
root.withdraw()

ventana_login = tk.Toplevel()
ventana_login.title("Acceso")
ventana_login.configure(bg="#2c3e50")

tk.Label(ventana_login, text="Sistema Nómina", fg="white", bg="#2c3e50", font=("Arial", 16)).pack(pady=10)
tk.Label(ventana_login, text="Autor: Daniel Alberto Guzman Afanassieva_146", fg="white", bg="#2c3e50").pack()

tk.Label(ventana_login, text="Contraseña", bg="#2c3e50", fg="white").pack()
entry_password = tk.Entry(ventana_login, show="*")
entry_password.pack()

tk.Button(ventana_login, text="Ingresar", command=validar_login, bg="#27ae60", fg="white").pack(pady=10)

# Función para crear la ventana de registro de nómina
def ventana_registro():
    global entry_id, entry_nombre, genero_var, cargo_var, entry_dias, valor_dia_var

    ventana = tk.Toplevel()
    ventana.title("Registro de nomina")
    ventana.configure(bg="#ecf0f1")

    tk.Label(ventana, text="Identificación").grid(row=0, column=0)
    entry_id = tk.Entry(ventana)
    entry_id.grid(row=0, column=1)

    tk.Label(ventana, text="Nombre").grid(row=1, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=1, column=1)

    tk.Label(ventana, text="Género").grid(row=2, column=0)
    genero_var = tk.StringVar(value="Masculino")
    tk.OptionMenu(ventana, genero_var, "Masculino", "Femenino").grid(row=2, column=1)

    tk.Label(ventana, text="Cargo").grid(row=3, column=0)
    cargo_var = tk.StringVar()
    cargo_var.trace("w", actualizar_valor_dia)
    tk.OptionMenu(ventana, cargo_var, *valores_cargo.keys()).grid(row=3, column=1)

    tk.Label(ventana, text="Valor Día").grid(row=4, column=0)
    valor_dia_var = tk.StringVar()
    tk.Entry(ventana, textvariable=valor_dia_var, state="readonly").grid(row=4, column=1)

    tk.Label(ventana, text="Días Laborados").grid(row=5, column=0)
    entry_dias = tk.Entry(ventana)
    entry_dias.grid(row=5, column=1)

    tk.Button(ventana, text="Guardar Registro", command=guardar_datos).grid(row=6, column=0)
    tk.Button(ventana, text="Calcular Nómina / Mostrar Reporte", command=mostrar_reporte).grid(row=6, column=1)
    tk.Button(ventana, text="Salir", command=salir).grid(row=7, column=0, columnspan=2)

# Iniciar la aplicación
root.mainloop()
