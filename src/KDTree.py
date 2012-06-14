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

class KDTree(object):
  '''
  Estrutura de dados kdtree
  '''
  def __init__(self, dimention):
    '''
    Construtor
    @param dimention dimensão da chave para ordenação dos dados
    '''
    self.nil = No(None, None)
    self.parent = self.left = self.right = self.root = self.nil
    self.dimention = dimention
    self.stack = []
    self.lista = []
    self.lista2 = []

  def insert(self, a, z, balance = False):
    z.parent = self.nil
    z.left = self.nil
    z.right = self.nil
    z.LC = z.RC = 0

    y = self.nil
    x = self.root
    dim = -1

    while x != self.nil:
      dim = (dim + 1) % self.dimention
      #print
      #print
      #print x.key, x.key[dim:]
      #print z.key, z.key[dim:]
      
      #print dim

      y = x
      if z.key[dim:] < x.key[dim:]:
        #print "LEFT"
        x = x.left
      else:
        #print "RIGHT"
        x = x.right
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
   
'''
    #self.lista = []
    if x == self.nil:
      x = self.root
    self.lista.append(z)
    self.inorderWalk(x, self.lista)
    self.__clear(x, x.LC + x.RC + 1)
    self.__rebuild()


  def __rebuild(self):
    self.stack = []
    Quicksort(self.lista)
    self.stack.append(self.lista)
    self.__reInsert()

  def __reInsert(self):
    self.lista = []
    if len(self.stack) > 0:
      temp = self.stack.pop(0)
      if len(temp) > 1:
        x = int(math.floor(len(temp)/2))
        k = temp.pop(x)
        self.stack.append(temp[:x])
        self.stack.append(temp[x:])
        self.insert(self.root, k, False)
      elif len(temp) == 1:
        self.insert(self.root, temp[0], False)
    else:
      self.__checkBalance()

  def __checkBalance(self):
    stack = []
    stack.append(self.root)
    while len(stack) > 0:
      x = stack.pop(0)
      if x != self.nil:
        if x.left != self.nil: stack.append(x.left)    
        if x.right != self.nil: stack.append(x.right)
        if x.LC + x.RC > 0:
          if min(x.LC, x.RC) <= (2**math.ceil(math.log(max(x.RC, x.LC),2)))/2 - 1:
            self.insertFixUp(x.parent, x)
'''

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

lista = []
a.inorderWalk(a.root, lista)
for i in lista:
  print i
print
print 
print

print "LISTA"
for i in a.lista:
  print i

print "STACK"
for i in a.stack:
  print"-"
  for j in i:
    print j