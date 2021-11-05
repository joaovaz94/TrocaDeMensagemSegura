from Crypto.Cipher import AES
import base64, os

def gera_chave_simetrica_secreta():
    tamanho_chave = 16
    chave_secreta = os.urandom(tamanho_chave)
    chave_codificada = base64.b64encode(chave_secreta)

    return chave_codificada

def cifracao_simetrica(msg, chave_codificada):
    chave_simetrica = base64.b64decode(chave_codificada)
    cifra = AES.new(chave_simetrica, AES.MODE_ECB)
    #cifra = AES.new(chave_codificada, AES.MODE_ECB)
    #tam_msg = len(msg)
    #adpata o tamanho da mensagem pra se adaptar ao tamanho requerido pelo AES
    msg_adaptada = msg
    while len(bytes(msg_adaptada, encoding='utf-8')) % 16 != 0:
        msg_adaptada = msg_adaptada + '|'
    #msg_adaptada = msg + ('|' * ((16 - len(msg)) % 16))
    #tam_msg = len(msg_adaptada)
    msg_cifrada = cifra.encrypt(msg_adaptada.encode())
    msg_cifrada_codificada = base64.b64encode(msg_cifrada)

    return msg_cifrada_codificada

def decifracao_simetrica(msg_cifrada_codificada, chave_codificada):
    chave_simetrica = base64.b64decode(chave_codificada)
    msg_cifrada = base64.b64decode(msg_cifrada_codificada)
    cifra = AES.new(chave_simetrica, AES.MODE_ECB)
    msg_decifrada = cifra.decrypt(msg_cifrada).decode("utf-8")
    msg_real = msg_decifrada.rstrip("|")

    return msg_real
