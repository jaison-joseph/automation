<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="EN" dir="ltr" xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<title>User Registration</title>
	<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	
	<body>
		
		<?php
			
			// variables for form fields
			$num = "";
			$date = "";
			
			// variables to enforce reuqired fields
			$num_re = "*";
			$date_re = "*";
			
			$flag = FALSE;	// flag that's set to TRUE if any of the required fields are not filled
			
			if (isset($_POST['enter'])) {
				if (isset($_POST['num'])) {
					$num = trim($_POST['num']);
				}
				if ($num == "") {
					$flag = TRUE;
					$num_re = '<span style="color:red">*</span>';
				}
				
				if (isset($_POST['date'])) {
					$date = trim($_POST['date']);
				}
				if ($date == "") {
					$flag = TRUE;
					$date_re = '<span style="color:red">*</span>';
				}
				
				if (!$flag) {
					Header ("Location:output.php?num=".$num."&date=".$date);
				}
			}
		?>
		
		<form action=test.php method="post">
			<div class="title">
				test
			</div>
			<div class = "mainContainer">
				<div class = "question">
				Number: <?php print $num_re; ?>
				<input type="number" value="<?php print $num; ?>" name="num" />
				</div>
				<div class = "question">
				Date: <?php print $date_re; ?>
				<input type="date" name="date" + value=<?php print $date?>>
				</div>
				<div class = "submitButton">
					<input name="enter" class="btn" type="submit" value="Submit" style="height: 30px; width: 60px; font-family: helvetica;"/> 
				</div>
			</div>
		</form>
	</body>
</html>
