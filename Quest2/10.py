#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input('Digite um numero inteiro:'))
n2 = int(input('Digite outro numero inteiro:'))

# pq ele tava mlstrando do n1 pra frente então tive q tirar
for c in range(n1, n2):
    if c != n1:
        print(c)
