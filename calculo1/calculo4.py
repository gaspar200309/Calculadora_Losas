import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Cálculo con Pestañas")

# Ajustar el tamaño de la ventana
root.geometry("800x420")  # Ajusta el ancho para que los resultados quepan en la misma fila
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

# Función para calcular en la segunda pestaña
def calcular_pestana2():
    try:
        mu = float(entry_mu.get())
        muenmn = mu / 1000
        label_resultado2.config(text=f"Resultado de MuenMn: {muenmn:.3f}")
    except ValueError:
        label_resultado2.config(text="Por favor ingrese un valor válido.")

# Función para calcular en la tercera pestaña
def calcular_pestana3():
    try:
        fc = float(entry_fc.get())
        fy = float(entry_fy.get())
        Mu = float(entry_Mu.get())
        b = float(entry_b.get())
        d = float(entry_d.get())
        Vu = float(entry_Vu.get())
        λ = float(entry_lambda.get())
        
        ø = 0.9
        # Cálculos
        ρ = (0.85 * fc / fy) * (1 - (1 - 2 * Mu / (ø * 0.85 * fc * b * d**2))**0.5)
        a = ρ * fy * d / (0.85 * fc)
        β1 = 0.85 if fc < 28 else (0.65 if fc < 55 else 0.85 - (0.05 * (fc - 28) / 7))
        c = a / β1
        єt = (d - c) * 0.003 / c
        As = ρ * (b * 100) * (d * 100)  # cm²
        ρmin_a = (0.0018 * 420 / fy) * 0.045
        ρmin_b = 0.0014 * 0.045
        ρmin = max(ρmin_a, ρmin_b)
        Nb = ρmin / 1.13
        ρmintemp_a = (0.0018 * 420 / fy) * 1 * d
        ρmintemp_b = 1.4 * 1 * d
        ρmintemp = max(ρmintemp_a, ρmintemp_b)
        øMn = ø * ρmin * fy * (d - (a / 2)) * (1000 / 1)  # Conversión a Kn.m
        
        cumple_momento = "CUMPLE" if øMn > Mu else "NO CUMPLE"
        cumple_cortante = "cortante no requiere estribos" if 1/2 * (ø) * (0.17) * (λ) * (fc**0.5) * (100) * b * d > Vu else "cortante requiere estribos"
        
        # Mostrar resultados
        label_resultado3.config(text=f"ρ: {ρ:.5f}\na: {a:.2f}\nβ1: {β1:.2f}\nc: {c:.2f}\nєt: {єt:.6f}\nAs: {As:.2f} cm²\n"
                                     f"ρmin: {ρmin:.5f}\nNb: {Nb:.2f}\npmintemp: {ρmintemp:.2f}\nøMn: {øMn:.2f} Kn.m\n"
                                     f"Verificación momento: {cumple_momento}\nVerificación cortante: {cumple_cortante}")
    except ValueError:
        label_resultado3.config(text="Por favor ingrese valores válidos.")

# Crear el notebook (pestañas)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Crear el primer frame (pestaña 1)
frame1 = ttk.Frame(notebook, padding=10)
notebook.add(frame1, text="Cálculo d")

# Crear el segundo frame (pestaña 2)
frame2 = ttk.Frame(notebook, padding=10)
notebook.add(frame2, text="Cálculo MuenMn")

# Crear el tercer frame (pestaña 3)
frame3 = ttk.Frame(notebook, padding=10)
notebook.add(frame3, text="Cálculos Estructurales")

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

# ---- Pestaña 3 (ajustada para que los resultados estén al costado) ----
label_fc = ttk.Label(frame3, text="fc")
label_fy = ttk.Label(frame3, text="fy")
label_Mu = ttk.Label(frame3, text="Mu")
label_b = ttk.Label(frame3, text="b")
label_d = ttk.Label(frame3, text="d")
label_Vu = ttk.Label(frame3, text="Vu")
label_lambda = ttk.Label(frame3, text="λ")

entry_fc = ttk.Entry(frame3, width=20)
entry_fy = ttk.Entry(frame3, width=20)
entry_Mu = ttk.Entry(frame3, width=20)
entry_b = ttk.Entry(frame3, width=20)
entry_d = ttk.Entry(frame3, width=20)
entry_Vu = ttk.Entry(frame3, width=20)
entry_lambda = ttk.Entry(frame3, width=20)

button_calcular3 = ttk.Button(frame3, text="Calcular", command=calcular_pestana3)

label_resultado3 = ttk.Label(frame3, text="", font=('Helvetica', 12, 'bold'), foreground="#007acc")

# Posicionar en el grid de la pestaña 3
frame3.grid_columnconfigure(0, weight=1)
frame3.grid_columnconfigure(1, weight=1)
frame3.grid_columnconfigure(2, weight=1)  # Añadimos una nueva columna para los resultados

# Entradas en la primera columna
label_fc.grid(row=0, column=0, padx=10, pady=10, sticky="E")
entry_fc.grid(row=0, column=1, padx=10, pady=10)

label_fy.grid(row=1, column=0, padx=10, pady=10, sticky="E")
entry_fy.grid(row=1, column=1, padx=10, pady=10)

label_Mu.grid(row=2, column=0, padx=10, pady=10, sticky="E")
entry_Mu.grid(row=2, column=1, padx=10, pady=10)

label_b.grid(row=3, column=0, padx=10, pady=10, sticky="E")
entry_b.grid(row=3, column=1, padx=10, pady=10)

label_d.grid(row=4, column=0, padx=10, pady=10, sticky="E")
entry_d.grid(row=4, column=1, padx=10, pady=10)

label_Vu.grid(row=5, column=0, padx=10, pady=10, sticky="E")
entry_Vu.grid(row=5, column=1, padx=10, pady=10)

label_lambda.grid(row=6, column=0, padx=10, pady=10, sticky="E")
entry_lambda.grid(row=6, column=1, padx=10, pady=10)

button_calcular3.grid(row=7, column=1, pady=20)

# Resultados en la segunda columna
label_resultado3.grid(row=0, column=2, rowspan=8, padx=10, pady=10, sticky="W")  # Ajustar la posición de los resultados

# Iniciar la ventana
root.mainloop()
