<?php

function db_connect() {
   $result = new mysqli('SAE_MYSQL_HOST_M', 'SAE_MYSQL_USER', 'SAE_MYSQL_PASS', 'SAE_MYSQL_DB');
   if (!$result) {
      return false;
   }
   $result->autocommit(TRUE);
   return $result;
}

function db_result_to_array($result) {
   $res_array = array();

   for ($count=0; $row = $result->fetch_assoc(); $count++) {
     $res_array[$count] = $row;
   }

   return $res_array;
}

?>
