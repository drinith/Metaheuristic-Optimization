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

    tsp=[]
    alpha=0
    

    def __init__(self,_tsp,_alpha):
        self.tsp=_tsp
        self.alpha=_alpha
  

    #Construção de uma solução viável 
    def construtivo(self,cidadeRandomica: int,
    LCRMenosListaSolucao: list):
        
        LCR=[]
        indice=0

        #inicializando a lista qie conterá os custos do vértices
        #para aquelas cidades        
        listaCidadesCusto=[]
        
        #pegando a lista de valores  dos custos até aquela cidade 
        #menos as cidades já visitadas
        for cidade in LCRMenosListaSolucao:
            listaCidadesCusto.append(self.tsp[cidadeRandomica]
            [cidade])
        
        #ordenando os custos para pegar o menor e o maior
        listaSort = listaCidadesCusto.copy()
        listaSort.sort()
        
        #separando o menor custo que está na posição 0 
        hmin = listaSort[0]
        
        #separando o maior que é o último 
        hmax = listaSort[len(listaSort)-1]
        print("hmin " +str(hmin) +' e ' +"hmax "+ str(hmax))
                  
        #escolhe os vertices onde hmin<=vertice<=hmax+
        #self.alpha*(hmin-hmax)
        for cidade in LCRMenosListaSolucao:
            
            #hmin<=vertice<=hmax+self.alpha*(hmin-hmax)
            if(hmin<=self.tsp[cidadeRandomica][cidade] and 
            self.tsp[cidadeRandomica][cidade]
            <=(hmax+self.alpha*(hmin-hmax))):
                
                #A lista LCR vai guardar os índices da cidade
                LCR.append(cidade)
            
            #Caminhando para o índice da próxima cidade
            
    
        print(f'Para hmin {hmin} e hmax {hmax} e self.alpha'
         f'{self.alpha},partindo da cidade {cidadeRandomica}'
         f'respeitando o conjunto solução {hmin}
         f'<=ci<={hmax+self.alpha*(hmin-hmax)}'
         f'temos a LCR{LCR}')
        
        return LCR

    def tspLCR(self,cidadeRandomica=None):

        if(cidadeRandomica==None):
            #escolhe um primeiro elemento aleatório
            cidadeRandomica = random.randint(0,len(self.tsp)-1)
        listaSolucao=[]
        #cidade que foi escolhida randomicamente sendo colocada na lista de solução
        listaSolucao.append(cidadeRandomica)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        print (f'Começando a lista randomica com a cidade {cidadeRandomica}\n')
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
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
            LCR = self.construtivo(cidadeRandomica,LCRMenosListaSolucao)
            print( f"Lista candidata gerada da cidade Randomica {cidadeRandomica} somente com as cidades não visitadas {LCR} ")
        
            
            #Pegando randomicamente um indice de uma cidade da lista das que aparecem na LCR 
            cidadeRandomica = LCR[random.randint(0,len(LCR)-1)]
            print(f'Pegando agora aleatóriamente a cidade {cidadeRandomica} ainda não visitada')
            listaSolucao.append(cidadeRandomica)

        #print('Solução possível '+str(listaSolucao) )
        #returna uma solução possivel 
        return listaSolucao
  
            
    def somaSolucao(self,solucao):
        soma=0
        count=0
        #percorrer cada ponto da solução somando o primeiro com o proximo e no ultimo somar com o primeiro fechando o ciclo
        for i in range(len(solucao)-1):
            
            if(count != len(solucao)):
                #pegar na matriz tsp os valores como explicado acima
                soma+=self.tsp[solucao[i]][solucao[i+1]]
            else:
                soma+=self.tsp[solucao[0]][solucao[i]]

        return soma
    
    def melhorSolucao(self,listaSolucao):
        listaValorSolucao = []
        #percorrer todas as solucões e criar uma lista de lista com soma da solução e solução
        for solucao in listaSolucao:
            listaValorSolucao.append([self.somaSolucao(solucao),solucao])
       
        listaValorSolucao.sort()
        #retornando a melhor solução
        return listaValorSolucao[0] 

    def buscaLocal(self,solucao):
       
        listaNovaSolucaoLocal=[]
        listaNovaSolucaoLocal.append(solucao)
        #criar outras soluções trocando a partir do primeiro item o i com i+1
        for i in range(len(solucao)):
            for j in range (i+1,len(solucao)):
                #criar uma copia da solução paa uma nova solução
                novaSolucao=solucao.copy()
                #troca duas cidades de posição
                novaSolucao[i]=solucao[j] 
                novaSolucao[j]=solucao[i]
                #adiciona a nova solução para uma lista de soluções
                listaNovaSolucaoLocal.append(novaSolucao)
            
            #buscar melhor solução local
            melhorLocal = self.melhorSolucao(listaNovaSolucaoLocal)
        return melhorLocal
    
    def grasp (self):
        LCRInicial = list(range(0, len(tsp))) 
        listaMelhorLocal =[]
        while (LCRInicial!=[]):
            
            cidadeIndiceRandomico = LCRInicial.pop(random.randint(0,len(LCRInicial)-1))
            
            solucaoViavel=self.tspLCR(cidadeIndiceRandomico)
            print(f'Solução Viável {solucaoViavel}')
            melhorLocal = self.buscaLocal(solucaoViavel)
            print('====================================================')
            print(f'Baseado na solução {solucaoViavel} a melhor solução Local tem peso {melhorLocal[0]} pertencendo a solução vizinha {melhorLocal[1]}')
            print('====================================================')
            listaMelhorLocal.append(melhorLocal)
            
        listaMelhorLocal.sort()
        print(f'Melhor global peso {listaMelhorLocal[0][0]} sendo a solução {listaMelhorLocal[0][1]}')

        #primeiro construir uma solucao viável com uma cidade randomica


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
    # Gerando randomicamente uma matr
    # tsp = mRan(1000,1,10)
    print(tsp)
    # gerando uma matriz randomica 

    cv = CaixeiroViajante(tsp,0)
    #cv.tspLCR()
    #cv.buscaLocal([1, 0, 2, 4, 3])
    cv.grasp()