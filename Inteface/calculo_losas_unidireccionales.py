from tkinter import messagebox

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
        messagebox.showerror("Por favor, ingrese valores válidos.")
        

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
        messagebox.showerror("Por favor, ingrese valores válidos.")
        
