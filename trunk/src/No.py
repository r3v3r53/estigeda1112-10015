#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
autor: Pedro Moreira, 10015
data: 17 de Junho de 2012

'''

class No(object):
    '''
    Classe dos nos de cada elemento
    '''
    def __init__(self, key, valor):
        """
        Criar um no para utilizacao em RB Trees
        @param key, chave do no
        @param valor, valor que o no tem guardado
        """
        self.key = key
        self.valor = valor
        self.LC = 0
        self.RC = 0
        self.dim = 0

        # Ao ser criado o no fica com os apontadores para si proprio (NIL)
        self.parent = self.left = self.right = None
        pass

    def __str__(self):
        """
        Override do metodo str
        Impressao personalizada do no
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