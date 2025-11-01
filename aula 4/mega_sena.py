import random

n1 = random.randint(1,10)
n2 = random.randint(11,20)
n3 = random.randint(21,30)
n4 = random.randint(31,40)
n5 = random.randint(41,50)
n6 = random.randint(51,60)

lista_numeros = []
lista_numeros.extend([n1,n2,n3,n4,n5,n6])

c1 = int(input(1-60))
c2 = int(input(1-60))
c3 = int(input(1-60))
c4 = int(input(1-60))
c5 = int(input(1-60))
c6 = int(input(1-60))

if (c1,c2,c3,c4,c5,c6) in lista_numeros:
    print('Acetou todos!😁👍')

else:
    print('Errou🍅🍅🍅')