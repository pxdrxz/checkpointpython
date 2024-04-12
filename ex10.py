def is_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True

def lista_primos(n):
    primos = []
    numero = 2
    while len(primos) < n:
        if is_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

n = int(input("Digite um número: "))
print(f"Os {n} primeiros números primos são:", lista_primos(n))

