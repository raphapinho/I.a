import numpy as np
from random import randint

matriz_inicial = np.array(
    [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]
    ]
)

def checa_sujeira(matriz,linha,coluna):
  #checando se o setor está sujo, se o valor for "1" o setor está sujo, se for "0" o setor está limpo 
        if matriz[linha][coluna] == 1: 
            print("sugeira encontrada, limpando")
            matriz[linha][coluna] = 0
            print(matriz)

def busca_profunda(matriz, linha, coluna):
    tamanho_Matriz = len(matriz) 
    matriz_visitada = np.full((tamanho_Matriz, tamanho_Matriz), False)#cria uma matriz NxN toda False
    matriz_obj = np.full((tamanho_Matriz, tamanho_Matriz), True)#cria uma matriz NxN toda True
    
    #printando posição inicial do agente
    print(f"Agente iniciando na posição [{linha+1},{coluna+1}]")
    print(matriz)
    checa_sujeira(matriz, linha, coluna)

    #colocando as direções que o agente pode se mover
    while True:
      
        matriz_visitada[linha][coluna] = True
        
        move = randint(1, 4) #Escolhendo valor aleatorio de 1 a 4 para ser utilizado na switch case.

        match move:
            
            #direita
            case 1:
                if coluna < 2 and matriz_visitada[linha][coluna+1] == False:
                    coluna += 1
                    print("agente se moveu para direita")
      
            #esquerda
            case 2:
                if coluna > 0 and matriz_visitada[linha][coluna-1] == False:
                    coluna -= 1
                    print("agente se moveu para esquerda")
         
                    
            #baixo
            case 3:    
                if linha < 2 and matriz_visitada[linha+1][coluna] == False:
                    linha += 1
                    print("agente se moveu para baixo")
         

            #cima     
            case 4:    
                if linha > 0 and matriz_visitada[linha-1][coluna] == False:
                    linha -= 1
                    print("agente se moveu para cima")
        

        print(f"Agente se moveu para a posição ({linha + 1},{coluna + 1}) de valor: {matriz[linha][coluna]}") #printado a posição atual do agente
        print(matriz)

        checa_sujeira(matriz,linha, coluna)
        
        #condição de parada
        compara_matriz = np.array_equal(matriz_visitada,matriz_obj)
        if compara_matriz == True:
            print("Agente limpou todo o setor.")
            break

busca_profunda(matriz_inicial,1,1)



