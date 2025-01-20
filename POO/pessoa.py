from datetime import datetime
from random import randint
class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(),'%Y'))
    def __init__(self,nome,idade,comendo=False,falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self,alimento):
        print(f"{self.nome} esta comendo {alimento}")
        self.comendo = True

    def get_nascimento(self):
        return self.ano_atual - self.idade
    
    #metodos de classe são referentes a classe e não a instancia
    @classmethod
    #usado para metodos globais da classe
    def por_ano_nascimento(cls,nome,ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome,idade)
    #Esse metodo de classe retorna a propria classe

    #metodos estaticos
    @staticmethod
    #dentro do corpo do metodo estatico não podemos usar nem self nem cls
    def gera_cpf():
        rand = randint(10000,19999)
        return rand
    
    #metodos Getters e Setters