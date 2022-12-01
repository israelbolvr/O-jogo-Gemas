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

from random import randint
import string

def entrada(): ###FUNÇÃO QUE IMPRIME O ÍNICIO DO JOGO
    print()
    print("-" * 45)
    print("          BEM VINDO AO JOGO GEMAS                ")
    print("-" * 45)
    print()
    print()
    
def printar_menu(): ###FUNÇÃO QUE IMPRIME O MENU DO JOGO NA TELA
    print('\n1 - Permutar as gemas')
    print('2 - Dicas')
    print('3 - Ajuda')
    print('4 - Sair \n')

def ajuda(): ### FUNÇÃO QUE IMPRIME O TUTORIAL DO JOGO NA TELA
    print('''O jogo Gemas consiste em um tabuleiro
com colunas e linhas contendo gemas de
cores distintas. A cada passo do jogo, o jogador ou
jogadora deve permutar de posição duas gemas
adjacentes de tal forma que se crie uma cadeia de
3 ou mais gemas da mesma cor.

Ao escolher a opção 1, o jogador irá permutar as gemas no tabuleiro.
Ao escolher a opção 2, o jogo irá dar uma dica ao jogador (cada dica solicitada resultará em menos 1 ponto.)
Ao escolher a opção 3, vai abrir o menu de tutorial do jogo.
Ao escolher a opção 4, o jogo encerra.''')

def dimensao(): ### FUNÇÃO QUE DEFINE A DIMENSÃO DO TABULEIRO
    linhas = int(input('Digite o número de linhas[3/10]: '))
    while linhas < 3 or linhas > 10: ### LIMITE DO TABULEIRO É DE 3 ATÉ 10 LINHAS
        print('Opção inválida, digite novamente: ')
        linhas = int(input('Digite o número de linhas[3/10]: '))
    colunas = int(input('Digite o número de colunas[3/10]: '))
    while colunas < 3 or colunas > 10: ### LIMITE DO TABULEIRO É DE 3 ATÉ 10 COLUNAS
        print('Opção inválida, digite novamente: ')
        colunas = int(input('Digite o número de colunas[3/10]: '))
    gemas = int(input('Digite o número de cores[3/26]: '))
    while gemas < 3 or linhas > 26: ### LIMITE DO TABULEIRO É DE 3 ATÉ 26 CORES
        print('Opção inválida, digite novamente: ')
        gemas = int(input('Digite o número de gemas[3/26]: '))
    print()

    return linhas, colunas, gemas ### RETORNA OS VALORES DAS LINHAS, COLUNAS E GEMAS

def criar_matriz(linhas,colunas,gemas): ### FUNÇÃO QUE CRIA O TABULEIRO EM FORMA DE MATRIZ
    m = [[string.ascii_uppercase[randint(0,gemas - 1)] for c in range(colunas)] for l in range(linhas)] ### PEGA AS LETRAS DO ALFABETO E RANDOMIZA NAS LINHAS E COLUNAS DO TABULEIRO

    return m ### RETORNA A MATRIZ

def validar_prontas_horizontal(m, linhas, colunas): ### FUNÇÃO QUE VALIDA AS GEMAS QUEBRADAS DAS LINHAS DA MATRIZ E AS QUEBRA
    for l in range(linhas): ### PERCORRE AS LINHAS
        contador = 1
        for c in range(colunas - 1): ### PERCORRE AS COLUNAS
            if (m[l][c]).lower() == (m[l][c + 1]).lower():
                contador += 1 
            else:
                contador = 1
            if contador >= 3: ### SE TIVER 3 OU MAIS GEMAS JUNTAS
                k = c + 1 
                while k > c + 1 - contador and m[c][k].isupper(): ### TRANSFORMARÁ AS GEMAS JUNTAS QUE ESTÃO EM LETRA MAIUSCULA EM LETRA MINUSCULA
                    m[l][k] = m[l][k].lower() ### A TRANSFORMAÇÃO DA LETRA MAIÚSCULA EM MINÚSCULA É A FORMA DE QUEBRAR AS GEMAS
                    k -= 1

    return m ### RETORNA A MATRIZ

def validar_prontas_vertical(m, linhas, colunas): ### FUNÇÃO QUE VALIDA AS GEMAS QUEBRADAS DAS COLUNAS DA MATRIZ E AS QUEBRA
    for c in range(colunas): ### PERCORRE AS COLUNAS
        contador = 1
        for l in range(linhas - 1): ### PERCORRE AS LINHAS
            if m[l][c].lower() == m[l+1][c].lower(): 
                contador +=1
            else:
                contador = 1
            if contador >= 3:
                j = l + 1
                while j > l + 1 - contador:
                    m[j][c] = m[j][c].lower() 
                    j -= 1
    return m

def validar_horizontal(m, linhas, colunas): ### FUNÇÃO QUE VALIDA AS LINHAS DA MATRIZ
    valido = False
    for l in range(linhas): 
        contador = 1
        for c in range(colunas - 1):            
            if (m[l][c]).lower() == (m[l][c + 1]).lower(): 
                contador += 1 
            else:
                contador = 1
            if contador >= 3: ### SE TIVER 3 OU MAIS GEMAS JUNTAS
                valido = True

    return valido

def validar_vertical(m, linhas, colunas): ### FUNÇÃO QUE VALIDA AS COLUNAS DA MATRIZ
    valido = False
    for c in range(colunas):
        contador = 1
        for l in range(linhas - 1):     
            if m[l][c].lower() == m[l+1][c].lower(): 
                contador +=1
            else:
                contador = 1
            if contador >= 3:
                valido = True

    return valido

def dicas_horizontal(m,linhas,colunas): ### FUNÇÃO QUE APRESENTA AS DICAS HORIZONTAIS AO JOGADOR
    lista_dicas = []
    for l in range(linhas): 
        for c in range(colunas - 1):
            m[l][c], m[l][c + 1] = m[l][c + 1], m[l][c] ### FAZ O MOVIMENTO DAS GEMAS NA COLUNA
            dica_horizontal = validar_horizontal(m, linhas, colunas) ### CHAMA A FUNÇÃO QUE VALIDA A HORIZONTAL
            dica_vertical = validar_vertical(m, linhas, colunas)    ### CHAMA A FUNÇÃO QUE VALIDA A VERTICAL
            if dica_horizontal or dica_vertical: ### SE ESSAS FUNÇÕES CHAMADAS FOREM VERDADEIRAS
                lista_dicas.append(f"Linha {l} e coluna {c}") ### DICAS HORIZONTAIS SERÃO ADICIONADAS À LISTA DE DICAS

            m[l][c], m[l][c + 1] = m[l][c + 1], m[l][c] ### DESFAZ O MOVIMENTO DAS GEMAS

    return lista_dicas

def dicas_vertical(m,linhas,colunas): ### FUNÇÃO QUE APRESENTA AS DICAS HORIZONTAIS AO JOGADOR
    lista_dicas = []
    for c in range(colunas): 
        for l in range(linhas - 1):   
            m[l][c], m[l + 1][c] = m[l + 1][c], m[l][c]
            dica_horizontal = validar_horizontal(m, linhas, colunas)
            dica_vertical = validar_vertical(m, linhas, colunas)    
            if dica_horizontal or dica_vertical:
                lista_dicas.append(f"Linha {l} e coluna {c}") ### DICAS VERTICAIS SERÃO ADICIONADAS À LISTA DE DICAS
            
            m[l][c], m[l + 1][c] = m[l + 1][c], m[l][c] ### DESFAZ O MOVIMENTO DAS GEMAS
    
    return lista_dicas ### RETORNA A LISTA

def quebrar_gemas(m, linhas, colunas): ### FUNÇÃO QUE QUEBRA AS GEMAS
    for l in range(linhas):
        for c in range(colunas):
            if m[l][c].islower(): ### SE A GEMA ESTIVER EM LETRA MINÚSCULA SERÁ TRANSFORMADA EM 0 (ZERO)
                m[l][c] = 0 
    return m

def pontuacao(m, linhas, colunas, pontos): ### FUNÇÃO QUE CONTA OS PONTOS
    for l in range(linhas):
        for c in range(colunas):
            if m[l][c] == 0: ### A CADA GEMA QUEBRADA (EM NÚMERO ZERO) NO TABULEIRO, ELE CONTA + 1 NA PONTUÇÃO
                pontos += 1
    return pontos

def descer_gemas(m, linhas, colunas): ### FUNÇÃO QUE DESCE AS GEMAS QUE ESTÃO ACIMA DAS QUEBRADAS
    for d in range(linhas):
        for l in range(linhas-1,0,-1):
            for c in range(colunas-1,-1,-1):
                if m[l][c] == 0: 
                    m[l][c], m[l-1][c] = m[l-1][c],m[l][c]
    return m

def gerar_novas_gemas(m, gemas): ### FUNÇÃO QUE GERA NOVAS GEMAS
    cont = 0
    for l in range(len(m)):
        for c in range(len(m[0])): ### LÊ O NÚMERO ZERO NA MATRIZ
            if m[l][c] == 0: ### SE TIVER NÚMERO ZERO CONTARÁ + 1
                cont += 1
                m[l][c] = string.ascii_uppercase[randint(0, gemas - 1)] ### CRIARÁ NOVAS GEMAS

### A VARIÁVEL CONT SERÁ USADA NA FUNÇÃO PRINCIPAL PARA VERIFICAR SE AINDA TEM GEMAS A SEREM QUEBRADAS, ENQUANTO CONT FOR MAIOR QUE 0, O JOGO NÃO PODERÁ RODAR

    return m, cont ### RETORNA A MATRIZ E O CONTADOR

def ciclagem(m, linhas, colunas, gemas, pontos): ### FAZ A CICLAGEM DAS FUNÇÕES 
    matriz = validar_prontas_horizontal(m,linhas,colunas)
    matriz = validar_prontas_vertical(m,linhas,colunas)
    matriz = quebrar_gemas(m,linhas,colunas)
    pontos = pontuacao(m,linhas,colunas, pontos)
    matriz = descer_gemas(m,linhas,colunas)
    matriz, cont = gerar_novas_gemas(m,gemas)

    return matriz, cont, pontos

def printar_matriz(m, linhas, colunas, pontos, total_gemas): ### FUNÇÃO QUE IMPRIME A MATRIZ NA TELA
    for l in range(linhas):
        for c in range(colunas):
            print(m[l][c], end='')
        print('')
    total_gemas += pontos
    print(f'\nSua pontuação atual é: {total_gemas}\n') ### IMPRIME TAMBÉM A PONTUAÇÃO DO JOGADOR A CADA CHAMADA DA FUNÇÃO

def solicitar_jogada(): ### FUNÇÃO QUE PEDE AO USUÁRIO QUAL A JOGADA QUE ELE QUER FAZER
    trocar_linha = int(input('Digite a linha da primeira gema a ser trocada: '))
    trocar_coluna = int(input('Digite a coluna da primeira gema a ser trocada: '))
    trocar_linha1 = int(input('Digite a linha da segunda gema a ser trocada: '))
    trocar_coluna1 = int(input('Digite a coluna da segunda gema a ser trocada: '))
    print()

    return trocar_linha, trocar_coluna, trocar_linha1, trocar_coluna1

def trocar_gemas(m, linhas, colunas, trocar_linha, trocar_coluna, trocar_linha1, trocar_coluna1): ### FUNÇÃO QUE FAZ OS MOVIMENTOS DO USUÁRIO
    for l in range(linhas):
        for c in range(colunas):
            troca1 = m[trocar_linha][trocar_coluna]
            troca2 = m[trocar_linha1][trocar_coluna1]
### FAZ A TROCA DAS LETRAS DIGITAS PELO USUÁRIO QUE ESTÃO PRESENTES NA MATRIZ 
            m[trocar_linha1][trocar_coluna1] = troca1
            m[trocar_linha][trocar_coluna] = troca2

            return m

def validacao_movimento(m, trocar_linha, trocar_coluna, trocar_linha1, trocar_coluna1): ### FUNÇÃO QUE FAZ A VALIDAÇÃO DO MOVIMENTO DIGITADO PELO USUÁRIO
    k = len(m) ### LÊ OS ELEMENTOS DA MATRIZ
    l = len(m[0])
    valido = 0
    if (trocar_linha > k or trocar_linha1 > k) or (trocar_coluna > l or trocar_coluna1 > l): ### SE O MOVIMENTO DIGITADO PELO USUÁRIO FOR MAIOR QUE A DIMENSÃO DA MATRIZ
        valido = 0
    elif abs(trocar_linha - trocar_linha1) + abs(trocar_coluna - trocar_coluna1) == 1:
        valido += 1

    return valido

    

    

    
