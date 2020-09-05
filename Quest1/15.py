qhoras = float(input('Digite o quanto voce recebe por hora: '))
nhoras = int(input('Digite o numero de horas trabalhados do mês: '))
sbruto = qhoras * nhoras
sindicato = sbruto * 5 / 100
ir = sbruto * 11 / 100
inss = sbruto * 8 / 100
print('O Seu Salario Bruto é: {:.2f} R$'.format(sbruto))
print('Quanto pagou ao Imposto de renda: {:.2f} R$'.format(ir))
print('Quanto pagou ao Sindicato: {:.2f} R$'.format(sindicato))
print('Quanto pagou ao INSS: {:.2f} R$'.format(inss))
print('Salario Liquido: {:.2f} R$'.format(sbruto - ir - sindicato - inss))
