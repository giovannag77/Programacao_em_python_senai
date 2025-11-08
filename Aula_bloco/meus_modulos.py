


# EXERCÍCIOS:



# Trabalhando um pouco mais com funções | loops | variáveis | listas …
# Crie com módulos das funções utilize parâmetros/return:
# 1 - Crie um número aleatório de 5,10
# 2 - Crie 3 números aleatórios
# 3 - Crie um número aleatório entre 10 a 30 utilize o range()
# 4 - Contagem regressiva simples Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)
# 5 - Soma de números pares
# Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.
# # Peça ao usuário que insira um número inteiro 
# # faça o loop com range e for ate´o numero
# # positivo e, em seguida, calcule a soma de 
# # todos os números pares de 2 até o número inserido.

# (use módulo, if, for)
# 6 - Tabuada de multiplicação
# Utilize print() na saída
# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
# (while ou for )
# 7 - Números ímpares reversos
# Exiba uma contagem regressiva de números ímpares de 99 a 1.
# (for)
# Chamar todas elas para o arquivo main() 


from os import times
import random
import time

def atividade_1():
    n = random.randint(5,10)
    return n

def atividade_2():
    n1=random.randint (0,100)
    n2=random.randint(0,100)
    n3=random.randint(0,100)
    return n1,n2,n3

def atividade_3():
    lista= (int(random.randrange(1,31)))
    n= lista
    return lista

def atividade_4 ():
    for i in range(10,1,-1):
          print (i)
    print('FOGO!')

def atividade_5 ():
    num = int(input('n°?'))
    n2 = int(input('n°?'))
if num and n2 % 2 == 0:
    conta = num + n2
    print(conta)
else:
    print('Não foi possivel calcular')