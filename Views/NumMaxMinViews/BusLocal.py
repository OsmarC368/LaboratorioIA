import tkinter as tk
from tkinter import END, ttk
from tkinter import messagebox
from Models.MaxNum import MaximoLocal

class BusLocalView:
    def __init__(self, mainWindow):
        self.min = None
        self.rang = None
        self.mainWindow = mainWindow
        self.window = tk.Tk()
        self.window.title("Busqueda Local")
        self.window.geometry("520x680")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Busqueda Local-/", font=("Arial", 18, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.pack(pady=9)
        #Labels Entrys
        self.labelRange = tk.Label(self.window, text="Introduzca el Rango para la Función", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelRange.pack(pady=8)
        self.entryRange = tk.Entry(self.window, width=20)
        self.entryRange.pack(pady=8)
        self.labelIter = tk.Label(self.window, text="Introduzca el Número de Iteraciones", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelIter.pack(pady=8)
        self.entryIter = tk.Entry(self.window, width=20)
        self.entryIter.pack(pady=8)

        self.buttonCalc = tk.Button(
            self.window, 
            command=lambda: self.calc(), 
            text="Calcular",
            background="#243d55",
            activebackground="#61b9eb",
            foreground="#aaaaaa",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
            ).pack(pady=5)
        
        #Result
        self.entryResult = tk.Entry(self.window, width=40)
        self.entryResult.pack(pady=8)
        self.labelResult = tk.Label(self.window, text="Resultado", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelResult.pack(pady=5)
        self.textResult = tk.Text(self.window, height=9, width=30)
        self.textResult.pack(pady=8)

        self.buttonGraph = tk.Button(
            self.window, 
            command=lambda: self.showGraph(), 
            text="Grafico",
            background="#243d55",
            activebackground="#61b9eb",
            foreground="#aaaaaa",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
            ).pack(pady=5)
        
        self.buttonMenu = tk.Button(
            self.window, 
            command= lambda : self.close(), 
            text="Menu Principal",
            background="#243d55",
            activebackground="#61b9eb",
            foreground="#aaaaaa",
            activeforeground="WHITE",
            border=3,
            font=("Arial", 10, "bold")
            ).pack(pady=5)

        
    def show(self):
        self.window.mainloop()

    def close(self):
        self.mainWindow.show()
        self.window.destroy()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message)

    def calc(self):
        try:
           self.rang = self.entryRange.get().split("/")
           self.rang = list(map(lambda x: int(x), self.rang))
           iteraciones = int(self.entryIter.get())
           self.min, tabla = MaximoLocal.solve(lambda x: (x**4) - (4*(x**3)) + (7*x), self.rang, iteraciones)
           self.textResult.delete('1.0', END)
           for x in tabla:
               self.textResult.insert('end', f"\n{x}")
           self.entryResult.delete(0, tk.END)
           self.entryResult.insert(0, f"El Minimo Y es {self.min[1]} dado por el X: {self.min[0]}")
        except:
            self.showMessage("ERROR", "Posible Error con la Entrada de Datos")


    def showGraph(self):
        try:
            if self.min == None:
                self.showMessage("ERROR", "Realice un Calculo Primero!")
            else:
                MaximoLocal.graph(self.rang, self.min, lambda x: (x**4) - (4*(x**3)) + (7*x))
        except:
             self.showMessage("ERROR", "FATAL ERROR")