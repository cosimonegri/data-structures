'''
 * A binary search tree implementation.
 *
 * Main inspiration: William Fiset
 * https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/binarysearchtree/BinarySearchTree.java
 *
 * @author Cosimo Giovanni Negri
 * @date   31 Aug 2022
'''

from ..queue.linked_queue import LinkedQueue


class Node:
    '''
    Node class to represent an element of the binary search tree.
    '''
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.value)


class BinarySearchTree():
    '''
    A binary search tree implementation.
    '''
    def __init__(self):
        self.__size = 0
        self.__root = None
        self.__trav_values = None
        self.__trav_index = None
    
    
    def __check_value_type(self, value):
        '''
        Raise an error if the value type is not valid, O(1).
        '''
        if isinstance(value, bool):
            raise TypeError("value must not be a boolean")
        
        if self.__root is None:
            try:
                value == value
                value > value
                value < value
            except:
                raise TypeError(f"uncomparable value: {type(value)}")
            
        else:
            root_value = self.__root.value
            try:
                value == root_value
                value > root_value
                value < root_value
            except:
                raise TypeError(f"{type(value)} not comparable with {type(root_value)}")
    
    
    def __recursive_clear(self, node):
        '''
        Cleanup memory of the given node, and then recurse into
        the left and the right subtrees.
        '''
        if node is None:
            return
        
        left_child = node.left
        right_child = node.right
        node.value = None
        node.left = node.right = None
        
        self.__recursive_clear(left_child)
        self.__recursive_clear(right_child)
    
    
    def clear(self):
        '''
        Empty the binary search tree, O(n).
        '''
        self.__recursive_clear(self.__root)    
        self.__size = 0
        self.__root = None
        
    
    def isempty(self):
        '''
        Return whether or not the binary search tree is empty, O(1).
        '''
        return self.__size == 0
    
    
    def __recursive_add(self, node, value):
        '''
        Add a node in the right place if the value does not exist
        in the binary search tree, otherwise do nothing.
        '''
        if node is None:
            self.__size += 1
            return Node(value)
        
        if value < node.value:
            node.left = self.__recursive_add(node.left, value)
        elif value > node.value:
            node.right = self.__recursive_add(node.right, value)
        
        return node
    
    
    def add(self, value):
        '''
        Add a node in the right place if the value does not exist
        in the binary search tree, otherwise do nothing, O(height).
        NOTE: If the value type is not valid, raise an error.
        '''
        self.__check_value_type(value)
        self.__root = self.__recursive_add(self.__root, value)
    
    
    def __get_leftmost_child(self, node):
        '''
        Return the leftmost child of the given node.
        '''
        while node.left is not None:
            node = node.left
        return node

    
    def getmin(self):
        '''
        Return the minimum value in the binary search tree, O(height).
        '''
        return self.__get_leftmost_child(self.__root).value
    
    
    def __get_rightmost_child(self, node):
        '''
        Return the rightmost child of the given node.
        '''
        while node.right is not None:
            node = node.right
        return node

    
    def getmax(self):
        '''
        Return the maximum value in the binary search tree, O(height).
        '''
        return self.__get_rightmost_child(self.__root).value
    
    
    def __recursive_search(self, node, value):
        '''
        Return the node with the given value if it exists in the
        binary search tree, otherwise return None.
        '''
        if node is None:
            return None
        
        if value == node.value:
            return node
        elif value < node.value:
            return self.__recursive_search(node.left, value)
        else:
            return self.__recursive_search(node.right, value)
    
    
    def __recursive_remove(self, node, value):
        '''
        Remove the node with a specific value from the binary search tree.
        '''
        if node is None:
            return None
        
        if value < node.value:
            node.left = self.__recursive_remove(node.left, value)
            return node
        if value > node.value:
            node.right = self.__recursive_remove(node.right, value)
            return node
        
        # here value == node.value
        
        if node.left is None:  # zero children or only right child
            return node.right
        if node.right is None:  # only left child
            return node.left
            
        else: # two children
            temp = self.__get_rightmost_child(node.left)
            node.value = temp.value
            node.left = self.__recursive_remove(node.left, temp.value)
            return node
    
    
    def remove(self, value):
        '''
        Remove the node with a specific value if it exists in the
        binary search tree, otherwise raise an error, O(height).
        NOTE: If the value type is not valid, raise an error.
        '''
        self.__check_value_type(value)
        node = self.__recursive_search(self.__root, value)
        
        if node is None:
            raise ValueError(f"{value} not in tree")
        else:
            self.__root = self.__recursive_remove(self.__root, value)
            self.__size -= 1
    
    
    def __recursive_height(self, node):
        '''
        Return the height of the given node using recursion.
        '''
        if node is None:
            return 0
        
        left_height = self.__recursive_height(node.left) + 1
        right_height = self.__recursive_height(node.right) + 1
        return max(left_height, right_height)
        
    
    def height(self):
        '''
        Return the height of the binary search tree, O(n).
        '''
        return self.__recursive_height(self.__root)
    
    
    def inorder(self):
        '''
        Traverse the binary search tree in order and
        return a copy of the list of values, O(n).
        '''
        values = []
        
        def explore(node):
            if node is None: return
            explore(node.left)
            values.append(node.value)
            explore(node.right)
        
        explore(self.__root)
        return values

    
    def preorder(self):
        '''
        Traverse the binary search tree in pre-order and
        return a copy of the list of values, O(n).
        '''
        values = []
        
        def explore(node):
            if node is None: return
            values.append(node.value)
            explore(node.left)
            explore(node.right)
        
        explore(self.__root)
        return values
    
    
    def postorder(self):
        '''
        Traverse the binary search tree in post-order and
        return a copy of the list of values, O(n).
        '''
        values = []
        
        def explore(node):
            if node is None: return
            explore(node.left)
            explore(node.right)
            values.append(node.value)
        
        explore(self.__root)
        return values
    
    
    def levelorder(self):
        '''
        Traverse the binary search tree in level-order and
        return a copy of the list of values, O(n).
        '''
        values = []
        nodes = LinkedQueue()
        nodes.enqueue(self.__root)
        
        while not nodes.isempty():
            node = nodes.dequeue()
            if node is None: continue
            
            values.append(node.value)
            nodes.enqueue(node.left)
            nodes.enqueue(node.right)
        
        return values
    
    
    def __len__(self):
        '''
        Return the size of the binary search tree, O(1).
        '''
        return self.__size
    
    
    def __contains__(self, value):
        '''
        Return whether or not a value
        is in the binary search tree, O(log(n)).
        '''
        return self.__recursive_search(self.__root, value) is not None
    
    
    def __iter__(self):
        '''
        Called when iteration is initialized, O(1).
        '''
        self.__trav_values = self.inorder()
        self.__trav_index = 0
        return self
    
    
    def __next__(self):
        '''
        To move to the next entry, O(1).
        '''
        if self.__trav_index is None or \
                self.__trav_index >= self.__size:
            raise StopIteration
        
        value = self.__trav_values[self.__trav_index]
        self.__trav_index += 1
        return value
    
    
    def __str__(self):
        '''
        Return a string to print the hash table, O(n)*.
        '''
        strings = []
        for value in self.inorder():
            strings.append(str(value))
        
        return '[' + ', '.join(strings) + ']'
        