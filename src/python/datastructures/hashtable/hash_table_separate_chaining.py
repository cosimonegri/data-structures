'''
 * A hash table implementation using separate chaining with a doubly linked list.
 *
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *         (conversion to Python) Cosimo Giovanni Negri
 * @date   27 Aug 2022
'''

from ..linkedlist.doubly_linked_list import DoublyLinkedList


class Entry:
    '''
    Entry class to represent the key-value pair of the hash table.
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)
    
    def __eq__(self, other):
        if self.hash != other.hash:
            return False
        return self.key == other.key
    
    def __str__(self):
        return f"{str(self.key)}: {str(self.value)}"


class HashTableSeparateChaining:
    '''
    A hash table implementation using separate chaining with a doubly linked list.
    '''
    
    def __init__(self):
        self.__INITIAL_CAPACITY = 4
        self.__LOAD_FACTOR = 0.75
        
        self.__capacity = self.__INITIAL_CAPACITY
        self.__threshold = int(self.__INITIAL_CAPACITY * self.__LOAD_FACTOR)
        self.__size = 0
        self.__table = [None for _ in range(self.__INITIAL_CAPACITY)]
        self.__iter_index = None
        self.__iterator = None
    
    
    def __check_key_type(self, key):
        '''
        Raise an error if the key type is not valid, O(1).
        '''
        if key is None:
            raise TypeError("key must not be None")
        if isinstance(key, bool):
            raise TypeError("key must not be a boolean")
        
        try:
            hash(key)
        except:
            raise TypeError(f"unhashable key: {type(key)}")
    
    
    def clear(self):
        '''
        Empty the hash table, O(n).
        '''
        for bucket in self.__table:
            if bucket is not None:
                bucket.clear()
            
        self.__capacity = self.__INITIAL_CAPACITY
        self.__threshold = int(self.__INITIAL_CAPACITY * self.__LOAD_FACTOR)
        self.__size = 0
        self.__table = [None for _ in range(self.__INITIAL_CAPACITY)]
    
    
    def isempty(self):
        '''
        Return whether or not the linked list is empty, O(1).
        '''
        return self.__size == 0
        
    
    def __get_index(self, hash):
        '''
        Convert a hash to an index and return it, O(1).
        '''
        # Strip the negative sign and place the hash in the domain [0, capacity - 1]
        return (~hash + 1) % self.__capacity
    
    
    def __resize_table(self):
        '''
        Resize the table holding buckets of entries, O(n).
        '''
        self.__capacity *= 2
        self.__threshold = int(self.__capacity * self.__LOAD_FACTOR)
        
        new_table = [None for _ in range(self.__capacity)]
        
        for bucket in self.__table:
            if bucket is None: continue
            
            for entry in bucket:
                new_bucket_index = self.__get_index(entry.hash)
                new_bucket = new_table[new_bucket_index]
                
                if new_bucket is None:
                    new_bucket = new_table[new_bucket_index] = DoublyLinkedList()
                    
                new_bucket.append(entry)
            
            # Memory cleanup of the copied bucket
            bucket.clear()
            bucket = None
        
        self.__table = new_table
    
    
    def __bucket_search_entry(self, bucket_index, key):
        '''
        Return the key's entry if the key exists in the given bucket
        of the hash table, otherwise return None, O(1)*.
        '''
        bucket = self.__table[bucket_index]
        if bucket is None: return None
        
        for entry in bucket:
            if type(entry.key) == type(key) and entry.key == key:
                return entry
        
        return None
    
    
    def get(self, key, default=None):
        '''
        Return the key's value if the key exists in the hash table,
        otherwise return the default value, O(1)*.
        NOTE: if only one argument is given, the default value is
        set to None, AND the function can return None even if
        a key's value is None, so watch out...
        '''
        self.__check_key_type(key)
        bucket_index = self.__get_index(hash(key))
        entry = self.__bucket_search_entry(bucket_index, key)
        
        if entry is None:
            return default
        else:
            return entry.value
    
    
    def __bucket_insert_entry(self, bucket_index, entry):
        '''
        Add an entry if the key does not exist in the given bucket
        of the hash table, otherwise update the key's value, O(1)*
        '''
        bucket = self.__table[bucket_index]
        if bucket is None:
            bucket = self.__table[bucket_index] = DoublyLinkedList()
        
        existent_entry = self.__bucket_search_entry(bucket_index, entry.key)
        if existent_entry is None:
            bucket.append(entry)
            self.__size += 1
            if self.__size > self.__threshold: self.__resize_table()
        else:
            existent_entry.value = entry.value
    
    
    def insert(self, key, value):
        '''
        Add a key-value pair if the key does not exist in the
        hash table, otherwise update the key's value, O(1)*
        '''
        self.__check_key_type(key)
        
        new_entry = Entry(key, value)
        bucket_index = self.__get_index(new_entry.hash)
        self.__bucket_insert_entry(bucket_index, new_entry)
    
    
    def __bucket_remove_entry(self, bucket_index, entry):
        '''
        Remove an entry and return the key's value, O(1)*.
        '''
        bucket = self.__table[bucket_index]
        bucket.remove(entry)
        self.__size -= 1
        return entry.value
    
    
    def remove(self, key, default=None):
        '''
        Remove a key-value pair and return the key's value
        if the key exists in the hash table,
        otherwise return the default value, O(1)*.
        NOTE: if only one argument is given, the default value is
        set to None, AND the function can return None even if
        a key's value is None, so watch out...
        '''
        self.__check_key_type(key)
        bucket_index = self.__get_index(hash(key))
        entry = self.__bucket_search_entry(bucket_index, key)
        
        if entry is None:
            return default
        else:
            return self.__bucket_remove_entry(bucket_index, entry)
    
    
    def keys(self):
        '''
        Return a copy of the list of keys
        found within the hash table, O(n).
        '''
        keys = []
        for bucket in self.__table:
            if bucket is None: continue
            
            for entry in bucket:
                keys.append(entry.key)
        
        return keys
    
    
    def values(self):
        '''
        Return a copy of the list of values
        found within the hash table, O(n).
        '''
        values = []
        for bucket in self.__table:
            if bucket is None: continue
            
            for entry in bucket:
                values.append(entry.value)
        
        return values
    
    
    def items(self):
        '''
        Return a copy of the list of key-value tuple pairs
        found within the hash table, O(n).
        '''
        items = []
        for bucket in self.__table:
            if bucket is None: continue
            
            for entry in bucket:
                items.append((entry.key, entry.value))
        
        return items
    
    
    def __len__(self):
        '''
        Return the size of the hash table, O(1).
        '''
        return self.__size
    
    
    def __getitem__(self, key):
        '''
        Return the key's value if the key exists in the hash table,
        otherwise raise an error, O(1)*.
        '''
        self.__check_key_type(key)
        bucket_index = self.__get_index(hash(key))
        entry = self.__bucket_search_entry(bucket_index, key)
        
        if entry is None:
            raise KeyError(f"{key}")
        else:
            return entry.value
    
    
    def __setitem__(self, key, value):
        '''
        Add a key-value pair if the key does not exist in the
        hash table, otherwise update the key's value, O(1)*
        '''
        self.insert(key, value)
    
    
    def __delitem__(self, key):
        '''
        Remove a key-value pair if the key exists in the hash table,
        otherwise raise an error, O(1)*.
        '''
        self.__check_key_type(key)
        bucket_index = self.__get_index(hash(key))
        entry = self.__bucket_search_entry(bucket_index, key)
        
        if entry is None:
            raise KeyError(f"{key}")
        else:
            self.__bucket_remove_entry(bucket_index, entry)
    
    
    def __contains__(self, key):
        '''
        Return whether ot not a key is in the hash table, O(1)*.
        '''
        try:
            self.__getitem__(key)
            return True
        except:
            return False
    
    
    def __iter__(self):
        '''
        Called when iteration is initialized, O(1).
        '''
        self.__iter_index = 0
        return self 
    
    
    def __next__(self):
        '''
        To move to the next entry, O(1).
        '''
        while self.__iter_index < self.__capacity:
            
            if self.__iterator is None:
                bucket = self.__table[self.__iter_index]
                if bucket is None:
                    self.__iter_index += 1
                    continue
                
                self.__iterator = iter(bucket)
            
            try:
                return next(self.__iterator).key
            except Exception:
                self.__iter_index += 1
                self.__iterator = None
        
        raise StopIteration
    
    
    def __str__(self):
        '''
        Return a string to print the hash table, O(n)*.
        '''
        strings = []
        for bucket in self.__table:
            if bucket is None: continue
            
            for entry in bucket:
                strings.append(str(entry))
        
        return '{' + ', '.join(strings) + '}'