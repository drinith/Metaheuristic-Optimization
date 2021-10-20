#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
#gerador aleatório de matriz
def matrixGenerateValues(size,min,max):

    matrix = [[0 for i in xrange(size)] for i in xrange(size)]

    for r in range (len(matrix)):
        for c in range (len(matrix)):
            ran = random.randint(min,max)
            if(r>c):
                matrix[r][c]=ran
                matrix[c][r]=ran
            elif(r==c):
                 matrix[r][c]=0

            
    return matrix


if __name__=="__main__":
    
    print(matrixGenerateValues(5,10,100))


