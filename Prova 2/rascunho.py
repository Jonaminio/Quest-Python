jarA = 0
jarB = 0
resto = 0
def encherJarro(jarroA, jarroB):
  jarA = jarroA
  jarB = jarroB
  #colocar toda agua do jarro A em reserva
  resto = jarA
  jarA = 0
  #Colocar toda a agua do jarro B no jarro A
  jarA = jarB
  jarB = 0
  #colocar o maximo de agua do resto no jarro B
  jarB = 3
  resto = 1
  #Colocar agua do jarro B no jarro A até completar o Jarro A
  jarA = 4
  jarB = 2
  # Colocar a agua do A no resto
  resto = resto + jarA
  jarA = 0
  # Colocar os dois litros do Jarro B no Jarro A
  jarA = jarB
  jarB = 0
  print('Volume jarro a: ' + str(jarA))
  print('Volume jarro b: ' + str(jarB))
  print('Resto: ' + str(resto))

encherJarro(4,3)