#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

n = int(input('Digite o numero a fazer a tabuada: '))
x = 1
for c in range(10):
    print("=" * 12,"\n{} x {} é {}".format(n, x, n * x))
    x += 1