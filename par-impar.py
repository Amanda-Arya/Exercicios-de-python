lista_par = []
lista_impar = []
qtd = int(input("Diga o número que delimitará sua lista: "))

for i in range (1,qtd):
    numero = i % 2
    if numero % 2 == 0:
        
        lista_par.append(i)
    else:
        lista_impar.append(i)    
        
print(lista_par)
print(lista_impar)
