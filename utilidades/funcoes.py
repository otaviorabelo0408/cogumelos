# Este módulo pertence ao pacote 'utilidades'
# e contém as funções que serão utilizadas
# ao longo da execução do algoritmo para
# a recepção dos dados e classificação
# dos cogumelos.

from math import sqrt


def recebe_e_converte_carac(quantidade, tupla):
    """Essa função recebe as características
    de cada um dos cogumelos e as converte de
    acordo com seu 'peso' determinado na tupla
    com os dicionários referentes a cada uma
    dessas características."""
    aux = list()
    cont = 0
    while cont < quantidade:
        aux += [input().split()]
        cont += 1
    for i in range(quantidade):
        for j in range(22):
            aux[i][j] = tupla[j][aux[i][j]]
    return aux


def recebe_rotulo(quantidade):
    """Essa função recebe os rótulos dos
    cogumelos já catalogados e os armazena
    em uma lista."""
    aux = list()
    cont = 0
    while cont < quantidade:
        entrada = str(input())
        if entrada == 'p' or entrada == 'e':
            aux += entrada
            cont += 1
        else:
            print("Entrada inválida. Essa entrada deve ser de apenas um rótulo por linha, sendo:")
            print("Letra 'e' para comestível;")
            print("Letra 'p' para venenoso.")
            print("Tente novamente!")
    return aux


def calcula_media(lista):
    """Essa função calcula a média dos
    22 atributos de cada cogumelo, com
    base na conversão dos parâmetros já
    realizada de acordo com a tupla de
    dicionários."""
    aux = list()
    cont = 0
    for j in range(22):
        for i in range(len(lista)):
            cont += lista[i][j]
        aux += [cont / len(lista)]
        cont = 0
    return aux


def calcula_desvio(lista, medias):
    """Essa função calcula o desvio
    padrão de cada atributo de cada
    cogumelo com base na média já
    calculada previamente para
    cada um desses atributos."""
    aux = list()
    cont = 0
    for j in range(22):
        for i in range(len(lista)):
            cont += (lista[i][j] - medias[j]) ** 2
        aux += [sqrt(cont / len(lista))]
        cont = 0
    return aux


def normaliza_dados(lista, medias, desvios):
    """Essa função normaliza os
    dados de cada atributo com
    base nas medias e nos desvios
    padrões já calculados para
    cada atributo listado."""
    for j in range(22):
        for i in range(len(lista)):
            if desvios[j] == 0:
                lista[i][j] = 0
            else:
                lista[i][j] = (lista[i][j] - medias[j]) / desvios[j]
    return 0


def calcula_resultado(lista_treinamento, lista_teste, rotulo, fim, plotar):
    """Essa função calcula as distâncias
    de cada atributo para sua média já
    calculada previamente. Depois, determina
    as menores distâncias com base no número de
    k-vizinhos e por fim classifica cada cogumelo
    individualmente como comestível ou venenoso."""
    aux = list()
    ven = 0
    com = 0
    resultado = list()
    cont = 0
    for i in range(len(lista_teste)):
        for j in range(len(lista_treinamento)):
            for k in range(22):
                cont += (lista_teste[i][k] - lista_treinamento[j][k]) ** 2
            aux += [sqrt(cont)]
            cont = 0
        menores_distancias = sorted(range(len(aux)), key=lambda var: aux[var])[:fim]
        for res in menores_distancias:
            resultado += rotulo[res]
        for end in resultado:
            if end == 'p':
                ven += 1
            else:
                com += 1
        if ven > com:
            plotar += 'p'
            print('p')
        else:
            plotar += 'e'
            print('e')
        aux.clear()
        menores_distancias.clear()
        resultado.clear()
        ven = 0
        com = 0
    return 0