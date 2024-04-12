def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))
resultado = fatorial(n) // (fatorial(k) * fatorial(n - k))
print("O resultado da equação é:", resultado)
