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
    self.head = self.tail = Node(None)
    self.tail.next = self.head
    self.head.next = self.tail

  def add(self, data):
    newNode = Node(data)
    if self.head.data is not None:
      self.tail.next = newNode
      self.tail = newNode
      newNode.next = self.head
    else:
      self.head = self.tail = newNode
      newNode.next = self.head
  def display(self):
    current = self.head;
    if self.head is None:
      print("List is empty");
      return;
    else:
      print("Nodes of the circular linked list: ");
      print(current.data)
      while(current.next != self.head):
        current = current.next;
        print(current.data)


cllist = CircularLinkedList()
cllist.add(5)
cllist.add(2)
cllist.add(1)
cllist.add(3)
cllist.display()
