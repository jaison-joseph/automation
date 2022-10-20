<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="EN" dir="ltr" xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<title>Form inputs</title>
	<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	
	<body>
		
		<?php
			$num =  $_GET['num'];
			$date =  $_GET['date'];
			?>
		
		<div class="title">
			Form entries
		</div>
		<div class = "mainContainer">
			<div class="answer">
				num: <?php print $num?>
			</div>
			<div class="answer">
				date: <?php print $date?>
			</div>
		</div>
	</body>
</html>
