# O “Game Mestre da Tabuada” deseja calcular a tabuada do 1 ao 10. Faça um programa que receba 
# um número entre 1 e 10, calcule e mostre a tabuada desse número. 

tabuada = int(input("Digite a tabuada que deseja calcular: "))

for i in range(1,11):
    res = tabuada * i
    print(f"{tabuada}x{i}:", res)
    
