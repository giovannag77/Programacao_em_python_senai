# loops

# for while condição
# estrutura de fluxo de controle

# for i in range (11):
#     print (i)

# while True:
#     print('Olá mundo')

# c = 0
# while c <=10:
#     print (c)
#     c = c + 1

# aula try and except

try:
    x  =  int(input('>')) 


    n = 10
    n2 = 0
    print(n/n2)
except ValueError as erro:
    print(erro)
except ZeroDivisionError as erro:
    print(erro)    
else:
    print('erro não identificado ')


finally:
    print('fim de carregamento... ')    

