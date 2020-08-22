<?php
	if(isset($_GET['keyword'])&&isset($_GET['url'])){
		$keyword = trim($_GET['keyword']);
		$url = trim($_GET['url']);
		echo shell_exec("python3 run.py '".$keyword."' '".$url."'");
	}
?>
