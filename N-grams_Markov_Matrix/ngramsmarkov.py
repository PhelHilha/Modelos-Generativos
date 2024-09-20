import random
from collections import defaultdict

# Lê o texto CORPUS.TXT e transforma em string
with open("CORPUS.TXT", "r", encoding='utf-8') as f:
    corpus = f.read()

#O código será dividido em diversas funções para manter sua transparência.

# Função responsável em criar os n-grams com base no texto.
def ngrams(text,n):
    tokens = []
    for i in range(len(text) - n + 1):
        n_gram = tuple(text[i:i + n])
        tokens.append(n_gram)
    return tokens

#Função responsavel em criar a matriz de markov associada aos n-grams.
def matriz_markov(ngram):
    matriz = defaultdict((lambda: defaultdict(int)))
    for i in range(len(ngram) - 1):
        ngram_atual = ngram[i]
        ngram_prox = ngram[i + 1][-1]
        matriz[ngram_atual][ngram_prox] += 1
    return matriz

#Função responsável por transformar os tokens da matriz de Markov em probabilidades
def prob_matriz(matriz_markov):
    probabilidades = defaultdict(dict)
    for ngram_atual, ngram_prox in matriz_markov.items():
        prox_total = sum(ngram_prox.values())
        for char,count in ngram_prox.items():
            probabilidades[ngram_atual][char] = count / prox_total
    return probabilidades

#Função responsável por gerar os textos com base nos n-grams        
def gerador_texto(matriz, start, n , tam):
    ngram_atual = start
    texto = list(ngram_atual)
    
    for i in range(tam - n):
        if ngram_atual in matriz:
            prox_char = random.choices(list(matriz[ngram_atual].keys()),
                                       list(matriz[ngram_atual].values()))[0]
            texto.append(prox_char)
            ngram_atual = tuple(texto[-n:])
    return ''.join(texto)

#Função main responsável pelo uso total do modelo.
def main(n,tam = 300):
    n_grams = ngrams(corpus, n)
    
    while True:
        start_ngram = random.choice(n_grams)
        if start_ngram[0] != ' ' and start_ngram[0] != '\n':
            break
    matriz = matriz_markov(n_grams)
    
    matriz_probabilidades = prob_matriz(matriz)
    
    texto = gerador_texto(matriz_probabilidades, start_ngram, n,tam)
    print(texto)



