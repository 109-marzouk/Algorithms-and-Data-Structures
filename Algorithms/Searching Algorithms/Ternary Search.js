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
    let firstMid = left + Math.floor((right - left) / 3);
    let secondMid = firstMid + Math.floor((right - left) / 3);
    if(arr[firstMid] == target) return firstMid;
    if(arr[secondMid] == target) return secondMid;
    if(target < arr[firstMid])
      return RecursiveTernarySearch(arr, left, firstMid - 1, target);
    else if(target > arr[secondMid])
      return RecursiveTernarySearch(arr, secondMid + 1, right, target);
    else
      return RecursiveTernarySearch(arr, firstMid + 1, secondMid - 1, target);
  }
  return -1;
}

function IterativeTernarySearch(arr, left, right, target){
  while(right >= left){
    let firstMid = left + Math.floor((right - left) / 3);
    let secondMid = firstMid + Math.floor((right - left) / 3);
    if(arr[firstMid] == target) return firstMid;
    if(arr[secondMid] == target) return secondMid;
    if(target < arr[firstMid])
      right = firstMid - 1;
    else if(target > arr[secondMid])
      left = secondMid + 1;
    else{
      left = secondMid + 1;
      right = firstMid - 1;
    }
  }
  return -1;
}
let arr = [1, 2, 3, 4, 5, 6, 15, 22];
console.log(RecursiveTernarySearch(arr, 0, arr.length - 1, 15));
console.log(IterativeTernarySearch(arr, 0, arr.length - 1, 22));
