#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
autor: Pedro Moreira, 10015
data: 3 de Junho de 2012

kd-tree
operaÃ§Ãµes:
- criar Ã¡rvore a partir de uma lista
- inserir
- apagar 
- pesquisa
- pesquisa do nÃ³ mais prÃ³ximo
- pesquisa do menor elemento
- pesquisa do maior elemento
- pesquisa do elemento seguinte  
'''
from Quicksort import *
from No import *
import math
import sys



class KDTree(object):
  '''
  Estrutura de dados kdtree
  '''
  def __init__(self, dimention):
    '''
    Construtor
    @param dimention dimensão da chave para ordenação dos dados
    '''
    sys.setrecursionlimit(10000)
    self.nil = No(None, None)
    self.parent = self.left = self.right = self.root = self.nil
    self.dimention = dimention
    self.stack = []
    self.lista = []
    self.lista2 = []
    

  def insert(self, a, z, balance = True):
    cont = 1
    z.parent = self.nil
    z.left = self.nil
    z.right = self.nil
    z.LC = z.RC = 0

    y = self.nil
    x = a
    dim = -1


    while x != self.nil:
      if x.key == z.key:
        x.valor = z.valor
        break

      dim = (dim + 1) % self.dimention

      y = x
      if z.key[dim:] < x.key[dim:]:
        x.LC += 1
        if balance:
          if min(x.LC, x.RC) <= (2**math.ceil(math.log(max(x.RC, x.LC),2)))/2 - 1:
            self.insertFixUp(x, z)
            cont = 0
            break
        x = x.left
      else:
        x.RC += 1
        if balance:
          if min(x.LC, x.RC) <= (2**math.ceil(math.log(max(x.RC, x.LC),2)))/2 - 1:
            self.insertFixUp(x, z)
            cont = 0
            break
        x = x.right
    if cont == 1:
      z.parent = y



      if y == self.nil:
        self.root = z
      elif z.key[dim:] < y.key[dim:]:
        y.left = z
      else:
        y.right = z
    

  def __clear(self, x, i):
    if x == self.root:
      self.root = self.nil
    else:
      z = x
      while(z != self.nil):
        if z.parent.left == z:
          z.parent.LC -= i

        else:
          z.parent.RC -= i
        z = z.parent

      if x.parent.left == x:
        x.parent.left = self.nil
      else:
        x.parent.right = self.nil

  def __clearCount(self, x, i):
    '''
    na me lembro pra ke raio keria isto!!! 
    '''
    z = x
    while(z != self.nil):
      if z.parent.left == z:
        z.parent.LC -= i
      else:
        z.parent.RC -= i
      z = z.parent

    if x.parent.left == x:
      x.parent.left = self.nil
    else:
      x.parent.right = self.nil

  def delete(self, z):
    if z.parent != self.nil:
      if z.parent.left == z.key:
        z.parent.left = self.nil
        z.parent.LC = 0
      else:
        z.parent.right = self.nil
        z.parent.RC = 0
    lista = []
    self.inorderWalk(z.left, lista)
    self.inorderWalk(z.right, lista)
    for i in lista:
      self.insert(self.root, i)
    z.parent = z.left = z.right = self.nil
    z.LC = z.RC = 0
    pass

  def searchByValue(self, x, k):
    '''
    pesquisar por valor
    @param x nó a partir do qual se efectua a pesquisa
    @param k valor a pesquisar
    @return nó com o resultado
    '''
    if x == self.nil or k == x.valor:
      return x
      if k < x.key:
        return self.search(x.left, k)
      else:
        return self.search(x.right, k)

  def searchByKey(self, x, k):
    '''
    Pesquisar nó pela chave
    '''
    if x == self.nil or k == x.key:
      return x
      if k < x.key:
        return self.search(x.left, k)
      else:
        return self.search(x.right, k)
    pass

  def minimum(self, x):
    '''
    Encontrar o menor elemento na árvore com raiz em x
    @param x árvore a pesquisar
    @return menor elemento
    '''
    while x.left != self.nil:
      x = x.left
    return x

  def maximum(self, x):
    '''
    Encontrar o maior elemento na árvore com raiz em x
    @param x árvore a pesquisar
    @return maior elemento
    '''
    while x.right != self.nil:
      x = x.right
    return x

  def sucessor(self, x):
    '''
    Encontrar o elemento seguinte
    @param x nó a partir do qual se efectua a pesquisa
    @return nó seguinte ou null no caso de o próprio ser o maior da árvore
    '''
    if x.right != self.nil:
      return minimum(x.right)
    y = x.parent
    while y != self.nil and x == y.right:
      x = y
      y = y.parent
    return y
    pass

  def inorderWalk(self, x, lista):
    '''
    Percorrer a árvore devolvendo uma lista ordenada com os nós
    @param x nó a partir do qual se constrói a lista
    @param lista para guardar os dados
    '''
    if x != self.nil:
      self.inorderWalk(x.left, lista)
      lista.append( x )
      self.inorderWalk(x.right, lista)


  def insertFixUp(self, x, z):
    '''
    o berbicacho está aqui!!!
    '''
    #print "ALERTA A ARVORE TA COXA EM " + str(x.key) + " NA INSERCAO DE " + str(z.key)
    self.lista = []
    self.lista.append(z)
    self.inorderWalk(x, self.lista)
    #self.insert(x, z, False)
    
    
    self.__clear(x, x.LC + x.RC + 1)
    Quicksort(self.lista)
    #for i in self.lista:
    #  self.insert(self.root, i, False)
    
    self.stack.append(self.lista)
    self.__reInsert()

  def __reInsert(self):

    a = self.stack.pop(0)
    if len(a) == 1:
      self.insert(self.root, a.pop(0), False)
    elif len(a) == 0:
      pass
    else:
      k = int(math.floor(len(a)/2))
      x = a.pop(k)
      x.parent = x.left = x.right = None
      self.insert(self.root, x, False)
      b = a[:k]
      if len(b) > 0: self.stack.append(b)
      b = a[k:]
      if len(b) > 0: self.stack.append(b)
    if len(self.stack) > 0:
      self.__reInsert()

  def nearestNeighbour(self, no):
    '''
    Percorre todos os elementos da árvore e calcula a distancia eucladiana 
    devolve o no com menor distancia
    @param no No que pretendemos fazer a pesquisa
    @return No mais proximo do fornecido
    '''
    lista = [] 
    self.inorderWalk(self.root, lista)
    distancia = sys.maxint
    x = self.nil
    for i in lista:
      if no != i:
        temp = 0
        for k in range(self.dimention):
          temp += (i.key[k] - no.key[k])**2
        temp = math.sqrt(temp)
        if distancia > temp:
          distancia = temp
          x = i
    return x




   
no = []
a = KDTree(2)


no.append(No((1,1), "Pedro"))
no.append(No((0,1), "Miguel"))
no.append(No((2,1), "Clemente"))
no.append(No((2,2), "Clemente"))
no.append(No((1,0), "Miguel"))
no.append(No((2,4), "Clemente"))
no.append(No((2,3), "Miguel"))
no.append(No((0,4), "Miguel"))
no.append(No((0,2), "Miguel"))
no.append(No((0,3), "Miguel"))
no.append(No((3,2), "Miguel"))
no.append(No((1,2), "Miguel"))

#Quicksort(no)
for i in no:
  a.insert(a.root, i)

#a.insert(a.root, a.stack[1][0])

print 
print
print
lista = []
a.inorderWalk(a.root, lista)
for i in lista:
  print i

print 
print

print
print no[1]
print a.nearestNeighbour(no[1])
