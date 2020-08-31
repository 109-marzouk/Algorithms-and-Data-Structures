/*
* Author: Mohamed Marzouk
* -------------------------
* Selection Sort Algorithm:
* -------------------------
* Time Complixty: O(N^2)
* Space Complixty: O(1)
*/

#include <iostream>
using namespace std;

int main() {

  const int arr_size = 10;
  int arr[arr_size] = {5, 2, 3, 4, 1, 10, 12, 7, 1, 4}, min_num, temp;

  for(int i = 0; i < arr_size; i++){
    min_num = arr[i];
    for(int x = i + 1; x < arr_size; x++){
      if( arr[x] < min_num){
        min_num = arr[x];
        temp = arr[i];
        arr[i] = min_num;
        arr[x] = temp;
      }
    }
  }
  for(int i = 0; i < arr_size; i++) cout << arr[i] << ", ";
}