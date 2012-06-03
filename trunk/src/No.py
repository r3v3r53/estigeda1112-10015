#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
autor: Jose Jasnau Caeiro
data: 7 de maio de 2012

Nós, vós, eles, e mais uns quantos para fazer doer a cabeça
'''

class No(object):
    '''
    Classe dos nós de cada elemento
    '''
    def __init__(self, key, valor):
        """
        Criar um nó para utilização em RB Trees
        @param key, chave do nó
        @param valor, valor que o nó tem guardado
        """
        self.key = key
        self.valor = valor
        self.dim = -1
        self.LC = self.RC = 0
        
        # Ao ser criado o nó fica com os apontadores para si próprio (NIL)
        self.parent = self.left = self.right = None
        pass

    def __str__(self):
        """
        Override do método str
        Impressão personalizada do nó
        """
        s = str(self.key) + ' : ' + str(self.valor)
        s += '('
        if self.parent == None: 
            s += 'None, ' 
        else:
            s += str(self.parent.key) + ', ' 

        if self.left == None:
            s += 'None, ' 
        else:
            s += str(self.left.key) + ', ' 

        if self.right == None:
            s += 'None, ' 
        else:
            s += str(self.right.key)
        s += ', ' + str(self.dim) + ')'
        s += ', LC = ' + str(self.LC)
        s += ', RC = ' + str(self.RC)
        return s
    pass