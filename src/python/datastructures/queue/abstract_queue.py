'''
 * An abstract base class for queue.
 *
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *                         liujingkun, liujkon@gmail.com
 *         (conversion to Python) Cosimo Giovanni Negri
 * @date   26 Aug 2022
'''

from abc import ABC, abstractmethod


class EmptyQueue(Exception):
    
    def __init__(self, message="Empty queue"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return self.message


class AbstractQueue(ABC):
    
    @abstractmethod
    def __len__(self):
        pass
    
    @abstractmethod
    def empty(self):
        pass
    
    @abstractmethod
    def enqueue(self, data):
        pass
    
    @abstractmethod
    def peek(self):
        pass
    
    @abstractmethod
    def dequeue(self):
        pass