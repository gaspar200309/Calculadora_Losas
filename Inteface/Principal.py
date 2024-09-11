import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)


_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

_style_code_ran = 0


class principal:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("787x624+548+193")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.496, rely=0.929, height=26, width=47)
        self.Button1.configure(background="#fefda6")
        self.Button1.configure(font="-family {Segoe UI} -size 9")
        self.Button1.configure(text='''EXIT''')

        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(relx=0.017, rely=0.022, relheight=0.894
                , relwidth=0.972)
        self.theEc1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.theEc1, padding=3)
        self.TNotebook1.tab(0, text='''Ecuacion 1''', compound="left"
                ,underline='''-1''', )
        self.theEc1.configure(background="#d9d9d9")
        self.theEc1.configure(highlightbackground="#d9d9d9")
        self.theEc1.configure(highlightcolor="#000000")
        self.theEc2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.theEc2, padding=3)
        self.TNotebook1.tab(1, text='''Ecuacion 2''', compound="left"
                ,underline='''-1''', )
        self.theEc2.configure(background="#d9d9d9")
        self.theEc2.configure(highlightbackground="#d9d9d9")
        self.theEc2.configure(highlightcolor="#000000")
        self.theEc3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.theEc3, padding=3)
        self.TNotebook1.tab(2, text='''Ecuacion 3''', compound="left"
                ,underline='''-1''', )
        self.theEc3.configure(background="#d9d9d9")
        self.theEc3.configure(highlightbackground="#d9d9d9")
        self.theEc3.configure(highlightcolor="#000000")

        self.btnCalcular = tk.Button(self.theEc1)
        self.btnCalcular.place(relx=0.472, rely=0.449, height=36, width=67)
        self.btnCalcular.configure(background="#fefda6")
        self.btnCalcular.configure(text='''Calcular''')

        self.entryRec = tk.Entry(self.theEc1)
        self.entryRec.place(relx=0.197, rely=0.324, height=20, relwidth=0.189)
        self.entryRec.configure(background="#fffee1")
        self.entryRec.configure(font="-family {Courier New} -size 10")
        self.entryRec.configure(insertbackground="black")

        self.entryD = tk.Entry(self.theEc1)
        self.entryD.place(relx=0.709, rely=0.223, height=20, relwidth=0.189)
        self.entryD.configure(background="#fffee1")
        self.entryD.configure(font="-family {Courier New} -size 10")
        self.entryD.configure(insertbackground="#000000")

        self.Label1 = tk.Label(self.theEc1)
        self.Label1.place(relx=0.039, rely=0.131, height=21, width=34)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(font="-family {Segoe UI} -size 9")
        self.Label1.configure(text='''H''')

        self.labD = tk.Label(self.theEc1)
        self.labD.place(relx=0.629, rely=0.225, height=21, width=34)
        self.labD.configure(anchor='w')
        self.labD.configure(background="#d9d9d9")
        self.labD.configure(compound='left')
        self.labD.configure(text='''d''')

        self.labRec = tk.Label(self.theEc1)
        self.labRec.place(relx=0.039, rely=0.318, height=21, width=34)
        self.labRec.configure(anchor='w')
        self.labRec.configure(background="#d9d9d9")
        self.labRec.configure(compound='left')
        self.labRec.configure(text='''Rec''')

        self.entryH = tk.Entry(self.theEc1)
        self.entryH.place(relx=0.197, rely=0.137, height=20, relwidth=0.189)
        self.entryH.configure(background="#fffee1")
        self.entryH.configure(font="-family {Courier New} -size 10")
        self.entryH.configure(insertbackground="#000000")

        self.entryAs = tk.Entry(self.theEc1)
        self.entryAs.place(relx=0.197, rely=0.223, height=20, relwidth=0.189)
        self.entryAs.configure(background="#fffee1")
        self.entryAs.configure(font="-family {Courier New} -size 10")
        self.entryAs.configure(insertbackground="#000000")

        self.labAso = tk.Label(self.theEc1)
        self.labAso.place(relx=0.039, rely=0.225, height=21, width=74)
        self.labAso.configure(anchor='w')
        self.labAso.configure(compound='left')
        self.labAso.configure(background="#d9d9d9")
        self.labAso.configure(font="-family {Segoe UI} -size 9")
        self.labAso.configure(text='''AsoPrincipal''')

        self.labTitle = tk.Label(self.theEc1)
        self.labTitle.place(relx=0.38, rely=0.037, height=41, width=234)
        self.labTitle.configure(anchor='w')
        self.labTitle.configure(background="#d9d9d9")
        self.labTitle.configure(compound='left')
        self.labTitle.configure(font="-family {Segoe UI} -size 16")
        self.labTitle.configure(text='''Titulo de la ecuacion 1''')

        self.Entry2 = tk.Entry(self.theEc2)
        self.Entry2.place(relx=0.642, rely=0.187, height=20, relwidth=0.189)
        self.Entry2.configure(background="#fffee1")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(insertbackground="#000000")

        self.Entry1 = tk.Entry(self.theEc2)
        self.Entry1.place(relx=0.157, rely=0.206, height=20, relwidth=0.189)
        self.Entry1.configure(background="#fffee1")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(insertbackground="#000000")

        self.labMu = tk.Label(self.theEc2)
        self.labMu.place(relx=0.052, rely=0.206, height=21, width=34)
        self.labMu.configure(anchor='w')
        self.labMu.configure(background="#d9d9d9")
        self.labMu.configure(compound='left')
        self.labMu.configure(text='''Mu''')

        self.labd = tk.Label(self.theEc2)
        self.labd.place(relx=0.577, rely=0.187, height=21, width=35)
        self.labd.configure(anchor='w')
        self.labd.configure(background="#d9d9d9")
        self.labd.configure(text='''d''')

        self.btnCal2 = tk.Button(self.theEc2)
        self.btnCal2.place(relx=0.472, rely=0.375, height=36, width=67)
        self.btnCal2.configure(background="#fefda6")
        self.btnCal2.configure(text='''Calcular''')

        self.labTitle2 = tk.Label(self.theEc2)
        self.labTitle2.place(relx=0.367, rely=0.037, height=31, width=224)
        self.labTitle2.configure(anchor='w')
        self.labTitle2.configure(background="#d9d9d9")
        self.labTitle2.configure(compound='left')
        self.labTitle2.configure(font="-family {Segoe UI} -size 14")
        self.labTitle2.configure(text='''Titulo de la ecuacion 2''')

        self.labTitle3 = tk.Label(self.theEc3)
        self.labTitle3.place(relx=0.38, rely=0.056, height=41, width=205)
        self.labTitle3.configure(anchor='w')
        self.labTitle3.configure(background="#d9d9d9")
        self.labTitle3.configure(compound='left')
        self.labTitle3.configure(font="-family {Segoe UI} -size 14")
        self.labTitle3.configure(foreground="#000000")
        self.labTitle3.configure(text='''Seleccione la ecuacion''')

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
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Crea un widget toplevel.
    global _top1, _w1
    _top1 = root
    _w1 = principal(_top1)  # Llama a la función principal para configurar la ventana
    root.mainloop()

if __name__ == '__main__':
    main()