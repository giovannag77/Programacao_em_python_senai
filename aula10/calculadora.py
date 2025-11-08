def calculadora ():
        #variaveis locais 
    print ('CALCULADOARA PYTHON')
    while True:
        n1 = float(input('n°>>'))
        op = input ('+I=| - | * | / |')
        if op == '+':
            n2 = float(input('n°>>'))
            print('=', n1 + n2)

        elif op == '-':
            n2 = float(input('n°>>'))
            print('=', n1 - n2)

        elif op == '*':
            n2 = float(input('n°>>'))
            print('=', n1 * n2)

        elif op == '/':
            n2 = float(input('n°>>'))
            print('=', n1 / n2)
        
        else:
            print('Erro')


calculadora()