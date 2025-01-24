class ContaBancaria:
    def __init__(self,numero,titular,saldo = 0.0):
        self.numero = numero
        self.titular = titular
        self.__saldo = saldo

    def depositar(self,valor):
        if valor>=0:
            self.__saldo += valor
            print(f"Valor depositado {valor:.2f}")
        else: print("Valor invalido")
        
    def sacar(self,valor):
        if self.__saldo < valor:
            print(f"Saldo insuficiente, valor disponivel para saque: {self.__saldo:.2f}")
        else:
            self.__saldo -= valor
            print("Saque realizado")
    
    def consultar_saldo(self):
        return self.__saldo
    
class ContaCorrente(ContaBancaria):
    def __init__(self, numero, titular, saldo=0.0, limite = 100.0):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def sacar(self,valor):
        if valor > 0 and valor <= (self.consultar_saldo() + self.limite):
            novo_saldo = self.consultar_saldo() - valor
            self.__saldo = novo_saldo
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor excede o saldo disponível e o limite do cheque especial.")

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, titular, saldo=0.0, taxa_rendimento=0.01):
        super().__init__(numero, titular, saldo)
        self.taxa_rendimento = taxa_rendimento

    def render_juros(self):
        rendimento = self.consultar_saldo() * self.taxa_rendimento
        self.depositar(rendimento)
        print(f"Rendimento de R${rendimento:.2f} aplicado ao saldo.")


#Esta dando um erro no saque, transformar a classe ContaBancaria em interface e deixar que suas filhas implementem o saque ja resolveria