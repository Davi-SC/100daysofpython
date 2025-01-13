#Listas são estruturas heterogeneas, podem ter dados de tipos diferentes

exemplo = ["davi",3.445,'a',3,"manelim",True]
print(exemplo)
print(exemplo[-2])
print(exemplo[1:4])
print(exemplo[2:])
print(exemplo[:3])
print(exemplo[1:4:2])
print(len(exemplo))
exemplo += ["novo"]
print(exemplo)
exemplo.append("novo2")
print(exemplo)
exemplo.insert(3,"novo3")
print(exemplo)
exemplo.remove("novo2")
print(exemplo)
del exemplo[3]
print(exemplo)
print('davi' in exemplo)
print('cuzcuz' not in exemplo)
for i,item in enumerate(exemplo):
    print(f"Indice: {i} - Item: {item}")

import random
print(random.choice(exemplo))
print(random.sample(exemplo,3))
print(random.choices(exemplo,k=3))

people = ["davi","cuzcuz","manelim","abestato","cabessao"]
print(people)
random.shuffle(people)
print(people)
people.sort()
print(people)
people.sort(reverse=True)
print(people)
people.reverse()
print(people)