# Este módulo pertence ao pacote 'utilidades'
# e é utilizado para a plotagem dos gráficos
# requeridos pelo algoritmo.

from matplotlib.pyplot import (pie, legend, title, axis, show)
from utilidades.administracao import verifica_login


@verifica_login
def pizza(lista):
    """Função utilizada para plotar
    um gráfico com a distribuição dos
    cogumelos após a analise do
    algoritmo."""
    dicionario = {'Comestíveis': 0, 'Venenosos': 0}
    for rotulo in lista:
        if rotulo == 'e':
            dicionario['Comestíveis'] += 1
        else:
            dicionario['Venenosos'] += 1
    pie(dicionario.values(), labels=dicionario.keys(), autopct='%1.2f%%', startangle=90)
    legend(title='Legenda:', shadow=True, loc='best')
    title("Distribuição das classes dos cogumelos")
    axis("equal")
    show()
    return 0