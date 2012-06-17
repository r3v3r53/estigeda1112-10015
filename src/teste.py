#!/usr/bin/env python
# -*- coding: utf-8 -*-
from KDTree import *
from random import randint as rand
import time
from pylab import *


def drawGraph(ys, labels, title):
	a = lambda:range(1, len(ys) + 1)
	plot(a(), ys)
	locs, labels = xticks(a(), labels)
	setp(labels, 'rotation', 'vertical')
	suptitle(title, fontsize=20)

	#x1,x2,y1,y2 = axis()
	#axis((x1,x2,0,1))
	show()
	pass


def inserirDados(lista, x):
	for i in range(x):
		lista.append(No((randint(0,1000),randint(0,1000)), randint(0, 1000000)))

def construirArvore(arvore, lista):
	#Quicksort(lista)
	for i in lista:
		arvore.malloc(i)

def inserir():

	maxN = 1000
	startN = 0
	increment = 100
	N = 40
	dados = []
	labels = []
	f1 = open('labels.dat', 'w')	
	f2 = open('dados.dat', 'w')	
	for k in range(startN, maxN, increment):
		b = 0.0
		for j in range(N):
			lista = []
			inserirDados(lista, k)
			arv = KDTree(k, 2)
			t1 = time.time()
			construirArvore(arv, lista)
			t2 = time.time()
			b += t2-t1
		f1.write(str(k))
		f2.write(str(b/N))
		print k, (b/N)
		dados.append(b/N)
		labels.append(k)

	f1.close()
	f2.close()


	drawGraph(dados, labels, "titulo")


def apagar():
	maxN = 1000
	startN = 1
	increment = 100
	N = 40
	dados = []
	labels = []
	f1 = open('labels.dat', 'w')	
	f2 = open('dados.dat', 'w')	
	for k in range(startN, maxN, increment):
		b = 0.0
		for j in range(N):
			lista = []
			inserirDados(lista, k)
			arv = KDTree(k, 2)
			construirArvore(arv, lista)
			t1 = time.time()
			arv.freeNo(lista[randint(0, len(lista))])
			t2 = time.time()
			b += t2-t1
		f1.write(str(k))
		f2.write(str(b/N))
		print k, (b/N)
		dados.append(b/N)
		labels.append(k)

	f1.close()
	f2.close()


	drawGraph(dados, labels, "titulo")


def maisProximo():
	maxN = 1000
	startN = 1
	increment = 100
	N = 40
	dados = []
	labels = []
	f1 = open('labels.dat', 'w')	
	f2 = open('dados.dat', 'w')	
	for k in range(startN, maxN, increment):
		b = 0.0
		for j in range(N):
			lista = []
			inserirDados(lista, k)
			arv = KDTree(k, 2)
			construirArvore(arv, lista)
			t1 = time.time()
			arv.nearestNeighbour(lista[randint(0, len(lista))])
			t2 = time.time()
			b += t2-t1
		f1.write(str(k))
		f2.write(str(b/N))
		print k, (b/N)
		dados.append(b/N)
		labels.append(k)

	f1.close()
	f2.close()


	drawGraph(dados, labels, "titulo")

#TESTES
print "INSERIR"
inserir()
print
print "APAGAR"
apagar()
print
print"MAIS PROXIMO"
maisProximo()