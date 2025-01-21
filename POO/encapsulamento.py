# O encapsulamento serve para proteção do codigo
"""
Em outras linguagens, há modificadores de acesso:
PUBLIC - publico fora da clase
PROTECTED - publico para classes filhas
PRIVATE - privao para classes externas

em python usamos os _ antes do nome do atributo para modificar o acesso

_ é protected
__ é privado
no python é tratado como privado e fortemente privado, não considera protected
Quando utilizamos o __ em um aributo, para acessarmos este atributo fora da classe é preciso fazer bd._BaseDeDados__dados
Ou seja objeto._Classe__atributo

para dar o acesso de __dados, por exemplo, é preciso fazer:
@property
def dados(self):
    return self.__dados
ou seja, utilizando um getter,então para modificar o atributo fortemente privado precisamos do setter

essa filosofia dos _ em python tambem funciona para modificar acesso de metodos
"""

class BaseDeDados:
    def __init__(self):  # apesar de init não ser um construtor é o que mais chega perto, por isso usamos ele em python
#dicionario estava publico, o que pode ser um perigo, logo mudamos  com as convenções
        #self.dados = {} 
        # Se um atributo esta com um _ antes ele é protected(privado)
        self._dados = {}
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}    
        else:
            self._dados['clientes'].update({id: nome} )  

    def lista_clientes(self):
        for id,nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self,id):
        del self._dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Davi')
bd.inserir_cliente(2, 'Artur')
bd.inserir_cliente(3, 'Thierry')
bd.apaga_clientes(2)

bd.lista_clientes()