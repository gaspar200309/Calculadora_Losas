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
        top.geometry("787x700+400+150")
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
        
        self.label_resultado_1 = tk.Label(self.theEc3, text="Resultado Cálculo 1: ", **label_config)
        self.label_resultado_1.place(relx=0.03, rely=0.6, height=21, width=250)

        self.label_resultado_2 = tk.Label(self.theEc3, text="Resultado Cálculo 2: ", **label_config)
        self.label_resultado_2.place(relx=0.03, rely=0.65, height=21, width=250)

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
        self.btnCalcular.configure(background="#fefda6", text='''Calcular''')
        self.btnCalcular.configure(font=("Comic Sans MS", 10, "bold"))
        #self.btnCalcular.configure(command = lambda: calcular_d(self.entry_h.get(), self.entry_rec.get(), self.entry_Asøprincipal.get(), self.entryD))
        self.btnCalcular.configure(command=lambda: self.actualizar_resultado_1(self.entry_h.get(), self.entry_rec.get(), self.entry_Asøprincipal.get()))

        
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
        self.btnCal2.configure(background="#fefda6", text='''Calcular''')
        #self.btnCal2.configure(command=lambda: calcular_MuenMn(self.entry_Mu.get(), self.res_Mu))
        self.btnCal2.configure(command=lambda: self.actualizar_resultado_2(self.entry_Mu.get()))


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
        
        #4to
        self.laba = tk.Label(self.theEc3)
        self.laba.place(relx=0.03, rely=0.356, height=21, width=25)
        self.laba.configure(**label_config,text='''a''')  
        
        self.entry_a = tk.Entry(self.theEc3)
        self.entry_a.place(relx=0.07, rely=0.356, height=20, relwidth=0.139)
        self.entry_a.configure(**entry_config)


        self.label_resultado_1 = tk.Label(self.theEc3, text="Resultado Cálculo 1: ", **label_config)
        self.label_resultado_1.place(relx=0.56, rely=0.40, height=21, width=250)
        self.label_resultado_2 = tk.Label(self.theEc3, text="Resultado Cálculo 2: ", **label_config)
        self.label_resultado_2.place(relx=0.56, rely=0.45, height=21, width=250)
                # self.optn12 = tk.Button(self.theEc3)

        self.calculate_button3 = tk.Button(self.theEc3, text='Calcular Acero', command=self.mostrar_calculo_acero, background="#fefda6")
        self.calculate_button3.place(relx=0.675, rely=0.537, height=46, width=237)
        
        self.resultado_acero = tk.Label(self.theEc3, text="Resultado: ", **label_config)
        self.resultado_acero.place(relx=0.027, rely=0.49, height=300, width=400)
    
    def actualizar_resultado_1(self, h, rec, Asøprincipal):
        resultado_1 = calcular_d(h, rec, Asøprincipal, self.entryD)
        if resultado_1 is not None:
            self.label_resultado_1.configure(text=f"Resultado Cálculo 1: {resultado_1}")
        else:
            self.label_resultado_1.configure(text="Error en el cálculo")

    def actualizar_resultado_2(self, Mu):
        resultado_2 = calcular_MuenMn(Mu, self.res_Mu)
        if resultado_2 is not None:
            self.label_resultado_2.configure(text=f"Resultado Cálculo 2: {resultado_2}")
        else:
            self.label_resultado_2.configure(text="Error en el cálculo")



    #calculos_acero(fc, fy, Mu, ø, b, d, Vu, λ):
    def mostrar_calculo_acero(self):
        try:
            # Extrayendo los valores de las entradas
            rec = float(self.entry_rec.get())
            h = float(self.entry_h.get())
            Mu = float(self.entry_Mu3.get())
            fc = float(self.entry_fc.get())
            fy = float(self.entry_fy.get())
            ρ = float(self.entry_P.get())
            Vu = float(self.entry_Vu.get())
            λ = float(self.entry_λ.get())
            ø = float(self.entry_ø.get())
            b = float(self.entry_b3.get())
            d = float(self.entry_d3.get())
            a = float(self.entry_a.get())

            # Cálculo de β1
            if fc < 28:
                β1 = 0.85
            elif fc < 55:
                β1 = 0.65
            else:
                β1 = 0.85 - (0.05 * (fc - 28) / 7)
            
            # Cálculo de la distancia al eje neutro 'c'
            c = a / β1

            # Cálculo de єt
            єt = d - (c * 0.003 / c)

            # Cálculo del área de acero requerida 'As'
            As = ρ * (b * 100) * (d * 100)  # La expresión está en cm

            # Refuerzo mínimo a flexión
            ρmin_a = (0.0018 * 420 / fy) * 0.045
            ρmin_b = 0.0014 * 0.045
            ρmin = max(ρmin_a, ρmin_b)

            # Número de barras
            Nb = ρmin / 1.13

            # Refuerzo corrugado de retracción y temperatura
            ρmintemp_a = (0.0018 * 420 / fy) * 1 * d
            ρmintemp_b = 1.4 * 1 * d
            ρmintemp = max(ρmintemp_a, ρmintemp_b)

            # Momento nominal
            øMn = ø * ρmin * fy * (d - (a / 2)) * (1000 / 1)  # Conversión a Kn.m

            # Verificación del momento
            momento_verificacion = "CUMPLE" if øMn > Mu else "NO CUMPLE"

            # Verificación al cortante
            cortante_verificacion = "cortante no requiere estribos" if 0.5 * ø * 0.17 * λ * (fc**0.5) * 100 * b * d > Vu else "cortante requiere estribos"

            # Resultados para mostrar
            resultado_texto = (
                f"β1: {β1:.2f}\n"
                f"c: {c:.2f}\n"
                f"єt: {єt:.2f}\n"
                f"As: {As:.2f}\n"
                f"ρmin: {ρmin:.4f}\n"
                f"Nb: {Nb:.2f}\n"
                f"ρmintemp: {ρmintemp:.4f}\n"
                f"øMn: {øMn:.2f} Kn.m\n"
                f"Verificación del momento: {momento_verificacion}\n"
                f"Verificación al cortante: {cortante_verificacion}"
            )

            # Mostrar los resultados en la interfaz o en una etiqueta
            self.resultado_acero.configure(text=resultado_texto)

        except ValueError:
            self.resultado_acero.configure(text="Error: Asegúrate de ingresar valores numéricos válidos.")


def main(*args):
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = principal(_top1)
    root.mainloop()

if __name__ == '__main__':
    main()