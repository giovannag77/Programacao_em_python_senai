import random


# mul = int(input('Multiplicador: '))
# for numero in range(11):
#     calculo =  numero * mul
#     print(mul, 'X', numero, '=', calculo)


# carrinho = []
# for n in range(10):
#     produto = input('produto: ')
#     carrinho.append(produto)
#     print(carrinho)


# for    while


# while True:
#     print('inifinito')




# contador =  0


# while contador <= 3:
#     print(contador)
#     contador = contador + 1



# if else elif 
# match case
# for while


ecommerce = {
     
        'celulares':{
             'SAMSUNG':1500.66,
             'IPHONE':3000.0
        },


        'roupas':{
            'camiseta':150.0,
            'calça':250.0


        },
        'acesorios':{
            'relogio':500.0,
            'anel':90.0
        }



}




carrinho = []
valores  =  [] # criar a lista valores


deseja = input('deseja comprar - sim / não ?')
while deseja == 'sim':
    secao = input('Secao - celulares roupas ou acesorios')
    p1 = input(f'Produto: {ecommerce[secao]}')
    carrinho.append(p1) # adionamos o produto
    valores.append(ecommerce[secao][p1])
    print(carrinho)
    total = sum(valores)
    print('R$', total)
    deseja = input('Deseja continuar   - sim / não?')
else:
    print('Obrigada volte sempre!')   