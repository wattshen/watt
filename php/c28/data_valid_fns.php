<?php

function filled_out($form_vars) {
  // test that each variable has a value
  foreach ($form_vars as $key => $value) {
     if ((!isset($key)) || ($value == '')) {
        return false;
     }
  }
  return true;
}

function valid_email($address) {
  // check an email address is possibly valid
  if (!filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL)) {
    return false;
    
  } else {
    return true;
  }
}
?>
