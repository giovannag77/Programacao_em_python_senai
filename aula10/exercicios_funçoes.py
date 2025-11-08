# def par_ou_impar ():
#     n1 = int(input('n°>>'))
#     n2 = int(input('n°>>'))
#     if n1 % 2 == 0 and n2 % 2 == 0:
#         print('Ambos são pares')
#     elif n1 % 2 == 1 and n2 % 2 == 1:
#         print('Ambos são impares')
#     else:
#         print('Apenas um é par')

# par_ou_impar()

# def multiplicar(x,y,z):
#   return x * z * y

#  print(multiplicar(20,2,3)) 

# multiplicacao ()

# def n_elevado ():
#     n = int(input('digite um numero: '))
#     valor = n ** 2
#     print ('seu numero elevado é: ', valor)

# n_elevado ()

# def idade ():
#     idade = int(input('Quantos anos você tem? '))
#     if idade == 18:
#         print(Style.BRIGHT+Back.YELLOW + Fore.GREEN + 'Você tem 18 anos')
#     else:
#         print ('Putz, você não tem 18 anos')

# idade()

# def desc_idade ():
#     i = int(input('Em qual ano você nasceu?'))
#     valor= 2025 - i 
#     print('você tem', valor, ' anos')

# desc_idade()

# def copa (ano,lista):
#     if ano in lista:
#         print('o BRASIL GANHOU NESTE ANO')
#     else:
#         print('Brasil não ganhou')
# anos = [1958,1962,1970,1994,2002.]
# copa(1999,anos)
    

def restaurante ():
   nome = input('Olá, qual o seu nome?')
   print('Seja bem-vindo(a)', nome,'!')
   cardápio = ['Salada, Macarronada, Sanduiche, Sorvete']
   print (cardápio)
   opcao = input('Qual opção deseja?')
   carrinho = []
   carrinho.append(opcao)
   print ('------------------------------------')
   print(opcao, 'Foi adicionado ao seu carrinho')
   loop = int(input('Deseja continuar? 1- sim 2- não '))

   while loop == 1:
        print (cardápio)
        opcao2 = input('Qual opção deseja?')
        carrinho = []
        carrinho.append(opcao2)
        print ('------------------------------------')
        print(opcao2, 'Foi adicionado ao seu carrinho')
        print ('------------------------------------')
        print (carrinho)
        loop = int(input('Deseja continuar? 1- sim 2- não '))
   else:
    print('Obrigada volte sempre!')

restaurante()