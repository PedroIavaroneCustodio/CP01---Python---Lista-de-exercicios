# 📘 Lista de Exercícios em Python – CP01

Este repositório contém uma lista de **10 exercícios introdutórios em Python**, com foco em estruturas condicionais (`if`, `else`, `elif`).  

O objetivo é praticar a lógica de programação e desenvolver raciocínio para tomada de decisão em programas simples.

---

## 📝 Exercícios

1. **Número positivo ou negativo**  
   Peça ao usuário um número inteiro e verifique se ele é **positivo**, **negativo** ou **zero**.

   Pensamento da resolução: Primeiro pedimos ao usuário que digite um número inteiro. Em seguida, verificamos as condições: se o número for maior que zero, ele é positivo. Se for menor que zero, ele é negativo. Caso não atenda a nenhuma dessas condições, só sobra uma possibilidade: o número ser igual a zero.

2. **Par ou ímpar**  
   Receba um número inteiro e verifique se ele é **par** ou **ímpar**.

   Pensamento da resolução: Para saber se um número é par ou ímpar, usamos o operador de resto da divisão (%). Se numero % 2 == 0, então o número é divisível por 2 e, portanto, par. Caso contrário, ele é ímpar.

3. **Maioridade**  
   Solicite a idade de uma pessoa e mostre se ela é **maior de idade (≥ 18 anos)** ou **menor de idade**.

   Pensamento da resolução: Pedimos a idade de uma pessoa e verificamos se ela é maior ou igual a 18. Se for, mostramos que é maior de idade. Caso contrário, é menor de idade.

4. **Nota de aprovação**  
   Receba a nota de um aluno (0 a 10) e diga se ele foi **aprovado (nota ≥ 6)** ou **reprovado**.

   Pensamento da resolução: Solicitamos a nota do aluno (de 0 a 10). Se for maior ou igual a 6, mostramos que está aprovado. Caso contrário, reprovado.

5. **Comparação de dois números**  
   Peça dois números inteiros e informe qual deles é **maior** ou se são **iguais**.

   Pensamento da resolução: Pedimos dois números inteiros. Primeiro verificamos se o primeiro é maior que o segundo. Se não for, verificamos se o primeiro é menor que o segundo. Se nenhuma das duas condições for verdadeira, significa que os números são iguais.

6. **Desconto em produto**  
   Receba o valor de um produto e mostre o preço final com **desconto de 10%** se o valor for **maior que 100**.  
   Caso contrário, mostre o preço **sem desconto**.

   Pensamento da resolução: Recebemos o valor de um produto. Se ele for maior que 100, aplicamos um desconto de 10%, ou seja, multiplicamos o valor por 0.9. Caso contrário, o preço continua igual.

7. **Login simples**  
   Peça um **nome de usuário** e uma **senha**.  
   - Se o usuário for `"admin"` e a senha `"1234"`, exiba **“Acesso permitido”**.  
   - Caso contrário, **“Acesso negado”**.

   Pensamento da resolução: Pedimos usuário e senha. Usamos uma comparação lógica: se o nome digitado for exatamente "admin" e a senha exatamente "1234", o acesso é permitido. Caso contrário, mostramos acesso negado.

8. **Par ou múltiplo de 5**  
   Solicite um número inteiro e verifique:  
   - Se ele é **par**, escreva “Par”.  
   - Senão, se for **múltiplo de 5**, escreva “Múltiplo de 5”.  
   - Caso contrário, escreva **“Outro número”**.

   Pensamento da resolução: Recebemos um número. Primeiro verificamos se ele é par. Se não for, testamos se ele é múltiplo de 5 (numero % 5 == 0). Se também não for, mostramos "Outro número".

9. **Conversão de temperatura**  
   Peça ao usuário uma temperatura em graus Celsius e mostre:  
   - **Abaixo de 0 → “Congelante”**  
   - **Entre 0 e 30 → “Agradável”**  
   - **Acima de 30 → “Quente”**

   Pensamento da resolução: Pedimos uma temperatura em graus Celsius. Primeiro verificamos se ela é menor que 0, se for classificamos como "Congelante". Senão verificamos se ela é maior que 0 e menor ou igual a 30, se for exibimos "Agradável". Por fim, utilizamos o else, pois a única outra possibilidade restante será imprimir "Quente"

10. **Calculadora simples**  
    Receba dois números inteiros e uma operação (`+`, `-`, `*`, `/`) digitada pelo usuário.  
    Use `if-else` para calcular e mostrar o resultado.

    Pensamento da resolução: Solicitamos dois números e um operador (+, -, * ou /). Depois, usamos if-elif-else para decidir qual operação matemática executar. Se for +, somamos; se -, subtraímos; se *, multiplicamos; se /, dividimos. Se o usuário digitar outra coisa que não seja uma dessas opções, mostramos mensagem de erro.

---

## 🚀 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/python-cp01.git
   cd python-cp01