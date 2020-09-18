"""
* Author: Mohamed Marzouk
* ------------------------
* Circular Linked List
* ------------------------
* Time Complixty:
    * Search: O(N)
    * Insert: O(1)
    * Deletion: O(1)
* Space Complixty: O(N)
* Used Language: Python
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
