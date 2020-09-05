n1 = int(input('Digite um numero inteiro:'))
n2 = int(input('Digite outro numero inteiro:'))
soma: int = 0
# pq ele tava mostrando do n1 pra frente então tive q tirar
for c in range(n1, n2):
    if c != n1:
        print(c)
        soma = soma + c
print(f'\nA soma de todos é {soma}')
