"""
* Author: Mohamed Marzouk
* ------------------------
* Doubly Linked List
* ------------------------
* Time Complixty:
    * Search: O(N)
    * Insert at Head/Tail: O(1)
    * Insert at Pos: O(N)
    * Deletion Head/Tail: O(1)
    * Deletion [middle / pos]: O(N)
* Space Complixty: O(N)
* Used Language: Python
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
