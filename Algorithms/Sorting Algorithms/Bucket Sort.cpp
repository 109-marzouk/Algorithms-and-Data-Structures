/*
* Author: Mohamed Marzouk
* -------------------------
* Bucket Sort Algorithm:
* -------------------------
* Worst Case Time Complixty: O(N^2)
  * => it depends also on the sorting algorithm used to sort the elements of the bucket.
* Average Case Time Complixty: O(N + (N^2/K) + K)
  * => where k is number of the buckets.
  * => O(N) when K ~ N
* Best Case Time Complixty: O(N + K)
  * => O(N) is the complexity for making the buckets.
  * => O(K) is the complexity for sorting the elements of the bucket using algorithms having linear time complexity at the best case.
* Space Complixty: O(N + K)
* Used Language: C++
*/
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

void bucketSort(float arr[], int size){
  vector<float> buckets[size];
  for(int i = 0; i < size; i++)
    buckets[(int)(arr[i] * 10)].push_back(arr[i]);

  for(int i = 0; i < size; i++)
    sort(buckets[i].begin(), buckets[i].end());

  int index = 0;
  for(int i = 0; i < size; i++)
    for(int j = 0; j < buckets[i].size(); j++)
      arr[index++] = buckets[i][j];
}
int main(){
  float arr[] = {0.325, 0.1, 0.547, 0.215114, 0.2574, 0.582, 0.78};
  int n = sizeof(arr)/sizeof(arr[0]);
  bucketSort(arr, n);

  cout << "Sorted array is \n";
  for (int i=0; i<n; i++) cout << arr[i] << " ";
  return 0;
} 
