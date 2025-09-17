# 1. Número positivo ou negativo
# Peça ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.

numero = int(input("Digite um número inteiro: \n"))

if numero >= 0:
    print(f"O numero {numero} eh positivo")
else:
    print(f"O numero {numero} eh negativo")