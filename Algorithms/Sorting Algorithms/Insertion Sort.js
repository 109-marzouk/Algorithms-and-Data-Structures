/*
* Author: Mohamed Marzouk
* -------------------------
* Insertion Sort Algorithm:
* -------------------------
* Worst Case Time Complixty: O(N^2)
* Space Complixty: O(1)
* Used Language: JavaScript
*/

let arr = [5, 2, 3, 4, 1, 10, 12, 7, 1, 4];

for(let i = 1; i < arr.length; i++){
  let curr = arr[i], j = i;
  while(--j >= 0 && curr < arr[j]) arr[j+1] = arr[j];
  arr[j+1] = curr;
}
console.log(arr);