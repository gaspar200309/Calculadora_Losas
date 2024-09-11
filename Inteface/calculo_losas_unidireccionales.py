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
        
def verificar_vigaT(ρ, fy, d, fc, entry_a):
    try:
        ρ =float(ρ)  
        fy =float(fy)  
        d =float(d)    
        fc =float(fc)  
    
        a=ρ*fy*d/(0.85*fc)
        messagebox.showinfo("Correcto", f'{a:.5f}')
        
        entry_a.delete(0, tk.END)
        entry_a.insert(0, f'{a:.5f}')
    except ValueError: 
        messagebox.showerror("error", "Por favor, ingrese valores válidos.")
        
def calcular_B1(fc):
    try:
        if fc<28:
            β1 = 0.85 
        elif fc<55:
            β1 = 0.65
        else:   
            β1 = 0.85-(0.05*(fc-28)/7)
        messagebox.showinfo("Correcto", f'{β1:.5f}')
    except ValueError: 
        messagebox.showerror("error", "Por favor, ingrese valores válidos.")
        
def calcular_c(a, β1, entry_c):
    try:
        a =float(a)  
        β1 =float(β1)  
        c=a/β1
        
        messagebox.showinfo("Correcto", f'{c:.5f}')
        entry_c.delete(0, tk.END)
        entry_c.insert(0, f'{c:.5f}')
    except ValueError: 
        messagebox.showerror("error", "Por favor, ingrese valores válidos.")
        
def calcular_Et(d, c):
    try:
        d =float(d)  
        c =float(c)  
        єt=d-c*0.003/(c)
        
        messagebox.showinfo("Correcto", f'{єt:.5f}')
    except ValueError: 
        messagebox.showerror("error", "Por favor, ingrese valores válidos.")
        
        
def calcular_As(ρ, b, d):
    try:

        ρ=float(ρ)
        b=float(b)
        d=float(d)
        
        #Realizar calculo
        As=ρ*(b*100)*(d*100)
        #Resultado
        messagebox.showinfo("Correcto", f'{As:.5f}')

    except ValueError:
        messagebox.showerror("error", "Por favor, ingrese valores válidos.")
        

def calcular_ρmin(fy, entry_pmin):
    try:

        fy=float(fy)
        ρmin_a = (0.0018*420/fy)*0.045
        ρmin_b= 0.0014*0.045
        
        
        #Realizar calculo
        ρmin=max(ρmin_a, ρmin_b)
        #Resultado
        messagebox.showinfo("Correcto", f'{ρmin:.5f}')
        entry_pmin.delete(0, tk.END)
        entry_pmin.insert(0, f'{ρmin:.5f}')

    except ValueError:
        messagebox.showerror("error", "Por favor, ingrese valores válidos.")
        
        
def calcular_Nb(ρmin):
    try:

        ρmin=float(ρmin)
        
        #Realizar calculo
        Nb= ρmin/1.13
        #Resultado
        messagebox.showinfo("Correcto", f'{Nb:.5f}')
    except ValueError:
        messagebox.showerror("error", "Por favor, ingrese valores válidos.")
        

def calcular_ρmintemp(fy, d):
        try:

            fy=float(fy)
            d=float(d)
            
            
            #Realizar calculo
            ρmintemp_a= (0.0018*420/fy)*1*d
            ρmintemp_b= 1.4*1*d
            ρmintemp= max(ρmintemp_a,ρmintemp_b)
            
            #Resultado
            messagebox.showinfo("Correcto", f'{ρmintemp:.5f}')

        except ValueError:
            messagebox.showerror("error", "Por favor, ingrese valores válidos.")
            
def calcular_øMn(ø, ρmin, d, a, fy, Mu=None):
        try:
            ø=float(ø)
            ρmin=float(ρmin)
            d=float(d)
            a=float(a)
            fy=float(fy)
            Mu=float(Mu)
            
            #Realizar calculo
            øMn= ø*ρmin*fy*(d-(a/2))*(1000/1)
            res = ""
            if(Mu):
                if øMn>Mu:
                    res="CUMPLE"
            else:
                res="NO CUMPLE"
            #Resultado
            messagebox.showinfo("Correcto", f'{øMn:.5f} {res}')
        except ValueError:
            messagebox.showerror("error", "Por favor, ingrese valores válidos.")
            

# def calcular_condicion ():
#     try:

#         øMn=float(entry_øMn.get())
#         Mu=float(entry_Mu.get())
        
        
#         #Resultado
#         resultado_label_Nb.config(text='CUMPLE')
#         resultado_label_Nb.config(text='NO CUMPLE')
#     except ValueError:
#         resultado_label_Nb.config(text="Por favor, ingrese valores válidos para øMn y Mu ")
        
def calcular_cortante(ø, λ, b, d, Vu, fc ):
    try:
        ø = float(ø)
        λ = float(λ)
        b = float(b)
        d = float(d)
        Vu = float(Vu)
        fc = float(Vu)  # Asegúrate de tener este valor definido o un Entry correspondiente

        # Resultado de la cortante (ejemplo de comparación)
        cortante = 1/2 * (ø) * (0.17) * (λ) * (fc**0.5) * (100) * b * d
        
        # Verificamos si el cortante es mayor que el Vu para realizar alguna acción
        if cortante > Vu:
            messagebox.showinfo(f"Cortante es mayor: {cortante:.2f}")
        else:
            messagebox.showinfo(f"Cortante es menor o igual: {cortante:.2f}")
            
    except ValueError:
        messagebox.showerror("error", "Por favor, ingrese valores válidos.")