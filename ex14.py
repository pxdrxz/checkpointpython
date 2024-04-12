def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

n = int(input("Digite o valor de n para a equação: "))
soma = sum([fatorial(i * 2 + 1) for i in range(1, n + 1)])
print("O resultado da equação é:", soma)
