# 4. Nota de aprovação
# Receba a nota de um aluno (0 a 10) e diga se ele foi aprovado (nota ≥ 6) ou reprovado.

nota = float(input("Digite a nota do aluno (0 a 10): \n"))

if nota >= 6:
    print("O aluno foi aprovado")
else:
    print("O aluno foi reprovado")