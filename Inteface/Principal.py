import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

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
        top.geometry("787x624+548+193")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#f9f6f2")
        self.top = top

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

        self.btnCalcular = tk.Button(self.theEc1)
        self.btnCalcular.place(relx=0.472, rely=0.449, height=36, width=67)
        self.btnCalcular.configure(background="#fefda6",text='''Calcular''')
        self.btnCalcular.configure(font=("Comic Sans MS", 10, "bold"))

        self.entryRec = tk.Entry(self.theEc1)
        self.entryRec.place(relx=0.197, rely=0.324, height=20, relwidth=0.189)
        self.entryRec.configure(**entry_config)
        self.entryD = tk.Entry(self.theEc1)
        self.entryD.place(relx=0.709, rely=0.223, height=20, relwidth=0.189)
        self.entryD.configure(**entry_config)

        self.Label1 = tk.Label(self.theEc1)
        self.Label1.place(relx=0.039, rely=0.131, height=21, width=34)
        self.Label1.configure(**label_config,text='''H''')
        self.labD = tk.Label(self.theEc1)
        self.labD.place(relx=0.629, rely=0.225, height=21, width=34)
        self.labD.configure(**label_config,text='''d''')
        self.labRec = tk.Label(self.theEc1)
        self.labRec.place(relx=0.039, rely=0.318, height=21, width=34)
        self.labRec.configure(**label_config,text='''Rec''')

        self.entryH = tk.Entry(self.theEc1)
        self.entryH.place(relx=0.197, rely=0.137, height=20, relwidth=0.189)
        self.entryH.configure(**entry_config)
        self.entryAs = tk.Entry(self.theEc1)
        self.entryAs.place(relx=0.197, rely=0.223, height=20, relwidth=0.189)
        self.entryAs.configure(**entry_config)

        self.labAso = tk.Label(self.theEc1)
        self.labAso.place(relx=0.039, rely=0.225, height=21, width=94)
        self.labAso.configure(**label_config,text='''AsoPrincipal''')
        self.labTitle = tk.Label(self.theEc1)
        self.labTitle.place(relx=0.38, rely=0.037, height=41, width=234)
        self.labTitle.configure(**title_config,text='''Titulo de la ecuacion 1''')

        self.Entry2 = tk.Entry(self.theEc2)
        self.Entry2.place(relx=0.642, rely=0.187, height=20, relwidth=0.189)
        self.Entry2.configure(**entry_config)
        self.Entry1 = tk.Entry(self.theEc2)
        self.Entry1.place(relx=0.157, rely=0.206, height=20, relwidth=0.189)
        self.Entry1.configure(**entry_config)

        self.labMu = tk.Label(self.theEc2)
        self.labMu.place(relx=0.052, rely=0.206, height=21, width=34)
        self.labMu.configure(**label_config,text='''Mu''')
        self.labd = tk.Label(self.theEc2)
        self.labd.place(relx=0.577, rely=0.187, height=21, width=35)
        self.labd.configure(**label_config,text='''d''')

        self.btnCal2 = tk.Button(self.theEc2)
        self.btnCal2.place(relx=0.472, rely=0.375, height=36, width=67)
        self.btnCal2.configure(background="#fefda6")
        self.btnCal2.configure(text='''Calcular''')

        self.labTitle2 = tk.Label(self.theEc2)
        self.labTitle2.place(relx=0.367, rely=0.037, height=31, width=224)
        self.labTitle2.configure(**title_config,text='''Titulo de la ecuacion 2''')

        self.labTitle3 = tk.Label(self.theEc3)
        self.labTitle3.place(relx=0.38, rely=0.056, height=41, width=255)
        self.labTitle3.configure(**title_config,text='''Seleccione la ecuacion''')

        self.optn1 = tk.Button(self.theEc3)
        self.optn1.place(relx=0.354, rely=0.206, height=46, width=237)
        self.optn1.configure(background="#fffee1")
        self.optn1.configure(foreground="#000000")
        self.optn1.configure(text='''Ecuacion 1''')
        #Pendiente a analizar
        self.optn2 = tk.Button(self.theEc3)
        self.optn2.place(relx=0.354, rely=0.337, height=46, width=237)
        self.optn2.configure(activebackground="#d9d9d9")
        self.optn2.configure(activeforeground="black")
        self.optn2.configure(background="#fffee1")
        self.optn2.configure(disabledforeground="#a3a3a3")
        self.optn2.configure(font="-family {Segoe UI} -size 9")
        self.optn2.configure(text='''Ecuacion 2''')

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