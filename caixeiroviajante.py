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
        print("hmin " +str(hmin) +' e ' +"hmax "+ str(hmax))
                  
        #escolhe os vertices onde hmin<=vertice<=hmax+alpha*(hmin-hmax)
        for cidadeCusto in listaCidadesCusto:
            #hmin<=vertice<=hmax+alpha*(hmin-hmax)
            if(hmin<=cidadeCusto and cidadeCusto<=(hmax+alpha*(hmin-hmax))):
                #A lista LCR vai guardar os indices da cidade
                LCR.append(indice)
            #Caminhando para o indice da próxima cidade
            indice+=1
    
        print(f'Para hmin {hmin} e hmax {hmax} e alpha {alpha} temos a LCR{LCR}')
        return LCR

    def tspLCR(self,alpha,tsp):

        #escolhe um primeiro elemento aleatório
        cidadeRandomica = random.randint(0,len(tsp)-1)
        listaSolucao=[]
        #Cidade que foi escolhida randomicamente sendo colocada na lista de solução
        listaSolucao.append(cidadeRandomica)
        print ('Começando a lista randomica com a cidade '+str(cidadeRandomica))
        
        #Dentre as possibilidades me parece que o algoritmo provoca
        #Uma Infeasible construction como previsto em et al [Mauricio,2016] na página
        #61        
        
        #Enquanto existe uma infeasible construção
        LCRMenosListaSolucao=[] #lista que serve para verificar solução feasible
        listaSolucao = []
        while (LCRMenosListaSolucao==[]):
        #criação da lista de solução feasible
            listaSolucao = []
            # percorrer as cidades e preenchendo a lista feasible
            for i in range(len(tsp)):
                #trazendo lista candidata
                LCR = self.listaCandidatoRestrita(cidadeRandomica,alpha,tsp)
                print( f"Lista candidata gerada da cidade Randomica {cidadeRandomica} somente com as cidades não visitadas ")
                #Tirando da LCR indices das cidades já visitadas
                LCRMenosListaSolucao = list(set(LCR)-set(listaSolucao))
                #teste de infeasible
                if(LCRMenosListaSolucao==[]):
                    print("solução infeasible")
                    break
                print(LCRMenosListaSolucao)
                #Pegando randomicamente um indice de uma cidade da lista das que aparecem na LCR e não foram vizitadas 
                cidadeRandomica = LCRMenosListaSolucao[random.randint(0,len(LCRMenosListaSolucao)-1)]
                listaSolucao.append(cidadeRandomica)
                

        print('Solução fiesible '+str(listaSolucao) )
            
         
#teste
if __name__=="__main__":
    
    #Exemplo baseado no livro de Resende, Mauricio GC, and Celso C. Ribeiro. Optimization by GRASP. Springer Science+ Business Media New York, 2016.
    #somente existe a diferença que aqui estamos usando os indices ou seja lá as cidades são 1,2,3,4,5 , aqui são respectivamente 0,1,2,3,4 
    tsp = [
        [0, 1, 2, 7, 5],
        [1, 0, 3, 4, 3],
        [2, 3, 0, 5, 2],
        [7, 4, 5, 0, 3],
        [5, 3, 2, 3, 0]
    ]
    #gerando uma matriz randomica 
    objetivo = 0
    cv = CaixeiroViajante()
    #cv.algoritmoConstrutivoListaVizinhoMaisProximo(rotasMatriz,objetivo)
    #print(cv.algoritmoRotaAleatoria(3,rotasMatriz))
    cv.tspLCR(0.5,tsp)