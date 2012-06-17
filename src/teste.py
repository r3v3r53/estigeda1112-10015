#!/usr/bin/env python
# -*- coding: utf-8 -*-
from KDTree import *
from random import randint as rand
import time
from pylab import *


def drawGraph(ys, labels, title):
	'''
	desenhar um gráfico dados os valores ys nos anos disponíveis na bd
	'''
	# http://matplotlib.sourceforge.net/examples/pylab_examples/vertical_ticklabels.html
	# http://www.secnetix.de/olli/Python/lambda_functions.hawk
	# http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.suptitle
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
		arvore.insert(arvore.root, i)

def main():


	dados = []
	labels = []
	f1 = open('labels.dat', 'w')	
	f2 = open('dados.dat', 'w')	
	for k in range(0, 100, 10):
		b = 0.0
		N = 5
		for j in range(N):
			lista = []
			inserirDados(lista, k)
			arv = KDTree(2)
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


main()


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

for i in no:
	a.insert(i)


lista = []
a.inorderWalk(a.root, lista)
for i in lista:
	print i
print
print 
print

print a.searchByValue(a.root, "Ai")
print a.minimum(a.root)
'''