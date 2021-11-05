import base64
from PrimoAleatorio import PrimoAleatorio
from PrimoAleatorio import ehPrimo
import random
import math


    
def gera_chaves(bits):
    #Geração de Chaves Públicas
    bitsp = int((bits +1) /2)
    bitsq = bits - bitsp
    p = PrimoAleatorio(bitsp) #Número Primo aleatório
    q = PrimoAleatorio(bitsq) #Número primo aleatório diferente de p
    n = p * q #Parte da chave pública resultado de p * q
    a = funcao_totiente(p)
    b = funcao_totiente(q)
    totiente_n = a * b #Como p e q são primos temos totiente_n = (p-1) * (q-1)
    e = gera_e(totiente_n) #Parte da chave Pública

    #Geração de chave privada
    d = inversoMultiplicativoMod(e, totiente_n)

    return e,n,d

    
def funcao_totiente(n):
    if ehPrimo(n):
        return n - 1
    else:
        resultado = 1

        for i in range(2, n):
            if math.gcd(i,n) == 1:
               resultado += 1 
    
        return resultado

    
def gera_e(totiente_n,):
    
    while True:
        gerado = random.randrange(2, totiente_n)
        if math.gcd(totiente_n, gerado) == 1:
            return gerado


def inversoMultiplicativoMod(a, m):
    if math.gcd(a, m) != 1:
        return None
    
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def guarda_chaves(nome_cifrador,n,e,d):
    with open( 'chaves/' + nome_cifrador + '_chave_publica_1.txt', 'w') as f:
        f.write(str(n))
    with open('chaves/' + nome_cifrador + '_chave_publica_2.txt', 'w') as f:
        f.write(str(e))
    with open('chaves/' + nome_cifrador + '_chave_privada.txt', 'w') as f:
        f.write(str(d))

def cifra_msg_assimetrica( msg, pubKe, pubKn):
    tam = len(msg)
    msgArr = []
    for i in range(tam):
        letra = msg[i]
        #asc = ord(letra)
        #cif = pow(asc, pubKe, pubKn)
        cif = pow(letra, pubKe, pubKn)
        msgArr.append(cif)
    #msg_codificada = base64.b64encode(msgArr)
    return msgArr

def decifra_msg_assimatrica(cif, privK, pubKn):
    #cif_decod = base64.b64decode(cif)
    msgArr = []
    for c in cif:
        msgdec = pow(c, privK,pubKn)
        #msgdec = msgdec % pubKn
        msgArr.append(chr(msgdec))
    strMsg =  ''.join(msgArr)
    return strMsg
