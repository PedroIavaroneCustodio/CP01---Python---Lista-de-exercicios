# 8. Par ou múltiplo de 5
# Solicite um número inteiro e verifique:
# Se ele é par, escreva “Par”.
# Senão, se for múltiplo de 5, escreva “Múltiplo de 5”.
# Caso contrário, escreva “Outro número”.

numero = int(input("Digite um número inteiro: \n"))
if numero % 2 == 0:
    print("Par")
elif numero % 5 == 0:
    print("Multiplo de 5")
else:
    print("Outro numero")