import tkinter as tk
from tkinter import messagebox
import numpy as np

def show_size_selection():
    matrix_input_frame.pack_forget()
    result_frame.pack_forget()
    size_selection_frame.pack(pady=20)

def show_matrix_input():
    try:
        size = int(matrix_size.get())
        size_selection_frame.pack_forget()
        create_matrix_input(size)
    except ValueError:
        messagebox.showerror("Error", "Seleccione un tamaño de matriz válido")

def create_matrix_input(size):
    global entries
    for widget in matrix_input_frame.winfo_children():
        widget.destroy()
    entries = []
    for i in range(size):
        row_entries = []
        for j in range(size):
            entry = tk.Entry(matrix_input_frame, width=5)
            entry.grid(row=i, column=j, padx=5, pady=5)
            row_entries.append(entry)
        entries.append(row_entries)
    tk.Button(matrix_input_frame, text="Calcular Determinante", command=lambda: calculate_determinant(size)).grid(row=size, column=0, columnspan=size, pady=10)
    tk.Button(matrix_input_frame, text="Regresar", command=show_size_selection).grid(row=size+1, column=0, columnspan=size, pady=10)
    matrix_input_frame.pack(pady=20)

def calculate_determinant(size):
    try:
        matrix = []
        for row_entries in entries:
            row = [float(entry.get()) for entry in row_entries]
            matrix.append(row)
        matrix = np.array(matrix)
        result = np.linalg.det(matrix)
        result_text.set(f"Determinante: {int(round(result))}")
        matrix_input_frame.pack_forget()
        result_frame.pack(pady=20)
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Calculadora de Determinantes")

size_selection_frame = tk.Frame(app)
tk.Label(size_selection_frame, text="Seleccione el tamaño de la matriz:").grid(row=0, column=0, padx=5, pady=5)
matrix_size = tk.StringVar(value="2")
tk.OptionMenu(size_selection_frame, matrix_size, "2", "3", "4", "5").grid(row=0, column=1, padx=5, pady=5)
tk.Button(size_selection_frame, text="Siguiente", command=show_matrix_input).grid(row=1, column=0, columnspan=2, pady=10)
size_selection_frame.pack(pady=20)

matrix_input_frame = tk.Frame(app)

result_frame = tk.Frame(app)
result_text = tk.StringVar()
tk.Label(result_frame, textvariable=result_text).pack(pady=20)
tk.Button(result_frame, text="Nuevo cálculo", command=show_size_selection).pack(pady=10)

app.mainloop()
