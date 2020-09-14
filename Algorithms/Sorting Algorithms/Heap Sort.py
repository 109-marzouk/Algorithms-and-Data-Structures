"""
* Author: Mohamed Marzouk
* ----------------------------------------
* Heap Sort Algorithm (Descending order):
* ----------------------------------------
* Time Complixty: O(N . log(N))
* Space Complixty: O(1)
* Used Language: Python
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

def heapSort(arr):
  size = len(arr)
  for i in range((size//2) - 1, -1, -1):
    heapify(arr, size, i)
  for i in range(size - 1, -1, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, i, 0)

arr = [9, 2, 3, 1, 8, 4, 10]
heapSort(arr)
print(arr)
