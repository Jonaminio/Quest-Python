#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Teste 1 Raiz A = 1 / B =  -4 / C = 4 | r == 2
#Teste 2 Raizes A = 1 / B = -5 / C = 6 | r1 == 3 , r2 == 2

print('=' * 30)
print('Raízes ou zero da função do 2º Grau')
print('=' * 30)
a = float(input('Digite o A: '))
b = float(input('Digite o B: '))
c = float(input('Digite o C: '))

if a != 0:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('A equação não possui raizes reais')
    elif d == 0:
        r = (-b) / (2 * a)
        print(f'A equação possui apenas uma raiz real que é: {r}')
    elif d > 0:
        r1 = ((b * -1) + (d ** 0.5))/ (2 * a)
        r2 = ((b * -1) - (d ** 0.5))/ (2 * a)
        print(f'A equação possui duas raizes reais que são r1: {r1} e r2: {r2}')
else:
    print('A equação não é do segundo grau')