<?php
$retraso = $_GET['retraso'];
$comando = "echo raspberry | sudo -S python /var/www/html/scripts/TPMApagarRiel.py ".$retraso;
system($comando);
?>