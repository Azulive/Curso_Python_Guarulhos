# Criar 3 variáveis, notas, tipo float()***

# Mostre no console a média das 3 variáveis***

# Passou de ano?  -  media >= 7***

n1 = float(input('Digite a nota: '))
n2 = float(input('Digite a nota: '))
n3 = float(input('Digite a nota: '))

media = (n1 + n2 + n3) / 3
passou = media >= 7

print(f'Sua média foi de {media:.2f} {passou}')