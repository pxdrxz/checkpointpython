deposito_inicial = float(input("Digite o valor do depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros (em %): ")) / 100
valor_deposito_mensal = float(input("Digite o valor do depósito mensal: "))
total_juros = 0
saldo = deposito_inicial
for mes in range(1, 25):
    saldo += valor_deposito_mensal
    saldo *= 1 + taxa_juros
    total_juros += valor_deposito_mensal * taxa_juros
    print(f"Mês {mes}: Saldo: R${saldo:.2f}")
print(f"Total ganho com juros em 24 meses: R${total_juros:.2f}")
