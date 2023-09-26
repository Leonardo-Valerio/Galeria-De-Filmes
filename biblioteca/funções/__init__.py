def linha():
    print('-' * 50)

def cabecalho(msg):
    linha()
    print(msg.center(50))
    linha()


def menu(menu):
    c = 1
    for i in menu:
        print(f'{c} - {i}')
        c +=1
    linha()
    opcao = lerInteiro('digite o número da opção deseijada: ')
    return opcao

def lerInteiro(num):
    while True:
        try:
            entrada = int(input(num))
        except:
            print('Digite um Número!')
        else:
            return entrada