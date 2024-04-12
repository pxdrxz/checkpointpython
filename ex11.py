quantidade = int(input("Digite a quantidade de números: "))
numeros = []
for _ in range(quantidade):
    numeros.append(int(input("Digite um número: ")))

maximo = max(numeros)
minimo = min(numeros)
media = sum(numeros) / quantidade

print(f"Valor máximo: {maximo}")
print(f"Valor mínimo: {minimo}")
print(f"Valor médio: {media}")
