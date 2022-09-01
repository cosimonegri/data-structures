'''
 * A set implementation using a hash table.
 *
 * @author Cosimo Giovanni Negri
 * @date   29 Aug 2022
'''

from ..hashtable.hash_table_separate_chaining import HashTableSeparateChaining


class Set:
    '''
    A set implementation using a hash table.
    '''
    def __init__(self):
        self.__hash_table = HashTableSeparateChaining()
        self.__iterator = None
    
    
    def __raise_error(self, value):
        '''
        Raise an error with the proper message, O(1).
        '''
        if value is None:
            raise TypeError("value must not be None")
        if isinstance(value, bool):
            raise TypeError("value must not be a boolean")
        
        try:
            hash(value)
        except:
            raise TypeError(f"unhashable value: {type(value)}")
    
    
    def clear(self):
        '''
        Empty the set, O(n).
        '''
        self.__hash_table.clear()
    
    
    def isempty(self):
        '''
        Return whether or not the set is empty, O(1).
        '''
        return self.__hash_table.isempty()
    
    
    def add(self, value):
        '''
        Add a value to the set, O(1)*.
        NOTE: If the value type is not valid, raise an error.
        '''
        try:
            self.__hash_table[value] = None
        except TypeError:
            self.__raise_error(value)
    
    
    def remove(self, value):
        '''
        Remove a value if it exists in the set,
        otherwise raise an error, O(1)*.
        NOTE: If the value type is not valid, raise an error.
        '''
        try:
            del self.__hash_table[value]
        except TypeError:
            self.__raise_error(value)
        except KeyError:
            raise ValueError(f"{value} not in set")
    
    
    def union(self, other):
        '''
        Return a new set containing all the values that
        are contained at least in one set, O(n1 + n2).
        '''
        if type(other) is not type(self):
            raise TypeError("union must be done with an other 'Set'")
        
        new_set = Set()
        for value1 in self.__hash_table:
            new_set.add(value1)
        for value2 in other.__hash_table:
            new_set.add(value2)
        
        return new_set
    
    
    def intersection(self, other):
        '''
        Return a new set containing only the values that
        are contained in both sets, O(min(n1, n2)).
        '''
        if type(other) is not type(self):
            raise TypeError("intersection must be done with an other 'Set'")
        
        new_set = Set()
        if len(self) <= len(other):
            small_set = self
            big_set = other
        else:
            small_set = other
            big_set = self
        
        for value in small_set.__hash_table:
            if value in big_set.__hash_table:
                new_set.add(value)
        
        return new_set
    
    
    def difference(self, other):
        '''
        Return a new set containing only the values that are
        contained in the first set and not in the second one, O(n1).
        '''
        if type(other) is not type(self):
            raise TypeError("difference must be done with an other 'Set'")
        
        new_set = Set()
        for value in self.__hash_table:
            if value not in other.__hash_table:
                new_set.add(value)
        
        return new_set
    
    
    def __len__(self):
        '''
        Return the size of the set, O(1).
        '''
        return len(self.__hash_table)

    
    def __or__(self, other):
        '''
        Return a new set containing all the values that
        are contained at least in one set, O(n1 + n2).
        '''
        return self.union(other)
    
    
    def __and__(self, other):
        '''
        Return a new set containing only the values that
        are contained in both sets, O(min(n1, n2)).
        '''
        return self.intersection(other)
    
    
    def __sub__(self, other):
        '''
        Return a new set containing only the values that are
        contained in the first set and not in the second one, O(n1).
        '''
        return self.difference(other)
    
    
    def __contains__(self, value):
        '''
        Return whether ot not a value is in the set, O(1)*.
        '''
        return value in self.__hash_table


    def __iter__(self):
        '''
        Called when iteration is initialized, O(1).
        '''
        self.__iterator = iter(self.__hash_table)
        return self
    
    
    def __next__(self):
        '''
        To move to the next node, O(1).
        '''
        return next(self.__iterator)
    
    
    def __str__(self):
        '''
        Return a string to print the set, O(n)*.
        '''
        strings = []
        for key in self.__hash_table:
            strings.append(str(key))
        
        return '{' + ', '.join(strings) + '}'