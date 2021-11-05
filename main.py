from RSA import *
from Interloucutores import *
from CifraSimetrica import *

#Incialização de Interloucutores gerando-se suas chaves públicas e privada
emissor = Interloucutor()
receptor = Interloucutor()

#Interloucutores trocam chave Públicas:
receptor.guarda_chaves_publicas_interloucutor(emissor.pubKn, emissor.pubKe)
emissor.guarda_chaves_publicas_interloucutor(receptor.pubKn, receptor.pubKe)

#Emissor Gera chave simetrica pra comunicação
chave_simetrica_comunicacao = gera_chave_simetrica_secreta()
emissor.guarda_chave_simetrica(chave_simetrica_comunicacao)

#Emissor Cifra e envia chave simétrica cifrada com a chave pública do receptor
chave_simetrica_cifrada = cifra_msg_assimetrica(emissor.chave_simetrica, emissor.interKe, emissor.interKn)
receptor.chave_simetrica_cifrada = chave_simetrica_cifrada

#Emissor escreve mensagem, faz sua assinatura, criptografa simetricamente a mensagem e envia
mensagem_comunicacao = """
    De certa forma, o trabalho de um crítico é fácil. Nos arriscamos pouco, e temos prazer em avaliar com superioridade os que nos submetem seu trabalho e reputação.
"""
emissor.mensagem = mensagem_comunicacao
assinatura_mensagem_comunicacao = assinar_msg(mensagem_comunicacao, emissor.privKd, emissor.pubKn)
mensagem_cifrada_comunicacao = cifracao_simetrica(emissor.mensagem, emissor.chave_simetrica)

print("Mensagem enviada: ", emissor.mensagem)

receptor.mensagem_cifrada = mensagem_cifrada_comunicacao
receptor.assinatura_mensagem = assinatura_mensagem_comunicacao

#Receptor descriptografa a chave simetrica com sua chave privada
receptor.chave_simetrica = decifra_msg_assimatrica(receptor.chave_simetrica_cifrada, receptor.privKd, receptor.pubKn)

#Receptor descriptografa mensagem com a chave simétrica
receptor.mensagem = decifracao_simetrica(receptor.mensagem_cifrada, receptor.chave_simetrica)
print("Mensagem recebida: " , receptor.mensagem)

#Receptor gera hash de mensagem recebida, descriptografa assinatura e compara hashes
receptor.hash_msg = gerar_hash_msg(receptor.mensagem)
resultado_conferencia = confere_assinatura(receptor.assinatura_mensagem,receptor.hash_msg, receptor.interKe, receptor.interKn)
print("Validade da Assinatura: ", resultado_conferencia)