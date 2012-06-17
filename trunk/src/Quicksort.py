#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
autor: Pedro Moreira, 10015
data: 31 de maio de 2012

algoritmo quicksort
'''
import random
class Quicksort():
    '''
    o que a classe faz...
    '''

    def __init__(self, A = [], dim = 0):
        '''
        construtor, pode inicializar
        uma lista de dados e ordena-la
        '''
        self.A = A
        self.dim = dim
        if len(A) > 1:
            self.sort(self.A, 0, len(self.A) - 1)

    #################################################
    # ORDENAR A LISTA
    
    def sort(self, A, p, q):
        '''
        ordenar lista
        '''
        #utilizando quicksort
        self.__randomizedQuicksort__(A, p, q)
        pass
        
    #################################################
    # livro pag 177
    # RANDOMIZED PARTITION

    def __randomizedPartition__(self, A, p, r):
        i = random.randint(p,r)
        A[r], A[i] = A[i], A[r]
        return self.__partition__(A, p, r)
    # FIM DO RANDOMIZED PARTITION
    #################################################


    #################################################
    # livro pag 169
    # PARTITION

    def __partition__(self, A, p, r):
        x = A[r].key[self.dim:]
        i = p - 1
        for j in range(p, r):
            if A[j].key[self.dim:] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
                pass
            pass
        A[i+1], A[r] = A[r], A[i+1]
        return i+1
    # FIM DO PARTITION
    #################################################

    
    #################################################
    # livro pag 177
    # RANDOMIZED QUICKSORT

    def __randomizedQuicksort__(self, A, p, r):
        if p < r:
            q = self.__randomizedPartition__(A, p, r)
            #q = self.__partition__(A, p, r)
            self.__randomizedQuicksort__(A, p, q - 1)
            self.__randomizedQuicksort__(A, q + 1, r)
            pass
        pass
    # FIM DO RANDOMIZED QUICKSORT
    #################################################
