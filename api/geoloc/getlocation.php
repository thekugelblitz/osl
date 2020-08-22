<?php
	if(isset($_GET['ip'])){
		$ip = trim($_GET['ip']);
		echo shell_exec("python3 geoloc.py '".$ip."'");
	}
?>
