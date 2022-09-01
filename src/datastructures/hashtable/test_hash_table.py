'''
 * A hash table unit test.
 *
 * @author  Cosimo Giovanni Negri
 * @mention William Fiset, william.alexandre.fiset@gmail.com
 * @date    28 Aug 2022
'''

import unittest
import sys
import os
import random

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from datastructures.hashtable.hash_table_separate_chaining import HashTableSeparateChaining
else:
    from .hash_table_separate_chaining import HashTableSeparateChaining


class HashableObject:
    
    def __init__(self, data, hash):
        self.data = data
        self.hash = hash
    
    def __hash__(self):
        return self.hash
    
    def __eq__(self, other):
        if self.hash != other.hash:
            return False
        return self.data == other.data


class NonHashableObject:
    
    def __init__(self, data):
        self.data = data
    
    def __eq__(self, other):
        return self.data == other.data


class HashTableTest(unittest.TestCase):
    
    def setUp(self):
        self.LOOPS = 200
        self.SIZE = 40
        self.MAX_RANDOM_NUM = 250
        
        self.dict = HashTableSeparateChaining()
    
    
    def test_empty_dict(self):
        self.assertTrue(self.dict.isempty())
        self.assertEqual(len(self.dict), 0)
    
    
    def test_none_key(self):
        with self.assertRaises(TypeError):
            self.dict.add(None, 5)
    
    
    def test_bool_key(self):
        with self.assertRaises(TypeError):
            self.dict.add(True, 3)
        with self.assertRaises(TypeError):
            self.dict.add(False, 3)
    
    
    def test_non_hashable_key(self):
        with self.assertRaises(TypeError):
            self.dict.add([], 3)
        with self.assertRaises(TypeError):
            self.dict.add({}, 3)
        with self.assertRaises(TypeError):
            self.dict.add(set(), 3)
        with self.assertRaises(TypeError):
            self.dict.add(NonHashableObject("data"), 3)
    
    
    def test_valid_key(self):
        for i in range(self.LOOPS // 2):
            self.dict.add("a", 10)
            self.assertEqual(self.dict.get("a"), 10)
            self.dict.add(1, 11)
            self.assertEqual(self.dict.get(1), 11)
            self.dict.add(1.1, 12)
            self.assertEqual(self.dict.get(1.1), 12)
            self.dict.add(("g", 2), 13)
            self.assertEqual(self.dict.get(("g", 2)), 13)
            
            object = HashableObject("data", i*100)
            self.dict.add(object, i*10)
            self.assertEqual(self.dict.get(object), i*10)
            
            self.assertEqual(len(self.dict), 5)
            self.assertFalse(self.dict.isempty())
            self.dict.clear()
    
    
    def test_add(self):
        self.dict.add(1, 10)
        self.assertEqual(self.dict.get(1), 10)
        self.dict.add(2, 20)
        self.assertEqual(self.dict.get(2), 20)
        self.dict.add(1, 5)
        self.assertEqual(self.dict.get(1), 5)
        self.dict.add(1, -7)
        self.assertEqual(self.dict.get(1), -7)
        self.assertEqual(len(self.dict), 2)
        
    
    def test_get(self):
        self.assertEqual(self.dict.get(1), None)
        self.assertEqual(self.dict.get(1, "nothing"), "nothing")
        self.dict.add(1, 10)
        self.assertEqual(self.dict.get(1), 10)
    
    
    def test_remove(self):
        self.assertEqual(self.dict.remove(1), None)
        self.assertEqual(self.dict.remove(1, "nothing"), "nothing")
        self.dict.add(1, 10)
        self.dict.add(2, 20)
        self.dict.add(3, 30)
        self.assertEqual(self.dict.remove(1), 10)
        self.assertEqual(self.dict.remove(2), 20)
        self.assertEqual(self.dict.remove(3), 30)
        self.assertEqual(len(self.dict), 0)
    
    
    def test_clear(self):
        self.dict.add(1, 10)
        self.dict.add(2, 30)
        self.dict.add(3, 30)
        self.assertEqual(len(self.dict), 3)
        self.dict.clear()
        self.assertEqual(len(self.dict), 0)
        self.dict.add(1, 10)
        self.dict.add(2, 30)
        self.dict.add(3, 30)
        self.assertEqual(len(self.dict), 3)
        self.dict.clear()
        self.assertEqual(len(self.dict), 0)
    
    
    def test_keys(self):
        self.dict.add(1, 10)
        self.dict.add(2, 20)
        self.dict.add(3, 30)
        self.dict.add(4, 40)
        self.dict.add(5, 50)
        self.assertEqual(
            sorted(self.dict.keys()),
            [1, 2, 3, 4, 5]
        )
    
    
    def test_values(self):
        self.dict.add(1, 10)
        self.dict.add(2, 20)
        self.dict.add(3, 30)
        self.dict.add(4, 40)
        self.dict.add(5, 50)
        self.assertEqual(
            sorted(self.dict.values()),
            [10, 20, 30, 40, 50]
        )

    
    def test_items(self):
        self.dict.add(1, 10)
        self.dict.add(2, 20)
        self.dict.add(3, 30)
        self.dict.add(4, 40)
        self.dict.add(5, 50)
        self.assertEqual(
            sorted(self.dict.items()),
            [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]
        )
    
    
    def test_random_remove(self):
        python_dict = {}
        
        for _ in range(self.LOOPS):
            rand_keys = self.get_rand_list()
            rand_values = self.get_rand_list()
            
            for key, value in zip(rand_keys, rand_values):
                self.dict[key] = value
                python_dict[key] = value
            
            random.shuffle(rand_keys)
            
            for key in rand_keys:
                value1 = self.dict.remove(key)
                value2 = python_dict.pop(key)
                self.assertEqual(value1, value2)
                self.assertEqual(len(self.dict), len(python_dict))
                
                # check that the dictionaries have the same elements
                dict_iter = iter(self.dict)
                while True:
                    try:
                        temp_key = next(dict_iter)
                        value1 = self.dict[temp_key]
                        value2 = python_dict[temp_key]
                        self.assertEqual(value1, value2)
                    except StopIteration:
                        break
                
            self.assertEqual(len(self.dict), 0)
            self.assertEqual(len(python_dict), 0)
    
    
    def test_complex_objects(self):
        object1 = HashableObject("data1", 666)
        object2 = HashableObject("data2", 777)
        object3 = HashableObject("data2", 888)
        object4 = HashableObject("data3", 999)
        
        self.dict.add(object1, 1)
        self.dict.add(object2, 2)
        self.dict.add(object3, 3)
        self.dict.add(object4, 4)
        self.dict.add(object4, 40)
        self.dict.add(object4, -67)
        self.assertEqual(len(self.dict), 4)
        
        self.dict.remove(object1)
        self.dict.remove(object2)
        self.dict.remove(object3)
        self.dict.remove(object4)
        self.assertEqual(len(self.dict), 0)
    
    
    def test_setitem(self):
        self.dict[1] = 10
        self.assertEqual(self.dict[1], 10)
        self.dict[2] = 20
        self.assertEqual(self.dict[2], 20)
        self.dict[1] = 5
        self.assertEqual(self.dict[1], 5)
        self.dict[1] = -7
        self.assertEqual(self.dict[1], -7)
        self.assertEqual(len(self.dict), 2)
    
    
    def test_getitem(self):
        with self.assertRaises(KeyError):
            self.dict[1]
        self.dict[1] = 10
        self.assertEqual(self.dict[1], 10)
    
    
    def test_delitem(self):
        with self.assertRaises(KeyError):
            del self.dict[1]
        self.dict[1] = 10
        self.dict[2] = 20
        self.dict[3] = 30
        del self.dict[1]
        del self.dict[2]
        del self.dict[3]
        self.assertEqual(len(self.dict), 0)
    
    
    def test_contains(self):
        self.assertFalse(3 in self.dict)
        self.dict.add(3, 5)
        self.assertTrue(3 in self.dict)
        self.assertEqual(len(self.dict), 1)
    
    
    def test_iteration(self):
        with self.assertRaises(StopIteration):
            iter_obj = iter(self.dict)
            next(iter_obj)
        
        self.dict.add(4, 40)
        self.dict.add(5, 50)
        self.dict.add(6, 60)
        self.assertEqual(len(self.dict), 3)
        
        keys = []
        iter_obj = iter(self.dict)
        for _ in range(3):
            keys.append(next(iter_obj))
        self.assertEqual(sorted(keys), [4, 5, 6])
        
        with self.assertRaises(StopIteration):
            next(iter_obj)
    
    
    def test_to_string(self):
        self.assertEqual(str(self.dict), "{}")
        self.dict.add('a', 1)
        self.assertEqual(str(self.dict), "{a: 1}")
        
        self.dict.add('b', 2)
        self.dict.add('c', 3)
        self.assertIn(
            str(self.dict),
            ["{a: 1, b: 2, c: 3}",
             "{a: 1, c: 3, b: 2}",
             "{b: 2, a: 1, c: 3}",
             "{b: 2, c: 3, a: 1}",
             "{c: 3, a: 1, b: 2}",
             "{c: 3, b: 2, a: 1}",]
        )
        
        self.dict.remove('b')
        self.assertIn(
            str(self.dict),
            ["{a: 1, c: 3}", "{c: 3, a: 1}"]
        )
    
    
    def get_rand_list(self):
        '''
        Generate a list of random numbers.
        '''
        list = random.sample(range(0, self.MAX_RANDOM_NUM), self.SIZE)
        random.shuffle(list)
        return list
    

if __name__ == '__main__':
    unittest.main()