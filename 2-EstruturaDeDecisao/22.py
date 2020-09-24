#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).


numero = int(input("Digite o numero a verificar: "))

c = numero % 2

if c == 0:
    print("o Numero é par!")
else:
    print("o numero é Impar!")