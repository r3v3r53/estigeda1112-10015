#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
autor: Pedro Miguel Moreira 
data: 25 de Maio de 2012

arvores de pesquisa binária
'''

class No(object):
    '''
    Classe dos nós de cada elemento
    '''
    def __init__(self, key, valor, cor):
        """
        Criar um nó para utilização em RB Trees
        @param key, chave do nó
        @param valor, valor que o nó tem guardado
        @param cor, cor actual do nó
        """
        self.key = key
        self.valor = valor
        self.cor = cor
        self.dim = -1
        
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
        s +=  ', ' + str(self.cor) + ')'
        s += ', ' + str(self.dim)
        return s
    pass


class ArvorePesquisaBinaria(object):
    '''
    Árvore de Pesquisa binária com listas ligadas
    e cores para
    '''
    def __init__(self, dimention):
        self.BLACK = 0
        self.RED = 1
        self.nil = No(0, "", self.BLACK)
        self.parent = self.left = self.right = self.root = self.nil
        self.dimention = dimention
        
    def insert(self, z, dim = -1):
        z.parent = z.left = z.right = y = self.nil
        x = self.root

        while x != self.nil:
            dim = (dim + 1) % self.dimention
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
            z.dim = dim

        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def search(self, x, k):
        if x == self.nil or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    def minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def maximum(self, x):
        while x.right != self.nil:
            x = x.right
        return x

    def sucessor(self, x):
        if x.right != self.nil:
            return self.minimum(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y

    def inorder_walk(self, x, lista):
        if x != self.nil:
            self.inorder_walk(x.left, lista)
            lista.append( x )
            self.inorder_walk(x.right, lista)

    #TODO ARRANJA
    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != self.nil:
            v.parent = u.parent

    #TODO ARRANJA
    def delete(self, z):
        if z.left == self.nil:
            self.transplant(z, z.right)
        elif z.right == self.nil:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
    

class ArvoreRedBlack(ArvorePesquisaBinaria):
    def __init__(self, dimension):
        super(ArvoreRedBlack, self).__init__(dimension)

    def left_rotate(self, x):
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
        

    def right_rotate(self, x):
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

    def rb_insert_fixup(self, z):
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
                        self.left_rotate(z)
                        pass
                    z.parent.cor = self.BLACK
                    z.parent.parent.cor = self.RED
                    self.right_rotate(z.parent.parent)
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
                        self.right_rotate(z)
                        pass
                    z.parent.cor = self.BLACK
                    z.parent.parent.cor = self.RED
                    self.left_rotate(z.parent.parent)
                pass
            pass
        self.root.cor = self.BLACK
        pass
        
    def rb_transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
        pass

    def rb_delete (self, z):
        y = z
        y_o_color = y.cor
        if z.left == self.nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_o_color = y.cor
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.cor = z.cor
        if y_o_color == self.BLACK:
            self.rb_delete_fixup(x)
        pass

    def rb_delete_fixup(self, x):
        while x != self.root and x.cor == self.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.cor == self.RED:
                    w.cor = self.BLACK
                    x.parent.cor = self.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.cor == self.BLACK and w.right.cor == self.BLACK:
                    w.cor = self.RED
                    x = x.parent
                else:
                    if w.right.cor == self.BLACK:
                        w.left.cor = self.BLACK
                        w.cor = self.RED
                        right_rotate(w)
                        w = x.parent.right
                    w.cor = x.parent.cor
                    x.parent.cor = self.BLACK
                    w.right.cor = self.BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.cor == self.RED:
                    w.cor = self.BLACK
                    x.parent.cor = self.RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.cor == self.BLACK and w.left.cor == self.BLACK:
                    w.cor = self.RED
                    x = x.parent
                else:
                    if w.left.cor == self.BLACK:
                        w.right.cor = self.BLACK
                        w.cor = self.RED
                        left_rotate(w)
                        w = x.parent.left
                    w.cor = x.parent.cor
                    x.parent.cor = self.BLACK
                    w.left.cor = self.BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.cor = self.BLACK

    def insert(self, z):
        super(ArvoreRedBlack, self).insert(z)
        
        z.cor = self.RED
        self.rb_insert_fixup(z)
    pass
'''
nos = [None for k in range(9)]

nos[0] = No(11, "Renoir", None)
nos[1] = No(2, "van Gogh", None)
nos[2] = No(14, "Picasso", None)
nos[3] = No(1, "Manet", None)
nos[4] = No(7, "da Vinci", None)
nos[5] = No(15, "Miguel Angelo", None)
nos[6] = No(5, "Rafael", None)
nos[7] = No(8, "Goya", None)
nos[8] = No(4, "Turner", None)

arv = ArvoreRedBlack()
print "NIL"
print arv.nil

arv.insert(nos[0])
arv.insert(nos[1])
arv.insert(nos[2])
arv.insert(nos[3])
arv.insert(nos[4])
arv.insert(nos[5])
arv.insert(nos[6])
arv.insert(nos[7])
arv.insert(nos[8])
'''

'''
print "INORDER"
lista = []
arv.inorder_walk(arv.root, lista)
for x in lista:
    print x

print
for x in nos:
    print x


print "PESQUISA"
print arv.search(arv.root, 15)

print "MINIMO"
print arv.minimum(arv.root)

print "MAXIMO"
print arv.maximum(arv.root)

print "SUCESSOR"
print arv.sucessor(nos[4])


print "APAGAR"
print arv.delete(nos[2])

for x in nos:
    print x

print "PESQUISA"
print arv.search(arv.root, 18)

print
print "INORDER"
lista = []
arv.inorder_walk(arv.root, lista)
for x in lista:
    print x

print "DEPOIS"
arv.rb_delete(nos[4])
lista = []
arv.inorder_walk(arv.root, lista)
for x in lista:
    print x


arv.left_rotate(nos[1])
print
print "INORDER AFTER LEFT ROTATE"
lista = []
arv.inorder_walk(arv.root, lista)
for x in lista:
    print x
    '''