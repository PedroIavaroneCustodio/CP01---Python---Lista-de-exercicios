# 10. Calculadora simples

# Receba dois números inteiros e uma operação (+, -, *, /) digitada pelo usuário. Use if-else para calcular e mostrar o resultado.

numero1 = int(input("Digite o primeiro numero inteiro: \n"))
numero2 = int(input("Digite o segundo numero inteiro: \n"))
operacao = input("Digite a operacao (+, -, *, /): \n")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    resultado = "Operacao invalida"

print(f"Resultado: {resultado}")