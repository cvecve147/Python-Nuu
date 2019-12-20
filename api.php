<?php

require_once('./AES.php');

$user = $_GET['acc'];

$user =MD5::decryptString(str_replace(" ","+",$user));
// echo "acc:".$user."<br>";
$password = $_GET['pwd'];
$password  = MD5::decryptString(str_replace(" ","+",$password));
// echo "pwd:".$password."<br>";
echo "runing ";
$ret = system('python "./run chrome.py" ' . $user . " " . $password);