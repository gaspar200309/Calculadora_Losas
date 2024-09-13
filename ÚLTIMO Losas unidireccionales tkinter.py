from tkinter import Tk, Label, Button, Entry, StringVar, ttk

#Creamos una clase
ventana=Tk()
ventana.title("Diseño Estructural")
ventana.geometry("400x800")

lbl =Label(ventana,text="CÁLCULO Y DIMENSIONADO DE LOSAS UNIDIRECCIONALES")
lbl.pack()

def calcular():
    try:
        # Obtener valores de las entradas
        h = float(entry_h.get())
        rec = float(entry_rec.get())
        Asøprincipal = float(entry_Asøprincipal.get())
        Mu = float(entry_Mu.get())
        fc = int(entry_fc.get())
        fy = int(entry_fy.get())
        ø = float(entry_ø.get())
        b = float(entry_b.get())

        # Calcular d
        d = h - rec - (Asøprincipal / 2)
        resultado_label_d.config(text=f'd = {d:.3f}', fg='blue')

        # Calcular MuenMn
        MuenMn = Mu / 1000
        resultado_label_MuenMn.config(text=f'MuenMn = {MuenMn:.4f}', fg='blue')
            
        ρ=(0.85*fc/fy)*(1-(1-(2*MuenMn/(ø*0.85*fc*b*d**2)))**0.5)
        resultado_label_ρ.config(text=f'ρ = {ρ:.6f}', fg='blue')

        # Calcular a
        a = ρ * fy * d / (0.85 * fc)
        resultado_label_a.config(text=f'a = {a:.3f}', fg='blue')
        verificar_a(a)

        # Calcular β1
        β1 = calcular_β1(fc)
        resultado_label_β1.config(text=f'β1 = {β1:.2f}', fg='blue')
        
        # Calcular c
        c = a / β1
        resultado_label_c.config(text=f'c = {c:.3f}', fg='blue')
        
        # Calcular єt
        єt = d-c*0.003/(c)
        resultado_label_єt.config(text=f'єt = {єt:.3f}', fg='blue')
        
        # Calcular As
        As = (ρ*(b*100)*(d*100))/2
        resultado_label_As.config(text=f'As = {As:.2f}', fg='blue')
        
        # Calcular Asmin
        Asmin = calcular_Asmin(fy)
        resultado_label_Asmin.config(text=f'Asmin = {Asmin:.2f}', fg='blue')
        
        # Obtener el valor del factor seleccionado
        factor = float(factor_var.get())
        
        # Calcular Nb
        Nb = Asmin / factor
       # Nb_redondeado = redondear_hacia_arriba (Nb)
        
        resultado_label_Nb_redondeado.config(text=f'Nb = {Nb:}', fg='blue', textvariable= '8mm')
        
        
        # Calcular Asmintemp
        Asmintemp= calcular_Asmintemp(fy, d)
        resultado_label_Asmintemp.config(text=f' Asmintemperatura = {Asmintemp:.2f}' , fg='blue')
        
        #Calcular øMn
        øMn = ø*Asmin*fy*(d-(a/2))*(1000/1)
        print("øMn" + øMn)
        resultado_label_øMn.config(text=f'øMn = {øMn:.2f}' , fg='blue')
        verificar_øMn(øMn)

    except ValueError:
        resultado_label_d.config(text="Por favor, ingrese valores válidos.")
        resultado_label_MuenMn.config(text="Por favor, ingrese valores válidos.")
        resultado_label_ρ.config(text="Por favor, ingrese valores válidos.")
        resultado_label_a.config(text="Por favor, ingrese valores válidos.")
        resultado_label_β1.config(text="Por favor, ingrese valores válidos.")
        resultado_label_c.config(text="Por favor, ingrese valores válidos.")
        resultado_label_єt.config(text="Por favor, ingrese valores válidos.")
        resultado_label_As.config(text="Por favor, ingrese valores válidos.")
        resultado_label_Asmin.config(text="Por favor, ingrese valores válidos.")
        resultado_label_Nb_redondeado.config(text="Por favor, ingrese valores válidos.")
        resultado_label_Asmintemp.config(text="Por favor, ingrese valores válidos.")
        resultado_label_øMn.config(text="Por favor, ingrese valores válidos.")

def verificar_a(a):
    if a > 0.05:
        resultado_verificacion.config(text='VIGA T ( a > hf(0.05m ))')
    else:
        resultado_verificacion.config(text='VIGA RECTANGULAR ( a < hf(0.05m ))')

def calcular_β1(fc):
    if fc < 28:
        return 0.85
    elif fc < 55:
        return 0.65
    else:
        return 0.85 - (0.05 * (fc - 28) / 7)

def calcular_Asmin(fy):
    Asmin_a = (0.0018 * 420 / fy) * (0.045 * 10000)
    Asmin_b = 0.0014 * (0.045 * 10000)
    return max(Asmin_a, Asmin_b)

def redondear_hacia_arriba(numero):
    entero = int(numero)  # Convertir el número a entero (descartar la parte decimal)
    if numero > entero:  # Si el número original tiene parte decimal
        return entero + 2  # Incrementar el entero
    return entero  # Si no tiene parte decimal, devolver el entero directamente

def calcular_Asmintemp(fy, d):
    Asmintemp_a= ((0.0018*420/fy)*1*d)*10000
    Asmintemp_b= (0.0014*1*d)*10000
    return max(Asmintemp_a, Asmintemp_b)

def verificar_øMn(øMn, Mu):    
    if øMn > Mu:
            resultado_verificacion.config(text='CUMPLE')
    elif øMn < Mu:
            resultado_verificacion.config(text='NO CUMPLE')
            
            
# Introducción de datos
Label(ventana, text="INTRODUCCIÓN DE DATOS").place(x=20, y=30)

#D1
Label(ventana, text="h=").place(x=20, y=60)
entry_h = Entry(ventana, width=5)
entry_h.place(x=50, y=60)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=60)

#D2
Label(ventana, text="b=").place(x=20, y=90)
entry_b = Entry(ventana, width=5)
entry_b.place(x=50, y=90)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=90)

#D3
Label(ventana, text="Asøprincipal=").place(x=130, y=60)
entry_Asøprincipal = Entry(ventana, width=8)
entry_Asøprincipal.place(x=220, y=60)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=270,y=60)

#D5
Label(ventana, text="Mu=").place(x=180, y=90)
entry_Mu = Entry(ventana, width=5)
entry_Mu.place(x=220, y=90)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=250,y=90)

#D6
Label(ventana, text="fc=").place(x=20, y=120)
entry_fc = Entry(ventana, width=5)
entry_fc.place(x=50, y=120)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=120)

#D7
Label(ventana, text="fy=").place(x=20, y=150)
entry_fy = Entry(ventana, width=5)
entry_fy.place(x=50, y=150)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=90,y=150)

#D8
Label(ventana, text="ø=").place(x=180, y=120)
entry_ø = Entry(ventana, width=5)
entry_ø.place(x=220, y=120)

#D9
Label(ventana, text="rec=").place(x=180, y=150)
entry_rec = Entry(ventana, width=5)
entry_rec.place(x=220, y=150)

label_after_entry = Label(ventana, text="m")
label_after_entry.place(x=250,y=150)

# Resultados
Label(ventana, text="RESULTADOS", fg='red').place(x=20, y=220)

#1
lbl =Label(ventana,text="BÚSQUEDA 1. DETERMINACIÓN DE LA ALTURA UTIL")
lbl.place(x=20,y=250)
resultado_label_d = Label(ventana, text="d = ")
resultado_label_d.place(x=20, y=270)

#2
lbl =Label(ventana,text="BÚSQUEDA 2. TRANSFORMACION DEL MOMENTO UTLIMO")
lbl.place(x=20,y=290)
resultado_label_MuenMn = Label(ventana, text="Mu a Mn = ")
resultado_label_MuenMn.place(x=20, y=310)

#3
lbl =Label(ventana,text="BÚSQUEDA 3. CUANTÍA O PORCENTAJE DE ACERO REQUERIDO (ρ)")
lbl.place(x=20,y=330)
resultado_label_ρ = Label(ventana, text="ρ = ")
resultado_label_ρ.place(x=20, y=350)

#4
lbl =Label(ventana,text="VERIFICACIÓN. VIGA RECTANGULAR O VIGA T")
lbl.place(x=20,y=370)
resultado_label_a = Label(ventana, text="a = ")
resultado_label_a.place(x=20, y=390)

resultado_verificacion = Label(ventana, text="Verificación")
resultado_verificacion.place(x=20, y=410)

#5
lbl =Label(ventana,text="VALORES β1 PARA LA DISTRIBUCIÓN DE ESFUERZO")
lbl.place(x=20,y=430)
resultado_label_β1 = Label(ventana, text="β1 = ")
resultado_label_β1.place(x=20, y=450)

#6
lbl =Label(ventana,text="BÚSQUEDA 3.2. DISTANCIA AL EJE NEUTRO")
lbl.place(x=20,y=470)
resultado_label_c = Label(ventana, text="c = ")
resultado_label_c.place(x=20, y=490)

#7
lbl =Label(ventana,text="BÚSQUEDA 3.3 Et A TRAVÉS DE LA RELACIÓN DE TRIÁNGULOS")
lbl.place(x=20,y=510)
resultado_label_єt = Label(ventana, text="єt = ")
resultado_label_єt.place(x=20, y=530)

#8
lbl =Label(ventana,text="#BÚSQUEDA 3.4 AREA REQUERIDO DE ACERO")
lbl.place(x=20,y=550)
resultado_label_As = Label(ventana, text="As = ")
resultado_label_As.place(x=20, y=570)

lbl = Label(ventana, text="BÚSQUEDA 3.5 REFUERZO MÍNIMO A FLEXIÓN EN LOSAS NO PREESFORZADAS") 
lbl.place(x=20,y=590)    
resultado_label_Asmin = Label(ventana, text="Asmin = ")
resultado_label_Asmin.place(x=20, y=610)

lbl = Label(ventana, text="BÚSQUEDA 3.5.1 NÚMERO DE BARRAS") 
lbl.place(x=20,y=630)    
resultado_label_Nb_redondeado = Label(ventana, text="Nb = ")
resultado_label_Nb_redondeado.place(x=20, y=650)

# Lista de posibles valores para el factor
factores = [1.13, 0.28, 1.20]

# Variable para el factor seleccionado
factor_var = StringVar(value=factores[0])

# Crear un menú desplegable para seleccionar el factor
Label(ventana, text="Acero:").place(x=170, y=650)  # Etiqueta para el menú desplegable
factor_menu = ttk.Combobox(ventana, textvariable=factor_var, values=factores)
factor_menu.place(x=220, y=650)

#Resolución
lbl =Label(ventana,text="#BÚSQUEDA 3.6. REFUERZO CORRUGADO DE RETRACCIÓN Y TEMPERATURA")
lbl.place(x=20,y=670)
resultado_label_Asmintemp = Label(ventana, text="Asmintemperatura = ")
resultado_label_Asmintemp.place(x=20, y=690)

lbl =Label(ventana,text="#BÚSQUEDA 3.7 DETERMINANDO EL MOMENTO NOMINAL")
lbl.place(x=20,y=710)
resultado_label_øMn= Label(ventana, text="øMn = ")
resultado_label_øMn.place(x=20,y=730)

#Resolución
resultado_verificacion = Label(ventana, text="Verificación øMn>(Mu/2)")
resultado_verificacion.place(x=20, y=750)      

# Botón de cálculo
Button(ventana, text="Calcular", command=calcular, bg="yellow").place(x=130, y=180)

ventana.mainloop()


