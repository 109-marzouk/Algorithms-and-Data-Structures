<?php
/*
* Author: Mohamed Marzouk
* --------------------------------
* Self Organized Search Algorithm:
* // Transpose Method [ array ]
* --------------------------------
* Worst Case Time Complixty: O(N)
* Space Complixty: O(1)
* Used Language: PHP
*/

$arr = array(5, 2, 3, 4, 6);
function SelfOrganizedSearch(&$arr, $target){
  for($i = 0; $i < count($arr); $i++){
    if($arr[$i] == $target){
      if($i != 0){
        $temp = $arr[$i];
        $arr[$i] = $arr[$i - 1];
        $arr[$i - 1] = $temp;
      }
      return $i;
    }
  }
  return -1;
}
echo SelfOrganizedSearch($arr, 2);
echo $arr[0];
