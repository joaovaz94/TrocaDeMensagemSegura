from Assinatura import *
from RSA import *


class Interloucutor:

    chave_simetrica = None
    chave_simetrica_cifrada = None
    mensagem = None
    mensagem_cifrada = None
    assinatura_mensagem = None
    hash_msg = None
    hash_assin = None

    def __init__(self) -> None:
        #gerar chaves pra testes
        self.pubKe, self.pubKn, self.privKd = gera_chaves(1024)
        self.interKn, self.interKe = None, None

    def guarda_chaves_publicas_interloucutor(self,n, e):
        self.interKn, self.interKe = n, e

    def envia_chaves_publicas(self):
        return self.pubKn, self.pubKe

    def guarda_chave_simetrica(self, chave_sim):
        self.chave_simetrica = chave_sim
