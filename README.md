# cogumelos
Este projeto consiste em um algoritmo do tipo KNN para classificação de cogumelos em comestíveis ou venenosos.
A primeira linha de entrada de dados consiste em um número inteiro, representando o número de "vizinhos próximos" (número de cogumelos já catalogados considerado para a classificação do cogumelo que ainda deve ser catalogado de acordo com a menor distância entre seus atributos). A segunda linha é composta por dois números inteiros, sendo o primeiro representando o número de cogumelos já catalogados 'n', e o segundo o número de cogumelos a serem catalogados 'm'. A partir de então, as linhas seguem o seguinte formato: 'n' linhas com 22 atributos cada, representando cada um dos 'n' cogumelos já classificados, 'n' linhas com os respectivos rótulos ('p' para venenoso e 'e' para comestível) na mesma ordem de inserção dos atributos de cada cogumelo, e por fim, 'm' linhas com os cogumelos a serem catalogados de acordo com as menores distâncias consideradas entre estes e os já classificados.
Ao fim do algoritmo, é impresso um gráfico com as porcentagens de cogumelos classificados como comestíveis ou venenosos.
