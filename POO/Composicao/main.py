# A composição é  relação mais forte entre classes
# Uma classe é dona de objetos de outra clsse, se a classe maior for apagada a menor tambem sera

from classes import Cliente

c1 = Cliente('Davi',23)
c1.insere_enderecos('Coi neto','MA')
print(c1.nome)
c1.lista_enderecos()
print()

c2 = Cliente('Diogo',32)
c2.insere_enderecos('Coi neto','MA')
c2.insere_enderecos('Teresina','PI')
print(c2.nome)
c2.lista_enderecos()
print()

#Quando um cliente é apagado da memoria, todos os seus enderecos serao apagados da memoria
#Nesse caso do exemplo, a classe endereço depende da classe cliente