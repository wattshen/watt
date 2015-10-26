<?php
function db_connect() {
    $result = new mysqli(SAE_MYSQL_HOST_M . ':' . SAE_MYSQL_PORT, SAE_MYSQL_USER, SAE_MYSQL_PASS);
   if (!$result) {
     throw new Exception('Could not connect to database server');
   } else {
     return $result;
   }
}


/*

function db_connect() {
    $result = new mysqli('w.rdc.sae.sina.com.cn:3307', 'xmz2z0nomw', '3jx15ymhy1hjjhw4mjj2ilm4yj3wl1km2xj4hwyz', 'app_yuhuc');
   if (!$result) {
     throw new Exception('Could not connect to database server');
   } else {
     return $result;
   }
}


*/

?>

