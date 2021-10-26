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

    #Cria uma lista de soluções aleatórias com um determinado número de cidades
    def algoritmoRotaAleatoria(self,qtCidades,rotasMatriz):
        
        listaIndicesCidade = list(range(len(rotasMatriz)))#cria uma lista de componentes com os index passados pelo range da Matriz
        rotaRandomica = []#lista de solução

        for i in range(qtCidades):#for em cima da dimensão da matriz
            #gerar o valor da cidade para a solução aleatoria
            cidadeRandomica = random.randint(0, len( listaIndicesCidade) - 1)
            #adicionar o código da cidade dentro da solução
            rotaRandomica.append(cidadeRandomica)
            #remover o código da cidade para ele não entrar mais na solução
            listaIndicesCidade.remove(cidadeRandomica)

        return rotaRandomica #retorna uma primeira solução possível


    def heuristicadaInsercaoMaisBarata (self,qtCidades,rotasMatriz):

        #buscando uma rota possível com valores de cidades determinado
        rota = self.algoritmoRotaAleatoria(qtCidades,rotasMatriz)
        
        #teste
        # rota = [0,1,2]
        
        #pegando a lista de indices de todas cidades    
        listaIndicesCidade = list(range(len(rotasMatriz)))
        
        #cidades não visitadas
        cidadeNaoVisitadas = list(set(listaIndicesCidade) - set(rota))
        
        #caminhar em cada passo da rota gerada e pegar os calores dos pesos dos vertices e comparar com uma possivel entrada
        for i in range(len(rota)-1):
            
            #pegar valor do vertice atual
            valorVertice = rotasMatriz[rota[i]][rota[i+1]]
            
            #pegar uma cidade não visitada randomicamente
            cidadeRandomicaNaoVisitada = cidadeNaoVisitadas[random.randint(0,len(cidadeNaoVisitadas)-1)]
            #cidadeRandomicaNaoVisitada = 3 #teste do valor amarrado
            #pegar o valor dos vertices entre essa cidade e as outras duas que estavam ligadas
            valorVerticePrim = rotasMatriz[i][cidadeRandomicaNaoVisitada]
            valorVerticeSegun = rotasMatriz[cidadeRandomicaNaoVisitada][i+1]
            
            #testar para ver se a soma dos vertices novos é menor que o antigo
            if(valorVerticePrim+valorVerticeSegun<valorVertice):
                print('É possível de inserir')
                rotaNova = rota[0:i+1]+[cidadeRandomicaNaoVisitada]+rota[i+1:len(rota)]




    #Algoritmo Construtivo Vizinho Mais Proximo
    def algoritmoConstrutivoListaVizinhoMaisProximo(self,rotasMatriz,objetivo):
        #1. Inicia-se uma rota vazia
        rota = []
        
        #lista das cidades visitadas 
        cidadeVisitada =list(range(0, len(rotasMatriz)))
        
                
        #2. Adiciona-se a cidade de origem à rota
        cidade = random.randint(0,len(rotasMatriz)-1)
        #cidade =3

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
                
                    
            #cidade passa a ser a melhor cidade no próximo salto
            cidade= cidadeMelhor
            #indice da cidade entra para a lista da rota
            rota.append(cidadeMelhor)
            #dizer que o indice daquela cidade foi visitado
            cidadeVisitada[cidade]="visitada"
            
        print(rota)

#teste
if __name__=="__main__":
    #cidade 1 [1,2,3,0] 3[3,0,2,1] 2[2, 0, 3, 1] 3[3, 0, 2, 1]

    #teste [0,1,2] coloco o 3 entre 0 e 1 [0,3,1,2]
    rotasMatriz = [
        [0, 900, 100, 300],
        [900, 0, 200, 450],
        [100, 200, 0, 400],
        [300, 450, 400, 0]
    ]
    #gerando uma matriz randomica 
    objetivo = 0
    cv = CaixeiroViajante()
    #cv.algoritmoConstrutivoListaVizinhoMaisProximo(rotasMatriz,objetivo)
   # print(cv.algoritmoRotaAleatoria(3,rotasMatriz))
    cv.heuristicadaInsercaoMaisBarata(3,rotasMatriz)
    print('fim')