#     Supondo que a população de um país A seja da ordem de 80000 habitantes com
#     uma taxa anual de crescimento de 3% e que a população de B seja 200000
#     habitantes com uma taxa de crescimento de 1.5%. Faça um programa que
#     calcule e escreva o número de anos necessários para que a população do país
#     A ultrapasse ou iguale a população do país B, mantidas as taxas de
#     crescimento.

c1: float = 80000
c2: float = 200000
i = 0
while c1 < c2:
    c1 = c1 + (c1 * 0.03)
    c2 = c2 + (c2 * 0.015)
    i += 1
    if c1 > c2:
        print('Em {} anos o país 1 vai ultrapassar a população do país 2 com  {:.0f} e {:.0f} respectivamente'.format(i,c1,c2))
