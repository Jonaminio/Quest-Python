#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

for c in range (0,2):
    c1 = float(input('Digite a população do Pais 1: '))
    t1 = float(input('Digite a % Taxa de Crescimentos do Pais 1: '))
    c2 = float(input('Digite a população do Pais 1: '))
    t2 = float(input('Digite a % Taxa de Crescimentos do Pais 1: '))
    i = 0
    while c1 < c2:
        c1 = c1 + (c1 * t1 // 100)
        c2 = c2 + round((c2 * t2 // 100))
        i += 1
        if c1 > c2:
            print(f'Em {i} anos o país 1 vai ultrapassar a população do país 2 com  {c1} e {c2} respectivamente')
    c = int(input('\nDigite < 1 > para Reiniciar  e < 2 > para Sair: '))
