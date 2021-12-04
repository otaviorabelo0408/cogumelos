import utilidades.funcoes as utl
import utilidades.plotagem as plt
print("Algoritmo KNN para classificação de cogumelos.\n")
print("A primeira linha de inserção deve conter o número de k-vizinhos que serão considerados;")
print("A segunda linha de inserção deve conter os números de casos de treinamento e de teste, separados por um espaço;")
print("A partir daí, devem der inseridos os 22 atributos de cada um dos cogumelos de treinamento;")
print("Depois, são inseridos os rótulos dos cogumelos de treinamento, sendo 'p' para venenoso e 'e' para comestível;")
print("Por fim, são inseridos os 22 atributos de cada um dos cogumelos de teste;\n")
print("Os atributos devem ser inseridos de acordo como descrito no site:\n")
print("https://www.kaggle.com/uciml/mushroom-classification\n")
print("De tal forma, segue-se o algoritmo:\n")
print("Digite as informações solicitadas, de acordo como apresentado no início do programa:\n")
# Declração da lista auxiliar para plotagem final do gráfico:
lista_plotagem = list()
# Tupla com os dicionários referentes a cada uma das 22 características dos cogumelos:
dicionarios = ({'b': 0, 'c': 1, 'x': 2, 'f': 3, 'k': 4, 's': 5}, {'f': 0, 'g': 1, 'y': 2, 's': 3},
               {'n': 0, 'b': 1, 'c': 2, 'g': 3, 'r': 4, 'p': 5, 'u': 6, 'e': 7, 'w': 8, 'y': 9},
               {'t': 0, 'f': 1}, {'a': 0, 'l': 1, 'c': 2, 'y': 3, 'f': 4, 'm': 5, 'n': 6, 'p': 7, 's': 8},
               {'a': 0, 'd': 1, 'f': 2, 'n': 3}, {'c': 0, 'w': 1, 'd': 2}, {'b': 0, 'n': 1},
               {'k': 0, 'n': 1, 'b': 2, 'h': 3, 'g': 4, 'r': 5, 'o': 6, 'p': 7, 'u': 8, 'e': 9, 'w': 10, 'y': 11},
               {'e': 0, 't': 1}, {'b': 0, 'c': 1, 'u': 2, 'e': 3, 'z': 4, 'r': 5, '?': 6},
               {'f': 0, 'y': 1, 'k': 2, 's': 3}, {'f': 0, 'y': 1, 'k': 2, 's': 3},
               {'n': 0, 'b': 1, 'c': 2, 'g': 3, 'o': 4, 'p': 5, 'e': 6, 'w': 7, 'y': 8},
               {'n': 0, 'b': 1, 'c': 2, 'g': 3, 'o': 4, 'p': 5, 'e': 6, 'w': 7, 'y': 8}, {'p': 0, 'u': 1},
               {'n': 0, 'o': 1, 'w': 2, 'y': 3}, {'n': 0, 'o': 1, 't': 2},
               {'c': 0, 'e': 1, 'f': 2, 'l': 3, 'n': 4, 'p': 5, 's': 6, 'z': 7},
               {'k': 0, 'n': 1, 'b': 2, 'h': 3, 'r': 4, 'o': 5, 'u': 6, 'w': 7, 'y': 8},
               {'a': 0, 'c': 1, 'n': 2, 's': 3, 'v': 4, 'y': 5},
               {'g': 0, 'l': 1, 'm': 2, 'p': 3, 'u': 4, 'w': 5, 'd': 6})
# Entrada e verificação do número de k-vizinhos considerados para a análise:
while True:
    try:
        k_viz = int(input())
        break
    except ValueError:
        print("Entrada inválida para o número de k-vizinhos. Tente novamente!")
# Entrada e verificação do número de casos de treinamento e de testes:
while True:
    try:
        n_train, n_test = input().split()
        n_train = int(n_train)
        n_test = int(n_test)
        break
    except ValueError:
        print("Entrada inválida para o número de casos de treinamento e de teste. Tente novamente!")
# Entrada e verificação das 22 características de cada um dos cogumelos de treinamento:
while True:
    try:
        lista_train = utl.recebe_e_converte_carac(n_train, dicionarios)
        break
    except IndexError:
        print("Você digitou um número inválido de características para um ou mais cogumelos. Comece de novo!")
    except KeyError:
        print("Você digitou alguma característica de um ou mais cogumelos de maneira inválida. Comece de novo!")
# Entrada dos rótulos dos cogumelos já catalogados. Nesse caso, a verificação ocorre dentro da própria função:
lista_rotulos = utl.recebe_rotulo(n_train)
# Entrada e verificação das 22 características de cada um dos cogumelos que serão testados:
while True:
    try:
        lista_test = utl.recebe_e_converte_carac(n_test, dicionarios)
        break
    except IndexError:
        print("Você digitou um número inválido de características para um ou mais cogumelos. Comece de novo!")
    except KeyError:
        print("Você digitou alguma característica de um ou mais cogumelos de maneira inválida. Comece de novo!")
lista_medias = utl.calcula_media(lista_train)
lista_desvios = utl.calcula_desvio(lista_train, lista_medias)
utl.normaliza_dados(lista_train, lista_medias, lista_desvios)
utl.normaliza_dados(lista_test, lista_medias, lista_desvios)
utl.calcula_resultado(lista_train, lista_test, lista_rotulos, k_viz, lista_plotagem)
while True:
    try:
        print("\nLista de opções finais:\n")
        print("1- Plotar um gráfico com a porcentagem de cogumelos comestíveis e venenosos;")
        print("2- Encerrar o algoritmo.\n")
        opc = int(input("Digite sua opção: "))
        if opc == 1:
            plt.pizza(lista_plotagem)
            break
        elif opc == 2:
            break
        else:
            print("Opção inválida. Tente novamente!")
    except ValueError:
        print("Entrada inválida. Tente novamente!")
