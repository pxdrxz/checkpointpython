def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Digite um número inteiro para calcular o fatorial: "))
print("O fatorial de", numero, "é:", fatorial(numero))
