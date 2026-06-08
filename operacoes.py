n1 = input("Digite um número> ")
n2 = input("Digite outro número ")

# Para realizar as operações aritméticas, será
# necessário converter as variáveis n1 e n2 e em
# tipos numéricos, que podem ser: int ou float

n1 = int(n1)
n2 = int(n2)

soma = n1 + n2
subtrair = n1 - n2
multiplicar = n1 * n2
dividir = n1 / n2

print(f"a soma entre os números {n1} e {n2} é {soma}")
print(f"a subtração entre os números {n1} e {n2} é {subtrair}")
print(f"a multiplicação entre os números {n1} e {n2} é {multiplicar}")
print(f"a divisão entre os números {n1} e {n2} é {dividir}")

