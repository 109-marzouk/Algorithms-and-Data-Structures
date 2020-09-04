/*
* Author: Mohamed Marzouk
* -------------------------
* Quick Sort Algorithm:
* -------------------------
* Best & Average Case Time Complixty: O(N . log(N))
* Worst Case Time Complixty: O(N^2)
* => this happens when the array is sorted.
* n * (n-1) * (n-2) * ...
* => to optmize this algorithm in the worst case we can choose the pivot
* from the the middle or randomly. (Organized Quick Sort)
* Space Complixty: O(1)
* Used Language: Java
*/

public class Main {

  public static int partition(int[] arr, int start, int end){
  	int pivotIndex = (start + end) / 2;
  	int temp = arr[end];
  	arr[end] = arr[pivotIndex];
  	arr[pivotIndex] = temp;
  	pivotIndex = end;
  	int partitionIndex = start;
  	for(; start < end; start++){
  		if(arr[start] <= arr[pivotIndex]){
  			int t = arr[start];
  			arr[start] = arr[partitionIndex];
  			arr[partitionIndex++] = t;
      }
    }
    int t2 = arr[partitionIndex];
    arr[partitionIndex] = arr[end];
    arr[end] = t2;
    return partitionIndex;
  }

  public static void quickSort(int[] arr, int start, int end){
    if(start < end){
  		int partitionIndex = partition(arr, start, end);
  		quickSort(arr, start, partitionIndex - 1);
  		quickSort(arr, partitionIndex + 1, end);
    }
  }

  public static void main( String args[] ) {
    int arr[] = {10, 7, 8, 9, 1, 5, 1};
    int n = arr.length; 
    quickSort(arr, 0, n-1);
    for(int i = 0; i < n; i++) System.out.print(arr[i] + " ");
  }
}
