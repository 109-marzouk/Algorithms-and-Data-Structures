"""
* Author: Mohamed Marzouk
* ------------------------
* Singly Linked List
* ------------------------
* Time Complixty:
    * Search: O(N)
    * Insert: O(N) [Except Insertion At Beginning: O(1)]
    * Deletion: O(N)
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

    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self, node, data):
        if node is None:
            print("The pervious Node must be in the LinkedList.")
            return
        newNode = Node(data)
        newNode.next = node.next
        node.next = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next():
            lastNode = lastNode.next
        lastNode.next = newNode

    def deleteAt(self, pos):
        if self.head is None: return
        tempNode = self.head
        for i in range(pos - 1):
            tempNode = tempNode.next
            if tempNode is None: break
        if tempNode is None or tempNode.next is None:
            return
        tempNode.next = tempNode.next.next
