#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from helps.help import matrixGenerateValues as mRan
from math import e

##################################
# Problema do caixeiro viajante usando metaheuristica. Neste Problema
# as rotas serão representadas por uma matriz onde os pontos da rota 
# são os indices e os valores as distancias da combinação dos inidices
# de linha com coluna.
#################################


class CaixeiroViajante ():

    tsp=[]
    alpha=0
    tabuList=[]
    

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
         f'respeitando o conjunto solução {hmin}'
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
  
    def pegaVizinhaca(self,solucao):
        listaNovaSolucaoLocal=[]
        listaNovaSolucaoLocal.append(solucao)
        #criar outras soluções trocando a partir do 
        # primeiro item o i com i+1
        for i in range(len(solucao)):
            for j in range (i+1,len(solucao)):
                #criar uma copia da solução paa uma nova solução
                novaSolucao=solucao.copy()
                #troca duas cidades de posição
                novaSolucao[i]=solucao[j] 
                novaSolucao[j]=solucao[i]
                #adiciona a nova solução para uma lista 
                # de soluções
                listaNovaSolucaoLocal.append(novaSolucao)
        return listaNovaSolucaoLocal


    def somaSolucao(self,solucao):
        soma=0
        count=0
        #percorrer cada ponto da solução somando o primeiro com 
        # o proximo e no ultimo somar com o primeiro fechando 
        # o ciclo
        for i in range(len(solucao)-1):
            
            if(count != len(solucao)):
                #pegar na matriz tsp os valores como explicado 
                # acima
                soma+=self.tsp[solucao[i]][solucao[i+1]]
            else:
                soma+=self.tsp[solucao[0]][solucao[i]]

        return soma
    
    def melhorSolucao(self,listaSolucao):
        listaValorSolucao = []
        #percorrer todas as solucões e criar uma lista de lista 
        # com 
        # soma da solução e solução
        for solucao in listaSolucao:
            listaValorSolucao.append([self.somaSolucao(solucao)
            ,solucao])
       
        listaValorSolucao.sort()
        #retornando a melhor solução
        return listaValorSolucao[0] 

    def buscaLocal(self,solucao):
       
        listaNovaSolucaoLocal=[]
        listaNovaSolucaoLocal.append(solucao)
        #criar outras soluções trocando a partir do 
        # primeiro item o i com i+1
        for i in range(len(solucao)):
            for j in range (i+1,len(solucao)):
                #criar uma copia da solução paa uma nova solução
                novaSolucao=solucao.copy()
                #troca duas cidades de posição
                novaSolucao[i]=solucao[j] 
                novaSolucao[j]=solucao[i]
                #adiciona a nova solução para uma lista 
                # de soluções
                listaNovaSolucaoLocal.append(novaSolucao)
            
            #buscar melhor solução local
            melhorLocal=self.melhorSolucao(listaNovaSolucaoLocal)
        return melhorLocal

    def movimentoAletorioVizinhaca(self,solucao):

        #fazendo uma movimentação aleatótiria para vizinhaça
        iAleatorio = random.randint(0,len(solucao)-1)
        jAleatorio = random.randint(0,len(solucao)-1)

        novaSolucao=solucao.copy()

        novaSolucao[iAleatorio]=solucao[jAleatorio] 
        novaSolucao[jAleatorio]=solucao[iAleatorio]
            
        return novaSolucao
    
    def grasp (self):
        #Inciando a lista de possíveis candidatos
        LCRInicial = list(range(0, len(tsp))) 
        #Iniciando lista que conterá todos melhores locais        
        listaMelhorLocal =[]
        
        #Manter loop enquanto estiverem possiveis candidatos
        while (LCRInicial!=[]):
            
            #Pegar um possível candidato randomicamente na 
            # lista
            cidadeIndiceRandomico = LCRInicial\
            .pop(random.randint
            (0,len(LCRInicial)-1))
            
            #Trazer uma possível solução através do método
            #utilizando a lista de candidato restrita
            solucaoViavel=self.tspLCR(cidadeIndiceRandomico)
            print(f'Solução Viável {solucaoViavel}')
            
            #Fazendo a busca de vizinhaça local e trazendo
            #o melhor local daquela vizinhaça
            melhorLocal = self.buscaLocal(solucaoViavel)
            print('===================================='
            f'================')
            print(f'Baseado na solução {solucaoViavel} '
            f'a melhor solução Local tem peso {melhorLocal[0]} '
            f'pertencendo a solução vizinha {melhorLocal[1]}')
            print('=========================================='
            f'==========')
            
            #guardando o melhor local
            listaMelhorLocal.append(melhorLocal)

        #organizando lista dos melhores locais     
        listaMelhorLocal.sort()
        print(f'Melhor global peso {listaMelhorLocal[0][0]}' 
        f'sendo a solução {listaMelhorLocal[0][1]}')

        #retornando peso do melhor global e retornando a melhor solução global
        return listaMelhorLocal[0][0] , listaMelhorLocal[0][1]

    def sa (self,asMax, T, t0, alpha ):

        #Gerar uma solução inicial *** FAzer aleatoria depois
        solucao = self.tspLCR(random.randint(0,len(tsp)-1))
        #inicializa iter e tInit
        iter = 0
        t = t0
        #inicializando solução global
        solucaoGlobal = list(range(0, len(tsp)))
        #Enquanto t menor que temperatura final
        while(t>T):
            #Loop referente ao asMax estabelecidado
            while (iter<asMax):

                iter+=1
                #soluçãoII é uma solução vinda de uma movimento aleatório na vizinhaça
                solucaoII = self.movimentoAletorioVizinhaca(solucao)
                # delta é gerado através da função objetivo relativo as soluções
                delta = self.somaSolucao(solucao)-self.somaSolucao(solucaoII)

                print(delta)

                #Caso delta positivo significa que solução inicial ainda é melhro que movimento
                if(delta>=0):
                    
                    #sendo delta maior igual a zero, significa que soluçãoII é menor que solução 
                    solucao = solucaoII
                        
                        #teste para ver se a solução é melhor que a global
                    if(self.somaSolucao(solucao)<self.somaSolucao(solucaoGlobal)):

                        solucaoGlobal = solucao
                else:

                    if(random.random()<e**(-delta/t)):
                        solucao=solucaoII


            t=alpha*t
            iter=0
        
        print(f'Melhor solução encontrada usando Simulated Annealing {solucaoGlobal} tendo o custo de {self.somaSolucao(solucaoGlobal)}')

        return solucaoGlobal

    # def inTabulits(solucao):

    #     if(self.tabuList(solucao)>=0):
    #         return true



    def tabuSeach(self,s0:list,stoppingCriteria,maxTabuSize):
        #
        sE= s0.copy()
        sB= s0.copy()
        self.tabuList = []
        self.tabuList.append(s0)
        count = 0
        #Criterio de parada
        while(stoppingCriteria!=count):
            sVizinhaca = self.pegaVizinhaca(sB)
            sB = sVizinhaca[0]

            for sCandidato in sVizinhaca:
                print(sCandidato in self.tabuList)
                print(f'soma sCandidato {self.somaSolucao(sCandidato)} e {self.somaSolucao(sB)}')
                #Testar se o elemento existe na tabulist e se função objetivo é melhor ou não
                if(False==(sCandidato in self.tabuList) and self.somaSolucao(sCandidato)<self.somaSolucao(sB) ):
                    print("Candidato não está na lista tabu e é melhor")
                    sB=sCandidato
                
                #Atualiza o s* (melhor global) com o valor de s barra
                sE = sB

                #coloca s barra na tabu list    
                self.tabuList.append(sB)

                #Se tabulist passar de um maximo tamanho estipulado retire um item dela
                if(len(self.tabuList)>maxTabuSize):
                    self.tabuList.pop(0)
            count+=1

        return sE






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
    #cv.grasp()
    #print(cv.sa(10,0.5,10,0.2))
    print(cv.tabuSeach([2,1,0, 3, 4],12,5))
