# No jogo “Descubra o Maior > e o Menor <”. Escreva um algoritmo que receba um conjunto de 
# valores inteiros e positivos, calcule e exiba o maior e o menor valor do conjunto. Considere que: 
# a. para encerrar a entrada de dados, deve ser digitado o valor zero; 
# b. para valores negativos, deve ser exibida uma mensagem;
# c. esses valores (zero e negativos) não entrarão nos cálculos.

lista_numeros = []
qtd = int(input("Quantos números você quer na sua lista: "))
i = 1

while i <= qtd:

    numero = int(input(f"Escolha o {i}º número: "))
    
    if numero > 0:
        lista_numeros.append(numero)
 
    if numero < 0:
      print("Número inválido!")  

    elif numero == 0:
        break

    i = i + 1 
print(lista_numeros)
print(f"O maior número da lista é:{max(lista_numeros)}")
print(f"O menor número da lista é:{min(lista_numeros)}")