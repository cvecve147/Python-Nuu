<?php
echo "123";
$user = "U0633126";
$password = "cplyuef357";
$ret = system('conda activate');
$ret = system('python "./run chrome.py" ' . $user . " " . $password);
echo $ret;
