import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ReinasViews.ReinasMenu import ReinasMenuView
from NumMaxMinViews.NumMaxMinMenu import NumMaxMinMenuView

class MenuView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Menu Principal")
        self.window.geometry("600x320")
        self.window.resizable(0,0)
        self.window.configure(background="#2b2f36")
        #labels
        self.labelTitle = tk.Label(self.window, text="\-Menu Principal-/", font=("Arial", 16, "bold"), foreground="WHITE", background="#2b2f36")
        self.labelTitle.pack(pady=12)

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

    def hide(self):
        self.window.withdraw()

    def show(self):
        self.window.deiconify()

    def initiate(self):
        self.window.mainloop()

    def showMessage(self, title, message):
        messagebox.showinfo(title, message,)

    def close(self):
        self.window.destroy()

    def createOptions(self):
        options = [ "Reinas", "Viajero", "FuncionMinMax" ]
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
    if k == "Reinas":
        showReinas(self)
    elif k == "Viajero":
        showReinas(self)
    elif k == "FuncionMinMax":
        showMaxMin(self)

def showReinas(self):
    self.hide()
    ReinasMenuView(self).initiate()

def showViajero(self):
    self.hide()
    #view = ReinasMenuView(self).initiate()

def showMaxMin(self):
    self.hide()
    NumMaxMinMenuView(self).initiate()


if __name__ == "__main__":   
    menu = MenuView()
    menu.initiate()