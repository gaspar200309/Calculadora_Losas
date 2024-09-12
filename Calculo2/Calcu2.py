from tkinter import messagebox
import tkinter as tk

# Variables globales
h = 0.25  # (m)
b = 0.10  # (m)
Asøprincipal = 0.0010  # (m)
rec = 0.025  # (m)
fc = 21  # (MPa)
fy = 420  # (MPa)
Mu = 21.93  # (Kn)
Vu = 26.36  # (Kn)
λ = 1
ø = 0.9 

# ECUACIÓN: Calcular d
def calcular_d(entryD):
    global h, rec, Asøprincipal
    try:
        # Realizar cálculo
        d = h - rec - (Asøprincipal / 2)
        print(f'd = {d:.2f}')
        entryD.delete(0, tk.END)
        entryD.insert(0, f'{d:.2f}')
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# ECUACIÓN: Calcular Mu en Mn
def calcular_MuenMn(res_Mu):
    global Mu
    try:
        # Realizar cálculo
        MuenMn = Mu / 1000
        print(f'Mu = {MuenMn:.2f}')
        res_Mu.delete(0, tk.END)
        res_Mu.insert(0, f'{MuenMn:.2f}')
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# ECUACIÓN: Calcular ρ
def calcular_p(entry_p):
    global fc, fy, Mu, ø, b, h
    try:
        d = h - rec - (Asøprincipal / 2)  # Asumiendo el valor de 'd' calculado antes
        ρ = (0.85 * fc / fy) * (1 - (1 - 2 * Mu / (ø * 0.85 * fc * b * d**2))**0.5)
        print(f'ρ = {ρ:.5f}')
        entry_p.delete(0, tk.END)
        entry_p.insert(0, f'{ρ:.5f}')
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# ECUACIÓN: Calcular cortante
def calcular_cortante():
    global ø, λ, b, h, Vu, fc
    try:
        d = h - rec - (Asøprincipal / 2)  # Usar 'd' calculado antes
        cortante = 1/2 * ø * 0.17 * λ * (fc**0.5) * 100 * b * d
        print(f'Cortante = {cortante:.2f}')
        
        if cortante > Vu:
            messagebox.showinfo("Resultado", f"Cortante es mayor: {cortante:.2f}")
        else:
            messagebox.showinfo("Resultado", f"Cortante es menor o igual: {cortante:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
