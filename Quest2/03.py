#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite o nome: ')
idade = int(input('Digite a Idade: '))
salario = int(input('Digite o Salario: '))
ecivil = str(input('Digite seu estado civil: '))

if len(nome) > 3:
    print(f'\n\nO nome {nome} possi mais que 3 caracteres')
if idade >= 0 and idade <= 150:
    print(f' A idade {idade} Está entre 0 e 150')
if salario > 0:
    print(f'O Salario {salario} é maior que 0')
if ecivil == 's' or 'c' or 'v' or 'd':
    print(f'Estado Civil: {ecivil}')
