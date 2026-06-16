import random

password = 1234
senha = ()
tentativas = 0
while senha != password:
    senha = int(input("Informe a senha de acesso: "))
    tentativas = tentativas + 1
    if senha != password:
        print("Senha Incorreta, tente novamente! ")
    elif senha == password:
        print("Acesso Liberado! ")

