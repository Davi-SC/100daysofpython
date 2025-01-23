# class Person:
#     def __init__(self,name,lastname):
#         self.name = name
#         self.lastname = lastname
    
#     def __str__(self):
#         class_str = f'{self.__class__.__name__} ({self.name} {self.lastname})'
#         return class_str


# if __name__ == '__main__' : 
#     jhon = Person('jhon','sons')
#     print(jhon)
#     #Se tivessesmos dois jhons(1 e 2) com nomes e sobrenomes iguais, teriamos que criar metodo para compração dos objetos, para comparar os lstnmes tambem
#     #Em resumo, pra classes normais no python cada operação precisriam de mais metodos, por isso surgiram as dataclasses     

from dataclasses import dataclass, field

@dataclass
class Person:
    name:str
    lastname:str
    active: bool = False #começar o objeto na instancia com a variavel active falsa
    addresses: list = field(default_factory = list)
    full_name: str= field(default='Missing',init=True, repr = False) 
    # se colocar o init como false é preciso criar o metodo __post_init__ pra criar o self.fullname 
    # pode colocar o repr = false na vriavel para ela não aparecer no print
# o dataclass ja tem metodos implementados que facilitam a criação de classes
    # existem muito modificadores dos campos , por exemplo
        # repr para não aparecer ou aparecer no objeto
        # existem muitas, olhar na documentação

if __name__ == '__main__' : 
    jhon1 = Person('jhon','sons',True,['R1'], 'jhon sons') 
    jhon2 = Person('jhon','sons',True, ['R2'])
    #print(jhon)
    #jhon.active = True #ou coloca na instancia
    print(jhon1)
    print(jhon2)
