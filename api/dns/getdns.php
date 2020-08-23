<?php
	if(isset($_GET['domain'])&&isset($_GET['record'])){
		$domain = trim($_GET['domain']);
		$record = trim($_GET['record']);
		echo shell_exec("python dnss.py ".$domain." ".$record);
	}
?>
