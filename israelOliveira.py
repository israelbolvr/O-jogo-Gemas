""""*******************************************************************************
Autor: Israel Vitor Barreto de Oliveira
Componente Curricular: Algoritmos I
Concluido em: 14/10/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************"""""      

import random ### IMPORTA A FUNÇÃO RANDOM
from bibliotecaIsraelOliveira import * ### IMPORTA AS FUNÇÕES DE OUTRO ARQUIVO PYTHON

### PROGRAMA PRINCIPAL

pontos = 0
lista_dicas = [] ### CRIA UMA LISTA VAZIA

entrada() ### CHAMA A FUNÇÃO ENTRADA
linhas, colunas, gemas = dimensao() ### COMEÇO DO PROGRAMA PRINCIPAL, CHAMA A FUNÇÃO "DIMENSÃO" E SOLICITA AO USUÁRIO A DIMENSÃO DA MATRIZ E QUANTAS GEMAS ELE QUER NO JOGO. SENDO A DIMENSÃO DO TABELEIRO 3X3 OU ATÉ 10X10, E O TOTAL DE GEMAS DE 3 A 26 CORES
matriz = criar_matriz(linhas, colunas, gemas) ### CRIA O TABULEIRO UTILIZANDO LETRAS ALEATORIAS DO TABULEIRO.
matriz, cont, pontos = ciclagem(matriz, linhas, colunas, gemas, pontos) ### CHAMA A FUNÇÃO CICLAGEM 
while cont != 0: ### ENQUANTO NÃO TIVER MAIS GEMAS A SEREM QUEBRADAS
    matriz, cont, pontos = ciclagem(matriz, linhas, colunas, gemas, pontos) ### ANALISA HORIZONTALMENTE E VERTICALMENTE AS GEMAS PRONTAS, QUEBRA AS GEMAS, DESCE AS GEMAS E GERA NOVAS GEMAS.

total_gemas = 0
pontos = 0

começar_jogo = list(dicas_vertical(matriz,linhas,colunas)+ dicas_horizontal(matriz,linhas,colunas)) ### CHAMA A FUNÇÃO QUE VAI COMEÇAR O MEU JOGO
if começar_jogo: ### SE CONTER ELEMENTOS DENTRO DA LISTA, O JOGO IRÁ COMEÇAR
  printar_matriz(matriz,linhas,colunas,pontos,total_gemas) ### CHAMA A FUNÇÃO QUE IMPRIME A MATRIZ NA TELA
  printar_menu() ### CHAMA A FUNÇÃO QUE IMPRIME O MENU
  continuar = 'S' ### CONDIÇÃO DO WHILE
  while continuar == 'S': ### INÍCIO DO JOGO
    encerrar = list(dicas_vertical(matriz,linhas,colunas) + dicas_horizontal(matriz,linhas,colunas)) 
    if len(encerrar) <= 0: ### SE A LISTA ESTIVER VAZIA O JOGO SERÁ ENCERRADO.
      print('Não existe mais combinações. Jogo encerrado')
      break           
    menu = int(input('Digite a opção desejada: [1/2/3/4] '))
    if menu == 1: ### 1 = PERMUTAR GEMAS
      trocar_linha, trocar_coluna, trocar_linha1, trocar_coluna1 = solicitar_jogada() ### CHAMA A FUNÇÃO QUE PEDE AO USUÁRIO QUAIS GEMAS ELE QUER MOVER
      adjacente = validacao_movimento(matriz, trocar_linha, trocar_coluna, trocar_linha1, trocar_coluna1) 
      if adjacente != 0: 
        trocar_gemas(matriz, linhas, colunas, trocar_linha, trocar_coluna, trocar_linha1, trocar_coluna1) ### CHAMA A FUNÇÃO QUE FAZ O MOVIMENTO DAS GEMAS
        printar_matriz(matriz,linhas,colunas,pontos,total_gemas) ### CHAMA A FUNÇÃO QUE IMPRIME A MATRIZ NA TELA
        matriz, cont, pontos = ciclagem(matriz, linhas, colunas, gemas, pontos) ### REALIZA A CICLAGEM APÓS O MOVIMENTO
        while cont != 0: ### ENQUANTO NÃO HOUVER GEMAS A SEREM QUEBRADAS
          matriz, cont, pontos = ciclagem(matriz, linhas, colunas, gemas, pontos)
        print('\n----------------- NOVO TABULEIRO -----------------\n')
        printar_matriz(matriz,linhas,colunas,pontos,total_gemas)
        encerrar = list(dicas_vertical(matriz,linhas,colunas) + dicas_horizontal(matriz,linhas,colunas))  
        if len(encerrar) <= 0:
          print('Não existe mais combinações. Jogo encerrado\n')
          print('*'*30, 'FIM DE JOGO', '*'*30)    
          break
        else:     
          printar_menu()   
      else:
        print('\nMovimento errado, jogue novamente.\n')
        printar_matriz(matriz,linhas,colunas,pontos,total_gemas) ### CHAMA A FUNÇÃO QUE IMPRIME A MATRIZ NA TELA
        printar_menu()
        
    elif menu == 2: ### 2 = DICAS 
      pontos -= 1 ### A CADA DICA PEDIDA, O USUÁRIO PERDE UM PONTO
      print(f'Você solicitou uma dica, portanto, perdeu 1 ponto. Sua pontuação atual é: {pontos}')
      dicas = dicas_vertical(matriz,linhas,colunas), dicas_horizontal(matriz,linhas,colunas)     
      print(f'Tente permutar as gemas na {random.choice(random.choice(dicas))}')
      printar_matriz(matriz,linhas,colunas,pontos,total_gemas) ### CHAMA A FUNÇÃO QUE IMPRIME A MATRIZ NA TELA
      printar_menu()

    elif menu == 3: ### 3 = TUTORIAL DO JOGO
      ajuda() ### CHAMA A FUNÇÃO QUE IMPRIME O TUTORIAL NA TELA
      print()
      printar_matriz(matriz,linhas,colunas,pontos,total_gemas) ### CHAMA A FUNÇÃO QUE IMPRIME A MATRIZ NA TELA
      printar_menu()

    elif menu == 4: ### 4 = SAIR DO JOGO
      print('Digite "N" para sair do jogo ou "S" para voltar ao menu.')
      continuar = (input('\nDeseja continuar jogando? \n')).strip().upper()[0] ### PERGUNTA SE O USUÁRIO QUER CONTINUAR JOGANDO
      while continuar not in 'SN':
          continuar = str(input("Opção inválida. Digite a opção corretamente [S/N]: ")).strip().upper()[0]
      if continuar == 'N':
          continuar = 'N'
      else:
          continuar = 'S'
          printar_matriz(matriz,linhas,colunas,pontos,total_gemas)
          print()
          printar_menu()
    else: ### SE O USUÁRIO DIGITAR UMA OPÇÃO INCORRETA
      print('\nCOMANDO INVÁLIDO! TENTE O COMANDO "AJUDA (3)" PARA RECEBER INFORMAÇÕES SOBRE O JOGO.\n') 
else:
  print('Jogo inválido, tente novamente.\n')