import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Cálculo con Pestañas")

# Ajustar el tamaño de la ventana
root.geometry("600x300")
root.config(bg="#f2f2f2")

# Función para calcular en la primera pestaña
def calcular_pestana1():
    try:
        h = float(entry_h.get())
        asoprincipal = float(entry_asoprincipal.get())
        rec = float(entry_rec.get())
        d = h - rec - (asoprincipal / 2)
        label_resultado1.config(text=f"Resultado de d: {d:.2f}")
    except ValueError:
        label_resultado1.config(text="Por favor ingrese valores válidos.")

# Función para calcular en la segunda pestaña: MuenMn = Mu / 1000
def calcular_pestana2():
    try:
        mu = float(entry_mu.get())
        muenmn = mu / 1000
        label_resultado2.config(text=f"Resultado de MuenMn: {muenmn:.3f}")
    except ValueError:
        label_resultado2.config(text="Por favor ingrese un valor válido.")

# Crear el notebook (pestañas)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Crear el primer frame (pestaña 1)
frame1 = ttk.Frame(notebook, padding=10)
notebook.add(frame1, text="Cálculo d")

# Crear el segundo frame (pestaña 2)
frame2 = ttk.Frame(notebook, padding=10)
notebook.add(frame2, text="Cálculo MuenMn")

# ---- Pestaña 1 ----
label_h = ttk.Label(frame1, text="H")
label_asoprincipal = ttk.Label(frame1, text="Asøprincipal")
label_rec = ttk.Label(frame1, text="rec")

entry_h = ttk.Entry(frame1, width=20)
entry_asoprincipal = ttk.Entry(frame1, width=20)
entry_rec = ttk.Entry(frame1, width=20)

button_calcular1 = ttk.Button(frame1, text="Calcular", command=calcular_pestana1)

label_resultado1 = ttk.Label(frame1, text="", font=('Helvetica', 12, 'bold'), foreground="#007acc")

# Posicionar en el grid de la pestaña 1
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=1)

label_h.grid(row=0, column=0, padx=10, pady=10, sticky="E")
entry_h.grid(row=0, column=1, padx=10, pady=10)

label_asoprincipal.grid(row=1, column=0, padx=10, pady=10, sticky="E")
entry_asoprincipal.grid(row=1, column=1, padx=10, pady=10)

label_rec.grid(row=2, column=0, padx=10, pady=10, sticky="E")
entry_rec.grid(row=2, column=1, padx=10, pady=10)

button_calcular1.grid(row=3, column=1, pady=20)

label_resultado1.grid(row=4, column=0, columnspan=2, pady=10)

# ---- Pestaña 2 ----
label_mu = ttk.Label(frame2, text="Mu")
entry_mu = ttk.Entry(frame2, width=20)

button_calcular2 = ttk.Button(frame2, text="Calcular", command=calcular_pestana2)

label_resultado2 = ttk.Label(frame2, text="", font=('Helvetica', 12, 'bold'), foreground="#007acc")

# Posicionar en el grid de la pestaña 2
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_columnconfigure(1, weight=1)

label_mu.grid(row=0, column=0, padx=10, pady=10, sticky="E")
entry_mu.grid(row=0, column=1, padx=10, pady=10)

button_calcular2.grid(row=1, column=1, pady=20)

label_resultado2.grid(row=2, column=0, columnspan=2, pady=10)

# Iniciar el loop de la ventana
root.mainloop()
