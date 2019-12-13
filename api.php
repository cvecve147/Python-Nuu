<?php
$user = $_GET['acc'];
$password = $_GET['pwd'];
echo "runing ";
$ret = system('python "./run chrome.py" ' . $user . " " . $password);