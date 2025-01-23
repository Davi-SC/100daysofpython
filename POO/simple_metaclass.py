# classes são modelos para criação de objetos
# a função type funciona para criar classes: 
    # Person = type('Person', (), {
    #     '__init__':init_person(chama o init fora que recebe os atributos)
    # })
# Porem isso não util se podemos utilizar class

class Meta(type): #Meta é o nome da classe e herdar de type faz dela uma metaclass
    def __new__(mcs, name, bases, namespace): #utiliza o mcs invez do self, new é executado antes do init
        namespace['adicionei'] = 'um valor'

        cls = super().__new__(mcs, name, bases, namespace)

        for base in bases:
            for key, value in base.__dict__.items():
                if getattr(value, '__is_abstract__', False):
                    if key not in cls.__dict__.keys():
                        raise NotImplementedError(
                            f'{key} not implemented in {cls.__name__}')

        return cls
#a metaclass é utilizada para criar a classe, o new cria o objeto e o init inicia os objetos(os atributos)

def abstractmethod(method):
    method.__is_abstract__ = True
    return method


class SuperPerson(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('__new__ da class')
        return super().__new__(cls)

    def __init__(self, name, lastname):
        print('__init__ da class')
        self.name = name
        self.lastname = lastname

    @abstractmethod
    def full_name(self):
        ...


class Person(SuperPerson):
    ...

    # def full_name(self): 
    #     return 'Sei lá'

# def init_person(self, name, lastname):
#     self.name = name
#     self.lastname = lastname


# Person = type('Person', (), {
#     '__init__': init_person
# })

print(type(Person))
person1 = Person('Luiz', 'Otávio')
person2 = Person('Maria', 'Oliveira')
print(person1.name)
print(person2.name)

#Afinal, quando utilizar metaclass?
    #Para ter classes abstratas por exemplo, mas não faz muito sentido pois ja temos o metodo abc no python