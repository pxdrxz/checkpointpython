soma = 0
quantidade = 0
numero = 1
while numero != 0:
    numero = int(input("Digite um número (0 para sair): "))
    soma += numero
    if numero != 0:
        quantidade += 1
media = soma / quantidade
print("Quantidade de números:", quantidade)
print("Soma dos números:", soma)
print("Média dos números:", media)
