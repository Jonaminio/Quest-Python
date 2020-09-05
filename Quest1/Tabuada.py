n = int(input('Digite o numero a fazer a tabuada: '))
x = 1
while x < 11:
    print("=" * 12,"\n{} x {} é {}".format(n, x, n * x))
    x += 1