"""
* Author: Mohamed Marzouk
* -----------------------
* Circular Queue:
* -----------------------
* Time Complixty: O(1)
* Space Complixty: O(N)
* Used Language: Python
* Usage:
    * CPU scheduling
    * Memory management
    * Traffic Management
"""
class CircularQueue():
  def __init__(self, size):
    self.size = size
    self.queue = [" "] * size
    self.first = self.last = -1

  def enqueue(self, item):
    if self.first == self.last == -1:
      self.queue[0] = item
      self.first = self.last = 0
    elif (self.last + 1) % self.size == self.first:
      print("The Circular Queue is full.")
    else:
      self.last = (self.last + 1) % self.size
      self.queue[self.last] = item

  def dequeue(self):
    if self.first == self.last == -1:
      print("The Circular Queue is empty.")
    elif self.first == self.last != -1:
      print(self.queue[self.first])
      self.queue[self.first] = " "
      self.first = self.last = -1
    else:
      print(self.queue[self.first])
      self.queue[self.first] = " "
      self.first = (self.first + 1) % self.size

  def print(self):
    print("".join(map(str, self.queue)))

obj = CircularQueue(5)
obj.enqueue(1)
obj.print()
obj.enqueue(2)
obj.print()
obj.enqueue(3)
obj.print()
obj.enqueue(4)
obj.print()
obj.enqueue(5)
obj.print()
obj.dequeue()
obj.print()
obj.dequeue()
obj.print()
obj.enqueue(6)
obj.print()
obj.enqueue(7)
obj.print()
obj.enqueue(8)
obj.print()
