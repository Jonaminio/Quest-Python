#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = 11
while nota >= 11:
    nota = float(input('Digite Uma Nota entre 0 e 10: '))
if nota < 11:
    print('Obg')
