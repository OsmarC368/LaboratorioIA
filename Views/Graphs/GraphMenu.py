import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .GraphTabu import GraphTabuView
from .GraphTemperature import GraphTempView

class GraphMenu:
    def __init__(self, mWindow):
        self.mainWindow = mWindow
        self.window = tk.Tk()
        self.window.title("Graph Menu")
        self.window.geometry("550x250")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Graph Menu-/", font=("Arial", 14, "bold"), foreground="WHITE", background="#2b2f36")
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
        options =  ["Tabu", "Temperatura"]
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
    if k == "Tabu":
        showTabu(self)
    elif k == "Temperatura":
        showTemp(self)


def showTabu(self):
    self.window.destroy()
    GraphTabuView(self.mainWindow).show()

def showTemp(self):
    self.window.destroy()
    GraphTempView(self.mainWindow).show()