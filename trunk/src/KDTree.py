#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
autor: Pedro Moreira, 10015
data: 16 de Junho de 2012

kd-tree
operacoes:
- criar arvore a partir de uma lista
- inserir
- apagar 
- pesquisa do no mais proximo




USAGE:

criar uma arvore para 1000 nos e 3 dimensoes na chave:
arvore = KDTRee(1000, 3)

inserir um no na arvore
no = No((0,0,0), "valor")
arvore.malloc(no)

procurar o no mais proximo
maisProximo = arvore.maisProximo(no)

eliminar um no
arvore.freeNo(no)


'''
from Quicksort import *
from No import *
import math
import sys

class KDTree(object):
  '''
  Estrutura de dados kdtree
  '''
  def __init__(self, size, dimention):
    '''
    Construtor
    @param dimention dimensao da chave para ordenacao dos dados
    @ param size tamanho da arvore
    '''
    #sys.setrecursionlimit(10000)
    self.root = self.nil = No(None, None)
    self.dimention = dimention
    self.stack = []
    self.lista = []
    self.free = [i for i in range(size)]
    self.pointers = [None for i in range(size)]

  def malloc(self, no):
    '''
    Tentar a alocacao de um No na arvore
    @param no Objecto a ser inserido na arvore
    @return -1 em caso de erro ou o no ja inserido na arvore
    '''
    if len(self.free) > 0:
      x = self.free.pop()
      self.pointers[x] = no.key
      no.pointer = x
      self.insert(self.root, no)
      return no
    else:
      print "out of space"
      return -1

  def freeNo(self, x):
    '''
    Eliminar no da arvore
    @param x no a Eliminar
    @return -1 caso o no nao exista ou 0 se a operacao correr com sucesso
    '''
    if self.pointers[x.pointer] != None:
      self.pointers[x.pointer] == None
      self.free.append(x.pointer)
      self.delete(x)
      return 0
    else:
      return -1

  def insert(self, a, z, balance = True):
    '''
    Inserir no na arvore
    @param a local a inserir o no
    @param z no a inserir
    @param balance informacao para balancear ou nao a arvore (true por defeito)
    '''
    z.parent = self.nil
    z.left = self.nil
    z.right = self.nil
    z.LC = z.RC = 0

    y = self.nil
    x = a
    dim = -1

    while x != self.nil:
      dim = (dim + 1) % self.dimention
      if x.key == z.key:
        x.valor = z.valor
        break

      z.dim = dim
      y = x
      if z.key[dim:] < x.key[dim:]:
        x.LC += 1
        x = x.left
      else:
        x.RC += 1
        x = x.right
    z.parent = y
    if y == self.nil:
      self.root = z
    elif z.key[dim:] < y.key[dim:]:
      y.left = z
    else:
      y.right = z
    
    if balance:
      self.checkBalance()

  def __clear(self, x):
    '''
    Contar os nos sucessores ao no pretendido
    e percorrer todos os seus antecessores retirando a respectiva contagem
    @param x no a partir do qual sera para limpar as contagens
    '''
    if x == self.root:
      self.root = self.nil
    else:
      z = x
      i = x.RC + x.LC + 1
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

  def inorderWalk(self, x, lista):
    '''
    Percorrer a arvore devolvendo uma lista ordenada com os nos
    @param x no a partir do qual se constroi a lista
    @param lista para guardar os dados
    '''
    if x != self.nil:
      self.inorderWalk(x.left, lista)
      lista.append( x )
      self.inorderWalk(x.right, lista)


  def __reInsert(self):
    '''
    Metodo para voltar a inserir na arvore nos 
    que tenham sido retirados por motidos de balanceamento
    '''
    if len(self.stack) > 0:
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
        if len(b) > 0: 
          self.stack.append(b)
        b = a[k:]
        if len(b) > 0: 
          self.stack.append(b)
      if len(self.stack) > 0:
        self.__reInsert()
    else:
      self.checkBalance()

  def nearestNeighbour(self, no):
    '''
    Percorre todos os elementos da arvore e calcula a distancia eucladiana 
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

  def isBalanced(self, x):
    '''
    verificar se o numero de sucessores para cada lado 
    do no em causa corresponde a dois ramos com a mesma altura
    @param x no a analisar
    '''
    a = x.LC
    b = x.RC
    if (a+b) < 2 : return True
    if (a+b) <= 4 and min(a,b) == 1: return True
    return min(a, b) > 2**(int(math.floor(math.log(max(a,b),2))))-1


  def checkBalance(self):
    '''
    percorrer todos os nos para 
    verificar se a arvore esta balanceada
    caso existam problemas, os nos sao retirados 
    e ordenados para serem reinseridos na arvore
    '''
    if self.root == self.nil:
      return
    stack = []
    stack.append(self.root)
    while len(stack) > 0:
      x = stack.pop(0)
      if x.left   != self.nil : stack.append(x.left)
      if x.right  != self.nil : stack.append(x.right)

      if self.isBalanced(x): continue
      parent = x.parent
      dim = x.dim
      self.__clear(x)
      lista = []
      self.inorderWalk(x, lista)
      Quicksort(lista, (dim + 1) % self.dimention)
      self.stack.append(lista)
      self.__reInsert()
    pass

  def delete(self, z):
    '''
    Eliminar um no e colocar todos os seus sucessores
    na lista para serem reinseridos na arvore
    @param z no a ser eliminado
    '''
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
    self.stack.append(lista)
    
    z.parent = z.left = z.right = self.nil
    z.LC = z.RC = 0
    self.__reInsert()
    self.checkBalance()
    pass
