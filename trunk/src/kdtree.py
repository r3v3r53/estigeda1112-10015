# -*- coding: utf-8 -*-
# biblioteca para operação com árvores k-d balanceadas

# Autor - Pedro Moreira, 10015 (mail@pedromoreira.org)
# Data: 2012-04-17

# funcionalidades:
#   - construção da árvore a partir de uma lista de dados;
#   - junção de elementos;
#   - remoção de elementos;
#   - pesquisa do elemento mais próximo;

import random

class kdtree:
    '''
    o que a classe faz...
    '''

    def __init__(self, A = []):
        '''
        construtor, pode inicializar
        uma lista de dados e ordená-la
        '''
        self.__A = A
        self.__balance__()
        pass

    #################################################
    # ORDENAR A LISTA
    
    def printSorted(self):
        '''
        obter cópia da lista ordenada
        '''
        #utilizando quicksort
        B = self.__A
        self.__randomizedQuicksort__(B, 0, len(self.__A) - 1)
        print B
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
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
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
            self.__randomizedQuicksort__(A, p, q - 1)
            self.__randomizedQuicksort__(A, q + 1, r)
            pass
        pass
    # FIM DO RANDOMIZED QUICKSORT
    #################################################


    #################################################
    # Balancear árvore

    def __balance__(self):
        """
        Balancear a árvore com o heap sort
        para optimizar as operações
        a efectuar com a lista
        """    
        pass
    # FIM DO BALANCEAR ÁRVORE
    #################################################
    
    def merge(self, A, B):
        '''
        fazer a junção de duas listas
        '''
        pass
    
    def search(self, A, k):
        '''
        pesquisar um elemento numa lista
        '''
        pass

    def insert(self, A, k):
        '''
        inserir um valor numa lista, ordenando-a
        '''
        pass

    def delete(self, A, k):
        '''
        eliminar um elemento da lista
        '''
        pass
    
    pass
