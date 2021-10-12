#usar py 3.7.12
#Objetivo: calcular km media por ano, 2 arquvos, carros km e ano de carros
import numpy as np
#carregando arquivos
km = np.loadtxt('data\carros-km.txt')
#diznedo que anos é do timpo inteiro
#por padrão é float
#so é possivel apenas 1 tipo de variavel no numpy
anos = np.loadtxt('data\carros-anos.txt', dtype=int)
#printando arquivo pra teste
#print (km)
#Obtendo a quilometragem média por ano
km_media = km / (2019 - anos)
#printando resultado
print (km_media)
#list comprehensions, pegar 2 arrays e coloar em lista e sem duplicados
#1 os arrays
dados = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
#2 alinhando nesse recurso do python primeiro inserindo o valor que vc quer e apos isso os ifs tradicionais
# o set serve para tirar as duplicadas
oi = list(set([item for lista in dados for item in lista]))

print(oi)

#------------------------------------------------> parte 02

#Numpy contando as linhas
print (km.shape)
#verificando tipo do array
print (km.dtype)

#Operações aritméticas com arrays Numpy
#criando 2 variaveis numpy
km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 1995])

#operação simples variavel - array e printando
idade = 2019 - anos
print(idade)

#operação entre 2 arrays
km_media = km / idade
print(km_media)

#criando matriz
dados = np.array([km, anos])
print(dados)
#vendo tamanho da matriz
print(dados.shape)

#manipulando uma matriz e fazendo calculos
km_media = dados[0] / (2019 - dados[1])
print(km_media)

#pegando todos que são da linha [1] ou seja anos maior q 2000
print(dados[:, dados[1] > 2000])

#Estatísticas com NumPy
anos = np.loadtxt('data\carros-anos.txt', dtype = int)
km = np.loadtxt('data\carros-km.txt')
valor = np.loadtxt('data\carros-valor.txt')

#juntando tudo em uma tupla (tabela)
dataset = np.column_stack((anos, km, valor))

#fazendo a media de cada coluna
print(np.mean(dataset, axis = 0)) #se for por linha ultilizar axis = 1

#desvio padrão
print(np.std(dataset[:,2])) #excluida a coluna anos