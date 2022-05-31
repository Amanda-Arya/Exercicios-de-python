# Neste jogo mostre que você domina par ou ímpar e vença seu adversário. Implemente um algoritmo 
# que solicite ao usuário 06 números inteiros e, ao final, informe a quantidade de números ímpares e 
# pares lidos. Calcule também a soma dos números pares e a média dos números ímpares.

cont = 0
contp = 0
somap = 0
conti = 0
somai = 0
media = 0.00
while cont <= 6:
    numero = int(input("Digite um número:"))
    if numero > 0:
        if numero % 2 ==0:
           contp = contp + 1
           somap = somap + numero
        else:
            conti = conti + 1
            somai = somai + numero  
        
    else:
        print("Número inválido!")
            
    cont = cont + 1
media = somai / conti

print(f"A quantidade de pares é: {contp}")
print(f"A quantidade de ímpares é: {conti}")
print(f"A soma dos números pares é: {somap}")
print(f"A média dos números ímpares é: {media}")