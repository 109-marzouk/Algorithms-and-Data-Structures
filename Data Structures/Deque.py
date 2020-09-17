"""
* Author: Mohamed Marzouk
* -----------------------
* Deque:
* -----------------------
* Time Complixty: O(1)
* Space Complixty: O(N)
* Used Language: Python
* Usage:
    * In undo operations on software.
    * To store history in browsers.
    * For implementing both stacks and queues.
"""
class Deque:
  def __init__(self):
    self.arr = []

  def isEmpty(self):
    return self.arr == []

  def addFront(self, item):
    self.arr.append(item)

  def addRear(self, item):
    self.arr.insert(0, item)

  def removeFront(self):
    return self.arr.pop()

  def removeRear(self):
    return self.arr.pop(0)

  def size(self):
    return len(self.arr)

d = Deque()
print(d.isEmpty())
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
print(d.size())
print(d.isEmpty())
d.addRear(11)
print(d.removeRear())
print(d.removeFront())
d.addFront(55)
d.addRear(45)
print(d.arr)
