"""Fase 4 – Componente Práctico - Prácticas Simuladas
----------------------------------------------------------------------
John Mitchell Hurtado Luna.
Daniel Alberto Guzman Afanassieva.
----------------------------------------------------------------------
Escuela de Ciencias Básicas Tecnología e Ingeniería
Universidad Nacional Abierta y a Distancia
202337120: Proyecto de Ingeniería I
Tutor: Henry Alfonso Garzón Sanchez
02 de abril de 2026
----------------------------------------------------------------------
"""

#Se importan las librestías necesarias para el desarrollo del prototipo, en este caso se utiliza tkinter para la interfaz gráfica y matplotlib para la visualización de datos.
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

#Definición de la función que evalúa el riesgo académico del estudiante basado en los datos ingresados por el usuario. La función también muestra una gráfica con los datos ingresados.
def evaluar_riesgo():
    try:
        nombre = entry_nombre.get()
        accesos = int(entry_accesos.get())
        tareas = int(entry_tareas.get())
        promedio = float(entry_promedio.get())

        # Lógica para determinar el nivel de riesgo basado en los datos ingresados (Esto lo haria la ia, pero se simula con una lógica simple para el prototipo)
        if accesos < 5 and tareas < 3 and promedio < 3.0:
            riesgo = "ALTO"
            mensaje = "Riesgo ALTO: Se requiere intervención inmediata."
        elif accesos < 10 or tareas < 5 or promedio < 3.5:
            riesgo = "MEDIO"
            mensaje = "Riesgo MEDIO: Se recomienda seguimiento."
        else:
            riesgo = "BAJO"
            mensaje = "Riesgo BAJO: El estudiante está en buen estado."

        resultado = f"Estudiante: {nombre}\nNivel de riesgo: {riesgo}\n\n{mensaje}"
        label_resultado.config(text=resultado)

        # Mostrar gráfica con los datos ingresados
        mostrar_grafica(accesos, tareas, promedio)

    except:
        messagebox.showerror("Error", "Por favor ingresa todos los datos correctamente.")

def mostrar_grafica(accesos, tareas, promedio):
    categorias = ["Accesos", "Tareas", "Promedio"]
    valores = [accesos, tareas, promedio]

    plt.figure()
    plt.bar(categorias, valores)
    plt.title("Análisis del Rendimiento del Estudiante")
    plt.xlabel("Variables")
    plt.ylabel("Valores")
    plt.show()

# Ventana principal de la aplicación utilizando tkinter, donde se ingresan los datos del estudiante y se muestra el resultado del análisis de riesgo académico. La ventana también incluye un botón para evaluar el riesgo y una sección para mostrar los resultados y la gráfica correspondiente.
ventana = tk.Tk()
ventana.title("Sistema de Detección de Riesgo Académico")
ventana.geometry("400x420")
ventana.resizable(False, False)

# Título de la aplicación
titulo = tk.Label(ventana, text="Sistema de Análisis Académico", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

# Cuadro de texto para ingresar el nombre del estudiante
tk.Label(ventana, text="Nombre del estudiante:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

# Cuadro de texto para ingresar el número de accesos a la plataforma virtual del curso. Este dato es importante para evaluar el nivel de participación del estudiante en el curso.
tk.Label(ventana, text="Número de accesos:").pack()
entry_accesos = tk.Entry(ventana)
entry_accesos.pack()

# Cuadro de texto para ingresar el número de tareas entregadas por el estudiante. Este dato es relevante para evaluar el cumplimiento de las actividades académicas por parte del estudiante.
tk.Label(ventana, text="Tareas entregadas:").pack()
entry_tareas = tk.Entry(ventana)
entry_tareas.pack()

# Cuadro de texto para ingresar el promedio del estudiante. Este dato es crucial para evaluar el rendimiento académico general del estudiante.
tk.Label(ventana, text="Promedio (0.0 - 5.0):").pack()
entry_promedio = tk.Entry(ventana)
entry_promedio.pack()

# Boton para evaluar el riesgo académico del estudiante basado en los datos ingresados. Al hacer clic en este botón, se ejecuta la función evaluar_riesgo que procesa los datos y muestra el resultado.
btn_evaluar = tk.Button(ventana, text="Evaluar Riesgo", command=evaluar_riesgo)
btn_evaluar.pack(pady=15)

# Etiqueta para mostrar el resultado del análisis de riesgo académico del estudiante. Esta sección se actualiza con el resultado cada vez que se evalúa el riesgo.
label_resultado = tk.Label(ventana, text="", justify="left", wraplength=350)
label_resultado.pack(pady=10)

# Ejecutar la ventana principal de la aplicación, lo que permite a los usuarios interactuar con la interfaz gráfica y utilizar las funcionalidades del sistema de detección de riesgo académico.
ventana.mainloop()