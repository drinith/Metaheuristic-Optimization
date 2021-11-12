#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from helps.help import matrixGenerateValues as mRan

##################################
# Problema do caixeiro viajante usando metaheuristica. Neste Problema
# as rotas serão representadas por uma matriz onde os pontos da rota 
# são os indices e os valores as distancias da combinação dos inidices
# de linha com coluna.
#################################

class CaixeiroViajante ():

    
    #Lista candidato restrita
    def listaCandidatoRestrita(self,cidadeRandomica,alpha,tsp):
        
        LCR=[]
        indice=0
        #pegando a lista de valores  dos custos até aquela cidade
        listaCidadesCusto = tsp[cidadeRandomica]
        #ordenando os custos para pegar o menor e o maior
        listaSort = listaCidadesCusto.copy()
        listaSort.sort()
        #separando o menor custo que sendo 0 o primeiro é zero pois é a posição da cidade para ela mesmo
        hmin = listaSort[1]
        #separando o maior que é custo da cidade pra ela mesmo 
        hmax = listaSort[len(tsp)-1]
        print(str(hmin) +' e ' +str(hmax))
        print(hmax+alpha*(hmin-hmax))
          
        #escolhe os vertices onde hmin<=vertice<=hmax+alpha*(hmin-hmax)
        for cidadeCusto in listaCidadesCusto:
            #hmin<=vertice<=hmax+alpha*(hmin-hmax)
            if(hmin<=cidadeCusto and cidadeCusto<=(hmax+alpha*(hmin-hmax))):
                #A lista LCR vai guardar os indices da cidade
                LCR.append(indice)
            #Caminhando para o indice da próxima cidade
            indice+=1
    

        return LCR

    def tspLCR(self,alpha,tsp):

        #escolhe um primeiro elemento aleatório
        cidadeRandomica = random.randint(0,len(tsp)-1)
        listaSolucao=[]
        #Cidade que foi escolhida randomicamente sendo colocada na lista de solução
        listaSolucao.append(cidadeRandomica)
        for i in range(len(tsp)-1):
            #trazendo lista candidata
            LCR = self.listaCandidatoRestrita(cidadeRandomica,alpha,tsp)
            print(LCR)
            #Tirando da LCR indices das cidades já visitadas
            LCRMenosListaSolucao = list(set(LCR)-set(listaSolucao))
            #Pegando randomicamente um indice de uma cidade da lista das que aparecem na LCR e não foram vizitadas 
            cidadeRandomica = LCRMenosListaSolucao[random.randint(0,len(LCRMenosListaSolucao)-1)]
            listaSolucao.append(cidadeRandomica)
            
         
#teste
if __name__=="__main__":
    #cidade 1 [1,2,3,0] 3[3,0,2,1] 2[2, 0, 3, 1] 3[3, 0, 2, 1]

    #teste [0,1,2] coloco o 3 entre 0 e 1 [0,3,1,2]
    tsp = [
        [0, 100, 500, 150, 250],
        [100, 0, 400, 200, 350],
        [500, 400, 0, 150, 10],
        [150, 200, 150, 0, 50],
        [250, 350, 10, 50, 0]
    ]
    #gerando uma matriz randomica 
    objetivo = 0
    cv = CaixeiroViajante()
    #cv.algoritmoConstrutivoListaVizinhoMaisProximo(rotasMatriz,objetivo)
    #print(cv.algoritmoRotaAleatoria(3,rotasMatriz))
    cv.tspLCR(0.5,tsp)