palavra = input("Digite um texto ")
qtd_palavra = len(palavra)
print(qtd_palavra)
cont = 0
while cont < qtd_palavra:
        print(f"A {cont+1}ª letra é {palavra[cont]}")
        cont+=1