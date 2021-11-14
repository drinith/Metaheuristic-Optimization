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
    
        print(f'Para hmin {hmin} e hmax {hmax} e alpha {alpha}, partindo da cidade {cidadeRandomica} respeitando o conjunto solução {hmin}<=ci<={hmax+alpha*(hmin-hmax)} temos a LCR{LCR}')
        return LCR


        #Lista candidato restrita
    def listaCandidatoRestrita(self,cidadeRandomica: int,LCRMenosListaSolucao: list,alpha,tsp):
        
        LCR=[]
        indice=0
        #pegando a lista de valores  dos custos até aquela cidade menos as cidades já visitadas
        listaCidadesCusto=[]
        for cidade in LCRMenosListaSolucao:
            listaCidadesCusto.append(tsp[cidadeRandomica][cidade])
        #ordenando os custos para pegar o menor e o maior
        listaSort = listaCidadesCusto.copy()
        listaSort.sort()
        #separando o menor custo que sendo 0 o primeiro é zero pois é a posição da cidade para ela mesmo
        hmin = listaSort[0]
        #separando o maior que é custo da cidade pra ela mesmo 
        hmax = listaSort[len(listaSort)-1]
        print("hmin " +str(hmin) +' e ' +"hmax "+ str(hmax))
                  
        #escolhe os vertices onde hmin<=vertice<=hmax+alpha*(hmin-hmax)
        for cidade in LCRMenosListaSolucao:
            #hmin<=vertice<=hmax+alpha*(hmin-hmax)
            if(hmin<=tsp[cidadeRandomica][cidade] and tsp[cidadeRandomica][cidade]<=(hmax+alpha*(hmin-hmax))):
                #A lista LCR vai guardar os indices da cidade
                LCR.append(cidade)
            #Caminhando para o indice da próxima cidade
            
    
        print(f'Para hmin {hmin} e hmax {hmax} e alpha {alpha}, partindo da cidade {cidadeRandomica} respeitando o conjunto solução {hmin}<=ci<={hmax+alpha*(hmin-hmax)} temos a LCR{LCR}')
        return LCR

    def tspLCR(self,alpha,tsp):

        #escolhe um primeiro elemento aleatório
        cidadeRandomica = random.randint(0,len(tsp)-1)
        listaSolucao=[]
        #cidade que foi escolhida randomicamente sendo colocada na lista de solução
        listaSolucao.append(cidadeRandomica)
        print ('Começando a lista randomica com a cidade '+str(cidadeRandomica))

        # Lista candidata inicial teria todos os indices possíveis   
        LCR =list(range(0, len(tsp)))
       
        # lista candidata sem os indices que já entraram na solução    
        LCRMenosListaSolucao=list(range(0, len(tsp))) 
        # percorrer as cidades e preenchendo a lista feasible
        for i in range(len(tsp)):
            
            #criar a lista dos não visitados
            LCRMenosListaSolucao = list(set(LCRMenosListaSolucao)-set(listaSolucao))

            #quando não houver mais solução sair do loop
            if(LCRMenosListaSolucao==[]):
                print('Termino de possíveis caminhos')
                break


            #trazendo lista candidata
            LCR = self.listaCandidatoRestrita(cidadeRandomica,LCRMenosListaSolucao,alpha,tsp)
            print( f"Lista candidata gerada da cidade Randomica {cidadeRandomica} somente com as cidades não visitadas {LCR} ")
        
            
            #Pegando randomicamente um indice de uma cidade da lista das que aparecem na LCR 
            cidadeRandomica = LCR[random.randint(0,len(LCR)-1)]
            print(f'Pegando agora aleatóriamente a cidade {cidadeRandomica} ainda não visitada')
            listaSolucao.append(cidadeRandomica)

                

        print('Solução possível '+str(listaSolucao) )
            
         
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
    cv.tspLCR(1,tsp)