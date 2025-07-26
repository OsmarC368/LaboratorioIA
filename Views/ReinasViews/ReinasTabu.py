import tkinter as tk
from tkinter import END, ttk
from tkinter import messagebox
from Models.Reinas import Tabu_4Reinas

class ReinasTabuView:
    def __init__(self, mainWindow):
        self.result = None
        self.mainWindow = mainWindow
        self.window = tk.Tk()
        self.window.title("Reinas Tabu")
        self.window.geometry("520x720")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Reinas Tabu-/", font=("Arial", 18, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.pack(pady=9)
        #Labels Entrys
        self.labelInitSol = tk.Label(self.window, text="Introduzca una Solución Incial:", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelInitSol.pack(pady=8)
        self.entryInitSol = tk.Entry(self.window, width=20)
        self.entryInitSol.pack(pady=8)

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
        

        #scrollbar
        self.scrollbar = ttk.Scrollbar(self.window, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        #Result
        self.labelResult = tk.Label(self.window, text="Resultado", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelResult.pack(pady=5)
        self.textResult = tk.Text(self.window, height=6, width=30)
        self.textResult.pack(pady=8)
        self.labelTabuList = tk.Label(self.window, text="TabuList", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTabuList.pack(pady=5)
        self.textTabu = tk.Text(self.window, height=15, width=32)
        self.textTabu.pack(pady=8)
        self.textTabu.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.textTabu.yview)


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
            initSol = self.entryInitSol.get().split("-")
            initSol = list(map(lambda x: int(x), initSol))
            self.result, tabuList = Tabu_4Reinas.solve(initSol)
            self.textResult.delete('1.0', END)
            self.textTabu.delete('1.0', END)
            self.textResult.insert('end', f"Resultado!")
            self.textResult.insert('end', f"\nPosiciones: {self.result[0]}")
            self.textResult.insert('end', f"\nNumero de Colisiones: {self.result[1]}")

            for x in tabuList:
                self.textTabu.insert('end', f"\n{x}")
        except:
            self.showMessage("ERROR", "Posible Error con la Entrada de Datos")

    def showGraph(self):
        try:
            if self.result == None:
                self.showMessage("ERROR", "Realice un Calculo Primero!")
            else:
                Tabu_4Reinas.graph(self.result[0], self.result[1])
        except:
                self.showMessage("ERROR", "FATAL ERROR")
            