<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="EN" dir="ltr" xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<title>Form inputs</title>
	<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	
	<body>
		
		<?php
			$userID =  $_GET['userID'];
			$listID =  $_GET['listID'];
			?>
		
		<div class="title">
			Form entries
		</div>
		<div class = "mainContainer">
			<div class="answer">
				userID: <?php print $userID?>
			</div>
			<div class="answer">
				listID: <?php print $listID?>
			</div>
		</div>
	</body>
</html>
