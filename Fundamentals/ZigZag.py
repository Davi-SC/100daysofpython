import sys, time, os

print("******** ZigZag ********")
print("Pressione CTRL-C para sair.")
os.system('pause')

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.09)
        if indentIncreasing:
            #aumentando o numero de espaços
            indent = indent + 1
            if indent == 20:
                #mudando a direção
                indentIncreasing = False
        else:
            #diminuindo o numero de espaços
            indent = indent - 1
            if indent == 0:
                #mudando a direção
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
