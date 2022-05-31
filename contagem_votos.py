# Simulador de Eleições. Fazer um algoritmo que calcule o resultado final das eleições para a 
# presidência de um clube “Os nerds”, sabendo-se que:
# a) existem três chapas concorrendo; 
# b) os eleitores votaram fornecendo o número da chapa escolhida;
# c) votaram ao todo 10 membros do clube.
# O programa deverá processar os votos recebidos e fornecer o total de votos de cada uma das 
# chapas, o total de votos em branco e o total de votos nulos. Além disso, o programa deverá verificar 
# se a chapa mais votada é vencedora no primeiro turno da eleição (mais de 50% dos votos) ou se 
# deverá ocorrer um segundo turn

nerds1 = 0
nerds2 = 0
nerds3 = 0
nulo = 0
branco = 0
i = 0

while i <= 10: 
    
    pergunta = int(input("Digite o número que representa seu voto: (1) nerds 1 (2) nerds 2 (3) nerds 3 (4) branco (5) nulo -->"))
    i = i + 1

    if pergunta == 1:
        nerds1 = nerds1 + 1

    if pergunta == 2:
        nerds2 = nerds2 + 1
    
    if pergunta == 3:
        nerds3 = nerds3 + 1

    if pergunta == 4:
        branco = branco + 1

    if pergunta == 5:
         nulo = nulo + nulo


print(f"votos Nerds 1: {nerds1}")
print(f"votos Nerds 2: {nerds2}")
print(f"votos Nerds 3: {nerds3}")
print(f"votos Nulo: {nulo}")
print(f"votos branco: {branco}")
if nerds1 >= 6:
    print("Nerds 1 venceram!")
if nerds1 == nerds2 or nerds1 == nerds3:
    print("Segundo turno!")
if nerds2 >= 6:
    print("Nerds 2 venceram!")
if nerds2 == nerds1 or nerds2 == nerds3:
    print("Segundo turno!")
if nerds3 >= 6:
    print("Nerds 3 venceram!")
if nerds3 == nerds1 or nerds3 == nerds2:
    print("Segundo turno!")