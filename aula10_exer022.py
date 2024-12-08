# ## Exercícios com funções:

# ***1*** 

# ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***

def comparacao():

     n1 = int(input('Digite um número: '))
     n2 = int(input('Digite outro número: '))

     if n1 % 2 == 0 and n2 % 2 == 0:
         print('São pares')

     elif n1 % 2 == 0 or n2 % 2 == 0:
         print('Um dos números é par')
     else:
         print('São impares')

comparacao()

# ***2***

# ***CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***

def multiplicacao():
     n1 = int(input('Digite o primeiro número: '))
     n2 = int(input('Digite o segundo número: '))
     n3 = int(input('Digite o terceiro número: '))

     resultado = n1 * n2 * n3

     print('Esse é o resultado: ', resultado)

multiplicacao()


# # ***3***

# # ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***

def potencia():
     n1 = int(input('Digite um número: '))
     resultado = n1 ** 2
     print(resultado)
potencia()

# ***4***

# ***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS***

def cumprimento():
     idade = int(input('Digite sua idade: '))
     if idade >= 18:
         print('Bem vindo')
     else:
         print('Volte daqui a alguns anos')

cumprimento()


# ***5***

# ***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***

def idad():
     ano_nascim = int(input('Digite o seu ano de nascimento: '))
     idade = 2024 - ano_nascim
     print(f'Você tem {idade} anos')
idad()

# ***6***

# ***DESENVOLVA UM AFUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999***

def verificar ():
     copa_pedido = 1999
     copa1 = 1958
     copa2 = 1962
     copa3 = 1970
     copa4 = 1994
     copa5 = 2002
     if copa_pedido == copa1 or copa_pedido == copa2 or copa_pedido == copa3 or copa_pedido == copa4 or copa_pedido == copa5:
         print('Ganhou')
     else:
        print('Não ganhou!')
verificar()
# ***7*** 

# ***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***


print('*****BEM VINDO AO RESTAURANTE DO ALLU*****')

def restaurante():
    pedido = input('Qual será o seu pedido?: '
                '\n1 - Salada'
                '\n2 - Macarronada'
                '\n3 - Sanduiche'
                '\n4 - Sorvete'
                '\nEscolha: ')
    
    print('******************************************')
    if pedido == '1':
        print('Você escolheu Salada'
              '\nPreço: R$', 41.5)       
        print('******************************************')
    elif pedido == '2':
        print('Você escolheu Macarronada'
              '\nPreço: R$', 65.5)      
        print('******************************************')
    elif pedido == '3':
        print('Você escolheu Sanduiche'
              '\nPreço: R$', 27.5)      
        print('******************************************')
    elif pedido == '4':
        print('Você escolheu Sorvete'
              '\nPreço: R$', 20.5)       
        print('******************************************')
    else:
        print('Opção inválida')

restaurante()

