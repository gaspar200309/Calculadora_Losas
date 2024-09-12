from tkinter import Tk, Label, Button, Entry
#Creamos una clase
ventana=Tk()
ventana.title("Diseño Estructural")
ventana.geometry("400x500")

lbl =Label(ventana,text="CÁLCULO Y DIMENSIONADO DE LOSAS UNIDIRECCIONALES")
lbl.pack()

lbl =Label(ventana,text="INTRODUCCION DE DATOS")
lbl.place(x=20,y=30)

#Resolución
lbl =Label(ventana,text="BÚSQUEDA 1. DETERMINACIÓN DE LA ALTURA UTIL")
lbl.place(x=20,y=30)

#ECUACIÓN
def calcular_d():
    try:

        h =float(entry_h.get())
        rec =float(entry_rec.get())
        Asøprincipal =float(entry_Asøprincipal.get())
        
        #Realizar calculo
        d=h-rec-(Asøprincipal/2)
        #Resultado
        resultado_label_d.config(text=f'd = {d:.2f}')
    except ValueError:
        resultado_label_d.config(text="Por favor, ingrese valores válidos.")
             
#widgets
#Dato 1
label_before_entry = Label(ventana, text="h=")
label_before_entry.place(x=20,y=60)

entry_h=Entry(ventana, width=5)
entry_h.place(x=50,y=60)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=60)

#Dato 2
label_before_entry = Label(ventana, text="b=")
label_before_entry.place(x=20,y=90)

entry_rec=Entry(ventana, width=5)
entry_rec.place(x=50,y=90)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=90)

#Dato 3
label_before_entry = Label(ventana, text="Asøprincipal=")
label_before_entry.place(x=20,y=110)

entry_Asøprincipal=Entry(ventana, width=8)
entry_Asøprincipal.place(x=115,y=110)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=150,y=110)

#Dato 4
label_before_entry = Label(ventana, text="rec=")
label_before_entry.place(x=20,y=130)

entry_rec=Entry(ventana, width=5)
entry_rec.place(x=50,y=130)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=130)     

#Botón    
btn = Button(ventana, text="Calcular", command=calcular_d, bg="yellow")
btn.pack(pady=150)
   
#Resultado
resultado_label_d = Label(ventana, text="d = ")
resultado_label_d.place(x=130,y=180)

#Resolución
lbl =Label(ventana,text="BÚSQUEDA 2. TRANSFORMACION DEL MOMENTO UTLIMO")
lbl.place(x=20,y=200)
        
#ECUACIÓN
def calcular_MuenMn():
    try:

        Mu =float(entry_Mu.get())
        
        #Realizar calculo
        MuenMn= Mu/1000
        #Resultado
        resultado_label_MuenMn.config(text=f'MuenMn = {MuenMn:.2f}')
    except ValueError:
        resultado_label_MuenMn.config(text="Por favor, ingrese valores válidos.")
        
#widgets
#Dato 1
label_before_entry = Label(ventana, text="Mu=")
label_before_entry.place(x=20,y=230)

entry_Mu=Entry(ventana, width=5)
entry_Mu.place(x=50,y=230)

label_after_entry = Label(ventana, text="Mn")
label_after_entry.place(x=90,y=230)

#Botón    
btn = Button(ventana, text="Calcular", command=calcular_d, bg="yellow")
btn.pack(pady=150)

#Resultado
resultado_label_MuenMn = Label(ventana, text="Mu = ")
resultado_label_MuenMn.place(x=130,y=270)

#Resolución
lbl =Label(ventana,text="#BÚSQUEDA 3.4 AREA REQUERIDO DE ACERO")
lbl =Label(ventana,text="As= ρ b d")
lbl.place(x=20,y=300)

#ECUACIÓN
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
             
#widgets
#Dato 1
label_before_entry = Label(ventana, text="ρ=")
label_before_entry.place(x=20,y=320)

entry_ρ=Entry(ventana, width=5)
entry_ρ.place(x=50,y=320)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=320)

label_before_entry = Label(ventana, text="b=")
label_before_entry.place(x=20,y=340)

entry_b=Entry(ventana, width=5)
entry_b.place(x=50,y=340)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=340)

label_before_entry = Label(ventana, text="d=")
label_before_entry.place(x=20,y=360)

entry_d=Entry(ventana, width=5)
entry_d.place(x=50,y=360)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=360)

#Botón    
btn = Button(ventana, text="Calcular", command=calcular_As, bg="yellow")
btn.pack(pady=150)

#Resultado
resultado_label_As= Label(ventana, text="As = ")
resultado_label_As.place(x=130,y=400)

        
#Resolución
lbl =Label(ventana,text="#BÚSQUEDA 3.5 REFUERZO MÍNIMO A FLEXIÓN EN LOSAS NO PREESFORZADAS")
lbl =Label(ventana,text="como f_y≥420MPa ⟾A_(s min)*(0.0018X420 )/((420MPa) )*(0.045m^2 )=0.000081m^2= 0.81〖cm〗^2")
lbl.place(x=20,y=420)

#ECUACIÓN
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
          
       #Resolución
    lbl =Label(ventana,text="#NÚMERO DE BARRAS")
    lbl =Label(ventana,text="#NÚMERO DE BARRAS")
    lbl.place(x=20,y=480)

#ECUACIÓN
def calcular_Nb():
    try:

        ρmin=float(entry_ρmin.get())
        
        #Realizar calculo
        Nb= ρmin/1.13
        #Resultado
        resultado_label_Nb.config(text=f' Nb = {Nb:.2f}')
    except ValueError:
        resultado_label_Nb.config(text="Por favor, ingrese valores válidos.")
        
    #widgets
    #Dato 1
    label_before_entry = Label(ventana, text=" ρmin=")
    label_before_entry.place(x=20,y=500)

    entry_ρ=Entry(ventana, width=5)
    entry_ρ.place(x=50,y=500)

    label_after_entry = Label(ventana, text="m")
    label_after_entry.place(x=90,y=500)

    
    #Resultado
    resultado_label_Nb= Label(ventana, text="Nb= ")
    resultado_label_Nb.place(x=130,y=540) 
    
    
    #Resolución
    lbl =Label(ventana,text="#BÚSQUEDA 3.6. REFUERZO CORRUGADO DE RETRACCIÓN Y TEMPERATURA")
    lbl =Label(ventana,text="As min⁡temperatura = ρ*b (1m analisis)*d (altura util de la carpeta 0.05m/2=0.025m )")
    lbl.place(x=20,y=560)

    #ECUACIÓN
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
            
            
        #widgets
        #Dato 1
label_before_entry = Label(ventana, text="fy=")
label_before_entry.place(x=20,y=580)

entry_ρ=Entry(ventana, width=5)
entry_ρ.place(x=50,y=580)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=580)

label_before_entry = Label(ventana, text="d=")
label_before_entry.place(x=20,y=600)

entry_b=Entry(ventana, width=5)
entry_b.place(x=50,y=600)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=600)

    
        #Resultado
resultado_label_ρmintemp= Label(ventana, text="ρmintemp = ")
resultado_label_ρmintemp.place(x=130,y=620)       

    
    #Resolución
lbl =Label(ventana,text="#BÚSQUEDA 3.7 DETERMINANDO EL MOMENTO NOMINAL")
lbl =Label(ventana,text="〖ø M〗n= ø As*fy*(d-a/2)")
lbl.place(x=20,y=640)

    #ECUACIÓN
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
            
            
        #widgets
        #Dato 1
label_before_entry = Label(ventana, text="øMn=")
label_before_entry.place(x=20,y=660)

entry_ρ=Entry(ventana, width=5)
entry_ρ.place(x=50,y=660)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=660)

label_before_entry = Label(ventana, text="ρmin=")
label_before_entry.place(x=20,y=680)

entry_b=Entry(ventana, width=5)
entry_b.place(x=50,y=680)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=680)

label_before_entry = Label(ventana, text="d=")
label_before_entry.place(x=20,y=700)

entry_b=Entry(ventana, width=5)
entry_b.place(x=50,y=700)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=700)

label_before_entry = Label(ventana, text="a=")
label_before_entry.place(x=20,y=720)

entry_b=Entry(ventana, width=5)
entry_b.place(x=50,y=720)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=720)

#Resultado
resultado_label_øMn= Label(ventana, text="øMn = ")
resultado_label_øMn.place(x=130,y=740)    

#Resolución
lbl =Label(ventana,text="#Verificación")
lbl.place(x=20,y=760)

#ECUACIÓN
def calcular_condicion ():
    try:

        øMn=float(entry_øMn.get())
        Mu=float(entry_Mu.get())
        
        
        #Resultado
        resultado_label_Nb.config(text='CUMPLE')
        resultado_label_Nb.config(text='NO CUMPLE')
    except ValueError:
        resultado_label_Nb.config(text="Por favor, ingrese valores válidos para øMn y Mu ")
        
        #widgets
        #Dato 1
label_before_entry = Label(ventana, text="øMn=")
label_before_entry.place(x=20,y=780)

entry_ρ=Entry(ventana, width=5)
entry_ρ.place(x=50,y=780)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=780)

label_before_entry = Label(ventana, text="Mu=")
label_before_entry.place(x=20,y=800)

entry_b=Entry(ventana, width=5)
entry_b.place(x=50,y=800)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=800)
        
        #Resultado
resultado_label_øMn= Label(ventana, text="condicion = ")
resultado_label_øMn.place(x=130,y=820)    
        
#Resolución
lbl =Label(ventana,text="#VERIFICACIÓN AL CORTANTE")
lbl.place(x=20,y=820)

        #ECUACIÓN
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
        #widgets
        #Dato 1
label_before_entry = Label(ventana, text="ø=")
label_before_entry.place(x=20,y=840)

entry_ρ=Entry(ventana, width=5)
entry_ρ.place(x=50,y=840)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=840)

label_before_entry = Label(ventana, text="λ=")
label_before_entry.place(x=20,y=860)

entry_b=Entry(ventana, width=5)
entry_b.place(x=50,y=860)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=860)
    
label_before_entry = Label(ventana, text="b=")
label_before_entry.place(x=20,y=880)

entry_b=Entry(ventana, width=5)
entry_b.place(x=50,y=880)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=880)

label_before_entry = Label(ventana, text="d=")
label_before_entry.place(x=20,y=900)

entry_b=Entry(ventana, width=5)
entry_b.place(x=50,y=900)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=900)

label_before_entry = Label(ventana, text="Vu=")
label_before_entry.place(x=20,y=920)

entry_b=Entry(ventana, width=5)
entry_b.place(x=50,y=920)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=920)

#Resultado
resultado_label_øMn= Label(ventana, text="condicion = ")
resultado_label_øMn.place(x=130,y=940)    
ventana.mainloop()
    