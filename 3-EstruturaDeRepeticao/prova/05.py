ano = float(input('Digite o ano: '))

for i in range(2020, 2080):
    if ((ano % 4) == 0 and (ano % 100) != 0) or (ano % 400) == 0:
        print('O ano é Bissexto')
        bi += 1
    else:
        print('O ano não é Bissexto')

dia = int(input(f"Digite o dia do seu nacimento: : "))
mes = int(input(f"Digite o mês do seu nacimento: : "))
ano = int((input(f"Digite o ano do seu nacimento: : "))
mes = mes * 30
ano = ano * 365
tudo = mes + dia + ano

print(f"Seu total de dias em via é {tudo}")

print(f"quantidades de anos bixestos:{bi} ")
