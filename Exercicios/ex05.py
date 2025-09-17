# 5. Comparação de dois números
# Peça dois números inteiros e informe qual deles é maior ou se são iguais.

numero1 = int(input("Digite o primeiro numero inteiro: \n"))
numero2 = int(input("Digite o segundo numero inteiro: \n"))

if numero1 > numero2:
    print("O primeiro numero eh maior do que o segundo numero")
elif numero1 < numero2:
    print("O segundo numero eh maior do que o primeiro numero")
else:
    print("Os dois numeros sao iguais")