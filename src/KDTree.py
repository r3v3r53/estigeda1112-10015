#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
autor: Pedro Moreira, 10015
data: 3 de Junho de 2012

kd-tree
operações:
- criar árvore a partir de uma lista
- inserir
- apagar 
- pesquisa
- pesquisa do nó mais próximo
- pesquisa do menor elemento
- pesquisa do maior elemento
- pesquisa do elemento seguinte  
'''
from Quicksort import *
from No import *
from RBT import *

class KDTree(object):
	'''
	Estrutura de dados kdtree
	'''
	def __init__(self, dimention):
		'''
		Construtor
		@param dimention dimensao da chave para ordenação dos dados
		'''
		self.nil = No(None, None)
		self.parent = self.left = self.right = self.root = self.nil
		self.dimention = dimention

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
				return self.searchByValue(x.left, k)
			else:
				return self.searchByValue(x.right, k)

	def searchByKey(self, x, k):
		'''
		Pesquisar nó
		'''
		if x == self.nil or k == x.key:
			return x
			if k < x.key:
				return self.searchByKey(x.left, k)
			else:
				return self.searchByKey(x.right, k)
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
        pass

	def maximum(self, x):
		'''
		Encontrar o maior elemento na árvore com raiz em x
		@param x árvore a pesquisar
		@return maior elemento
		'''
		while x.right != self.nil:
			x = x.right
		return x
        pass

	def sucessor(self, x):
		'''
		Encontrar o elemento seguinte
		@param x nó a partir do qual se efectua a pesquisa
		@return nó seguinte ou null no caso de o próprio ser o maior da árvore
		'''
		if x.right != self.nil:
			return self.minimum(x.right)
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

	def insert(self, a, z):
		'''
		Inserir Nó na árvore
		@param z nó a inserir
		'''
		z.parent = self.nil
		z.left = self.nil
		z.right = self.nil

		y = self.nil
		x = self.root

		dim = -1
		while x != self.nil:
			dim = (dim + 1) % self.dimention
			y = x
			if z.key[dim] < x.key[dim]:
				x.LC += 1
				x = x.left
			else:
				x.RC += 1
				x = x.right
			if abs(x.RC - x.LC) > self.dimention:
				self.fixTree(x, z)
		z.parent = y
		if y == self.nil:
			self.root = z
		elif z.key[dim] < y.key[dim]:
			y.left = z
		else:
			y.right = z
		z.dim = dim
		pass

	def fixTree(self, x, z):
		'''
		o berbicacho está aqui!!!
		'''
		dim = x.dim
		lista = []
		arvore = RBT()
		if x != self.nil:
			print x
			self.inorderWalk(x, lista)
			for i in lista:
				arvore.insere(i)
			lista2 = []
			arvore.inorderWalk(arvore.root, lista2)
			print "$#$#$#$#$#$##$"
			#for i in lista2:
			#	print i
			print "--------------------"
		'''arvores = []
		for i in range(self.dimention):
			arvores.append ArvoreRedBlack()
		
		lista = []
		self.kinorderWalk(x, lista)
		arv = ArvoreRedBlack()
		print "#############################"
		for i in lista:
			arv.insert(i)

		lista = []
		arv.inorder_walk(arv.root, lista)
		for i in lista:
			print i

		print "#############################"

		pass
		'''

no = No((0,0), "Pedro")
a = KDTree(2)
a.insert(a.root, no)
print a.root

b = RBT()
b.insere(no)

a.insert(a.root, b.root)
print b.root
print a.root == b.root
lista = []
b.inorderWalk(b.root, lista)
for i in lista:
	print i
'''
no = []
a = KDTree(2)


no.append(No((1,1), "Pedro"))
no.append(No((0,1), "Miguel"))
no.append(No((2,1), "Clemente"))
no.append(No((2,2), "Clemente"))
no.append(No((2,4), "Clemente"))
no.append(No((1,0), "Miguel"))
no.append(No((2,3), "Miguel"))
no.append(No((0,4), "Miguel"))
no.append(No((0,2), "Miguel"))
no.append(No((0,3), "Miguel"))
no.append(No((3,2), "Miguel"))
no.append(No((1,2), "Miguel"))

for i in no:
	a.insert(a.root, i)

lista = []
a.inorderWalk(a.root, lista)
for i in lista:
	print i
'''