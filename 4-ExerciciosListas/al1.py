palavras = ('mundo', 'caixa', 'bola')

for c in palavras:
    print(f'\n na palavra {c} temos:', end=' ')
    for letra in c:
        if letra in 'aeiou':
            print(f'{letra}', end= ' ')