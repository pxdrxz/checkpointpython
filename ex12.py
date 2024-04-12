def fibonacci(n):
    fibonacci_seq = [0, 1]
    for _ in range(2, n):
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return fibonacci_seq

N = int(input("Digite o valor de N para a sequência de Fibonacci: "))
print("Sequência de Fibonacci com", N, "valores:", fibonacci(N))
