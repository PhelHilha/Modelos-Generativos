Projeto:
Modelos generativos em Engenharia Biomédica: investigação e aplicações

Orientadores: Frederico Caetano Jandre de Assis Tavares / Gabriel Casulari da Motta Ribeiro

Financiamentos: Bolsa PIBIC/UFRJ; Bolsa PQ-CNPq

Autoria : Raphael Henrique da Silva Pereira

Instruções do programa
----------------------------------------------
Corpo do texto : CORPUS.TXT

Funções do programa:

ngrams(text,n) # Função responsável em criar os n-grams com base no texto.
->text = Corpo do texto que será lido
->n = tamanho do n-gram

matriz_markov(ngram) # Função responsavel em criar a matriz de markov associada aos n-grams.
->ngram = lista de tokens contendo os n-grams

prob_matriz(matriz_markov) # Função responsável por transformar os tokens da matriz de Markov em probabilidades
->matriz_markov = dicionário contendo ngrams com proximos caracteres e seu nº de ocorrências.

gerador_texto(matriz,start,n,tam) # Funçao responsável por gerar os textos com base nos n-grams        
->matriz = dicionário contendo ngrams com proximos caracteres e sua probabilidade de ocorrências.
->start = n-gram inicial do texto.
->n = tamanho do n-gram.
->tam = tamanho máximo do texto gerado.

main(n,tam) #Função main responsável pelo uso total do modelo.
->n = tamanho do n-gram
->tam = tamanho máximo do texto gerado.
----------------------------------------------
