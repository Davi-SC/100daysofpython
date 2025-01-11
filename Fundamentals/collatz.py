def collatz(number):
    if(number % 2 == 0):
        return number // 2
    else:
        return 3 * number + 1

try:
    number = int(input("Digite um número: "))
    while True:
        number = collatz(number)
        print(number)
        if number == 1:
            break
except ValueError:
    print("Você não digitou um número!")