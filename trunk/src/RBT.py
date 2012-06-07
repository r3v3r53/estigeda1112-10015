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
        self.nil = No(None, None)
        self.nil.color = self.BLACK
        self.root = self.nil

        pass
    
    def RBTLeftRotate(self, x):
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

    def RBTRightRotate(self, x):
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

    def RBTInsertFixup(self, z):
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
                        self.RBTLeftRotate(z)
                        pass
                    z.parent.cor = self.BLACK
                    z.parent.parent.cor = self.RED
                    self.RBTRightRotate(z.parent.parent)
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
                        self.RBTRightRotate(z)
                        pass
                    z.parent.cor = self.BLACK
                    z.parent.parent.cor = self.RED
                    self.RBTLeftRotate(z.parent.parent)
                pass
            pass
        self.root.cor = self.BLACK
        pass

    def RBTInsert(self, z):

        z.parent = z.left = z.right = self.nil
        
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key[z.dim] < x.key[z.dim]:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key[z.dim] < y.key[z.dim]:
            y.left = z
        else:
            y.right = z

        z.cor = self.RED
        self.RBTInsertFixup(z)
    pass
     
    def __append__(self, x):
        self.RBTInsert(x)

