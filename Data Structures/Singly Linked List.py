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
    self.head = self.tail = None
    self.size = 0

  def __len__(self): return self.size

  # O(1)
  def insertAtBeginning(self, data):
    newNode = Node(data)
    newNode.next = self.head
    self.head = newNode
    self.size += 1

  # O(N)
  def insertAfter(self, node, data):
    if node is None:
      print("The pervious Node must be in the LinkedList.")
      return
    newNode = Node(data)
    newNode.next = node.next
    node.next = newNode
    self.size += 1

  # O(1)
  def insertAtEnd(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = self.tail = newNode
      self.head.next = self.tail
      return
    self.tail.next = newNode
    self.tail = newNode
    self.size += 1

  # O(1)
  def deleteAtBeginning(self):
    self.head = self.head.next

  # O(N)
  def deleteAt(self, pos):
    if self.head is None: return
    tempNode = self.head
    for i in range(pos - 1):
      tempNode = tempNode.next
      if tempNode is None: break
    if tempNode is None or tempNode.next is None:
      return
    tempNode.next = tempNode.next.next

  # O(N)
  def reverse(self):
    prev = Node(None)
    currentNode = self.head
    following = currentNode.next
    while currentNode:
      currentNode.next = prev
      prev = currentNode
      currentNode = following
      if following:
        following = following.next
    self.head, self.tail = self.tail, self.head

  def __str__(self):
    currentNode = self.head
    result = ""
    while currentNode:
      s = ""
      if currentNode.next is not None: s = " -> "
      result += (str(currentNode.data) + s)
      currentNode = currentNode.next
    return result

llist = SinglyLinkedList()
llist.insertAtEnd(1)
llist.insertAtBeginning(2)
llist.insertAtBeginning(3)
llist.insertAtEnd(4)
llist.insertAfter(llist.head.next, 5)

print('Linked list:')
print(llist)

print("\nAfter deleting an element:")
llist.deleteAt(3)
print(llist)

print("\nAfter reversing the linked list:")
llist.reverse()
print(llist)
