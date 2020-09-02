/*
* Author: Mohamed Marzouk
* -------------------------
* Bubble Sort Algorithm:
* -------------------------
* Worst Case Time Complixty: O(N . log(N))
* Space Complixty: N + log(N) => O(N)
* Used Language: C#
*/
using System;

class MainClass {

  static void merge(int[] arr, int leftIndex, int endLeftIndex, int endRightIndex){
    // leftArr [leftIndex ... endLeftIndex]
    // rightArr [endLeftIndex + 1 ...  endRightIndex]
    int leftArrLength = endLeftIndex - leftIndex + 1;
    int rightArrLength = endRightIndex - endLeftIndex;

    int[] leftArr = new int[leftArrLength], rightArr = new int[rightArrLength];

    // Copying the data from the parent Array to the leftArr & rightArr
    for(int i = 0; i < leftArrLength; i++)
      leftArr[i] = arr[leftIndex + i];
    for(int j = 0; j < rightArrLength; j++)
      rightArr[j] = arr[endLeftIndex + j + 1];

    // the start index of the array that will be merged
    int mergedArrIndex = leftIndex;

    // set two start pointers for both left and right arrays
    int leftIndexMerge = 0, rightIndexMerge = 0;

    // the merging operation
    while(leftIndexMerge < leftArrLength && rightIndexMerge < rightArrLength){
      if(leftArr[leftIndexMerge] < rightArr[rightIndexMerge])
        arr[mergedArrIndex++] = leftArr[leftIndexMerge++];
      else
        arr[mergedArrIndex++] = rightArr[rightIndexMerge++];
    }

    // copying the rest elements
    while(leftIndexMerge < leftArrLength)
      arr[mergedArrIndex++] = leftArr[leftIndexMerge++];

    while(rightIndexMerge < rightArrLength)
      arr[mergedArrIndex++] = rightArr[rightIndexMerge++];
  }

  static void mergeSort(int[] arr, int leftIndex, int endRightIndex){
    if(leftIndex < endRightIndex){
      // leftArr [leftIndex ... m]
      // rightArr [m + 1 ...  endRightIndex]
      int m = leftIndex + (endRightIndex - leftIndex) / 2;
      mergeSort(arr, leftIndex, m);
      mergeSort(arr, m + 1, endRightIndex);
      merge(arr, leftIndex, m, endRightIndex);
    }
  }
  public static void Main (string[] args) {
    int[] arr = {1,2,5,10,1,2,3,4,4};
    mergeSort(arr, 0, arr.Length-1);
    foreach(int i in arr) Console.WriteLine(i);
  }
}
