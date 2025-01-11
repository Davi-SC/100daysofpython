#Soma de Fatoriais : desafio 1161 na beecrowd - https://judge.beecrowd.com/pt/problems/view/1161

def calcularfatorial(x):
    if x == 0:
        return 1
    else:
        return x * calcularfatorial(x-1)

while True:
    try:
        m,n = input().split()
        m = int(m)
        n = int(n)
        fatm = calcularfatorial(m)
        fatn = calcularfatorial(n)
        print(fatm+fatn)
    except EOFError:
        break