"""
* Author: Mohamed Marzouk
* ------------------------
* Hash Table
* ------------------------
* Average Case Time Complixty:
    * Search, Insert and Delete: O(1)
* Worst Case Time Complixty:
    * Search, Insert and Delete: O(N)
* Space Complixty: O(N)
* Used Language: Python
"""
hashTable = [[]] * 10
def checkPrime(n):
  if n == 1 or n == 0:
    return 0
  for i in range(2, n//2):
    if n % i == 0:
      return 0
  return 1

def getPrime(n):
  if n % 2 == 0:
    n = n + 1
  while not checkPrime(n):
    n += 2
  return n

def hashFunction(key):
  capacity = getPrime(10)
  return key % capacity

def insertData(key, data):
  index = hashFunction(key)
  if key in hashTable[index]:
    hashTable[index].append(data)
    return
  hashTable[index] = [key, data]

def removeData(key):
  index = hashFunction(key)
  hashTable[index] = 0

insertData(404, "mohamed")
insertData(404, "ahmed")
insertData(500, "mido")

print(hashTable)
