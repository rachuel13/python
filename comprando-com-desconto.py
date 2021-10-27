valor_mercadoria = float(input())
quant_mercadoria = int(input())

sem_desconto = quant_mercadoria * valor_mercadoria

fixo = 10 + quant_mercadoria

com_desconto = sem_desconto-(sem_desconto*fixo/100)

print(f'{sem_desconto:.2f}')
print(f'{com_desconto:.2f}')
