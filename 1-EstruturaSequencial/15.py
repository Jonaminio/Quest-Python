#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo

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
