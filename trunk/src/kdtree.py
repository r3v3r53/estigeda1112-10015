# -*- coding: utf-8 -*-
# biblioteca para operação com árvores k-d balanceadas

# Autor - Pedro Moreira, 10015 (mail@pedromoreira.org)
# Data: 2012-04-27

# funcionalidades:
#   - construção da árvore a partir de uma lista de dados;
#   - junção de elementos;
#   - remoção de elementos;
#   - pesquisa do elemento mais próximo;

import random
import math
import LinkedList
from arvorebinariaRB import *
import time


    
class kdtree():
    '''
    o que a classe faz...
    '''

    def __init__(self, A = []):
        '''
        construtor, pode inicializar
        uma lista de dados e ordená-la
        '''
        self.A = A
        #self.heap
        #self.__balance__()
        if len(A) > 1:
            self.sort(self.A, 0, len(self.A) - 1)
        
    def __len__(self):
        return len(self.A)


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
        x = A[r].key
        i = p - 1
        for j in range(p, r):
            if A[j].key <= x:
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


   
    def printe(self):
        print self.__A

'''
A = [(1,1), (0,2), (1,2), (0,1), (0,3), (2,0), (2,3)]
x = kdtree(A)
print A
'''

t1 = time.clock()
nos = []

nos.append(No((3,1), "Renoir", None))
nos.append(No((1,2), "Van Gogh", None))
nos.append(No((2,3), "Picasso", None))
nos.append(No((1,3), "Manet", None))
nos.append(No((0,4), "Da Vinci", None))
nos.append(No((1,1), "Miguel Angelo", None))
nos.append(No((0,6), "Rafael", None))
nos.append(No((7,1), "Goya", None))
nos.append(No((9,9), "Turner", None))

arv = kdtree(nos)
for x in nos:
    print str(x)



arv = ArvoreRedBlack(len(nos[0].key))

x = math.floor(len(nos)/2)
a = x-1
z = x+1

for i in range(len(nos)):
    arv.insert(nos[i])
    
lista2 = []
arv.inorder_walk(arv.root, lista2)

for i in lista2:
    print i

#print arv.root
#print arv.search(arv.root, nos[2].key)
#a = arv.search(arv.root, (0,1))
#print "APAGAR"
#print arv.delete(nos[2])

#for x in range(len(lista)):
#    print str(x) + str(lista[x])

'''

t2 = time.clock();
print "CENA 1 = " + str(t2-t1)

nos = [None for k in range(9)]

nos[0] = No(11, "Renoir", None)
nos[1] = No(2, "van Gogh", None)
nos[2] = No(14, "Picasso", None)
nos[3] = No(1, "Manet", None)
nos[4] = No(7, "da Vinci", None)
nos[5] = No(15, "Miguel Angelo", None)
nos[6] = No(5, "Rafael", None)
nos[7] = No(8, "Goya", None)
nos[8] = No(4, "Turner", None)

arv = kdtree(nos)
for x in nos:
    print str(x)

arv = ArvoreRedBlack()
print "NIL"
print arv.nil
print nos[0] < nos[1]

t1 = time.clock()
arv.insert(nos[0])
arv.insert(nos[1])
arv.insert(nos[2])
arv.insert(nos[3])
arv.insert(nos[4])
arv.insert(nos[5])
arv.insert(nos[6])
arv.insert(nos[7])
arv.insert(nos[8])
t2 = time.clock();

print "insertion time: " + str(t2-t1) 
print "INORDER"
lista = []
arv.inorder_walk(arv.root, lista)
for x in lista:
    print x

print "CENA 2 = " 
print "DEPOIS"
arv.rb_delete(nos[4])
lista = []
arv.inorder_walk(arv.root, lista)
for x in lista:
    print x
'''