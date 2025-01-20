""" TESTANDO A CLASSE PESSOA
from pessoa import Pessoa

p1 = Pessoa('luiz',38)
p2 = Pessoa('joao',15)

p1.comer('limao')

print(p1.get_nascimento())

#usando o metodo de classe
p2 = Pessoa.por_ano_nascimento('luiz',1987)
print(p2)
print(p2.nome , p2.idade)
print(p2.get_nascimento())

#testando o metodo estatico


print(p2.gera_cpf())"""

from produto import Produto

p1 = Produto("camiseta",50)
p1.desconto(10)
print(p1.preco)

p2 = Produto("caneca",15)
p2.desconto(10)
print(p2.preco)

