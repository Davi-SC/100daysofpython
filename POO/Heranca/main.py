'''
ASSOCIAÇÃO - usa ;; AGREGAÇÃO - tem ;; COMPOSIÇÃO - é dono ;; HERANÇA - É

A herança em python é definida colocando o nome da classe pai entre parenteses apos a declaração da classe filho
As subclasses não precisam ter apenas os atributos e metodos da classe pai, as subclasses tem seus comportamentos expecificos
'''

from classe import *

c1 = Cliente('Davi',23)
print(c1.nome)


a1 = Aluno('Diogo',32)
print(a1.nome)


