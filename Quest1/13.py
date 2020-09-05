altura = float (input('Digite sua Altura: '))
s = int (input('Digite 1 para Homem e 2 para Mulher: '))
if s == 1:
    print('Seu peso ideal é: {:.2f}'.format(72.7 * altura - 52))
else:
    print('Seu peso ideal é: {:.2f}'.format(62.1 * altura - 44.7))