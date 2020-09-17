#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

phora = float(input('Digite o quanto vc recebe por hora: '))
nhora = float(input('Digite o numero de horas trabalhadas desse mês: '))
print('Total do Salario desse mês: {:.2f} R$'.format(phora*nhora))