"""
* Author: Mohamed Marzouk
* -----------------------
* Queue:
* -----------------------
* Time Complixty: O(1)
* Space Complixty: O(N)
* Used Language: Python
* Usage:
    * CPU scheduling, Disk Scheduling
    * When data is transferred asynchronously between two processes.The queue is used for synchronization. eg: IO Buffers, pipes, file IO, etc
    * Handling of interrupts in real-time systems.
    * Call Center phone systems use Queues to hold people calling them in an order
"""
class Queue:
    def __init__(self): self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1: return None
        return self.queue.pop(0)

    def display(self): print(self.queue)

    def size(self): return len(self.queue)

q = Queue()
q.enqueue(3)
q.enqueue(2)
q.enqueue(5)
q.enqueue(4)

q.display()

q.dequeue()
print("After removing an element")
q.display()
