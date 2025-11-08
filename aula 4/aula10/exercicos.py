# #exercicio 1
try:
   n = int(input('Insira um número: '))
   print('Seu número é:', n)
except ValueError as erro:
    print(erro)
else:
    print('Erro não identificado')
finally:
    print('Fim de carregamento...')

#exercicio 2

try:
    n1 = int(input('Insira um número: '))
    n2 = int(input('Insira outro número: '))
    divisao = n1 / n2
    print('A divisão dos números é', divisao)
except ValueError as erro:
    print(erro)
except ZeroDivisionError as erro:
    print(erro)
else:
    print('erro não identificado')
finally:
    print('fim de carregamento...')
# ValueError ZeroDivisionError

#exercicio 3 

try:
    lista = [6,2,4]
    n = int(input('Peça um número da lista entre 0 a 2: '))
    print('Seu número foi: ', lista[n])
except IndexError as erro:
    print(erro)
except ValueError as erro:
    print(erro)
else:
  print('erro não identificado')
finally:
    print('Fim de carregamento...')
