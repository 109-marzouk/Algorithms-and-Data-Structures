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
    for i in range((size // 2) - 1, -1, -1):
      heapify(arr, size, i)

def deleteNode(arr, num):
  size = len(arr)
  i = 0
  for i in range(0, size):
    if arr[i] == num: break
  arr[i], arr[size - 1] = arr[size - 1], arr[i]
  arr.remove(size - 1)
  for i in range((len(arr) // 2) - 1, -1, -1):
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
deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
