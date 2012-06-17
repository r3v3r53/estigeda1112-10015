#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
autor: Pedro Moreira, n.º 10015
data: 17 de Junho de 2012

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
        self.LC = 0
        self.RC = 0
        self.dim = 0

        # Ao ser criado o nó fica com os apontadores para si próprio (NIL)
        self.parent = self.left = self.right = None
        pass

    def __str__(self):
        """
        Override do método str
        Impressão personalizada do nó
        """
        s = str(self.key) + " : "#+ str(self.valor)
        s += '('
        s += str(self.parent.key) + ', ' 
        s += str(self.left.key) + ', ' 
        s += str(self.right.key)
        s += ', ' + str(self.size) + ')'
        s += ', LC = ' + str(self.LC)
        s += ', RC = ' + str(self.RC)
        s += ', dim = ' + str(self.dim)
        return s