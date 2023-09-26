from ..funções import *

def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        return False
    else:
        return True
def criar(arquivo):
    try:
        a = open(arquivo, 'wt+')
    except:
        print('erro ao criar arquivo')
    else:
        print('arquivo criado com sucesso')
        a.close()

def exibir(arquivo):
    try:
        a = open(arquivo, 'r')
    except:
        print('erro ao exibir arquivo')
    else:
        for l in a:
            dado = l.split(';')
            print(f'Filme: {dado[0]}/ Gênero: {dado[1]}/ Avaliação: {dado[2]}')
        a.close()
        linha()
def adicionar(arquivo, filme, genero, avaliacao):
    try:
        a= open(arquivo, 'at')
    except:
        print('erro ao adicionar')
    else:
        a.write(f'{filme};{genero};{avaliacao}\n')

def buscar(arquivo,gen):
    try:
        a = open(arquivo, 'r')
    except:
        print('erro ao exibir arquivo')
    else:
        for l in a:
            dado = l.split(';')
            if dado[1] == gen:
                print(f'Filme: {dado[0]}/ Gênero: {dado[1]}/ Avaliação: {dado[2]}')
        a.close()
        linha()
def editar(arquivo, identificar, novo_avaliacao):
    try:
        # Lendo o arquivo
        a = open(arquivo, 'r')
        linhas = a.readlines()
        a.close()

        # Reabrindo o arquivo para escrita
        a = open(arquivo, 'w')
        for linha in linhas:
            filme, genero, avaliacao = linha.strip().split(';')
            if filme == identificar:
                avaliacao = str(novo_avaliacao)  # Alterando a avaliação
                print('Avaliação editada com sucesso!')
            a.write(f'{filme};{genero};{avaliacao}\n')
        a.close()
    except:
        print('Erro ao editar a avaliação.')


