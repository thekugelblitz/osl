<?php
	if(isset($_GET['domain'])&&isset($_GET['record'])){
		$domain = trim($_GET['record']);
		$record = trim($_GET['url']);
		echo shell_exec("python3 dns.py '".$keyword."' '".$url."'");
	}
?>
