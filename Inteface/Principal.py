import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from calculo_losas_unidireccionales import *

title_config = {
    "background": "#f9f6f2",
    "font": ("Comic Sans MS", 15, "bold"),
    "foreground": "black",
    "anchor": "w",
}

label_config = {
    "background": "#f9f6f2",
    "font": ("Comic Sans MS", 11),
    "foreground": "black",
    "anchor": "w",   
}

entry_config = {
    "background": "#fffee1",
    "font": ("Comic Sans MS", 11, "italic"),
    "foreground": "black",
    "insertbackground": "black",
}

class principal:
    def __init__(self, top=None):
        top.geometry("787x624+400+150")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Calculadora de Losas")
        top.configure(background="#f9f6f2")
        self.top = top

        def bloquear_escritura(event):
             return "break"
        
        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.496, rely=0.929, height=26, width=47)
        self.Button1.configure(background="#fefda6",font=("Courier New", 10, "bold"))
        self.Button1.configure(text='''EXIT''', command=self.top.destroy)

        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(relx=0.017, rely=0.022, relheight=0.894, relwidth=0.972)
        self.theEc1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.theEc1, padding=3)
        self.TNotebook1.tab(0, text='''Ecuacion 1''', compound="left",underline='''-1''', )
        self.theEc1.configure(background="#f9f6f2")
        self.theEc2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.theEc2, padding=3)
        self.TNotebook1.tab(1, text='''Ecuacion 2''', compound="left",underline='''-1''', )
        self.theEc2.configure(background="#f9f6f2")
        self.theEc3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.theEc3, padding=3)
        self.TNotebook1.tab(2, text='''Ecuacion 3''', compound="left",underline='''-1''', )
        self.theEc3.configure(background="#d9d9d9")
        
        #Ecuacion 1

        self.entryD = tk.Entry(self.theEc1)
        self.entryD.place(relx=0.709, rely=0.223, height=20, relwidth=0.189)
        self.entryD.configure(**entry_config)
        self.entryD.bind("<Key>",bloquear_escritura)

        self.entry_rec = tk.Entry(self.theEc1)
        self.entry_rec.place(relx=0.197, rely=0.324, height=20, relwidth=0.189)
        self.entry_rec.configure(**entry_config)

        self.Label1 = tk.Label(self.theEc1)
        self.Label1.place(relx=0.039, rely=0.131, height=21, width=34)
        self.Label1.configure(**label_config,text='''H''')
        self.labD = tk.Label(self.theEc1)
        self.labD.place(relx=0.629, rely=0.225, height=21, width=34)
        self.labD.configure(**label_config,text='''d''')
        self.labRec = tk.Label(self.theEc1)
        self.labRec.place(relx=0.039, rely=0.318, height=21, width=34)
        self.labRec.configure(**label_config,text='''Rec''')
        
        self.entry_h = tk.Entry(self.theEc1)
        self.entry_h.place(relx=0.197, rely=0.137, height=20, relwidth=0.189)
        self.entry_h.configure(**entry_config)

        self.entry_Asøprincipal = tk.Entry(self.theEc1)
        self.entry_Asøprincipal.place(relx=0.197, rely=0.223, height=20, relwidth=0.189)
        self.entry_Asøprincipal.configure(**entry_config)

        self.labAso = tk.Label(self.theEc1)
        self.labAso.place(relx=0.039, rely=0.225, height=21, width=94)
        self.labAso.configure(**label_config,text='''AsoPrincipal''')
        self.labTitle = tk.Label(self.theEc1)
        
        self.btnCalcular = tk.Button(self.theEc1)
        self.btnCalcular.place(relx=0.472, rely=0.449, height=36, width=67)
        self.btnCalcular.configure(background="#fefda6",text='''Calcular''')
        self.btnCalcular.configure(font=("Comic Sans MS", 10, "bold"))
        self.btnCalcular.configure(command = lambda: calcular_d(self.entry_h.get(), self.entry_rec.get(), self.entry_Asøprincipal.get(), self.entryD))
        
        self.labTitle.place(relx=0.28, rely=0.037, height=41, width=534)
        self.labTitle.configure(**title_config,text='''DETERMINACIÓN DE LA ALTURA UTIL''')

        self.Entry2 = tk.Entry(self.theEc2)
        self.Entry2.place(relx=0.642, rely=0.187, height=20, relwidth=0.189)
        self.Entry2.configure(**entry_config)
        self.Entry1 = tk.Entry(self.theEc2)
        self.Entry1.place(relx=0.157, rely=0.206, height=20, relwidth=0.189)
        self.Entry1.configure(**entry_config)
        
        #Ecuacion 2 
        
        self.entry_Mu = tk.Entry(self.theEc2)
        self.entry_Mu.place(relx=0.157, rely=0.206, height=20, relwidth=0.189)
        self.entry_Mu.configure(**entry_config)       

        self.res_Mu = tk.Entry(self.theEc2)
        self.res_Mu.place(relx=0.642, rely=0.187, height=20, relwidth=0.189)
        self.res_Mu.configure(**entry_config)
        self.res_Mu.bind("<Key>",bloquear_escritura)
        self.labMu = tk.Label(self.theEc2)
        self.labMu.place(relx=0.052, rely=0.206, height=21, width=34)
        self.labMu.configure(**label_config,text='''Mu''')
        
        self.labd = tk.Label(self.theEc2)
        self.labd.place(relx=0.507, rely=0.187, height=21, width=75)
        self.labd.configure(**label_config,text='''MuenMn''')

        self.btnCal2 = tk.Button(self.theEc2)
        self.btnCal2.place(relx=0.472, rely=0.375, height=36, width=67)
        self.btnCal2.configure(background="#fefda6")
        self.btnCal2.configure(text='''Calcular''')
        self.btnCal2.configure(command=lambda: calcular_MuenMn(self.entry_Mu.get(), self.res_Mu))

        self.labTitle2 = tk.Label(self.theEc2)
        self.labTitle2.place(relx=0.207, rely=0.037, height=31, width=524)
        self.labTitle2.configure(**title_config,text='''TRANSFORMACION DEL MOMENTO ULTIMO''')
        
        
        
        #Ecuacion 3

        self.labTitle3 = tk.Label(self.theEc3)
        self.labTitle3.place(relx=0.35, rely=0.056, height=41, width=240)
        self.labTitle3.configure(**title_config,text='''Seleccione la ecuacion''')


        #Entradas
        
        self.labfc = tk.Label(self.theEc3)
        self.labfc.place(relx=0.03, rely=0.206, height=21, width=25)
        self.labfc.configure(**label_config,text='''fc''')
        
        self.entry_fc = tk.Entry(self.theEc3)
        self.entry_fc.place(relx=0.07, rely=0.206, height=20, relwidth=0.139)
        self.entry_fc.configure(**entry_config)  
        
        self.labfy = tk.Label(self.theEc3)
        self.labfy.place(relx=0.230, rely=0.206, height=21, width=25)
        self.labfy.configure(**label_config,text='''fy''')   
        
        self.entry_fy = tk.Entry(self.theEc3)
        self.entry_fy.place(relx=0.284, rely=0.206, height=20, relwidth=0.139)
        self.entry_fy.configure(**entry_config)  
        
        self.labMu = tk.Label(self.theEc3)
        self.labMu.place(relx=0.455, rely=0.206, height=21, width=25)
        self.labMu.configure(**label_config,text='''Mu''')   
        
        self.entry_Mu3 = tk.Entry(self.theEc3)
        self.entry_Mu3.place(relx=0.505, rely=0.206, height=20, relwidth=0.139)
        self.entry_Mu3.configure(**entry_config)
        
        self.labP = tk.Label(self.theEc3)
        self.labP.place(relx=0.675, rely=0.206, height=21, width=25)
        self.labP.configure(**label_config,text='''p''')   
        
        self.entry_P = tk.Entry(self.theEc3)
        self.entry_P.place(relx=0.725, rely=0.206, height=20, relwidth=0.139)
        self.entry_P.configure(**entry_config)
        
        #2da  
        
        self.labVu = tk.Label(self.theEc3)
        self.labVu.place(relx=0.03, rely=0.256, height=21, width=25)
        self.labVu.configure(**label_config,text='''Vu''')   
        
        self.entry_Vu = tk.Entry(self.theEc3)
        self.entry_Vu.place(relx=0.07, rely=0.256, height=20, relwidth=0.139)
        self.entry_Vu.configure(**entry_config)  
        
        self.labλ = tk.Label(self.theEc3)
        self.labλ.place(relx=0.230, rely=0.256, height=21, width=25)
        self.labλ.configure(**label_config,text='''λ''')   
        
        self.entry_λ = tk.Entry(self.theEc3)
        self.entry_λ.place(relx=0.284, rely=0.256, height=20, relwidth=0.139)
        self.entry_λ.configure(**entry_config)   
        
        self.labø = tk.Label(self.theEc3)
        self.labø.place(relx=0.455, rely=0.256, height=21, width=25)
        self.labø.configure(**label_config,text='''ø''')  
        
        self.entry_ø = tk.Entry(self.theEc3)
        self.entry_ø.place(relx=0.505, rely=0.256, height=20, relwidth=0.139)
        self.entry_ø.configure(**entry_config)   
        
        self.labc = tk.Label(self.theEc3)
        self.labc.place(relx=0.675, rely=0.256, height=21, width=25)
        self.labc.configure(**label_config,text='''c''')  
        
        self.entry_c = tk.Entry(self.theEc3)
        self.entry_c.place(relx=0.725, rely=0.256, height=20, relwidth=0.139)
        self.entry_c.configure(**entry_config)   
        
        #3ra
        
        self.labb = tk.Label(self.theEc3)
        self.labb.place(relx=0.03, rely=0.306, height=21, width=25)
        self.labb.configure(**label_config,text='''b''')   
        
        self.entry_b3 = tk.Entry(self.theEc3)
        self.entry_b3.place(relx=0.07, rely=0.306, height=20, relwidth=0.139)
        self.entry_b3.configure(**entry_config)  
        
        self.labd3 = tk.Label(self.theEc3)
        self.labd3.place(relx=0.230, rely=0.306, height=21, width=25)
        self.labd3.configure(**label_config,text='''d''')   
        
        self.entry_d3 = tk.Entry(self.theEc3)
        self.entry_d3.place(relx=0.284, rely=0.306, height=20, relwidth=0.139)
        self.entry_d3.configure(**entry_config)   
        
        self.labB1 = tk.Label(self.theEc3)
        self.labB1.place(relx=0.455, rely=0.306, height=21, width=25)
        self.labB1.configure(**label_config,text='''B1''')  
        
        self.entry_B1 = tk.Entry(self.theEc3)
        self.entry_B1.place(relx=0.505, rely=0.306, height=20, relwidth=0.139)
        self.entry_B1.configure(**entry_config)   
        
        self.labpmin = tk.Label(self.theEc3)
        self.labpmin.place(relx=0.675, rely=0.306, height=21, width=35)
        self.labpmin.configure(**label_config,text='''pmin''')  
        
        self.entry_pmin = tk.Entry(self.theEc3)
        self.entry_pmin.place(relx=0.725, rely=0.306, height=20, relwidth=0.139)
        self.entry_pmin.configure(**entry_config)
        
        


        self.optn1 = tk.Button(self.theEc3)
        self.optn1.place(relx=0.03, rely=0.437, height=46, width=237)
        self.optn1.configure(background="#fffee1")
        self.optn1.configure(foreground="#000000")
        self.optn1.configure(text='''Porcentaje de acero requerido''')
        self.optn1.configure(command=lambda: calcular_p(self.entry_fc.get(), self.entry_fy.get(), self.entry_Mu3.get(), self.entry_ø.get(), self.entry_b3.get(), self.entry_d3.get(),self.entry_P))
        
        self.optn2 = tk.Button(self.theEc3)
        self.optn2.place(relx=0.03, rely=0.537, height=46, width=237)
        self.optn2.configure(activebackground="#d9d9d9")
        self.optn2.configure(activeforeground="black")
        self.optn2.configure(background="#fffee1")
        self.optn2.configure(disabledforeground="#a3a3a3")
        self.optn2.configure(font="-family {Segoe UI} -size 9")
        self.optn2.configure(text='''Verificacion viga T''')
        
        self.optn3 = tk.Button(self.theEc3)
        self.optn3.place(relx=0.03, rely=0.637, height=46, width=237)
        self.optn3.configure(activebackground="#d9d9d9")
        self.optn3.configure(activeforeground="black")
        self.optn3.configure(background="#fffee1")
        self.optn3.configure(disabledforeground="#a3a3a3")
        self.optn3.configure(font="-family {Segoe UI} -size 9")
        self.optn3.configure(text='''β1 para distribucion de esfuerzo''')
        
        self.optn4 = tk.Button(self.theEc3)
        self.optn4.place(relx=0.03, rely=0.737, height=46, width=237)
        self.optn4.configure(activebackground="#d9d9d9")
        self.optn4.configure(activeforeground="black")
        self.optn4.configure(background="#fffee1")
        self.optn4.configure(disabledforeground="#a3a3a3")
        self.optn4.configure(font="-family {Segoe UI} -size 9")
        self.optn4.configure(text='''Distancia al eje neutro''')
        
        self.optn5 = tk.Button(self.theEc3)
        self.optn5.place(relx=0.03, rely=0.837, height=46, width=237)
        self.optn5.configure(activebackground="#d9d9d9")
        self.optn5.configure(activeforeground="black")
        self.optn5.configure(background="#fffee1")
        self.optn5.configure(disabledforeground="#a3a3a3")
        self.optn5.configure(font="-family {Segoe UI} -size 9")
        self.optn5.configure(text='''Et a traves de la relacion de triangulos''')
        
        self.optn6 = tk.Button(self.theEc3)
        self.optn6.place(relx=0.354, rely=0.437, height=46, width=237)
        self.optn6.configure(activebackground="#d9d9d9")
        self.optn6.configure(activeforeground="black")
        self.optn6.configure(background="#fffee1")
        self.optn6.configure(disabledforeground="#a3a3a3")
        self.optn6.configure(font="-family {Segoe UI} -size 9")
        self.optn6.configure(text='''Area requerida de acero''')
        
        self.optn7 = tk.Button(self.theEc3)
        self.optn7.place(relx=0.354, rely=0.537, height=46, width=237)
        self.optn7.configure(activebackground="#d9d9d9")
        self.optn7.configure(activeforeground="black")
        self.optn7.configure(background="#fffee1")
        self.optn7.configure(disabledforeground="#a3a3a3")
        self.optn7.configure(font="-family {Segoe UI} -size 9")
        self.optn7.configure(text='''Refuerzo minimo''')
        
        self.optn8 = tk.Button(self.theEc3)
        self.optn8.place(relx=0.354, rely=0.637, height=46, width=237)
        self.optn8.configure(activebackground="#d9d9d9")
        self.optn8.configure(activeforeground="black")
        self.optn8.configure(background="#fffee1")
        self.optn8.configure(disabledforeground="#a3a3a3")
        self.optn8.configure(font="-family {Segoe UI} -size 9")
        self.optn8.configure(text='''Numero de barras''')
        
        self.optn9 = tk.Button(self.theEc3)
        self.optn9.place(relx=0.354, rely=0.737, height=46, width=237)
        self.optn9.configure(activebackground="#d9d9d9")
        self.optn9.configure(activeforeground="black")
        self.optn9.configure(background="#fffee1")
        self.optn9.configure(disabledforeground="#a3a3a3")
        self.optn9.configure(font="-family {Segoe UI} -size 9")
        self.optn9.configure(text='''Refuerzo corrugado''')
        
        self.optn10 = tk.Button(self.theEc3)
        self.optn10.place(relx=0.354, rely=0.837, height=46, width=237)
        self.optn10.configure(activebackground="#d9d9d9")
        self.optn10.configure(activeforeground="black")
        self.optn10.configure(background="#fffee1")
        self.optn10.configure(disabledforeground="#a3a3a3")
        self.optn10.configure(font="-family {Segoe UI} -size 9")
        self.optn10.configure(text='''Momento nominal''')
        
        self.optn11 = tk.Button(self.theEc3)
        self.optn11.place(relx=0.675, rely=0.437, height=46, width=237)
        self.optn11.configure(activebackground="#d9d9d9")
        self.optn11.configure(activeforeground="black")
        self.optn11.configure(background="#fffee1")
        self.optn11.configure(disabledforeground="#a3a3a3")
        self.optn11.configure(font="-family {Segoe UI} -size 9")
        self.optn11.configure(text='''Verificacion al cortante''')

        
        self.optn12 = tk.Button(self.theEc3)
        self.optn12.place(relx=0.675, rely=0.537, height=46, width=237)
        self.optn12.configure(activebackground="#d9d9d9")
        self.optn12.configure(activeforeground="black")
        self.optn12.configure(background="#fffee1")
        self.optn12.configure(disabledforeground="#a3a3a3")
        self.optn12.configure(font="-family {Segoe UI} -size 9")
        self.optn12.configure(text='''Calcular todo''')

def main(*args):
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creamos un widget global
    global _top1, _w1
    _top1 = root
    _w1 = principal(_top1)# Llamamos a la funcion pa configurar la ventana
    root.mainloop()

if __name__ == '__main__':
    main()