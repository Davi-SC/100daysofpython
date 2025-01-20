# variaveis de classe

class A:
    vc = 123 #variavel de classe
    def __init__(self): 
        #self.vc = 321 #variavel de instancia
        pass

a1 = A()
a2 = A()


print(a1.vc)
print(a2.vc)
print(A.vc)

# o compilador do python busca primeiro na instancia e depois na classe

# para alterar uma variavel de classe que mude em todas as instancias devemos altera-la a partir da classe]
A.vc = 1010
print(a1.vc)
print(a2.vc)
print(A.vc)