import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .BusLocal import BusLocalView
from .NumGen import MaxMinGenetico

class NumMaxMinMenuView:
    def __init__(self, mWindow):
        self.mainWindow = mWindow
        self.window = tk.Tk()
        self.window.title("Minimos Maximos Menu")
        self.window.geometry("550x250")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Minimos Maximos Menu-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.pack(pady=8)

        #Create Options
        self.createOptions()
        self.exitButton = tk.Button(
            self.window,
                text="Salir",
                width=25,
                height=2,
                command= lambda: self.close(),
                background="#243d55",
                activebackground="#61b9eb",
                foreground="#aaaaaa",
                activeforeground="WHITE",
                border=3,
                font=("Arial", 10, "bold")
        ).pack(pady=6)


    def initiate(self):
        self.window.mainloop()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message,)

    def close(self):
        self.mainWindow.show()
        self.window.destroy()

    def createOptions(self):
        options =  ["Busqueda Local", "Genetico"]
        for key in options:
            tk.Button(
                self.window,
                text=f"{key}",
                width=25,
                height=2,
                command= lambda k=key: option(self, k),
                background="#243d55",
                activebackground="#61b9eb",
                foreground="#aaaaaa",
                activeforeground="WHITE",
                border=3,
                font=("Arial", 10, "bold")
            ).pack(pady=6)
    
    def hide(self):
        self.window.withdraw()


def option(self, k):
    if k == "Busqueda Local":
        showLocal(self)
    elif k == "Genetico":
        showGen(self)


def showLocal(self):
    self.window.destroy()
    BusLocalView(self.mainWindow).show()
    

def showGen(self):
    self.window.destroy()
    MaxMinGenetico(self.mainWindow).show()
