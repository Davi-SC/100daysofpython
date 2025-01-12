# Podemos importar bibliotecas inteiras ou apenas algumas funções.
#   - biblioteca inteira: import math
#   - biblioteca específica: from math import sqrt
print("\nExemplo biblioteca math:")
import math

num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print(f"A raiz de {num} é igual a {raiz:.2f}")
# math.ceil(raiz) arredonda para cima
# math.floor(raiz) arredonda para baixo

print("\nExemplo biblioteca random:")
import random
num = random.randint(1, 10)
print(f"Numero aletorio : {num}")

print("\nExemplo biblioteca emoji:")
# pip install emoji no cmd
import emoji
print(emoji.emojize("Olá, mundo :sunglasses:", use_aliases=True))

print("\nExemplo biblioteca datetime:")
import datetime
data = datetime.datetime.now()
print("Data atual: ",data)

print("\nExemplo biblioteca colorama:")
# pip install colorama no cmd
from colorama import Fore, Back, Style
print(Fore.RED + "Olá, mundo!")
print(Back.GREEN + "Olá, mundo!")
print(Style.RESET_ALL)

#Existtem muitas bibliotecas para Python.Como por exemplo:
#   - Pandas: biblioteca para análise de dados
#   - Numpy: biblioteca para cálculos matemáticos
#   - Matplotlib: biblioteca para criação de gráficos
#   - Scikit-learn: biblioteca para aprendizado de máquina
#   - TensorFlow: biblioteca para deep learning
#   - PyTorch: biblioteca para deep learning
#   - Django: framework para desenvolvimento web
#   - Flask: framework para desenvolvimento web
#   - PyGame: biblioteca para criação de jogos
#   - PyQt: biblioteca para criação de interfaces gráficas
#   - PSutil: biblioteca para monitoramento de sistema
#   - Requests: biblioteca para requisições HTTP
#   - Watchdog: biblioteca para monitoramento de arquivos
# Entre muitas outras bibliotecas.