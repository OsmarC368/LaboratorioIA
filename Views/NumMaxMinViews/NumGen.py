import tkinter as tk
from tkinter import END, ttk
from tkinter import messagebox
from Models.MaxNum import AlgoritmoGenetico

class MaxMinGenetico:
    def __init__(self, mainWindow):
        self.rang = None
        self.max = None
        self.mainWindow = mainWindow
        self.window = tk.Tk()
        self.window.title("Maximo Minimo Genetico")
        self.window.geometry("740x850")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Maximo Minimo Genetico-/", font=("Arial", 18, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.pack(pady=9)
        #Labels Entrys
        self.labelRang = tk.Label(self.window, text="Introduzca el Rango", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelRang.pack(pady=8)
        self.entryRang = tk.Entry(self.window, width=20)
        self.entryRang.pack(pady=8)
        #
        self.labelNumInd = tk.Label(self.window, text="Introduzca el Numero de Individuos por Poblacion", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelNumInd.pack(pady=8)
        self.entryNumInd = tk.Entry(self.window, width=20)
        self.entryNumInd.pack(pady=8)
        #
        self.labelNumGen = tk.Label(self.window, text="Introduzca el Numero de Generaciones", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelNumGen.pack(pady=8)
        self.entryNumGen = tk.Entry(self.window, width=20)
        self.entryNumGen.pack(pady=8)

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
        
        #
        #Result
        self.labelResult = tk.Label(self.window, text="Resultado", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelResult.pack(pady=5)
        self.textResult = tk.Text(self.window, height=6, width=30)
        self.textResult.pack(pady=8)
        #
        self.labelTabla = tk.Label(self.window, text="Ultima Generación", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTabla.pack(pady=5)
        self.tabla = ttk.Treeview(self.window, columns=("col1","col2", "col3", "col4"), height=10)
        self.tabla.column("#0", width=120)
        self.tabla.column("col1", width=120, anchor=tk.CENTER)
        self.tabla.column("col2", width=120, anchor=tk.CENTER)
        self.tabla.column("col3", width=120, anchor=tk.CENTER)
        self.tabla.column("col4", width=120, anchor=tk.CENTER)
        self.tabla.heading("#0", text="N", anchor=tk.CENTER)
        self.tabla.heading("col1", text="Población", anchor=tk.CENTER)
        self.tabla.heading("col2", text="X", anchor=tk.CENTER)
        self.tabla.heading("col3", text="Fitness", anchor=tk.CENTER)
        self.tabla.heading("col4", text="Porcentaje", anchor=tk.CENTER)
        self.tabla.pack()


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
            self.textResult.delete('1.0', END)
            indNum = int(self.entryNumInd.get())
            self.rang = self.entryRang.get().split("/")
            self.rang = list(map(lambda x: int(x), self.rang))
            genNum = int(self.entryNumGen.get())
            self.max, table = AlgoritmoGenetico.solve(indNum, genNum, self.rang)    

            self.textResult.insert('end', f"Resultado Encontrado!")
            self.textResult.insert('end', f"\nMaximo Local")
            self.textResult.insert('end', f"\nX: {self.max[0]}  Y: {self.max[1]}")


            for i in self.tabla.get_children():
                self.tabla.delete(i)

            for x in table:
                self.tabla.insert("", tk.END, text=f"{x[0]}", values=(x[1], x[2], x[3], x[4]))

        except:
            self.showMessage("ERROR", "Posible Error con la Entrada de Datos")

    def showGraph(self):
        try:
            if self.max == None:
                self.showMessage("ERROR", "Realice un Calculo Primero!")
            else:
                AlgoritmoGenetico.graph(self.rang, self.max[0])
        except:
                self.showMessage("ERROR", "FATAL ERROR")