<?php

function db_connect()
{
    $result = new mysqli(SAE_MYSQL_HOST_M.':'.SAE_MYSQL_PORT,SAE_MYSQL_USER,SAE_MYSQL_PASS,SAE_MYSQL_DB);
    if(!$result){
        throw new Exception('could not connect to database server');
    }else
    {
        return $result;
    }
    
    
    
}


?>

