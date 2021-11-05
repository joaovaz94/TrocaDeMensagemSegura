Gerador/Verificador de Assinaturas

O trabalho foi desenvolvido em python organizado em arquivos diferentes implementando algumas
partes diferentes e a lógica principal é implementada no arquivo main.py que é o arquivo que deve ser
executado. Observação: para rodar o código é necessária a instalação do pip pycrypto que implementa a
cifração simétrica.


Estrutura de arquivos:

main.py – Lógica principal de interloucutores trocando chaves, mensagem e assinaturas.
Assinatura.py – Possui funções de gerar hash de mensagens, assinar mensagens e conferir assinaturas
CifraSimetrica.py – Usa a biblioteca externa AES de Crypto.Cipher para gerar chaves simétricas,
cifrá-las e decifrá-las
Interloucutores.py – Implementa uma classe de interloucutores para trocar mensagens de modo
seguro usando chaves simétricas e assimétricas e assinaturas.
PrimoAleatoria.py – implementa funções para a geração de números primos aleatórios com muitos
bits de tamanho certificando eles pelo teste de Miller Rabin.
RSA.py – Implementa funções de geração de chaves, cifração e decifração assimétrica aos moldes do
RSA.


Referências utilizadas para implementação do trabalho:

https://medium.com/@tarcisioma/algoritmo-de-criptografia-assim%C3%A9trica-rsa-c6254a3c7042
https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/
https://www.geeksforgeeks.org/sieve-of-eratosthenes/
https://pt.wikipedia.org/wiki/RSA_(sistema_criptogr%C3%A1fico)https://www.geeksforgeeks.org/sha3-in-python/
https://pythonprogramming.net/encryption-and-decryption-in-python-code-example-with-explanation/