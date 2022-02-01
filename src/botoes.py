import tkinter as tk

class Botoes(tk.Frame):
    def __init__(self):
        def adicionarnum(num):
            global expression
            expression = expression + str(num)
            self.input_text.set(expression)

        def limpar():
            global expression

            expression = ""

            self.input_text.set("")

        def resultado():
            global expression 

            resultado = str(eval(expression))
            self.input_text.set(resultado)
            expression = resultado
            
        #! Entry Box principal
        self.input_text = tk.StringVar()
        self.entrada = tk.Entry(textvariable= self.input_text)
        self.entrada.config(font=(36), background="#3c3c3c", foreground="White", border= False)
        self.entrada.place(y=1,height=30, width=251)

        #! Simbolos:
        self.ce = tk.Button(text="CE", command= lambda: limpar())
        self.ce.config(background="#bebebe", border= False, cursor= "hand2", font=(20))
        self.ce.place(x=205,y=30, height=40, width=45)

        self.igual = tk.Button(text="=", command=lambda:resultado())
        self.igual.config(background="#bebebe", border= False, cursor= "hand2", font=(26))
        self.igual.place(x=205, y = 235, height=65, width=45)

        self.mais = tk.Button(text="+", command=lambda:adicionarnum("+"))
        self.mais.config(background="#bebebe", border= False, cursor= "hand2", font=(20))
        self.mais.place(x=205,y=194, height=40, width=45)

        self.menos = tk.Button(text="-", command=lambda:adicionarnum("-"))
        self.menos.config(background="#bebebe", border= False, cursor= "hand2", font=(20))
        self.menos.place(x=205,y=153, height=40, width=45)

        self.vezes = tk.Button(text="*", command=lambda:adicionarnum("*"))
        self.vezes.config(background="#bebebe", border= False, cursor= "hand2", font=(20))
        self.vezes.place(x=205,y=112, height=40, width=45)

        self.divisao = tk.Button(text="/", command=lambda:adicionarnum("/"))
        self.divisao.config(background="#bebebe", border= False, cursor= "hand2", font=(20))
        self.divisao.place(x=205,y=71, height=40, width=45)

        #! Numeros:
        self.zero = tk.Button(text="0", command= lambda: adicionarnum('0'))      
        self.zero.config(border= False, background="#808080", cursor= "hand2", font=(20))
        self.zero.place(x=67, y=237, height=68, width=68)

        self.um = tk.Button(text="1", command= lambda: adicionarnum('1'))      
        self.um.config(border= False, background="#808080", cursor= "hand2", font=(20))
        self.um.place(x=0.5, y=168, height=68, width=65)

        self.dois = tk.Button(text="2", command= lambda: adicionarnum('2'))      
        self.dois.config(border= False, background="#808080", cursor= "hand2", font=(20))
        self.dois.place(x=67, y=168, height=68, width=68)

        self.tres = tk.Button(text="3", command= lambda: adicionarnum('3'))      
        self.tres.config(border= False, background="#808080", cursor= "hand2", font=(20))
        self.tres.place(x=136, y=168, height=68, width=68)

        self.quatro = tk.Button(text="4", command= lambda: adicionarnum('4'))      
        self.quatro.config(border= False, background="#808080", cursor= "hand2", font=(20))
        self.quatro.place(x=0.5, y=99, height=68, width=65)

        self.cinco = tk.Button(text="5", command= lambda: adicionarnum('5'))      
        self.cinco.config(border= False, background="#808080", cursor= "hand2", font=(20))
        self.cinco.place(x=67, y=99, height=68, width=68)

        self.seis = tk.Button(text="6", command= lambda: adicionarnum('6'))      
        self.seis.config(border= False, background="#808080", cursor= "hand2", font=(20))
        self.seis.place(x=136, y=99, height=68, width=68)

        self.sete = tk.Button(text="7", command= lambda: adicionarnum('7'))      
        self.sete.config(border= False, background="#808080", cursor= "hand2", font=(20))
        self.sete.place(x=0.5, y=30, height=68, width=65)

        self.oito = tk.Button(text="8", command= lambda: adicionarnum('8'))      
        self.oito.config(border= False, background="#808080", cursor= "hand2", font=(20))
        self.oito.place(x=67, y=30, height=68, width=68)

        self.nove = tk.Button(text="9", command= lambda: adicionarnum('9'))      
        self.nove.config(border= False, background="#808080", cursor= "hand2", font=(20))
        self.nove.place(x=136, y=30, height=68, width=68)

        self.ponto = tk.Button(text=".", command= lambda: adicionarnum("."))
        self.ponto.config(border= False, background="#808080", cursor= "hand2", font=(20))
        self.ponto.place(x=136, y=237, height=68, width=68)

        self.expression = ""
        self.input_text.set("")

        limpar()

