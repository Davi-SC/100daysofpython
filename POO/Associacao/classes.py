"""
Como fazer uma classe conversr com outra?

A associação é uma relação onde as classes 
e conversão mas não são dependentes uma da outra
"""

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta
    
    
class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print("Caneta escrevendo")
    
class MaquinaEscrever:
    
    def escrever(self):
        print("Maquina escrevendo")