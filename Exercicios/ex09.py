# 9. Conversão de temperatura
# Peça ao usuário uma temperatura em graus Celsius e mostre se está:
# Abaixo de 0 → “Congelante”
# Entre 0 e 30 → “Agradável”
# Acima de 30 → “Quente”

temperatura = float(input("Digite a temperatura em graus Celsius: \n"))

if temperatura < 0:
    print("Congelante")
elif temperatura <= 30:
    print("Agradável")
else:
    print("Quente")