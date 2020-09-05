n = int(input('Digite o numero a fazer a tabuada: '))
x = 1
for c in range(10):
    print("=" * 12,"\n{} x {} é {}".format(n, x, n * x))
    x += 1