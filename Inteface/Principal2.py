import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

class CalculadoraLosas:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Losas Unidireccionales")
        master.geometry("800x600")
        master.configure(bg="#f0f0f0")

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TNotebook', background="#f0f0f0")
        self.style.configure('TNotebook.Tab', padding=[10, 5], font=('Helvetica', 10))
        self.style.configure('TFrame', background="#ffffff")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Altura Útil")
        self.notebook.add(self.tab2, text="Momento Último")
        self.notebook.add(self.tab3, text="Cálculo de Acero")

        self.setup_tab1()
        self.setup_tab2()
        self.setup_tab3()

    def setup_tab1(self):
        frame = ttk.Frame(self.tab1, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Altura (h):", font=('Helvetica', 10)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_h = ttk.Entry(frame, width=15)
        self.entry_h.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Recubrimiento (rec):", font=('Helvetica', 10)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_rec = ttk.Entry(frame, width=15)
        self.entry_rec.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="As∅principal:", font=('Helvetica', 10)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_As = ttk.Entry(frame, width=15)
        self.entry_As.grid(row=2, column=1, pady=5)

        ttk.Button(frame, text="Calcular d", command=self.calcular_d).grid(row=3, column=0, columnspan=2, pady=10)

        self.label_resultado_d = ttk.Label(frame, text="Resultado:", font=('Helvetica', 10, 'bold'))
        self.label_resultado_d.grid(row=4, column=0, columnspan=2, pady=5)

    def setup_tab2(self):
        frame = ttk.Frame(self.tab2, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Momento último (Mu):", font=('Helvetica', 10)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_Mu = ttk.Entry(frame, width=15)
        self.entry_Mu.grid(row=0, column=1, pady=5)

        ttk.Button(frame, text="Calcular Mu en Mn", command=self.calcular_MuenMn).grid(row=1, column=0, columnspan=2, pady=10)

        self.label_resultado_Mu = ttk.Label(frame, text="Resultado:", font=('Helvetica', 10, 'bold'))
        self.label_resultado_Mu.grid(row=2, column=0, columnspan=2, pady=5)

    def setup_tab3(self):
        frame = ttk.Frame(self.tab3, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        inputs = [
            ("fc:", "entry_fc"), ("fy:", "entry_fy"), ("Mu:", "entry_Mu3"),
            ("Vu:", "entry_Vu"), ("λ:", "entry_lambda"), ("∅:", "entry_phi"),
            ("b:", "entry_b"), ("d:", "entry_d"), ("a:", "entry_a")
        ]

        for i, (label, attr) in enumerate(inputs):
            ttk.Label(frame, text=label, font=('Helvetica', 10)).grid(row=i, column=0, sticky=tk.W, pady=5)
            setattr(self, attr, ttk.Entry(frame, width=15))
            getattr(self, attr).grid(row=i, column=1, pady=5)

        ttk.Button(frame, text="Calcular Acero", command=self.calcular_acero).grid(row=len(inputs), column=0, columnspan=2, pady=10)

        self.text_resultado_acero = tk.Text(frame, height=10, width=50, font=('Helvetica', 10))
        self.text_resultado_acero.grid(row=len(inputs)+1, column=0, columnspan=2, pady=5)

    def calcular_d(self):
        try:
            h = float(self.entry_h.get())
            rec = float(self.entry_rec.get())
            As = float(self.entry_As.get())
            d = h - rec - (As / 2)
            self.label_resultado_d.config(text=f"d = {d:.4f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def calcular_MuenMn(self):
        try:
            Mu = float(self.entry_Mu.get())
            MuenMn = Mu / 1000
            self.label_resultado_Mu.config(text=f"Mu en Mn = {MuenMn:.4f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido para Mu.")

    def calcular_acero(self):
        try:
            fc = float(self.entry_fc.get())
            fy = float(self.entry_fy.get())
            Mu = float(self.entry_Mu3.get())
            Vu = float(self.entry_Vu.get())
            λ = float(self.entry_lambda.get())
            ø = float(self.entry_phi.get())
            b = float(self.entry_b.get())
            d = float(self.entry_d.get())
            a = float(self.entry_a.get())

            # Cálculos (usando las fórmulas que proporcionaste)
            if fc < 28:
                β1 = 0.85
            elif fc < 55:
                β1 = 0.65
            else:
                β1 = 0.85 - (0.05 * (fc - 28) / 7)

            c = a / β1
            єt = d - (c * 0.003 / c)
            ρ = (0.85 * fc / fy) * (1 - (1 - 2 * Mu / (ø * 0.85 * fc * b * d**2))**0.5)
            As = ρ * (b * 100) * (d * 100)
            ρmin_a = (0.0018 * 420 / fy) * 0.045
            ρmin_b = 0.0014 * 0.045
            ρmin = max(ρmin_a, ρmin_b)
            Nb = ρmin / 1.13
            ρmintemp_a = (0.0018 * 420 / fy) * 1 * d
            ρmintemp_b = 1.4 * 1 * d
            ρmintemp = max(ρmintemp_a, ρmintemp_b)
            øMn = ø * ρmin * fy * (d - (a / 2)) * (1000 / 1)

            momento_verificacion = "CUMPLE" if øMn > Mu else "NO CUMPLE"
            cortante_verificacion = "No requiere estribos" if 0.5 * ø * 0.17 * λ * (fc**0.5) * 100 * b * d > Vu else "Requiere estribos"

            resultado = f"""
            β1: {β1:.4f}
            c: {c:.4f}
            єt: {єt:.4f}
            ρ: {ρ:.4f}
            As: {As:.4f} cm²
            ρmin: {ρmin:.4f}
            Numero de barras : {Nb:.2f}
            ρmintemp: {ρmintemp:.4f}
            øMn: {øMn:.2f} kN·m
            Verificación del momento: {momento_verificacion}
            Verificación al cortante: {cortante_verificacion}
            """

            self.text_resultado_acero.delete('1.0', tk.END)
            self.text_resultado_acero.insert(tk.END, resultado)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos en todos los campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraLosas(root)
    root.mainloop()