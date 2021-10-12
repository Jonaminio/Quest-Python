n = int(input('Digite o numero a fazer a tabuada: '))

x = int(input('Digite o numero a COMEÇAR a tabuada: '))

a = int(input('Digite o numero a TERMINAR a tabuada: '))


while x < a+1:
    print("=" * 12,"\n{} x {} é {}".format(n, x, n * x))
    x += 1