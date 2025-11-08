import statistics
import modulo as mdl

print('empresa 1')
empresa1 = [1000,6000,1200,8000,1400]

print('media',mdl.media(empresa1))
print('mediana',mdl.mediana(empresa1))
print('desvio',mdl.desvio(empresa1))
print('variancia',mdl.variancia(empresa1))
print('amplitude', mdl.amplitude(empresa1))

# media muito distante da mediana e teve um alto desvio

print('empresa 2')
empresa2 = [5000,4000,3000,2000,7000]

print('media',mdl.media(empresa2))
print('mediana',mdl.mediana(empresa2))
print('desvio',mdl.desvio(empresa2))
print('variancia',mdl.variancia(empresa2))
print('amplitude', mdl.amplitude(empresa2))

# media parecido com a mediana mas com um desvio e variancia muito altos
print('empresa 3')
empresa3 = [1200,1300,8000,3000,15000]

print('media',mdl.media(empresa3))
print('mediana',mdl.mediana(empresa3))
print('desvio',mdl.desvio(empresa3))
print('variancia',mdl.variancia(empresa3))
print('amplitude', mdl.amplitude(empresa3))

# média não muito proxima a mediana com desvio alto 
print('empresa 4')
empresa4 = [1400,1750,2000,4500,5900]

print('media',mdl.media(empresa4))
print('mediana',mdl.mediana(empresa4))
print('desvio',mdl.desvio(empresa4))
print('variancia',mdl.variancia(empresa4))
print('amplitude', mdl.amplitude(empresa4))

#amplitude baixa media não muito proxima a mediana, desvio alto

# empresa 2 pq a media e a mediana sao proximas e em comparação ao desvio a variancia e a amplitude estao baixos comparado aos outros