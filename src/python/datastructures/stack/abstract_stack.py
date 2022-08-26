'''
 * An abstract base class for stack.
 *
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *                         liujingkun, liujkon@gmail.com
 *         (conversion to Python) Cosimo Giovanni Negri
 * @date   26 Aug 2022
'''

from abc import ABC, abstractmethod


class EmptyStack(Exception):
    
    def __init__(self, message="Empty stack"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return self.message


class AbstractStack(ABC):
    
    @abstractmethod
    def __len__(self):
        pass
    
    @abstractmethod
    def empty(self):
        pass
    
    @abstractmethod
    def push(self, data):
        pass
    
    @abstractmethod
    def peek(self):
        pass
    
    @abstractmethod
    def pop(self):
        pass