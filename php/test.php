<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="EN" dir="ltr" xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<title>User Registration</title>
	<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	
	<body>
		
		<?php
			
			// variables for form fields
			$userID = "";
			$listID = "";
			
			// variables to enforce reuqired fields
			$userID_re = "*";
			
			$flag = FALSE;	// flag that's set to TRUE if any of the required fields are not filled
			
			if (isset($_POST['enter'])) {
				if (isset($_POST['userID'])) {
					$userID = trim($_POST['userID']);
				}
				if ($userID == "") {
					$flag = TRUE;
					$userID_re = '<span style="color:red">*</span>';
				}
				
				if (isset($_POST['listID'])) {
					$listID = trim($_POST['listID']);
				}
				
				if (!$flag) {
					Header ("Location:output.php?userID=".$userID."&listID=".$listID);
				}
			}
		?>
		
		<form action=test.php method="post">
			<div class="title">
				test
			</div>
			<div class = "mainContainer">
				<div class = "question">
				Enter UserID: <?php print $userID_re; ?>
				<input type="text" maxlength = "50" value="<?php print $userID; ?>" name="userID" />
				</div>
				<div class = "question">
					Enter listID: 
				<input type = "radio" name = "listID" value = "male" <?php if ($listID=="male") echo "checked";?> >male
				<input type = "radio" name = "listID" value = "female" <?php if ($listID=="female") echo "checked";?> >female
				</div>
				<div class = "submitButton">
					<input name="enter" class="btn" type="submit" value="Submit" style="height: 30px; width: 60px; font-family: helvetica;"/> 
				</div>
			</div>
		</form>
	</body>
</html>
