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
import math

class KDTree(object):
	'''
	Estrutura de dados kdtree
	'''
	def __init__(self, dimention):
		'''
		Construtor
		@param dimention dimensao da chave para ordenação dos dados
		'''
		self.nil		= No(None, None)
		self.root		= self.nil
		self.dimention	= dimention
		self.check		= True

	def delete(self, z):
		if z.parent != self.nil:
			if z.parent.left == z.key:
				z.parent.left	= self.nil
				z.parent.LC		= 0
			else:
				z.parent.right	= self.nil
				z.parent.RC 	= 0
		lista = []

		self.inorderWalk(z.left,	lista)
		self.inorderWalk(z.right,	lista)
		
		for i in lista:
			self.insert(self.root, i)
		
		z.parent = z.left = z.right = self.nil
		z.LC = z.RC = 0

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
		while x.left != self.nil: x = x.left
		return x

	def maximum(self, x):
		'''
		Encontrar o maior elemento na árvore com raiz em x
		@param x árvore a pesquisar
		@return maior elemento
		'''
		while x.right != self.nil: x = x.right
		return x

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

	def insert(self, z):
		'''
		Inserir Nó na árvore
		@param z nó a inserir
		'''
		z.parent = self.nil
		z.left = self.nil
		z.right = self.nil
		z.LC = z.RC = 0

		y = self.nil
		x = self.root

		dim = -1
		while x != self.nil:
			dim = (dim + 1) % self.dimention
			z.dim = dim
			y = x
			if z.key[dim] < x.key[dim]:
				x.LC += 1
				if abs(x.RC - x.LC) > self.dimention and self.check:
					self.fixTree(x, z)
				else:
					x = x.left

			elif z.key[dim] > x.key[dim]:
				if abs(x.RC - x.LC) > self.dimention and self.check:
					pass#self.fixTree(x, z)
				else:
					x.RC += 1
				x = x.right
			else:
				break
		z.parent = y
		if y == self.nil:
			self.root = z
		elif z.key[dim] < y.key[dim]:
			y.left = z
		else:
			y.right = z
		
		pass

	def fixTree(self, x, z):
		'''
		o berbicacho está aqui!!!
		'''
		
		#self.check = False


		if x.parent != self.nil:
			if x.parent.left == x:
				x.parent.left = self.nil
				x.parent.LC -= x.LC + x.RC
			else:
				x.parent.right = self.nil
				x.parent.RC -= x.LC + x.RC
		else:
			self.root = self.nil

		lista = []
		self.inorderWalk(x, lista)
		r = RBT();
		#Quicksort(lista, x.dim)

		for i in lista:
			r.RBTInsert(i)
		'''
		pilha = []
		pilha2 = []
		pilha.append(lista)
		
		while len(pilha) > 0:
			a = pilha.pop(0)

			if len(a) > 1:
				x = int(math.floor(len(pilha)/2))
				pilha.append(a[:x])
				pilha.append(a[x+1:])
				pilha2.append(a[x])
			if len(a) == 1:
				pilha2.append(a[0])

		for i in pilha2:
			print i
		#self.check = True
		'''
		'''
			#self.insert(x)
		'''
		
		'''
		
		lista = []
		a = rb.root
		lista.append(a) 
		while len(lista) > 0:
			a = lista.pop(0)

			if a.left != rb.nil:
				lista.append(a.left)
			if a.right != rb.nil:
				lista.append(a.right)
			if a != rb.nil:
				self.insert(a)
		#limpar contagens
		a = x.parent
		y = x
		if a != self.nil:
			apaga = y.LC + y.RC
			while a != self.nil:
				if a.left == y:
					a.LC -= y.LC + y.RC
				else: a.RC -= apaga
				y = a
				a = a.parent
			if x.parent.left == x:
				x.parent.left = self.nil
			else:
				x.parent.right = self.nil
		'''
'''
		dim = x.dim

		x.LC = 0
		x.RC = 0
		lista = []
		arvore = RBT()
		if x != self.nil:
			self.inorderWalk(x, lista)

		for i in lista:
			print i
		'''
'''
			for i in lista:
				i.LC = 0
				i.RC = 0
				arvore.RBTInsert(i)

			stack = []
			a = arvore.root
			if a != arvore.nil:
				stack.append(a)
				y = a
				#while len(stack) > 0:
				while y.left != arvore.nil and y.right != arvore.nil:
					y = stack.pop(0)
					if y.left != arvore.nil:
						stack.append(y.left)
					if y.right != arvore.nil:
						stack.append(y.right)
					#self.insert(self.root, y)
arvores = []
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

no = []
a = KDTree(2)

b = RBT()
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
no.append(No((1,2), "Miguel"))

for i in no:
	b.RBTInsert(i)


lista = []
lista2 = []
lista.append(b.root)
while len(lista) > 0:
	x = lista.pop(0)
	print str(x) + ","
	if x.left != b.nil:
		lista.append(x.left)
	if x.right != b.nil:
		lista.append(x.right)
	lista2.append(x)

for i in lista:
	a.insert(i)
	
lista = []
a.inorderWalk(a.root, lista)

for i in lista:
	print i
