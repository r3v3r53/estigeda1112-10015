#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
autor: Jose Jasnau Caeiro
data: 7 de maio de 2012

arvores de pesquisa binária
'''
from No import *      
    
class RBT(object):
    def __init__(self):
        self.BLACK = 0
        self.RED = 1
        self.nil = No(None,None)
        self.nil.color = self.BLACK
        self.parent = self.nil
        self.left = self.nil
        self.right = self.nil
        self.root = self.nil        
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

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        pass

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        pass

    def insertFixup(self, z):
        '''
        BLA BLA BLA
        '''
        while z.parent.cor == self.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.cor == self.RED:
                    z.parent.cor = self.BLACK
                    y.cor = self.BLACK
                    z.parent.parent.cor = self.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.leftRotate(z)
                        pass
                    z.parent.cor = self.BLACK
                    z.parent.parent.cor = self.RED
                    self.rightRotate(z.parent.parent)
                pass
            else:
                y = z.parent.parent.left
                if y.cor == self.RED:
                    z.parent.cor = self.BLACK
                    y.cor = self.BLACK
                    z.parent.parent.cor = self.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rightRotate(z)
                        pass
                    z.parent.cor = self.BLACK
                    z.parent.parent.cor = self.RED
                    self.leftRotate(z.parent.parent)
                pass
            pass
        self.root.cor = self.BLACK
        pass


    def insert(self, z):
        z.parent = z.left = z.right = self.nil

        y = self.nil
        x = self.root

        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.cor = self.RED
        self.insertFixup(z)
    pass


nos = [None for k in range(9)]

nos[0] = No(11, "Renoir")
nos[1] = No(2, "van Gogh")
nos[2] = No(14, "Picasso")
nos[3] = No(1, "Manet")
nos[4] = No(7, "da Vinci")
nos[5] = No(15, "Miguel Angelo")
nos[6] = No(5, "Rafael")
nos[7] = No(8, "Goya")
nos[8] = No(4, "Turner")

arv = RBT()

arv.insert(nos[0])
arv.insert(nos[1])
arv.insert(nos[2])
arv.insert(nos[3])
arv.insert(nos[4])
arv.insert(nos[5])
arv.insert(nos[6])
arv.insert(nos[7])
arv.insert(nos[8])

lista = []
arv.inorderWalk(arv.root, lista)

for i in lista:
    print i