import os

print("Calculadora")

def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    return a / b
def exponenciacao(a, b):
    return a ** b
def fatorial(a):
    if a == 0:
        return 1
    else:
        return a * fatorial(a-1)
def raiz_quadrada(a):
    return a ** 0.5
def raiz_cubica(a):
    return a ** (1/3)



while True:
    os.system("cls")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - exponenciação")
    print("6 - fatorial")
    print("7 - raiz quadrada")
    print("8 - raiz cúbica")
    print("9 - sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == '9':
        print("Saindo...")
        break
    elif opcao == '1':
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print("Soma = ",soma(a, b))
        os.system("pause")
    elif opcao == '2':
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print("Subtração = ",subtracao(a, b))
        os.system("pause")
    elif opcao == '3':
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print("Multiplicação = ",multiplicacao(a, b))
        os.system("pause")
    elif opcao == '4':
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print("Divisão = ",divisao(a, b))
        os.system("pause")
    elif opcao =='5':
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print("Exponenciação = ",exponenciacao(a, b))
        os.system("pause")
    elif opcao == '6':
        a = int(input("Digite o número: "))
        print("Fatorial = ",fatorial(a))
        os.system("pause")
    elif opcao == '7':
        a = int(input("Digite o número: "))
        print("Raiz quadrada = ",raiz_quadrada(a))
        os.system("pause")
    elif opcao == '8':
        a = int(input("Digite o número: "))
        print("Raiz cúbica = ",raiz_cubica(a))
        os.system("pause")
    else:
        print("Opção inválida")
        os.system("pause")
    