import tkinter as tk
from Interface import GerenciadorContasApp

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorContasApp(root)
    app.criar_interface_operacoes()
    root.mainloop()
