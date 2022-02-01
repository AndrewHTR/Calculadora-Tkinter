import tkinter as tk
from botoes import Botoes

class Application(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.botoes = Botoes()

root = tk.Tk()
root.title("Calculadora")
root.geometry("250x300")
root.resizable(0,0)
root.iconbitmap("./src/imagens/icone.ico")
root.configure(background="#262626")
input_text = tk.StringVar()
Application(root)
root.mainloop()