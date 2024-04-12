divida = float(input("Digite o valor inicial da dívida: "))
juros_mensal = float(input("Digite a taxa de juros mensal (em %): ")) / 100
pagamento_mensal = float(input("Digite o valor do pagamento mensal: "))
total_pago = 0
total_juros_pago = 0
meses = 0
while divida > 0:
    divida *= 1 + juros_mensal
    divida -= pagamento_mensal
    total_pago += pagamento_mensal
    total_juros_pago += divida * juros_mensal
    meses += 1
print(f"Total de meses para pagar: {meses}")
print(f"Total pago: R${total_pago:.2f}")
print(f"Total de juros pago: R${total_juros_pago:.2f}")
