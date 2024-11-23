# Exercícios: 

# UTILIZE VARIÁVEIS!!!!!! 


# Crie um sistema de cadastro com as estruturas que vc já conhece(Use apenas input, print e variavel)


print('**************************************')

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))
nome_rua = input('Digite o nome da sua rua: ')
email = input('Digite seu email: ')

nome_completo = nome + ' ' + sobrenome

print(f'Seu nome é {nome_completo}'
      f'\nVocê tem {idade} anos'
      f'\nVocê mora na rua {nome_rua}'
      f'\nSeu e-mail cadastrado é: {email}')