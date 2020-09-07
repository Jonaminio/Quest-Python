l1 = float(input('Digite o lado 1 do triangulo: ' ))
l2 = float(input('Digite o lado 2 do triangulo: ' ))
l3 = float(input('Digite o lado 3 do triangulo: ' ))
if (l1 + l2 >= l3) and (l2 + l3 >= l1) and (l3 + l2 >= l1):
    if ((l1+l2+l3) / 3) == l1:
        print('Triângulo Equilátero, três lados iguais')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triângulo Isósceles, quaisquer dois lados iguais')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('Triângulo Escaleno, três lados diferentes')
else:
    print('! !'*11)
    print('Não forma um Triangulo')
    print('! !' * 11)