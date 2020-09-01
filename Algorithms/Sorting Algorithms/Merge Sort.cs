using System;

class MainClass {
  static void merge(int[] arr, int leftIndex, int endLeftIndex, int endRightIndex){
    int leftArrLength = endLeftIndex - leftIndex + 1;
    int rightArrLength = endRightIndex - endLeftIndex;
    int[] leftArr = new int[leftArrLength], rightArr = new int[rightArrLength];

    for(int i = 0; i < leftArrLength; i++) leftArr[i] = arr[leftIndex + i];
    for(int j = 0; j < rightArrLength; j++) rightArr[j] = arr[endLeftIndex + j + 1];

    int mergedArrIndex = leftIndex;
    int leftIndexMerge = 0, rightIndexMerge = 0;
    while(leftIndexMerge < leftArrLength && rightIndexMerge < rightArrLength){
      if(leftArr[leftIndexMerge] < rightArr[rightIndexMerge]) arr[mergedArrIndex++] = leftArr[leftIndexMerge++];
      else arr[mergedArrIndex++] = rightArr[rightIndexMerge++];
    }
    while(leftIndexMerge < leftArrLength) arr[mergedArrIndex++] = leftArr[leftIndexMerge++];
    while(rightIndexMerge < rightArrLength) arr[mergedArrIndex++] = rightArr[rightIndexMerge++];
  }

  static void mergeSort(int[] arr, int leftIndex, int rightIndex){
    if(leftIndex < rightIndex){
      int m = leftIndex + (rightIndex - 1) / 2;
      mergeSort(arr, leftIndex, m);
      mergeSort(arr, m + 1, rightIndex);
      merge(arr, leftIndex, m, rightIndex);
    }
  }
  public static void Main (string[] args) {
    int[] arr = {1,2,5,10,1,2,3,4,4};
    mergeSort(arr, 0, arr.Length - 1);
    foreach(int i in arr) Console.WriteLine(i);
  }
}
