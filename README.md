# Metaheuristic-Optimization
Metaheuristic Optimization

## Algoritmos Construtivos

#### Lista de Candidatos Restrita

>"Candidate list strategies correspond to different techniques that make it possible to implement local search methods in the most efficient ways by dealing faster or with fewer neighbors instead of the full neighborhood. Basically, these candidate
list strategies provide a number of techniques to speed up the local search either by restraining the number of neighbors investigated (for instance, when the neighborhood is very large) or by avoiding repetitive computations that can be saved from
one iteration to the next (typically, whenever the computation of the objective function is expensive)"[Mauricio,2016].

![Isso é uma imagem](https://github.com/drinith/Metaheuristic-Optimization/blob/main/RCL.png) [Mauricio,2016]


1. Seja ci o critério guloso referente a inserção de um elemento i na solução corrente.

2. Define-se então hmin = min ci , hmax = max c i , α ∈ [0,1] e LCR = {i | hmin ≤ ci ≤ hmax + α(hmin − hmax )}

3. Uma vez tendo construído a LCR, escolhe-se aleatoriamente
um elemento pertencente a ela.





## Referência
Resende, Mauricio GC, and Celso C. Ribeiro. Optimization by  GRASP. Springer Science+ Business Media New York, 2016.