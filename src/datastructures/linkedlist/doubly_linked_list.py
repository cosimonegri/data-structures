'''
 * A doubly linked list implementation.
 *
 * Main inspiration: William Fiset
 * https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/linkedlist/DoublyLinkedList.java
 *
 * @author Cosimo Giovanni Negri
 * @date   25 Aug 2022
'''

class Node:
    '''
    Node class to represent an element of the linked list.
    '''
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
    def __str__(self):
        return str(self.value)


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
    
    
    def append(self, value):
        '''
        Add a node to the tail of the linked list, O(1).
        '''
        if self.isempty():
            self.__head = self.__tail = Node(value)
        else:
            new_node = Node(value, prev=self.__tail)
            self.__tail.next = new_node
            self.__tail = new_node
            
        self.__size += 1
    
    
    def appendleft(self, value):
        '''
        Add a node to the head of the linked list, O(1).
        '''
        if self.isempty():
            self.__head = self.__tail = Node(value)
        else:
            new_node = Node(value, next=self.__head)
            self.__head.prev = new_node
            self.__head = new_node
        
        self.__size += 1
    
    
    def insert(self, index, value):
        '''
        Add a node at a specific index, O(n).
        '''
        if index < 0 or index > self.__size:
            raise IndexError("list index out of range")
        
        if index == self.__size:
            self.append(value)
            return
        
        if index == 0:
            self.appendleft(value)
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
            
        new_node = Node(value, prev=trav, next=trav.next)
        trav.next.prev = new_node
        trav.next = new_node
        self.__size += 1
    
    
    def peek(self):
        '''
        Return the value of the last node if it exists, O(1).
        '''
        if self.isempty():
            raise IndexError("peek of empty list")
        return self.__tail.value
    
    
    def peekleft(self):
        '''
        Return the value of the first node if it exists, O(1).
        '''
        if self.isempty():
            raise IndexError("peekleft of empty list")
        return self.__head.value
    
    
    def __remove_node(self, node):
        '''
        Remove a node from the linked list,
        and return its value, O(1).
        '''
        if node.next is None:
            return self.pop()
        if node.prev is None:
            return self.popleft()
        
        value = node.value
        node.prev.next = node.next
        node.next.prev = node.prev
        self.__size -= 1
        
        # Memory cleanup of the node that was just removed
        node.prev = node.next = None
        node = None
        
        return value
    
    
    def pop(self):
        '''
        Remove the node at the tail of the linked list
        and return its value, O(1).
        '''
        if self.isempty():
            raise IndexError("pop from empty list")
        
        value = self.__tail.value
        self.__tail = self.__tail.prev
        self.__size -= 1
        
        if (self.isempty()):
            self.__head = None
        else:
            # Memory cleanup of the node that was just removed
            self.__tail.next = None
        
        return value

     
    def popleft(self):
        '''
        Remove the node at the head of the linked list
        and return its value, O(1).
        '''
        if self.isempty():
            raise IndexError("popleft from empty list")
        
        value = self.__head.value
        self.__head = self.__head.next
        self.__size -= 1
        
        if self.isempty():
            self.__tail = None
        else:
            # Memory cleanup of the node that was just removed
            self.__head.prev = None
        
        return value
    
    
    # raise ValueError if item not present?
    def remove(self, value):
        '''
        Remove the first node with a specific value.
        Return true if a node was deleted, false otherwise, O(n).
        '''
        trav = self.__head
        while trav is not None:
            if trav.value == value:
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
    def index(self, value):
        '''
        Return the index of the first node with a specific value
        if it exists, otherwise return None, O(n).
        '''
        index = 0
        trav = self.__head
        
        while trav is not None:
            if trav.value == value:
                return index
            index += 1
            trav = trav.next
        
        return None
    
    
    def __len__(self):
        '''
        Return the size of the linked list, O(1).
        '''
        return self.__size
    
    
    def __contains__(self, value):
        '''
        Return whether ot not a value is in the linked list, O(n).
        '''
        return self.index(value) is not None
    
    
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
        
        value = self.__trav.value
        self.__trav = self.__trav.next
        return value
    
    
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