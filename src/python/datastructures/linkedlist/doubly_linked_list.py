'''
 * A doubly linked list implementation.
 *
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *         (conversion to Python) Cosimo Giovanni Negri
 * @date   25 Aug 2022
'''

class Node:
    '''
    Node class to represent an element of the linked list.
    '''
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        
    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    '''
    A doubly linked list implementation.
    '''
    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None
        self.__trav = None


    def clear(self):
        '''
        Empty the linked list, O(n).
        '''
        trav = self.__head
        
        # Memory cleanup of all the nodes
        while trav is not None:
            temp = trav.next
            trav.prev = trav.next = None
            trav = temp
        
        self.__size = 0
        self.__head = self.__tail = None
    
    
    def isempty(self):
        '''
        Return whether or not the linked list is empty, O(1).
        '''
        return self.__size == 0
    
    
    def append(self, data):
        '''
        Add a node to the tail of the linked list, O(1).
        '''
        if self.isempty():
            self.__head = self.__tail = Node(data)
        else:
            new_node = Node(data, prev=self.__tail)
            self.__tail.next = new_node
            self.__tail = new_node
            
        self.__size += 1
    
    
    def appendleft(self, data):
        '''
        Add a node to the head of the linked list, O(1).
        '''
        if self.isempty():
            self.__head = self.__tail = Node(data)
        else:
            new_node = Node(data, next=self.__head)
            self.__head.prev = new_node
            self.__head = new_node
        
        self.__size += 1
    
    
    def insert(self, index, data):
        '''
        Add a node at a specific index, O(n).
        '''
        if index < 0 or index > self.__size:
            raise IndexError("list index out of range")
        
        if index == self.__size:
            self.append(data)
            return
        
        if index == 0:
            self.appendleft(data)
            return
        
        # Search from the front of the linked list
        if index < self.__size // 2:
            trav = self.__head
            i = 0
            while i != index - 1:
                trav = trav.next
                i += 1
        
        # Search from the back of the linked list
        else:
            trav = self.__tail
            i = self.__size - 1
            while i != index - 1:
                trav = trav.prev
                i -= 1
            
        new_node = Node(data, prev=trav, next=trav.next)
        trav.next.prev = new_node
        trav.next = new_node
        self.__size += 1
    
    
    def peek(self):
        '''
        Return the value of the last node if it exists, O(1).
        '''
        if self.isempty():
            raise IndexError("peek of empty list")
        return self.__tail.data
    
    
    def peekleft(self):
        '''
        Return the value of the first node if it exists, O(1).
        '''
        if self.isempty():
            raise IndexError("peekleft of empty list")
        return self.__head.data
    
    
    def __remove_node(self, node):
        '''
        Remove a node from the linked list,
        and return its value, O(1).
        '''
        if node.next is None:
            return self.pop()
        if node.prev is None:
            return self.popleft()
        
        data = node.data
        node.prev.next = node.next
        node.next.prev = node.prev
        self.__size -= 1
        
        # Memory cleanup of the node that was just removed
        node.prev = node.next = None
        node = None
        
        return data
    
    
    def pop(self):
        '''
        Remove the node at the tail of the linked list
        and return its value, O(1).
        '''
        if self.isempty():
            raise IndexError("pop from empty list")
        
        data = self.__tail.data
        self.__tail = self.__tail.prev
        self.__size -= 1
        
        if (self.isempty()):
            self.__head = None
        else:
            # Memory cleanup of the node that was just removed
            self.__tail.next = None
        
        return data

     
    def popleft(self):
        '''
        Remove the node at the head of the linked list
        and return its value, O(1).
        '''
        if self.isempty():
            raise IndexError("popleft from empty list")
        
        data = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        
        if self.isempty():
            self.__tail = None
        else:
            # Memory cleanup of the node that was just removed
            self.__head.prev = None
        
        return data
    
    
    # raise ValueError if item not present?
    def remove(self, data):
        '''
        Remove the first node with a specific value.
        Return true if a node was deleted, false otherwise, O(n).
        '''
        trav = self.__head
        while trav is not None:
            if trav.data == data:
                self.__remove_node(trav)
                return True
            trav = trav.next
        
        return False
    
    
    def removeindex(self, index):
        '''
        Remove a node at a specific index, O(n).
        '''
        if index < 0 or index >= self.__size:
            raise IndexError("list index out of range")
        
        # Search from the front of the linked list
        if index < self.__size // 2:
            trav = self.__head
            i = 0
            while i != index:
                trav = trav.next
                i += 1
        
        # Search from the back of the linked list
        else:
            trav = self.__tail
            i = self.__size - 1
            while i != index:
                trav = trav.prev
                i -= 1
        
        return self.__remove_node(trav)      
        
    
    # raise a ValueError if item not found
    def index(self, data):
        '''
        Return the index of the first node with a specific value
        if it exists, otherwise return None, O(n).
        '''
        index = 0
        trav = self.__head
        
        while trav is not None:
            if trav.data == data:
                return index
            index += 1
            trav = trav.next
        
        return None
    
    
    def __len__(self):
        '''
        Return the size of the linked list, O(1).
        '''
        return self.__size
    
    
    def __contains__(self, data):
        '''
        Return whether ot not a value is in the linked list, O(n).
        '''
        return self.index(data) is not None
    
    
    def __iter__(self):
        '''
        Called when iteration is initialized, O(1).
        '''
        self.__trav = self.__head
        return self
    
    
    def __next__(self):
        '''
        To move to the next node, O(1).
        '''
        if self.__trav is None:
            raise StopIteration
        
        data = self.__trav.data
        self.__trav = self.__trav.next
        return data
    
    
    def __str__(self):
        '''
        Return a string to print the linked list, O(n)*.
        '''
        strings = []
        trav = self.__head
        while trav is not None:
            strings.append(str(trav))
            trav = trav.next
        
        return '[' + ', '.join(strings) + ']'