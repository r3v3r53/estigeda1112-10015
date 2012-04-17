# -*- coding: utf-8 -*-
# biblioteca para operação com árvores k-d balanceadas

# Autor - Pedro Moreira, 10015 (mail@pedromoreira.org)
# Data: 2012-04-17

# funcionalidades:
#   - construção da árvore a partir de uma lista de dados;
#   - junção de elementos;
#   - remoção de elementos;
#   - pesquisa do elemento mais próximo;

class kdtree:
    '''
    o que a classe faz...
    '''

    def __init__(self, A = []):
        '''
        construtor, pode inicializar
        uma lista de dados e ordená-la
        '''
        self.__A = A
        self.__sort__()
        pass

    def __sort__(self):
        '''
        ordenar a lista, escolhendo o método apropriado
        '''
        pass

    def merge(self, A, B):
        '''
        fazer a junção de duas listas
        '''
        pass
    
    def search(self, A, k):
        '''
        pesquisar um elemento numa lista
        '''
        pass

    def insert(self, A, k):
        '''
        inserir um valor numa lista, ordenando-a
        '''
        pass

    def delete(self, A, k):
        '''
        eliminar um elemento da lista
        '''
        pass
    
    pass


from kdtree import *

def main():
    A = [1,2,3]
    b = kdtree(A)
    pass

main()
