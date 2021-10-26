nome = input('Seu nome? ')
idade = int(input('Sua idade? '))
salario = float(input('Seu salário? '))

if idade > 25 and salario >= 10000.00:
    print('Poderá ter a conta bancária black')
else:
    print('Não poderá ter a conta bancária black')

print(f'Até logo {nome}!')
