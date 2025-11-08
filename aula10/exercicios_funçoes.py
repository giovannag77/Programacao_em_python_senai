# def par_ou_impar ():
#     n1 = int(input('n°>>'))
#     if n1 % 2 == 0:
#         print('Este numero é par')
#     else:
#         print('Este número é impar')

# par_ou_impar()

# def multiplicacao ():
#     n1 = int(input('numero 1?'))
#     n2 = int(input('numero 2?'))
#     n3 = int(input('numero 3?'))
#     multiplicador = n1 * n2 *n3
#     print('Os três números multiplicados são:', multiplicador)    

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


def restaurante ():
   nome = input('Olá, qual o seu nome?')
   print('Seja bem-vindo(a)', nome,'!')
   cardápio = ['Salada, Macarronada, Sanduiche, Sorvete']
   print (cardápio)
   opcao = input('Qual opção deseja?')
   carrinho = []
   carrinho.append(opcao)
   print(opcao, 'Foi adicionado ao seu carrinho')
   loop = int(input('Deseja continuar? 1- sim 2- não '))

   if loop == 1:
        print (cardápio)
        opcao2 = input('Qual opção deseja?')
        carrinho = []
        carrinho.append(opcao2)
        print(opcao2, 'Foi adicionado ao seu carrinho')
        print (carrinho)
        loop = int(input('Deseja continuar? 1- sim 2- não '))
   else:
    print('Obrigada volte sempre!')

   

restaurante()