/*
* Author: Mohamed Marzouk
* -------------------------
* Counting Sort Algorithm:
* -------------------------
* Time Complixty (all cases): O(N + k) or O(size + max_element)
* Space Complixty: O(max_element)
* Used Language: Dart
* Notice:
  * it is bad if the integers are very large because the array of that size should be made.
  * For More Explantion: https://www.programiz.com/dsa/counting-sort
*/
void countingSort(var arr){
  int size = arr.length;
  if(size > 1){
    int max_element = arr[0];
    for(int i = 1; i < size; i++)
      if(arr[i] > max_element) max_element = arr[i];

    var counting_list = new List(++max_element);
    for(int i = 0; i < max_element; i++){
      int count = 0;
      for(int j = 0; j < size; j++)
        if(arr[j] == i) count++;
      counting_list[i] = count;
    }

    for(int i = 1; i < max_element; i++)
      counting_list[i] += counting_list[i - 1];

    var output = new List(size + 1);
    for(int i = size - 1; i >= 0; i--)
      output[counting_list[arr[i]]-- - 1] = arr[i];

    for(int i = 0; i < size; i++) arr[i] = output[i];
  }
}
void main() {
  var arr = [9, 2, 2, 1, 4, 3, 6, 5, 7, 8, 0];
  countingSort(arr);
  print(arr);
}
