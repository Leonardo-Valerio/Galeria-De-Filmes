from biblioteca.funções import *
from biblioteca.arq_fuctions import *
arquivo = 'filmes.txt'
if arquivoExiste(arquivo) == True:
    print('arquivo existe')
else:
    print('arquivo nao exite')
    criar(arquivo)
cabecalho('Biblioteca de Filmes')
while True:
    resp = menu(['Adicionar Filme', 'Listar Filmes','Buscar Filme por Gênero', 'Editar Avaliação','Sair'])
    if resp == 1:
        cabecalho('Adicionar Filme')
        filme = input('Digite o filme que deseja adicionar: ').upper()
        genero = input('Digite o genero desse filme: ').upper()
        avaliacao = lerInteiro('Digite a avaliação de estrelas dele: ')
        adicionar(arquivo, filme, genero, avaliacao)
    elif resp == 2:
        cabecalho('Listar Filmes')
        exibir(arquivo)
    elif resp == 3:
        cabecalho('Buscar Filme por Gênero')
        gen = input('digite o genero que deseja filtrar: ').upper()
        buscar(arquivo,gen)
    elif resp == 4:
        cabecalho('Editar Avaliação')
        identificar = input('Digite o nome do filme que deseja editar a avaliação: ').upper()
        novo = lerInteiro('Digite a nova avaliação entre 0 e 5: ')
        editar(arquivo, identificar, novo)
    elif resp == 5:
        cabecalho('Sair')
        break
    else:
        cabecalho('Erro, digite um número dentro das opções do menu!')