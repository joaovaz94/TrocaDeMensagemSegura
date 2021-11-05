import random

#metodo pra retornar inteiro aleatório de n bits
def nbitsrandom(n):
    return(random.randrange(2**(n-1)+1, 2**n - 1))

#função para retornar primos até um número n
def crivodeeratostenes(n):
    primo = [True for i in range(n+1)]
    p = 2

    while (p * p <= n):
        if(primo[p] == True):
            for i in range(p * p, n+1, p):
                primo[i] = False
        p += 1

    lista_primos = []
    for p in range(2, n+1):
        if primo[p]:
            lista_primos.append(p)

    return lista_primos


#forma lista das primeiras centenas de primos
lista_primeiros_primos = crivodeeratostenes(400)

#função pra retornar números primos pequenos


def retornatesteprimospequenos(n):
    while True:
        provavel_primo = nbitsrandom(n)

        for divisor in lista_primeiros_primos:
            if provavel_primo % divisor == 0 and divisor**2 <= provavel_primo:
                break
            else:
                return provavel_primo

def dividePorPrimosPequenos(candidato):
        for divisor in lista_primeiros_primos:
            if candidato % divisor == 0 and divisor**2 <= candidato:
                return True
            else:
                return False



def testeMillerRabinPassou(candidato):
    maximadivisaopordois = 0
    componentepar = candidato - 1

    while componentepar % 2 == 0:
        componentepar >>= 1
        maximadivisaopordois += 1

    assert(2**maximadivisaopordois * componentepar == candidato - 1)

    def testecomponente(unidade_teste):
        if pow(unidade_teste, componentepar, candidato) == 1:
            return False
        for i in range(maximadivisaopordois):
            if pow(unidade_teste, 2**i * componentepar, candidato) ==  candidato - 1:
                return False
        return True

    numerodetentativasteste = 20
    for i in range(numerodetentativasteste):
        unidade_teste = random.randrange(2, candidato)
        if testecomponente(unidade_teste):
            return False

    return True

def PrimoAleatorio(n):

    while True:
        candidato_primo = retornatesteprimospequenos(n)
        #print("Testando candidatos: " + carregando)
        if not testeMillerRabinPassou(candidato_primo):
            continue
        else:
            break
    
    return candidato_primo

def ehPrimo(candidato):

    if dividePorPrimosPequenos(candidato):
        return False
    else:
        if testeMillerRabinPassou(candidato):
            return True
