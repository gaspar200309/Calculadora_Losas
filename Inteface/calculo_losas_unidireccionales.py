from tkinter import messagebox
import tkinter as tk

#ECUACIÓN
def calcular_d(h, rec, Asøprincipal, entryD):
    try:
        h =float(h)
        rec =float(rec)
        Asøprincipal =float(Asøprincipal)
        
        #Realizar calculo
        d=h-rec-(Asøprincipal/2)
        #Resultado
        # resultado_label_d.config(text=f'd = {d:.2f}')
        
        entryD.insert(0, f'{d:.2f}')
    except ValueError:
        messagebox.showerror("error", "Por favor, ingrese valores válidos.")
        

#ECUACIÓN
def calcular_MuenMn(Mu, res_Mu):
    try:
        Mu =float(Mu)  
        #Realizar calculo
        MuenMn= Mu/1000
        #Resultado
        # resultado_label_MuenMn.config(text=f'MuenMn = {MuenMn:.2f}')
        
        res_Mu.insert(0, f'{MuenMn:.2f}')
    except ValueError:
        messagebox.showerror("error", "Por favor, ingrese valores válidos.")
        
def calcular_p(fc, fy, Mu, ø, b, d, entry_p):
    try:
        fc =float(fc)  
        fy =float(fy)  
        Mu =float(Mu)  
        ø =float(ø)  
        b =float(d)  
        d =float(d)  
    
        
        ρ=(0.85*fc/fy)*(1-(1-2*Mu/(ø*0.85*fc*b*d**2))**0.5)
        
        messagebox.showinfo("Correcto", f'{ρ:.5f}')
        
        entry_p.delete(0, tk.END)
        entry_p.insert(0, f'{ρ:.5f}')
        
    except ValueError:
        messagebox.showerror("error", "Por favor, ingrese valores válidos.")
        
def calcular_As():
    try:

        ρ=float(entry_ρ.get())
        b=float(entry_b.get())
        d=float(entry_d.get())
        
        #Realizar calculo
        As=ρ*(b*100)*(d*100)
        #Resultado
        resultado_label_As.config(text=f'As = {As:.2f}')
    except ValueError:
        resultado_label_As.config(text="Por favor, ingrese valores válidos.")
        

def calcular_ρmin():
    try:

        fy=float(entry_fy.get())
        ρmin_a == (0.0018*420/fy)*0.045
        ρmin_b= 0.0014*0.045
        
        
        #Realizar calculo
        ρmin=max(ρmin_a, ρmin_b)
        #Resultado
        resultado_label_ρmin.config(text=f' ρmin = {ρmin:.2f}')
    except ValueError:
        resultado_label_ρmin.config(text="Por favor, ingrese valores válidos.")
        
        #widgets
        #Dato 1
        label_before_entry = Label(ventana, text="fy=")
        label_before_entry.place(x=20,y=440)

        entry_ρ=Entry(ventana, width=5)
        entry_ρ.place(x=50,y=440)
        
        #Resultado
        resultado_label_ρmin= Label(ventana, text="ρmin= ")
        resultado_label_ρmin.place(x=130,y=460)
        
        
def calcular_Nb():
    try:

        ρmin=float(entry_ρmin.get())
        
        #Realizar calculo
        Nb= ρmin/1.13
        #Resultado
        resultado_label_Nb.config(text=f' Nb = {Nb:.2f}')
    except ValueError:
        resultado_label_Nb.config(text="Por favor, ingrese valores válidos.")
        

def calcular_ρmintemp():
        try:

            fy=float(entry_fy.get())
            d=float(entry_d.get())
            
            
            #Realizar calculo
            ρmintemp_a= (0.0018*420/fy)*1*d
            ρmintemp_b= 1.4*1*d
            ρmintemp= max(ρmintemp_a,ρmintemp_b)
            
            #Resultado
            resultado_label_Nb.config(text=f' ρmintemp = {ρmintemp:.2f}')
        except ValueError:
            resultado_label_Nb.config(text="Por favor, ingrese valores válidos para fy y d.")
            
def calcular_øMn():
        try:

            øMn=float(entry_øMn.get())
            ρmin=float(entry_ρmin.get())
            d=float(entry_d.get())
            a=float(entry_a.get())
            
            #Realizar calculo
            øMn= ø*ρmin*fy*(d-(a/2))*(1000/1)
            
            #Resultado
            resultado_label_Nb.config(text=f'øMn = {øMn:.2f}')
        except ValueError:
            resultado_label_Nb.config(text="Por favor, ingrese valores válidos ")
            

def calcular_condicion ():
    try:

        øMn=float(entry_øMn.get())
        Mu=float(entry_Mu.get())
        
        
        #Resultado
        resultado_label_Nb.config(text='CUMPLE')
        resultado_label_Nb.config(text='NO CUMPLE')
    except ValueError:
        resultado_label_Nb.config(text="Por favor, ingrese valores válidos para øMn y Mu ")
        
def calcular_cortante():
    try:
        ø = float(entry_ø.get())
        λ = float(entry_λ.get())
        b = float(entry_b.get())
        d = float(entry_d.get())
        Vu = float(entry_Vu.get())
        fc = float(entry_fc.get())  # Asegúrate de tener este valor definido o un Entry correspondiente

        # Resultado de la cortante (ejemplo de comparación)
        cortante = 1/2 * (ø) * (0.17) * (λ) * (fc**0.5) * (100) * b * d
        
        # Verificamos si el cortante es mayor que el Vu para realizar alguna acción
        if cortante > Vu:
            resultado_label_Nb.config(text=f"Cortante es mayor: {cortante:.2f}")
        else:
            resultado_label_Nb.config(text=f"Cortante es menor o igual: {cortante:.2f}")
            
    except ValueError:
        resultado_label_Nb.config(text="Por favor, ingrese valores válidos para los datos.") 