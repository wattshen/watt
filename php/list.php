<?php

$users = fopen("users.txt", "r");
while ($line = fgets($users, 4096))
{
 	  list($name, $value, $color) = explode("|", $line);
 	  printf("Name: %s <br>", $name);
 	  printf("value: %s <br>", $value);
 	  printf("Color: %s <br>", $color);
 	}
 	$a = range(0, 60, 5);
 	  



?>