#                                   RECURSÃO
def fatorial(n):
    if n <= 1:                   #base da recursão
        return 1
    else:
        return n * fatorial(n-1) #chamada recursiva

import pytest
@pytest.mark.parametrize('entrada, esperado',[
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
    ])

def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado



#####################################################################################




def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    



##########################################################################################
    
#                                   MAIS SOBRE RECURSÃO

def busca_binaria(lista, elemento, min = 0, max = None):
    if max == None:
        max = len(lista) - 1

    if max < min:
        return False
    else:
        meio = min + (max-min)//2

    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio-1)
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio+1, max)

    else:
        return meio

#################################################################################


def merge_sort(lista):
    if len(lista) <= 1:             #BASE DA RECURSÃO
        return lista

    meio = len(lista) // 2

    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito

    if not lado_direito:
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])

    
    




    
