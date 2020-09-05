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
