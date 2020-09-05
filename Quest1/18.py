tarquivo = int(input('Digite o tamanho do arquivo em MB: '))
tvelocidade = int(input('digite a velocidade da internet em Mbps: '))
tempo = tarquivo / (tvelocidade / 8)
minutos = tempo / 60
segundos = tempo % 60
print('O Download custará : {:.0f} Minuto(s) e {:.0f} Segundo(s).'.format(minutos, segundos))
