import string
import random


def GeraSenha():
    size = int(input('Digite a quantidade de caracteres: '))
    # inicializa duas listas com letras de A-Z
    a_to_z_lower = list(string.ascii_lowercase)  # a-z em caixa baixa
    a_to_z_upper = list(string.ascii_uppercase)  # A-Z em caixa alta
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    a_to_z_both = a_to_z_upper + a_to_z_lower + numbers  # criando lista com ambos para gerar senha
    password = []
    # Gerando a senha
    for letra in range(1, size + 1):
        rand = random.randrange(0, len(a_to_z_both))
        password += a_to_z_both[rand]

    # Se a primeira letra nao for maiúsuclo,é executado um loop até que a primeira letra seja maiúscula
    while password[0].isupper() == False:
        rand = random.randrange(0, len(a_to_z_both))
        password[0] = a_to_z_both[rand]

    # Exibindo a senha gerada
    for letra in password:
        print(letra, end='')


if __name__ == '__main__':
    GeraSenha()
