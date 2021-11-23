# Este módulo pertence ao pacote 'utilidades'
# e é utilizado para permitir acesso a
# determinados recursos somente pelo
# administrador e desenvolvedor do programa.

from time import sleep


def login():
    """Função que realiza o login
    do administrador, ou permanece
    o usuário como comum."""
    var = 0
    while True:
        print("Lista de opções:\n")
        print("1- login como administrador;")
        print("2- permanecer como usuário comum.\n")
        opc = int(input("Digite sua opção e tecle enter: "))
        if opc == 1:
            usu = str(input("Digite seu nome de usuário: "))
            sen = str(input("Digite sua senha: "))
            #Aqui, devem ser definidos o usuario e a senha desejados:
            if usu == 'usuario' and sen == 'senha':
                var = 1
                print("\nBem vindo, usuario. Aguarde 4 segundos.\n")
                sleep(4)
                break
            else:
                print("\nUsuário e/ou senha errados. Você continuará como usuário comum. Aguarde 4 segundos.\n")
                sleep(4)
                break
        elif opc == 2:
            print("\nVocê permanece como usuário comum. Aguarde 4 segundos.\n")
            sleep(4)
            break
        else:
            print("\nEntrada inválida. Tente novamente após 4 segundos de espera!\n")
            sleep(4)
    return var


def verifica_login(func):
    """Função que verifica
    o login do usuário."""
    def verifica(*args):
        if login() == 1:
            func(*args)
        else:
            print("Acesso negado para usuário comum!")
    return verifica
