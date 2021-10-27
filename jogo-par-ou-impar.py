numero = int(input())

if (numero-1) % 2 == 1:
    numero_anterior = numero - 1 
else:
    numero_anterior = numero - 2

if (numero+1) % 2 == 0:
    numero_posterior = numero + 1
else:
    numero_posterior = numero + 2

print(numero_anterior,numero_posterior)
