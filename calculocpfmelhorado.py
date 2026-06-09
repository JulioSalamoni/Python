cpf_original = input("Digite o CPF apenas com números: ")

# Verifica se o CPF possui 11 dígitos
if len(cpf_original) != 11 or not cpf_original.isdigit():
    print("CPF inválido!")
else:
    cpf = cpf_original[:9]

    # Primeiro dígito verificador
    soma = 0
    peso = 10

    for numero in cpf:
        soma += int(numero) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        primeiro_digito = "0"
    else:
        primeiro_digito = str(11 - resto)

    cpf += primeiro_digito

    # Segundo dígito verificador
    soma = 0
    peso = 11

    for numero in cpf:
        soma += int(numero) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        segundo_digito = "0"
    else:
        segundo_digito = str(11 - resto)

    cpf += segundo_digito

    # Verificação final
    if cpf == cpf_original:
        print("CPF válido!")
    else:
        print("CPF inválido!")