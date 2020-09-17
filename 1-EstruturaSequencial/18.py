#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)

tarquivo = int(input('Digite o tamanho do arquivo em MB: '))
tvelocidade = int(input('digite a velocidade da internet em Mbps: '))
tempo = tarquivo / (tvelocidade / 8)
minutos = tempo / 60
segundos = tempo % 60
print('O Download custará : {:.0f} Minuto(s) e {:.0f} Segundo(s).'.format(minutos, segundos))
