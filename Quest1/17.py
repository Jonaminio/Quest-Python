#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

m2 = float(input('Digite o m2 da parede: '))
## declarei tudo p ficar mais visual, porem melhor no format
mtinta = 6
galao = 18
lata = 3.6
precogalao = 80
precolata = 25
litros = math.ceil(m2 / mtinta)
tinta1 = math.ceil(litros / galao)
tinta2 = math.ceil(litros / lata)

print('\n===> Distintos entre galão e lata ficará: \n| Precisará de : {} Litros|'.format(litros))
print('Se comprares em apenas Galões de 18l serão:{} latas e custará:{:.2f}R$'.format(tinta1, tinta1 * precogalao))
print('Se comprares em apenas latas de 3.6l serão:{} latas e custará:{:.2f}R$'.format(tinta2, tinta2 * precolata))
# so aplicando os 10% e arredondando pra cima
litros = math.ceil(litros + (litros * 10 / 100))
print('\n===> aplicando 10% e misturado entre galão e lata ficará: \n|Precisará de : {} Litros |'.format(litros))
## 10.8 é a quantidade de litros em 3 latas que sai em conta pois 3 latas = 75R$
## obs: se n fosse o preço era so botar 18, q é o maximo de litros
if litros <= 10.8:
    print('\nPrecisará de: \n0 latas de 18l \n{} latas de 3.6l \ncustará: {} R$'.format(tinta2, tinta2 * precolata))
## se não for então o galão entra, vamos pegar o galão normalmente e mostrar
## o auxiliar tinta3 servirá para saber o resto dos galões de 18 que serão em latas
## ou seja litros % 18
## porem se o resto da divisão em que os litros forem maiores que 18(galão) ocorrerá erro
## calculará errado as latas, solução: logo se litros estiver entre 10.8 e 18, tinta3 será 0
if litros >= 10.8 and litros <= 18:
    tinta3 = 0
    ##print(tinta3)
    ## somando o preço das duas
    preco = (tinta1 * precogalao) + ((tinta3 / lata) * precolata)
    print(
        '\nEm:\n{} latas de 18l\n{} latas de 3.6l \ncustará: {:.2f} R$'.format(tinta1, math.ceil(tinta3 / lata), preco))
else:
    tinta3 = litros % 18
    preco = (tinta1 * precogalao) + ((tinta3 / lata) * precolata)
    ##print(tinta3)
    print('Em:\n{} latas de 18l\n{} latas de 3.6l \ncustará: {:.2f} R$'.format(tinta1, math.ceil(tinta3 / lata), preco))
