# 2. Par ou ímpar
# Receba um número inteiro e verifique se ele é par ou ímpar.

numero = int(input("Digite um número inteiro: \n"))

if numero % 2 == 0:
    print(f"O numero {numero} eh par")
else:
    print(f"O numero {numero} eh impar")