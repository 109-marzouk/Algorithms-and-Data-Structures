"""
* Author: Mohamed Marzouk
* ------------------------
* Singly Linked List
* ------------------------
* Time Complixty:
    * Search: O(N)
    * Insert: O(1)
    * Deletion: O(1)
* Space Complixty: O(N)
* Used Language: Python
* Usage:
    * Dynamic memory allocation.
    * Implemented in stack and queue.
    * In undo functionality of softwares.
    * Hash tables, Graphs.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
