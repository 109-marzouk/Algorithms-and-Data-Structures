/*
* Author: Mohamed Marzouk
* -------------------------
* Shell Sort Algorithm:
* -------------------------
* Worst Case Time Complixty: O(N^2)
* Average Case Time Complixty: O(N^(5/4)) or O(N^(3/2))
* => it depends on the gap's size.
* Space Complixty: O(1)
* Used Language: C++
*--------------------
* not stable.
*/
#include <iostream>
using namespace std;
void shellSort(int arr[], int n) {
  for(int gap = n / 2; gap > 0; gap /= 2){
    for(int i = gap; i < n; i++){
      int temp = arr[i];
      int j;
      for(j = i; j >= gap && arr[j - gap] > temp; j -= gap){
        arr[j] = arr[j - gap];
      }
      arr[j] = temp;
    }
  }
}
void printArray(int array[], int size) {
  for (int i = 0; i < size; i++) cout << array[i] << " ";
  cout << endl;
}
int main() {
  int arr[] = {8, 2, 3, 4, 1, 5, 9};
  int size = sizeof(arr) / sizeof(arr[0]);
  shellSort(arr, size);
  cout << "Sorted array: \n";
  printArray(arr, size);
}
