"""
* Author: Mohamed Marzouk
* -------------------------------------
* Binary Heap Data Structure (Min Heap)
* -------------------------------------
* Time Complixty:
    * Building: O(N)
    * Inserting: O(log(N))
    * Peaking [first element]: Big Theta(1)
    * Polling [delete]: Big Theta(log(N))
    * Merging: Big Theta(N)
* Used Language: Python
* Usage:
    * Heap is used while implementing a priority queue.
    * Dijkstra’s Algorithm
    * Heap Sort
"""
def heapify(arr, size, i):
  smallest = i;
  left = 2 * i + 1;
  right = 2 * i + 2;

  if left < size and arr[i] > arr[left]:
    smallest = left;
  if right < size and arr[smallest] > arr[right]:
    smallest = right
  if smallest != i:
    arr[i], arr[smallest] = arr[smallest], arr[i] # Swapping
    heapify(arr, size, smallest)

def insert(arr, num):
  size = len(arr)
  arr.append(num)
  if size != 0:
    for i in range(((len(arr) - 1) // 2), -1, -1):
      heapify(arr, len(arr), i)

def deleteNode(arr, num):
  size = len(arr)
  for i in range(0, size):
    if arr[i] == num: break
  arr[i], arr[size - 1] = arr[size - 1], arr[i]
  arr.remove(arr[size - 1])
  for i in range(((len(arr) - 1) // 2), -1, -1):
    heapify(arr, len(arr), i)

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Min-Heap array: " + str(arr))
"""
     2
    / \
   3   9
  /\
 5  4
"""

deleteNode(arr, 2)
print("After deleting an element: " + str(arr))
"""
     3
    / \
   4   9
  /
 5
"""
