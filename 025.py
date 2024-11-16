import random
import time


while True:

    pc = random.randint(1, 3)

    print('Bem vindo ao JOKEMPO em Python!!!')

    jogador = int(input('1 - Pedra'
                        '\n2 - Papel'
                        '\n3 - Tesoura'
                        '\n4 - Sair'
                        '\n--------------> '))
    if jogador == 4:
            print('Obrigado por jogar')

    print('JO')
    time.sleep(1)
    print('KEM')
    time.sleep(1)
    print('PO')
    time.sleep(1)
    print('Pensando...')
    time.sleep(2)

    print('*************************************')



    if jogador == pc:
        print('Empate')
    elif ((jogador == 1 and pc == 3) or
        (jogador == 2 and pc == 1) or
        (jogador == 3 and pc == 2)):
        print('Você Ganhou!!!')
    else:
        print('Você Perdeu!')
    break
print('*************************************')
