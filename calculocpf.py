# Pedir ao usuário a entrada dos números do cpf e guarda na variável 
# cpf_original. Aqui o usuário digitará o cpf completo

cpf_original = input("Digite o seu cpf apenas com números: ")
# a variável i ajuda a contar os números do cpf no laço while
i = 0
# a variável cpf_9 irá guardar os 9 primeiros digitos do CPF
cpf_9 = ""

# aqui o cpf9 está pegando cada posição do cpf original digitado pelo usuário
# de 0 a 8 (considerando que o 0 é a primeira posição, utilizando a variável i como referencia de posição) 
# e vai adicionando esses numeros um ao lado do outro na variável cpf_9
# que resultará nas 9 primeiras posições
# podemos considerar que nesse momento os numeros sao uma string
while i < 9:
    cpf_9+=cpf_original[i]
    i+=1

 
# devemos trazer o i de volta para 0 e criar as variáveis para o peso e o resultado
# aqui o resultado vai ser o digito na posição da referencia do "i" da variável cpf_9 multiplicado pelo peso (que vai de 10 a 2)
# precisaremos mudar a variável cpf_9 para int, pois no momento ela estava como uma string, e não seria possível fazer a conta

i = 0
peso = 10
resultado = 0
while i < 9:
    resultado += int(cpf_9[i]) * peso
# precisaremos aumentar a posição do i para mudar a referencia de posição no grupo e diminuir o peso
# utilizando a forma de calcular cpf como base (peso indo de 10..9..8 a 2) 
    peso -= 1
    i += 1

# aqui criaremos a variável resto, que é o resto da divisão do resultado dividido por 11
# se o resultado for menor que 2, o digito se torna 0 (pela regra), entre aspas pois será uma string
# que será adicionada na string cpf 9, caso não seja menor que 2, vai fazer a regra de 11 subtraido pelo resto,
# e precisamos transformar o resultado dessa conta em string para ser adicionada a string cpf_9
resto = resultado % 11
if resto < 2:
    cpf_9 += "0"
else:
    cpf_9 += str(11-resto)


# para pegar o segundo digito verificador, faremos o exato mesmo processo, porém com alguns ajustes
# o peso agora será 11 pois tem um numero a mais pela regra e a variável i temos que aumentar mais um, pois tem mais uma posição.
i = 0
peso = 11
resultado = 0
while i < 10:
    resultado += int(cpf_9[i]) * peso
    peso -= 1
    i += 1

resto = resultado % 11
if resto < 2:
    cpf_9 += "0"
else:
    cpf_9 += str(11-resto)

if cpf_9 == cpf_original:
    print("CPF Válido")
else:
    print("CPF Inválido")
