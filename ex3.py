soma = 0  
while True:
    try:
        n = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")
        continue
    if n == 0:
        break
    soma += n

print(f"A soma de todos os números digitados é: {soma}")
