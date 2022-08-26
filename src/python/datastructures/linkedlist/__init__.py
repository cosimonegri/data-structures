import sys
import os

if __package__:
    from .doubly_linked_list import DoublyLinkedList
else:
    sys.path.append(os.path.dirname(__file__))
    from doubly_linked_list import DoublyLinkedList