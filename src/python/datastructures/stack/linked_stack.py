'''
 * A stack implementation using a doubly linked list.
 *
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *         (conversion to Python) Cosimo Giovanni Negri
 * @date   26 Aug 2022
'''

import sys
import os

if __package__:
    from .abstract_stack import AbstractStack
    from ..linkedlist import DoublyLinkedList
else:
    sys.path.append(os.path.dirname(__file__))
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from abstract_stack import AbstractStack
    from linkedlist import DoublyLinkedList


class LinkedStack(AbstractStack):
    '''
    A stack implementation using a doubly linked list.
    '''
    def __init__(self):
        self.__list = DoublyLinkedList()
        self.__iterator = None
    
    
    def isempty(self):
        '''
        Return whether or not the stack is empty, O(1).
        '''
        return len(self.__list) == 0
    
    
    def push(self, data):
        '''
        Push a node on the stack, O(1).
        '''
        self.__list.append(data)
    
    
    def pop(self):
        '''
        Pop a node off the stack and return its value, O(1).
        '''
        if self.isempty():
            raise IndexError("pop from empty stack")
        return self.__list.pop()
    
    
    def peek(self):
        '''
        Return the value of the node at the top of the stack, O(1).
        '''
        if self.isempty():
            raise IndexError("peek of empty stack")
        return self.__list.peek()
    
    
    def __len__(self):
        '''
        Return the size of the stack, O(1).
        '''
        return len(self.__list)
    
    
    def __iter__(self):
        '''
        Called when iteration is initialized, O(1).
        '''
        self.__iterator = iter(self.__list)
        return self
    
    
    def __next__(self):
        '''
        To move to the next node, O(1).
        '''
        return next(self.__iterator)
    
    
    def __str__(self):
        '''
        Return a string to print the stack, O(n)*.
        '''
        return str(self.__list)