e_commerce = {
    'tenis nike': 600.0,
    'camiseta adidas':150.0,
    'fone':250.99,
    }
produto_1 = input('Digite o nome do produto: ')
produto_2 = input('Digite o nome do produto: ')

carrinho = []
valores = []

carrinho.append(produto_1)
carrinho.append(produto_2)
print(carrinho)

valores.append(e_commerce[produto_1])
valores.append(e_commerce[produto_2])

print('R$', valores)
somar=sum(valores)
print('R$', somar)