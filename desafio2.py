# Desafio 2:  Condicionais***
# Sistema de Reservas de Hotel:***
# Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.
# Cadastro de Cliente:*
# O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*
# Reservas de Quartos:*
# O sistema deve oferecer 3 tipos de quartos:*** 
# "Simples", "Duplo" e "Luxo".***
# Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***
# Cálculo da Estadia:***
# O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***
# Exemplo: 
# valor_cliente3 = preco_duplo * cliente3_dias***
# Pagamento:*
# O sistema deve exibir o valor total a ser pago por cada cliente após a aplicação do desconto.*

cliente = {}
cliente2 = {}
cliente3 = {}
usuario = {}

print('*******************BEM VINDO AO CADASTRO************************')

usuario['login'] = input('Nome de usuário: ')
usuario['senha'] = input('Senha: ')

print('*************************')

print('Para proseseguir, informe usuario e senha')

login = input('Nome de usuário: ')
senha = input('Senha: ')

if login == usuario['login'] and senha == usuario['senha']:

    print('*******************BEM VINDO AO HOTEL ALLU************************')

    cliente['nome'] = input('Digite o nome completo do primeiro hóspede: ')
    cliente['idade'] = int(input('Digite sua idade: '))

    print('******************************************')

    cliente2['nome'] = input('Digite o nome completo do segundo hóspede: ')
    cliente2['idade'] = int(input('Digite sua idade: '))

    print('******************************************')

    cliente3['nome'] = input('Digite o nome completo do terceiro hóspede: ')
    cliente3['idade'] = int(input('Digite sua idade: '))

    print('******************************************')

    tipo_quarto = ['Simples', 'Duplo', 'Luxo']
    precos_diarias = [100.00, 150.00, 250.00]

    valor_total_cliente1 = 0.00
    valor_total_cliente2 = 0.00
    valor_total_cliente3 = 0.00

    tipo_quarto_cliente1 = input(f"\n{cliente['nome']}, escolha o tipo de quarto (Simples, Duplo, Luxo): ").lower()
    dias_cliente1 = int(input(f"Quantos dias você ficará no hotel, {cliente['nome']}?: "))

    if tipo_quarto_cliente1 == "simples":
        valor_total_cliente1 = precos_diarias[0] * dias_cliente1
    elif tipo_quarto_cliente1 == "duplo":
        valor_total_cliente1 = precos_diarias[1] * dias_cliente1
    elif tipo_quarto_cliente1 == "luxo":
        valor_total_cliente1 = precos_diarias[2] * dias_cliente1

    tipo_quarto_cliente2 = input(f"\n{cliente2['nome']}, escolha o tipo de quarto (Simples, Duplo, Luxo): ").lower()
    dias_cliente2 = int(input(f"Quantos dias você ficará no hotel, {cliente2['nome']}?: "))

    if tipo_quarto_cliente2 == "simples":
        valor_total_cliente2 = precos_diarias[0] * dias_cliente2
    elif tipo_quarto_cliente2 == "duplo":
        valor_total_cliente2 = precos_diarias[1] * dias_cliente2
    elif tipo_quarto_cliente2 == "luxo":
        valor_total_cliente2 = precos_diarias[2] * dias_cliente2

    tipo_quarto_cliente3 = input(f"\n{cliente3['nome']}, escolha o tipo de quarto (Simples, Duplo, Luxo): ").lower()
    dias_cliente3 = int(input(f"Quantos dias você ficará no hotel, {cliente3['nome']}?: "))

    if tipo_quarto_cliente3 == "simples":
        valor_total_cliente3 = precos_diarias[0] * dias_cliente3
    elif tipo_quarto_cliente3 == "duplo":
        valor_total_cliente3 = precos_diarias[1] * dias_cliente3
    elif tipo_quarto_cliente3 == "luxo":
        valor_total_cliente3 = precos_diarias[2] * dias_cliente3

    print(f"\nCliente: {cliente['nome']}")
    print(f"Tipo de Quarto: {tipo_quarto_cliente1.capitalize()}")
    print(f"Dias de Estadia: {dias_cliente1}")
    print(f"Valor Total: R$ {valor_total_cliente1:.2f}")

    print(f"\nCliente: {cliente2['nome']}")
    print(f"Tipo de Quarto: {tipo_quarto_cliente2.capitalize()}")
    print(f"Dias de Estadia: {dias_cliente2}")
    print(f"Valor Total: R$ {valor_total_cliente2:.2f}")

    print(f"\nCliente: {cliente3['nome']}")
    print(f"Tipo de Quarto: {tipo_quarto_cliente3.capitalize()}")
    print(f"Dias de Estadia: {dias_cliente3}")
    print(f"Valor Total: R$ {valor_total_cliente3:.2f}")

else:
    print('Login invalido')