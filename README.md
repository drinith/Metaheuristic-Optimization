# Metaheuristic-Optimization
Metaheuristic Optimization

## Algoritmos Construtivos

### Exemplo Caixeiro Viajante Simétrico
#### Heurística do Vizinho Mais Próximo
1. Inicia-se uma rota vazia
2. Adiciona-se a cidade de origem à rota
3. Escolhe, dentre todas as cidades que ainda não foram
visitadas, a cidade i que tiver a menor distância para a
última cidade inserida na rota.
4. Adicione i à rota.
5. Caso exista cidade não visitada, retorne ao passo 3.
Senão, encerre o algoritmo.


### Exemplo Caixeiro Viajante Simétrico
#### Heurística da Inserção Mais Barata
1. Construir uma rota passo a passo, partindo de uma rota
inicial envolvendo 3 cidades (obtidas por qualquer
método).
2. Adicionar a cada passo, a cidade k (ainda não visitada)
entre as cidades i e j, cujo custo de inserção (distância)
seja o mais barato.


#### Lista de Candidatos Restrita
1. Seja ci o critério guloso referente a inserção de um elemento i
na solução corrente.
2. Define-se então hmin = min ci , hmax = max c i , α ∈ [0,1] e
 
LCR = {i | hmin ≤ ci ≤ hmax + α(hmin − hmax )}

3. Uma vez tendo construído a LCR, escolhe-se aleatoriamente
um elemento pertencente a ela.