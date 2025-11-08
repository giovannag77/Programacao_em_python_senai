import statistics

def estatistica(lista):
    dados2 =  set(lista)
    ''' moda é o que mais aparece'''
    if len(lista) != len(dados2):
        moda = statistics.mode(lista)
        print('moda', moda)

    else:    
        print('Não tem moda')

def media(lista):
    ''' soma dos indices /  quantidade'''
    media  =  statistics.mean(lista)
    return 'media', media

def mediana(lista):
    ''' esta no meio da frequencia'''
    med  =  statistics.median(lista)
    return med

def desvio(lista):
    ''' a raiz quadrada da variancia '''
    d =  statistics.stdev(lista)
    return d

def variancia(lista):
    ''' a distancia entre a media quadratica a os indices '''
    variancia   =  statistics.variance(lista)
    return variancia


def amplitude(lista):
    ampl = max(lista) -  min(lista)
    return ampl
