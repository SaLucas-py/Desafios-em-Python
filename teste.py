'''
Desafio 12
Escreva uma função em Python para verificar a validade de uma senha.

A senha deve ter:

Pelo menos 1 letra entre [a-z] e 1 letra entre [A-Z].
Pelo menos 1 número entre [0-9].
Pelo menos 1 caractere de [$ # @].
Comprimento mínimo de 6 caracteres.
Comprimento máximo de 16 caracteres.
Entradas: "12345678", "J3sus0", "#Te5t300", "J*90j12374", "Michheeul", "Monk3y6"

A saída deve ser a senha e um texto indicando se a senha é válida ou inválida:

"1234" - Senha inválida
"Qw#1234" - Senha válida
'''

import re
#Função pedida
def validator(senha):
    min_len = 6
    max_len = 16
    maiuscula = 1
    minuscula = 1
    min_numero = 1
    especial = 1
    

    if len(senha or ()) < min_len and len(senha or() > max_len):
        print('Senha inválida - Numero de caracteres inválidos')

    elif len(re.findall(r"[A-Z]", senha)) < maiuscula:
        print('Senha inválida - Número de letras maiusculas inválidas')
    
    elif len(re.findall(r"[a-z]", senha)) < minuscula:
        print('Senha inválida - Número de letras minusculas inválidas')
    elif len(re.findall(r"[0-9]", senha)) < min_numero:
        print('Senha inválida - Quantidade de algarismos inválidos')
    elif len(re.findall(r"[$#@]", senha)) < especial:
        print('Senha inválida - Quantidade de caracteres especiais inválidos')
    else: 
        print('Senha correta!')


#programa principal
senha = input('Digite sua senha: ')
validando = validator(senha)
