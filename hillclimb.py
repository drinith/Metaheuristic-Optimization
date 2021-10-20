import random

class HillClimb:

    #Matriz de rotas onde as posições da matriz são as cidades e os valores são os custos das rotas
    route = []

    #Matriz de beneficios da facility
    beneficio = []

    def __init__(self,routeEx):
        self.route = routeEx


    #soluções randomicas
    def randomSolution(self,route):
        
        facility = list(range(len(self.route)))#cria uma lista de componentes com os index passados pelo range da Matriz
        solution = []#lista de solução

        for i in range(len(self.route)):#for em cima da dimensão da matriz
            #gerar o valor da cidade para a solução aleatoria
            randomFacility = facility[random.randint(0, len(facility) - 1)]
            #adicionar o código da cidade dentro da solução
            solution.append(randomFacility)
            #remover o código da cidade para ele não entrar mais na solução
            facility.remove(randomFacility)

        return solution #retorna uma primeira solução possível


    #Somando o valor das soluções
    def routeLength(self, solution):
        routeLength = 0
        # vai percorrer as soluções através dos indices das cidades
        for i in range(len(solution)):
            #indice das cidades na lista de solução onde a combinação de uma indice com o outro dará a posição da matriz que está os pesos 
            routeLength += self.route[solution[i - 1]][solution[i]]
        return routeLength


    def getNeighbours(self,solution):
        neighbours = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                #criação de um vizinho apartir da lista de solução
                neighbour = solution.copy()
                #troca das posições do vizinho  
                neighbour[i] = solution[j]
                neighbour[j] = solution[i]
                #guarda em uma lista de vizinhaça
                neighbours.append(neighbour)
        return neighbours

    def hillClimbSolution(self):
        #busco uma solução possível
        solution = self.randomSolution(self.route)
        #busco a vizinha de soluções possíveis
        neighborList = self.getNeighbours(solution)
        #busco peso possível da solução
        sLength = self.routeLength(solution)
        print('Para uma possível solução')
        print(solution)
        #Rodar a lista de soluções vizinhas possíveis e ver se elas são melhores que a primeira e qual é a melhor entre elas
        for nSolution in neighborList:
            #pegando o peso de uma nova solução
            newLength = self.routeLength(nSolution)
            #comparar com o peso da melhor até agora 
            if(sLength>newLength):
                #peso da melhor solução recebe o peso da Nova
                sLength = newLength
                #melhor solução recebe a Nova
                solution = nSolution

        print('A melhor solução vizinha é ')
        print(solution)
        return solution




#teste
if __name__=="__main__":

    route = [
        [0, 800, 500, 300],
        [800, 0, 200, 500],
        [500, 200, 0, 600],
        [300, 500, 600, 0]
    ]

    hc = HillClimb(route)
    hc.hillClimbSolution()
   
    print('fim')