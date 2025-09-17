# 6. Desconto em produto
# Receba o valor de um produto e mostre o preço final com desconto de 10% se o valor for maior que 100; caso contrário, mostre o preço sem desconto.

valor_produto = float(input("Digite o valor do produto: \n"))

if valor_produto > 100:
    valor_final = valor_produto * 0.9
    print(f"O preço final do produto com desconto ficou R${valor_final}, totalizando um desconto de R${valor_produto * 0.1}")
else:
    print(f"O preço do produto eh R${valor_produto}")