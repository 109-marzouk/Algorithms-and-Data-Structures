/*
* Author: Mohamed Marzouk
* -------------------------
* Bubble Sort Algorithm:
* -------------------------
* Worst Case Time Complixty: O(N^2)
* Space Complixty: O(1)
* Used Language: C#
*/

using System;
class MainClass {
  public static void Main (string[] args) {

    int[] arr = {5, 2, 3, 4, 1, 10, 12, 7, 1, 4};
    int temp;

    for(int i = 0; i < arr.Length; i++){
      for(int x = arr.Length - 1; x > 0; x--){
        if(arr[x-1] > arr[x]){
          temp = arr[x];
          arr[x] = arr[x-1];
          arr[x-1] = temp;
        }
      }
    }
    for(int i = 0; i < arr.Length; i++) Console.Write(arr[i] + ", ");
  }
}