# e-commerce

carrinho = []
meu_total = []


#lista de produtos
lista_produtos = [' ', 'hd','ssd','iphone 17', 'pc dell']
valores_produtos = [' ',250.55,20.5,7000,8000.99]

print(f'''
{lista_produtos[1]} - R$ {valores_produtos[1]}
{lista_produtos[2]} - R$ {valores_produtos[2]}
{lista_produtos[3]} - R$ {valores_produtos[3]}
{lista_produtos[4]} - R$ {valores_produtos[4]}

''')


#variaveis que vao escolher o produto da lista
produto_1 = int(input('ID do produto: '))
produto_2 = int(input('ID do produto: '))
produto_3 = int(input('ID do produto: '))

carrinho.append(lista_produtos[produto_1])
print('Você inseriu no seu carrinho - ', carrinho)
meu_total.append(valores_produtos[produto_1])
print('R$', sum(meu_total))

carrinho.append(lista_produtos[produto_2])
print('Você inseriu no seu carrinho - ', carrinho)
meu_total.append(valores_produtos[produto_2])
print('R$', sum(meu_total))

carrinho.append(lista_produtos[produto_3])
print('Você inseriu no seu carrinho - ', carrinho)
meu_total.append(valores_produtos[produto_3])
print('R$', sum(meu_total))


print('--------------------------------------------')
print('Seu pedido ficou R$', sum(meu_total))
print(carrinho)
print('--------------------------------------------')

#pagamento

forma_pag = ['1 - PIX','2- Cartão de Crédito','3 - Cartão de débito']
print(forma_pag)
print('--------------------------------------------')
      
pag = int(input('ESCOLHA A FORMA DE PAGAMENTO A PARTIR DO ID: '))
print('Sua forma de pagamento é', forma_pag[pag])
print('--------------------------------------------')   
print('Obrigada Volte sempre!')