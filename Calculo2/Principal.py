import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import messagebox
import math

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

button_config = {
    "background": "#fefda6",
    "font": ("Comic Sans MS", 10, "bold"),
}

class Principal:
    def __init__(self, top=None):
        self.top = top
        top.geometry("787x624+400+150")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("Calculadora de Losas")
        top.configure(background="#f9f6f2")

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.496, rely=0.929, height=26, width=47)
        self.Button1.configure(text='EXIT', command=self.top.destroy, **button_config)

        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(relx=0.017, rely=0.022, relheight=0.894, relwidth=0.972)
        
        self.theEc1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.theEc1, padding=3)
        self.TNotebook1.tab(0, text='Ecuacion 1', compound="left", underline='-1')
        self.theEc1.configure(background="#f9f6f2")
        
        self.theEc2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.theEc2, padding=3)
        self.TNotebook1.tab(1, text='Ecuacion 2', compound="left", underline='-1')
        self.theEc2.configure(background="#f9f6f2")
        
        self.theEc3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.theEc3, padding=3)
        self.TNotebook1.tab(2, text='Ecuacion 3', compound="left", underline='-1')
        self.theEc3.configure(background="#f9f6f2")
        
        self.setup_ec1()
        self.setup_ec2()
        self.setup_ec3()

    def setup_ec1(self):
        self.labTitle = tk.Label(self.theEc1)
        self.labTitle.place(relx=0.28, rely=0.037, height=41, width=534)
        self.labTitle.configure(text='DETERMINACIÓN DE LA ALTURA UTIL', **title_config)

        labels = [
            ("H", 0.039, 0.131),
            ("d", 0.629, 0.225),
            ("Rec", 0.039, 0.318),
            ("AsoPrincipal", 0.039, 0.225)
        ]

        for text, x, y in labels:
            label = tk.Label(self.theEc1)
            label.place(relx=x, rely=y, height=21, width=94)
            label.configure(text=text, **label_config)

        self.entry_h = tk.Entry(self.theEc1)
        self.entry_h.place(relx=0.197, rely=0.137, height=20, relwidth=0.189)
        self.entry_h.configure(**entry_config)

        self.entry_Asøprincipal = tk.Entry(self.theEc1)
        self.entry_Asøprincipal.place(relx=0.197, rely=0.223, height=20, relwidth=0.189)
        self.entry_Asøprincipal.configure(**entry_config)

        self.entry_rec = tk.Entry(self.theEc1)
        self.entry_rec.place(relx=0.197, rely=0.324, height=20, relwidth=0.189)
        self.entry_rec.configure(**entry_config)

        self.entryD = tk.Entry(self.theEc1)
        self.entryD.place(relx=0.709, rely=0.223, height=20, relwidth=0.189)
        self.entryD.configure(**entry_config)

        self.btnCalcular = tk.Button(self.theEc1)
        self.btnCalcular.place(relx=0.472, rely=0.449, height=36, width=67)
        self.btnCalcular.configure(text='Calcular', command=self.calcular_d, **button_config)

    def setup_ec2(self):
        self.labTitle2 = tk.Label(self.theEc2)
        self.labTitle2.place(relx=0.207, rely=0.037, height=31, width=524)
        self.labTitle2.configure(text='TRANSFORMACION DEL MOMENTO ULTIMO', **title_config)

        self.labMu = tk.Label(self.theEc2)
        self.labMu.place(relx=0.052, rely=0.206, height=21, width=34)
        self.labMu.configure(text='Mu+', **label_config)

        self.labd = tk.Label(self.theEc2)
        self.labd.place(relx=0.507, rely=0.187, height=21, width=75)
        self.labd.configure(text='MuenMn+', **label_config)
        
        
        self.labd = tk.Label(self.theEc2)
        self.labd.place(relx=0.507, rely=0.287, height=21, width=75)
        self.labd.configure(text='MuenMn-', **label_config)
        
        self.labMuNegativo = tk.Label(self.theEc2)
        self.labMuNegativo.place(relx=0.052, rely=0.406, height=21, width=34)
        self.labMuNegativo.configure(text='Mu-', **label_config)

        self.entry_Mu = tk.Entry(self.theEc2)
        self.entry_Mu.place(relx=0.157, rely=0.206, height=20, relwidth=0.189)
        self.entry_Mu.configure(**entry_config)    
        
        self.entry_MuNegativo = tk.Entry(self.theEc2)
        self.entry_MuNegativo.place(relx=0.157, rely=0.406, height=20, relwidth=0.189)
        self.entry_MuNegativo.configure(**entry_config)    

        self.res_Mu = tk.Entry(self.theEc2)
        self.res_Mu.place(relx=0.642, rely=0.187, height=20, relwidth=0.189)
        self.res_Mu.configure(**entry_config)
        
        self.res_MuNegativo = tk.Entry(self.theEc2)
        self.res_MuNegativo.place(relx=0.642, rely=0.287, height=20, relwidth=0.189)
        self.res_MuNegativo.configure(**entry_config)

        self.btnCal2 = tk.Button(self.theEc2)
        self.btnCal2.place(relx=0.472, rely=0.375, height=36, width=67)
        self.btnCal2.configure(text='Calcular', command=self.calcular_MuenMn, **button_config)

    def setup_ec3(self):
        self.labTitle3 = tk.Label(self.theEc3)
        self.labTitle3.place(relx=0.35, rely=0.056, height=41, width=240)
        self.labTitle3.configure(text='Cálculos y dimensionado de losas unidireccionales', **title_config)

        labels = [
            ('fc', 0.03, 0.206), ('fy', 0.230, 0.206), ('Mu+', 0.455, 0.206), ('Mu-', 0.685, 0.206),
            ('Vu', 0.03, 0.256), ('λ', 0.230, 0.256), ('ø', 0.455, 0.256),
            ('b', 0.03, 0.306), ('h', 0.230, 0.306), ('rec', 0.455, 0.306), ('Asøprincipal', 0.685, 0.306),
        ]

        self.entries = {}
        for text, x, y in labels:
            label = tk.Label(self.theEc3)
            label.place(relx=x, rely=y, height=21, width=75)
            label.configure(text=text, **label_config)

            entry = tk.Entry(self.theEc3)
            entry.place(relx=x+0.07, rely=y, height=20, relwidth=0.139)
            entry.configure(**entry_config)
            self.entries[text] = entry

        # Add factor selector
        self.factor_label = tk.Label(self.theEc3)
        self.factor_label.place(relx=0.03, rely=0.356, height=21, width=75)
        self.factor_label.configure(text='Factor', **label_config)

        self.factor_var = tk.StringVar(value='1.13')
        self.factor_selector = ttk.Combobox(self.theEc3, textvariable=self.factor_var, values=['1.13', '0.785', '1.54', '0.283'])
        self.factor_selector.place(relx=0.1, rely=0.356, height=20, relwidth=0.139)

        self.resultados_listbox = tk.Text(self.theEc3, height=10, width=35)
        self.resultados_listbox.place(relx=0.05, rely=0.45)
        self.resultados_listbox.configure(font=('Helvetica', 10))
        
        self.resultados_listbox2 = tk.Text(self.theEc3, height=10, width=35)
        self.resultados_listbox2.place(relx=0.5, rely=0.45)
        self.resultados_listbox2.configure(font=('Helvetica', 10))

        self.btnCalcularTodo = tk.Button(self.theEc3)
        self.btnCalcularTodo.place(relx=0.35, rely=0.8, height=46, width=237)
        self.btnCalcularTodo.configure(text='Calcular todo', command=self.calcular_todo, **button_config)
    def calcular_d(self):
        try:
            h = float(self.entry_h.get())
            rec = float(self.entry_rec.get())
            Asøprincipal = float(self.entry_Asøprincipal.get())
            d = h - rec - (Asøprincipal / 2)
            self.entryD.delete(0, tk.END)
            self.entryD.insert(0, f'{d:.4f}')
            messagebox.showinfo("Resultado", f"d = {d:.4f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def calcular_MuenMn(self):
        try:
            Mu = float(self.entry_Mu.get())
            MuNegativo = float(self.entry_MuNegativo.get())
            
            MuenMn = Mu / 1000
            self.res_Mu.delete(0, tk.END)
            self.res_Mu.insert(0, f'{MuenMn:.4f}')
            
            if MuNegativo:
                MuenMn2 = MuNegativo / 1000
                self.res_MuNegativo.delete(0, tk.END)
                self.res_MuNegativo.insert(0, f'{MuenMn2:.4f}')
            
            messagebox.showinfo("Resultado", f"Mu en Mn = {MuenMn:.4f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido para Mu.")



    def calcular_todo(self):
        try:
            # Get values from entries
            h = float(self.entries['h'].get())
            b = float(self.entries['b'].get())
            Asøprincipal = float(self.entries['Asøprincipal'].get())
            rec = float(self.entries['rec'].get())
            fc = float(self.entries['fc'].get())
            fy = float(self.entries['fy'].get())
            Mu_pos = float(self.entries['Mu+'].get())
            Mu_neg = float(self.entries['Mu-'].get())
            Vu = float(self.entries['Vu'].get())
            λ = float(self.entries['λ'].get())
            ø = float(self.entries['ø'].get())
            factor = float(self.factor_var.get())

            # Calculate for positive moment
            resultados_pos = self.calcular(h, b, Asøprincipal, rec, fc, fy, Mu_pos, Vu, λ, ø, factor)
            
            # Calculate for negative moment
            resultados_neg = self.calcular(h, b, Asøprincipal, rec, fc, fy, Mu_neg, Vu, λ, ø, factor)

            # Display results
            self.resultados_listbox.delete('1.0', tk.END)
            self.resultados_listbox.insert(tk.END, "Resultados para M+:\n" + resultados_pos)
            
            self.resultados_listbox2.delete('1.0', tk.END)
            self.resultados_listbox2.insert(tk.END, "Resultados para M-:\n" + resultados_neg)

        except ValueError:
            messagebox.showerror("Error", "Por favor, asegúrese de ingresar valores numéricos válidos en todos los campos.")

    def calcular(self, h, b, Asøprincipal, rec, fc, fy, Mu, Vu, λ, ø, factor):
        # Calculations
        d = h - rec - (Asøprincipal / 2)
        MuenMn = Mu / 1000
        ρ = (0.85*fc/fy)*(1-(1-(2*MuenMn/(ø*0.85*fc*b*d**2)))**0.5)
        a = ρ * fy * d / (0.85 * fc)
        
        if fc < 28:
            β1 = 0.85 
        elif fc < 55:
            β1 = 0.65
        else:   
            β1 = 0.85 - (0.05 * (fc - 28) / 7)
        
        c = a / β1
        єt = d - c * 0.003/(c)
        As = (ρ*(b*100)*(d*100))/2   # en cm²
        
        ρmin_a = (0.0018 * 420 / fy) * (0.045 * 10000)
        ρmin_b = 0.0014 * (0.045 * 10000)
        ρmin = max(ρmin_a, ρmin_b)
        
        Nb = math.ceil(ρmin / factor)
        
        
        ρmintemp_a = ((0.0018*420/fy)*1*d)*10000
        ρmintemp_b = (0.0014*1*d)*10000
        ρmintemp = max(ρmintemp_a, ρmintemp_b)
        
        øMn = ø*As*fy*(d-(a/2))*(1000/1)  # en kN·m
        
        cortante = 1/2 * ø * 0.17 * λ * (fc**0.5) * b * d * 1000  # en kN

        # Prepare results
        resultados = f"""
        β1: {β1:.4f}
        c: {c:.4f}
        єt: {єt:.4f}
        ρ: {ρ:.4f}
        ρmin: {ρmin:.4f}
        ρmintemp: {ρmintemp:.4f}
        Altura útil (d) = {d:.4f} m
        Área de acero (As) = {As:.2f} cm²
        Numero de barras (Nb) = {Nb}
        Momento: {'CUMPLE' if øMn >= Mu else 'NO CUMPLE'}
        """

        return resultados

def main():
    root = tk.Tk()
    app = Principal(root)
    root.mainloop()

if __name__ == '__main__':
    main()