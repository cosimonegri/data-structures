'''
 * An abstract base class for queue.
 *
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *                         liujingkun, liujkon@gmail.com
 *         (conversion to Python) Cosimo Giovanni Negri
 * @date   26 Aug 2022
'''

from abc import ABC, abstractmethod


class AbstractQueue(ABC):
    
    @abstractmethod
    def isempty(self):
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