import datetime
from datetime import date

nome = str(input('Digite seu nome: '))
tvacina = str(input('digite o tipo de vacina que deseja tomar, Pfizer ou Astrazeneca: '))
print('digite a data que esta tomando a primeira dose em ano/mês/dias: ')

year = int(input('Digite o ano: '))
month = int(input('Digite o mês: '))
day = int(input('Digite o dia: '))

date1 = datetime.date(year, month, day)

print(date1)

x = date1.strftime('%d/%m/%Y')
print(x)

if(tvacina == "pfizer"):
    futuro = date.fromordinal(date1.toordinal()+21)
else:
    futuro = date.fromordinal(date1.toordinal() + 28)

y = futuro.strftime('%d/%m/%Y')

print(f'Prezado(a) Sr(a): {nome},você tomou a vacina PFIZER, no dia {x} Sua segunda dose deverá ocorrer dia {y} ,Não se esqueça!')

