/*
* Author: Mohamed Marzouk
* -------------------------
* Binary Search Algorithm:
* -------------------------
* Worst Case Time Complixty: O(log(N))
* Space Complixty: O(N) [in case of recursive implementation] / O(1) [in case of iterative implementation]
* Used Language: C#
*/

using System;
class MainClass {
  public static int BinarySearch(int[] arr, int start, int end, int target){
    // this fuction return the target's index if it exists.
    if(end >= start){
      int mid = (start + end) / 2;
      if(arr[mid] == target) return mid;
      else if(arr[mid] < target) return BinarySearch(arr, start, end - 1, target);
      else return BinarySearch(arr, mid + 1, end, target);
    }
    // return -1 if the target dosn't exist.
    return -1;
  }
  public static void Main (string[] args) {
    int[] arr = {5, 2, 3, 1};
    Console.WriteLine (BinarySearch(arr, 0, arr.Length - 1, 1));
  }
}
