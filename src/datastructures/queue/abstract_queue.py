'''
 * An abstract base class for a queue.
 *
 * @author Cosimo Giovanni Negri
 * @date   26 Aug 2022
'''

from abc import ABC, abstractmethod


class AbstractQueue(ABC):
    
    @abstractmethod
    def isempty(self):
        pass
    
    @abstractmethod
    def enqueue(self, value):
        pass
    
    @abstractmethod
    def peek(self):
        pass
    
    @abstractmethod
    def dequeue(self):
        pass
    
    @abstractmethod
    def __len__(self):
        pass
    
    @abstractmethod
    def __iter__(self):
        pass
    
    @abstractmethod
    def __next__(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass