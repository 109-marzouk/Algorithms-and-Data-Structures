/*
* Author: Mohamed Marzouk
* -------------------------
* Ternary Search Algorithm:
* -------------------------
* Worst Case Time Complixty: O(log3(N))
* Space Complixty: O(N) [in case of recursive implementation] / O(1) [in case of iterative implementation]
* Used Language: JavaScript
*/
function RecursiveTernarySearch(arr, left, right, target){
  if(right > left){
    let firstMid = left + (right - left) / 3;
    let secondMid = firstMid + (right - left) / 3;
    if(arr[firstMid] == target) return firstMid;
    if(arr[secondMid] == target) return secondMid;
    if(target < arr[firstMid])
      return RecursiveTernarySearch(arr, left, firstMid - 1, target);
    else if(target > arr[secondMid])
      return RecursiveBinarySearch(arr, secondMid + 1, right, target);
    else
      return RecursiveBinarySearch(arr, firstMid + 1, secondMid - 1, target);
  }
  return -1;
}

let arr = [1, 2, 3, 4, 5, 6, 15, 22];
