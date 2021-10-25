#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from helps.help import matrixGenerateValues as mRan

##################################
# Problema do caixeiro viajante usando metaheuristica. Nesse Problema
# as rotas serão representadas por uma matriz onde os pontos da rota 
# são os indices e os valores as distancias da combinação dos inidices
# de linha com coluna.
#################################

class CaixeiroViajante ():

    #Algoritmo Construtivo Vizinho Mais Proximo
    def AlgoritmoConstrutivoListaVizinhoMaisProximo(self,rotasMatriz,objetivo):
        #1. Inicia-se uma rota vazia
        rota = []
        
        #lista das cidades visitadas 
        cidadeVisitada =list(range(0, len(rotasMatriz)))
        
                
        #2. Adiciona-se a cidade de origem à rota
        #cidade = random.randint(0,len(rotasMatriz)-1)
        cidade =3

        #dizer que o indice daquela cidade foi visitado
        cidadeVisitada[cidade]="visitada"
       
        #inicialização a rota com a cidade escolhida randomicamente
        rota.append(cidade)

        #inicialização do indice da cidade melhor para destino
        cidadeMelhor=0

        

        # 3. Escolhe, dentre todas as cidades que ainda não foram
        # visitadas, a cidade i que tiver a menor distância para a
        # última cidade inserida na rota.     
        
        while(len(rota)<len(rotasMatriz)):
            
            rotaMelhor = 9999999999999999999999999
      
            for i in range(len(rotasMatriz)):#Caminhando sobre os indices que representam as cidades
                #verificar se a rota é melhor para o destino e se esse destino já foi visitado
                if (cidadeVisitada[i]!="visitada" and cidade!=i and rotaMelhor>=rotasMatriz[i][cidade]):
                    #rotamelhor vai receber o valor da melhor rota
                    rotaMelhor = rotasMatriz[i][cidade]
                    #Recebe o indice da melhor cidade de destino
                    cidadeMelhor = i
                
                    
            #cidade passa a ser a melhor cidade o próximo salto
            cidade= cidadeMelhor
            #indice da cidade entra para a lista da rota
            rota.append(cidadeMelhor)
            #dizer que o indice daquela cidade foi visitado
            cidadeVisitada[cidade]="visitada"
            
        print(rota)

#teste
if __name__=="__main__":
    #cidade 1 [1,2,3,0] 3[3,0,2,1] 2[2, 0, 3, 1] 3[3, 0, 2, 1]
    rotasMatriz = [
        [0, 800, 100, 300],
        [800, 0, 200, 500],
        [100, 200, 0, 600],
        [300, 500, 600, 0]
    ]
    #gerando uma matriz randomica 
    objetivo = 0
    cv = CaixeiroViajante()
    cv.AlgoritmoConstrutivoListaVizinhoMaisProximo(rotasMatriz,objetivo)
   
    print('fim')