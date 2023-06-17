import random
import time
import sys
import re
import string

# -*- coding: utf-8 -*-

sys.stdout.reconfigure(encoding='utf-8')

def imprimir_caixa(largura, altura):
    for i in range(altura):
        for j in range(largura):
            if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def carregar_perguntas_respostas(arquivo):
    perguntas_respostas = []
    with open(arquivo, 'r', encoding='utf-8') as file:
        for linha in file:
            try:
                pergunta, resposta = re.split(r'\s*::\s*', linha.strip())
                perguntas_respostas.append((pergunta, resposta))
            except ValueError:
                print(f"Erro de formatação na linha: {linha}")

    return perguntas_respostas


def encontrar_pergunta_similar(pergunta, perguntas_respostas):
    pergunta_formatada = pergunta.lower().translate(str.maketrans('', '', string.punctuation))
    melhor_pergunta_similar = None
    melhor_pontuacao = 0
    for pergunta_existente in perguntas_respostas:
        pergunta_existente_formatada = pergunta_existente[0].lower().translate(str.maketrans('', '', string.punctuation))
        pontuacao = sum([1 for palavra in pergunta_formatada.split() if palavra in pergunta_existente_formatada])
        if pontuacao > melhor_pontuacao:
            melhor_pergunta_similar = pergunta_existente
            melhor_pontuacao = pontuacao
    return melhor_pergunta_similar

def digitar_texto(texto):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(0.05)  # Pausa de 0.05 segundos entre cada caractere
    print()

def chatbot():
    arquivo_perguntas_respostas = 'generic_answers.txt'
    perguntas_respostas = carregar_perguntas_respostas(arquivo_perguntas_respostas)

    while True:
        pergunta = input('Faça sua pergunta (ou digite "sair" para encerrar): ')
        if pergunta.lower() == 'sair':
            break

        pergunta_similar = encontrar_pergunta_similar(pergunta, perguntas_respostas)
        if pergunta_similar:
            digitar_texto(pergunta_similar[1])
        else:
            digitar_texto('Desculpe, não encontrei uma resposta para essa pergunta.')

imprimir_caixa(10, 6)
chatbot()