'''
 * A queue implementation using a doubly linked list.
 *
 * Main inspiration: William Fiset
 * https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/queue/LinkedQueue.java
 *
 * @author Cosimo Giovanni Negri
 * @date   26 Aug 2022
'''

from .abstract_queue import AbstractQueue
from ..linkedlist.doubly_linked_list import DoublyLinkedList


class LinkedQueue(AbstractQueue):
    '''
    A queue implementation using a doubly linked list.
    '''
    def __init__(self):
        self.__list = DoublyLinkedList()
        self.__iterator = None
    
    
    def isempty(self):
        '''
        Return whether or not the queue is empty, O(1).
        '''
        return len(self.__list) == 0
    
    
    def enqueue(self, value):
        '''
        Add a node to the back of the queue, O(1).
        '''
        self.__list.append(value)
    
    
    def dequeue(self):
        '''
        Remove the node at the front of the queue
        and return its value, O(1).
        '''
        if self.isempty():
            raise IndexError("dequeue from empty queue")
        return self.__list.popleft()
    
    
    def peek(self):
        '''
        Return the value of the node at the front of the queue, O(1).
        '''
        if self.isempty():
            raise IndexError("peek of empty queue")
        return self.__list.peekleft()
    
    
    def __len__(self):
        '''
        Return the size of the queue, O(1).
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
        Return a string to print the queue, O(n)*.
        '''
        return str(self.__list)