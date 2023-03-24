
# Linhas
import os

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

print('               Jogo da velha!!!               ')

# Função que mostra o tabuleiro

def prints ():
  os.system("cls")
  
  print('          |           |          ')
  print(f'   {l1[0]}      |     {l1[1]}     |     {l1[2]}    ')
  
  print('          |           |          ')

  print('---------- ----------- ---------')

  print('          |           |          ')
  print(f'    {l2[0]}     |     {l2[1]}     |     {l2[2]}    ')
  print('          |           |          ')

  print('---------- ----------- ----------')

  print('          |           |          ')
  print(f'    {l3[0]}     |     {l3[1]}     |     {l3[2]}    ')
  print('          |           |          ')

prints()

historicoPrenchidos = []

isPlayerOne = True; 
#show_tabu.. 


# While que repete a partida até que alguém ganhe



while True:
  escolhaX = int(input('Insira o número da casa para inserir o X: '))

  if(escolhaX in historicoPrenchidos ):
    print('queridao essa ja foi!!! (- - )')
    continue
  
  historicoPrenchidos.append(escolhaX)
  
  isPlayerOne = not isPlayerOne

  if escolhaX > 9 or escolhaX< 0:
    print('A casa escolhida não existe, por favor tente novamente:\n')
    continue  
  #Insere o X na casa escolhida 
  elif escolhaX <= 3:
    l1[escolhaX-1] = 'x' if isPlayerOne else "o"
    l1i = l1[escolhaX-1]
    if l1i == False:
      escolhaX = int(input('Casa já ocupada, tente novamente:'))
      continue

  elif escolhaX <= 6 and escolhaX > 3:
    l2[escolhaX-4] = 'x' if isPlayerOne else "o"
    l2i = l2[escolhaX-4]
    if l2i == False:
      escolhaX = int(input('Casa já ocupada, tente novamente:'))
      continue

  elif escolhaX <=9 and escolhaX > 6:
    l3[escolhaX-7] = 'x' if isPlayerOne else "o"
    l3i = l3[escolhaX-7]
    if l3i == False:
      escolhaX = int(input('Casa já ocupada, tente novamente:'))
      continue
    
  prints()

  if l1[0] == l1[1] and l1[0] == l1[2]:
    print(f'Parabéns o: {l1[1]} foi o ganhador do jogo!')
    break
    
  elif l2[0] == l2[1] and l2[0] == l2[2]:
    print(f'Parabéns o: {l2[0]} foi o ganhador do jogo!')
    break
    
  elif l3[0] == l3[1] and l3[0] == l3[2]:
    print(f'Parabéns o: {l3[0]} foi o ganhador do jogo!')
    break
  
  # Colunas

  elif l1[0] == l2[0] and l1[0] == l3[0]:
    print(f'Parabéns o: {l1[0]}')
    break
  
  elif l1[1] == l2[1] and l1[1] == l3[1]:
    print(f'Parabéns o: {l1[1]}')
    break

  elif l1[2] == l2[2] and l1[2] == l3[2]:
    print(f'Parabéns o: {l1[2]}')
    break

  # Diagonais

  elif l1[0] == l2[1] and l1[0] == l3[2]:
    print(f'Parabéns o: {l1[0]}')
    break

  elif l1[2] == l2[1] and l1[2] == l3[0]:
    print(f'Parabéns o: {l1[2]}')
    break

