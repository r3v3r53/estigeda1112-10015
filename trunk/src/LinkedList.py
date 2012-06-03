# -*- coding: utf-8 -*-
# usage:
#
# x = L.malloc(22)
#    L.insert(x)
# N = 5
# L = LinkedList(N)

class LinkedList:
    def __init__(self,N):
        self.apontadores_memoria = Stack(N)
        for k in range(N):
            self.apontadores_memoria.push(k)
            pass
        self.points = [None for k in range(N)]
        self.head = None

    def malloc(self, k):
        x = self.apontadores_memoria.pop()
        self.points[x] = Point(k, None, None)
        return x

    def free(self, x):
        self.apontadores_memoria.push(x)

    def insert(self, x):
        self.points[x].next = self.head
        if self.head != None:
            self.points[self.head].prev = x
            pass
        self.head = x
        self.points[x].prev = None
        
    def search(self, k):
        x = self.head
        while x != None and self.points[x].value != k:
                x = selfpoinst[x].next
        return x
        
    def delete(self,x):
        if self.points[x].prev != None:

            self.points[selfpoints[x].prev].next = self.points[x].next
        else:
            self.head = self.poits[x].next
        if self.next[x] != None:
            self.prev[self.next[x]] = self.prev[x]
        
class Stack:
    def __init__(self, N):
        self.top = -1
        self.S = [0 for k in range(N)]
        
    def stack_empty(self):
        if self.top == 0:
            return True
        else:
            return False
        
    def push(self, x):
        self.top += 1
        self.S[self.top] = x
        
    def pop(self):
        if self.stack_empty():
            return "underflow"
        else:
            self.top -= 1
            return self.S[self.top+1]
        
    def __str__(self):
        s = ""
        s += str(self.top+1) + ": "
        for k in range(0, self.top+1):
            s += ' ' + str(self.S[k])
        return s


class Point:
    """
    Classe para representar cada um dos pontos
    """
    def __init__(self, parent, next, previous, value):
        """
        @param parent: raiz para o nível deste ponto
        @param next: próximo ponto na lista
        @param previous: ponto anterior na lista
        @param value: valor guardado no ponto
        """
        self.parent = parent
        self.next = next
        self.previous = previous
        self.value = value
        pass

    def compare(self, k):
        """
        Comparar dois pontos
        @return -1 se k < value; 0 se = value, 1 se k > value 
        """
        if self.value < value:      return 1
        elif self.value > value:    return -1
        return 0

    def toString(self): return str(self.value)
    def next(self):     return self.next
    def previous(self): return self.previous
    def parent(self):   return self.parent
    def value(self):    return self.value