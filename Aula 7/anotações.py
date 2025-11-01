# inserir
lista  =  [] # LISTA VAZIA*** 

# append  -  inserir um dado
lista.append(10)

# extend  -  varios dados de uma vez
lista.extend([10,30,3010,30,30])

# (+=) -  inseri varios dados tb
lista +=(10,30,30,10,30,30)

# insert -  inserir na posição que você quiser
lista.insert(0,1500)

print(lista)

-----

# remover

# remove() remove por valor não por indice
lista.remove(1500)

# del - remove por indice
del lista[0]

# pop() -  remove ultimo valor
lista.pop()

# pop(com indice) -  remove o indice que vc quiser
lista.pop(2)
print(lista)


------------
# verificar algo
# tamanho  -  len()
print(len(lista))

# somar a numeros das listas
print(sum(lista))

# max() maior numero da lista
maior = max(lista)
print(maior)

# min() menor numero da lista
menor =  min(lista)
print(menor)

# count() quantidade de algum dado especifico dentro da lista
print(lista.count(30))

# sort() orgdanizar do menor para o maior
lista.sort(reverse = True )# maior para o menor 
lista.sort() # menor para maior
print(lista)

# copy() copia a lista 
copia  =  lista.copy()
print(copia)


# clear() limpa a lista
lista.clear()
print(lista)
