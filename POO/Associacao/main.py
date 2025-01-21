from classes import Escritor
from classes import Caneta
from classes import MaquinaEscrever

escritor = Escritor('Pedro')
caneta = Caneta('Bic')
maquina = MaquinaEscrever()

print(escritor.nome)
caneta.escrever()
maquina.escrever()

print("")

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

# essa associação é fraca, quando o escritor é apagado do programa a caneta e a maquina ainda existe