import sys
import hashlib

if sys.version_info < (3, 6):
    import sha3

def gerar_hash_msg(msg):
    encode_msg = msg.encode()
    return hashlib.sha3_256(encode_msg).hexdigest()

def assinar_msg(msg, privKd, pubKn):
    #1 hash da msg
    hash = gerar_hash_msg(msg)

    #2 Assinatura com cifração de hash
    # assinatura = mensagem ^ chave_privada mod de chave_publica_n
    tam = len(hash)
    assinaturaArr = []
    for i in range(tam):
        char = hash[i]
        asc = ord(char)
        ass = pow(asc, privKd, pubKn)
        assinaturaArr.append(ass)
    return assinaturaArr

def confere_assinatura(assinatura, hashMsg, pubKe, pubKn):
    # mensagem = assinatura ^ chave_publica_e mod de chave_publica_n
    hashArr = []
    for s in assinatura:
        hashdec = pow(s, pubKe,pubKn)
        hashArr.append(chr(hashdec))
    strHash =  ''.join(hashArr)

    if strHash == hashMsg:
        return True
    else:
        return False
