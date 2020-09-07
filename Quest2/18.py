d = int (input('Digite o dia: '))

if d <= 31:
    m = int (input('Digite o mês: '))
    if m <= 12:
        a = int (input('Digite o ano: '))
        if len(a) == 4:
            print(f'A data {d}/{m}/{a} é valida')
else:
    print('Não é Valida')
