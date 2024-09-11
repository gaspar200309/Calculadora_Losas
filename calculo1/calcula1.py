import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Cálculo")

root.geometry("400x300")
root.config(bg="#f2f2f2")  

# Función para el botón de calcular
def calcular_action():
    try:
        # Obtener los valores ingresados y convertirlos a flotantes
        h = float(entry_h.get())
        asoprincipal = float(entry_asoprincipal.get())
        rec = float(entry_rec.get())
        
        # Cálculo de d
        d = h - rec - (asoprincipal / 2)
        
        # Mostrar el resultado de d en la etiqueta
        label_resultado.config(text=f"Resultado de d: {d:.2f}")
    except ValueError:
        # Manejo de errores si los valores no son numéricos
        label_resultado.config(text="Por favor ingrese valores válidos.")

# Estilo para los elementos
style = ttk.Style()
style.configure('TLabel', background='#f2f2f2', font=('Helvetica', 12), foreground='#333')
style.configure('TButton', background='#007acc', foreground='#ffffff', font=('Helvetica', 12))  # Color de texto blanco

# Etiquetas (Labels)
label_h = ttk.Label(root, text="H")
label_asoprincipal = ttk.Label(root, text="Asøprincipal")
label_rec = ttk.Label(root, text="rec")

# Campos de texto (Entry)
entry_h = ttk.Entry(root, width=20)
entry_asoprincipal = ttk.Entry(root, width=20)
entry_rec = ttk.Entry(root, width=20)

# Botón de Calcular
button_calcular = ttk.Button(root, text="Calcular", command=calcular_action)

# Etiqueta para mostrar el resultado de d
label_resultado = ttk.Label(root, text="", font=('Helvetica', 12, 'bold'), foreground="#007acc")

# Posicionar los elementos en el grid
label_h.grid(row=0, column=0, padx=10, pady=10, sticky="E")
entry_h.grid(row=0, column=1, padx=10, pady=10)

label_asoprincipal.grid(row=1, column=0, padx=10, pady=10, sticky="E")
entry_asoprincipal.grid(row=1, column=1, padx=10, pady=10)

label_rec.grid(row=2, column=0, padx=10, pady=10, sticky="E")
entry_rec.grid(row=2, column=1, padx=10, pady=10)

button_calcular.grid(row=3, column=1, pady=20)

# Posicionar la etiqueta del resultado
label_resultado.grid(row=4, column=1, padx=10, pady=10)

# Iniciar el loop de la ventana
root.mainloop()
