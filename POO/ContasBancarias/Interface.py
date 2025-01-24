import tkinter as tk
from tkinter import messagebox
from Classes import ContaPoupanca,ContaBancaria,ContaCorrente

class GerenciadorContasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Contas Bancárias")
        
        # Lista para armazenar contas
        self.contas = {}

        # Interface inicial
        self.criar_interface_inicial()

    def criar_interface_inicial(self):
        # Labels e inputs
        tk.Label(self.root, text="Número da Conta:").grid(row=0, column=0)
        self.input_numero = tk.Entry(self.root)
        self.input_numero.grid(row=0, column=1)

        tk.Label(self.root, text="Titular:").grid(row=1, column=0)
        self.input_titular = tk.Entry(self.root)
        self.input_titular.grid(row=1, column=1)

        tk.Label(self.root, text="Tipo de Conta:").grid(row=2, column=0)
        self.tipo_conta = tk.StringVar(value="ContaCorrente")
        tk.OptionMenu(self.root, self.tipo_conta, "ContaCorrente", "ContaPoupanca").grid(row=2, column=1)

        # Botão para criar conta
        tk.Button(self.root, text="Criar Conta", command=self.criar_conta).grid(row=3, columnspan=2)

    def criar_conta(self):
        numero = self.input_numero.get()
        titular = self.input_titular.get()
        tipo = self.tipo_conta.get()

        if numero and titular:
            if tipo == "ContaCorrente":
                self.contas[numero] = ContaCorrente(numero, titular)
            elif tipo == "ContaPoupanca":
                self.contas[numero] = ContaPoupanca(numero, titular)
            messagebox.showinfo("Sucesso", f"Conta {tipo} criada para {titular}.")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos.")

    def criar_interface_operacoes(self):
        tk.Label(self.root, text="Número da Conta:").grid(row=4, column=0)
        self.input_numero_operacao = tk.Entry(self.root)
        self.input_numero_operacao.grid(row=4, column=1)

        tk.Label(self.root, text="Valor:").grid(row=5, column=0)
        self.input_valor = tk.Entry(self.root)
        self.input_valor.grid(row=5, column=1)

        tk.Button(self.root, text="Depositar", command=self.depositar).grid(row=6, column=0)
        tk.Button(self.root, text="Sacar", command=self.sacar).grid(row=6, column=1)
        tk.Button(self.root, text="Consultar Saldo", command=self.consultar_saldo).grid(row=7, columnspan=2)

    def depositar(self):
        numero = self.input_numero_operacao.get()
        valor = float(self.input_valor.get())

        if numero in self.contas:
            self.contas[numero].depositar(valor)
            messagebox.showinfo("Sucesso", f"Depósito de R${valor:.2f} realizado.")
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")

    def sacar(self):
        numero = self.input_numero_operacao.get()
        valor = float(self.input_valor.get())

        if numero in self.contas:
            self.contas[numero].sacar(valor)
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")

    def consultar_saldo(self):
        numero = self.input_numero_operacao.get()

        if numero in self.contas:
            saldo = self.contas[numero].consultar_saldo()
            messagebox.showinfo("Saldo", f"Saldo atual: R${saldo:.2f}")
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")

#lembrando alguns conceitos do tkinter:
# tk.Tk(): cria a janela principal e é a raiz de todos os elementos do aplicativo. (root = tk.Tk())
# root.title(titulo): define o titulo da pagina principal
# tk.Label(): cria um rotulo de texto(tk.Label(self.root, text="Número da Conta:").grid(row=0, column=0))master: Janela ou frame em que o rótulo será colocado.
    # Parametros principais: 
    # text: Texto a ser exibido.
    # font: Define a fonte (tamanho, estilo).
    # fg (opcional): Cor do texto.
    # bg (opcional): Cor de fundo.
# tk.Entry(): cria um campo de entrada de texto(self.input_numero = tk.Entry(self.root))
     # Parâmetros principais:
        # master: Janela ou frame onde o campo será colocado.
        # show: (opcional) Substitui os caracteres digitados por algo como * (útil para senhas).
# tk.Button(): Cria um botão(tk.Button(self.root, text="Criar Conta", command=self.criar_conta).grid(row=3, columnspan=2))
    # Parâmetros principais:
        # master: Janela ou frame onde o botão será colocado.
        # text: Texto exibido no botão.
        # command: Função a ser chamada quando o botão é clicado.
# tk.OptionMenu():  Cria um menu suspenso para selecionar uma opção.
    # (Exemplo
    # self.tipo_conta = tk.StringVar(value="ContaCorrente")
    # tk.OptionMenu(self.root, self.tipo_conta, "ContaCorrente", "ContaPoupanca").grid(row=2, column=1)
    # )
    # Parametros: 
        # master: Janela ou frame onde o menu será colocado.
        # variable: Variável que armazena a opção selecionada.
        # value1, value2, ...: Opções disponíveis no menu.
# entre varios outros
# 
