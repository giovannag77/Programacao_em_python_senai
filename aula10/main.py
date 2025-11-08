# arquivo main.py

import modulo as mdl

vendas  =  [1,2,10,15,1,22,33,35,40,50]

print(mdl.imc(65,1.70))
print(mdl.calcular_soma(10,30))
print(mdl.verificar_idade(25))
mdl.estatistica(vendas)
print('media',mdl.media(vendas))
print('mediana',mdl.mediana(vendas))
print('desvio',mdl.desvio(vendas))
print('variancia',mdl.variancia(vendas))
print('amplitude', mdl.amplitude(vendas))
