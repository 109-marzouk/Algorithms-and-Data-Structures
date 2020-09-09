"""
* Author: Mohamed Marzouk
* -------------------------
* Linear Search Algorithm:
* [Sequential Search]
* -------------------------
* Time Complixty: O(N)
* Space Complixty: O(1)
* Used Language: Python
"""
my_list = [5, 2, 3, 4, 1, 8]
def LinearSearch(arr, target):
  i = 0
  while i < len(arr):
    if arr[i] == target:
      return i
    i += 1
  return -1
print(LinearSearch(my_list, 1))
print(LinearSearch(my_list, 9))
