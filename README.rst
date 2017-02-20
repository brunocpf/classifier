TP3 - Mini Pokédex
=============================
:Disciplina: Introdução à Computação Visual - 2016/2 - Universidade Federal de Minas Gerais
:Autor: Bruno Cesar Pimenta Fernandes <brunocpf@dcc.ufmg.br>

Scripts Python para um classificador de imagens simples, usando o algoritmo *k-nearest neighbors* (k-NN). De acordo com a especificação, funciona como uma "Mini Pokédex". A ferramenta receberá uma imagem de entrada e encontrará a espécie de Pokémon mais parecida no dataset, e então abrirá a página correspondente em http://www.pokemon.com/br/pokedex/ no navegador web. Além dos Pokémon incluidos no dataset original (Bulbasaur, Charmander, Pikachu e Squirtle) foram adicionados Eevee e Snorlax. A ferramenta foi escrita de forma que mais espécies possam ser adicionadas ao dataset. A interface da ferramenta é uma aplicação desktop feita com a biblioteca Tkinter.
Para utilizar a ferramenta, execute o script ``gui.py``.

Estes scripts foram desenvolvidos com a ajuda do script de exemplo ``/samples/digits.py`` do OpenCV.

Estes scripts foram desenvolvidos com Python 2.7 e OpenCV 3.1.0.

Extração de características e treinamento
------------------------------------------
Cada subdiretório do dataset (diretório ``images``) é uma espécie de Pokémon, e deve conter imagens do Pokémon correspondente. Para usar o algoritmo de algoritmo de *5-fold cross-validation* (discutido na próxima seção) o total de imagens do dataset deve ser divisível por 5.

O algoritmo de extração de característica escolhido foi o histograma de cores (HSV) normalizado, pois é simples de ser implementado e tem uma acurácia razoável para estes tipos de imagem.

A função ``get_data()`` do módulo ``train`` analizará as imagens do dataset, retornando uma lista de histogramas e uma de labels, que são números inteiros correspondentes aos Pokémon no dataset (em ordem alfabética).

O script ``generatedata.py`` monta o dataset. Ele usa a função ``get_data()`` do módulo ``train`` para gerar o arquivo ``data.npy`` que contém uma *array numpy* com os histogramas e os labels correspondentes, que serão usados pelo classificador de padrões. Note que para o objetivo de testes, o dataset é randomizado.

O arquivo ``data.npy`` será carregado pela ferramenta para treinar o classificador de características. No caso, como dito anteriormente, foi escolhido o classificador *k-nearest neighbors* (k-NN), que faz parte do OpenCV, e é simples e rápido. Note que foi escolhido k = 6. Ao clicar no botão "Identificar Pokémon", a ferramenta carrega a imagem de entrada e calcula seu histograma. Então, o classificador é trainado com o dataset. Logo em seguida, o classificador prediz o label correspondente à classe de histogramas (que correspondem às espécies de Pokémon) mais próxima, e retorna o nome da espécie de Pokémon, que é concatenado à url da Pokédex para abrir a página no navegador web.

Para traduzir labels em nomes de Pokémon, foi criado o dicionário Python ``POKEDEX_LABELS`` no módulo ``pokedex``. Ele deve ser atualizado se o dataset for modificado (sempre em ordem alfabética).

Avaliação
------------------------------------------
O *5-fold cross-validation* foi implementado no script ``validation.py``. Ele divide os histogramas e labels em 5 listas com um número igual de elementos cada, ordenadas aleatoriamente (mantendo a correspondência de labels), e itera sobre estas listas de modo que uma delas é usada como a bateria de testes e o resto como a entrada para treinamento do classificador a cada *fold* (iteração). O script calcula a acurácia média, o desvio padrão e a matriz de confusão em cada *fold*.

O arquivo ``verification.txt`` possui a saída da execução deste script.
