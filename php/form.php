<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="EN" dir="ltr" xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>User Registration</title>
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>

	<body>

		<?php

			// required files
			require_once('functions.php');
            
			$fn = "";
			$ln = "";
			$em = "";
			$alsoem = "";
			$gender = "Male";
            $ps = "";
			$alsops = "";
            $dept = "";
            $st = "";
            $tnc = FALSE;

			$msg = "";

			// below are the variables that are set based on whether the input field was filled or not
			$fnre="*";		// first name
			$lnre="*";		// last name
			$emre="*";		// email
			$psre="*";		// password
			$stre = "*";	// status
			$tncre = "*";	// t&c 
			$maleChecked = "";
			$femaleChecked = "";		
			
			$emma = "";		// email match
			$psma = "";		// password match

			$flag = FALSE;	// var to check if all the fields have been set and comply with the conditions for the assignment

			$foo = "";	// output vairable for the checkPassword function
			

			if (isset($_POST['enter'])) //check if this page is requested after Submit button is clicked
			{
				// take the information submitted and send to a process file
			
				$fn = trim($_POST['firstName']); //always trim the user input to get rid of the additiona white spaces on both ends of the user input
				
				$ln = trim($_POST['lastName']);

				//use filter_input function to validate email
				if (!filter_input(INPUT_POST, 'em',FILTER_VALIDATE_EMAIL)) 
					$emre = '<span style="color:red">*</span>';
				$em = trim($_POST['em']);
				
				if (isset($_POST['gender']))
					$gender = trim($_POST['gender']);

				if (isset($_POST['st']))
					$st = trim($_POST['st']);
				
				if (isset($_POST['dept']))
					$dept = trim($_POST['dept']);
				
				if (isset($_POST['alsoem']))
					$alsoem = trim($_POST['alsoem']);

				if (isset($_POST['ps']))
					$ps = trim($_POST['ps']);
				
				if (isset($_POST['alsops']))
					$alsops = trim($_POST['alsops']);
				
				if ($gender=="Male") {
					$maleChecked="checked";
					$femaleChecked="";
				}
				else {
					$maleChecked="";
					$femaleChecked="checked";
				}
			
				if (!isset($_POST['tnc'])) {
					$flag = TRUE;	
					$tncre = "<span style=\"color:red\">*</span>";
				}

				if (strlen($fn) == 0){
					$flag = TRUE;
					$fnre = "<span style=\"color:red\">*</span>";
				}

				if (strlen($ln) == 0){
					$lnre = '<span style="color:red">*</span>';
					$flag = TRUE;
				}

				if (strlen($st) == 0){
					$flag = TRUE;
					$stre = '<span style="color:red">*</span>';
				}

				// passwordCheck returns FALSE if the passwords dont meet criterion, TRUE otherwise
				// flag is TRUE if we have an error
				if (!passwordCheck($ps, $alsops, $psre, $psma)) {
					$flag = TRUE;
				}
							
				if ($em == "") {
					$flag = TRUE;
					$emre = '<span style="color:red">*</span>';
					$emma = '<span style="color:red">*</span>';
				}
				elseif (strcmp($em, $alsoem) != 0) {
					$flag = TRUE;
					$emma = '<span style="color:red">Emails do not match</span>';
				}

				if (!$flag) {
					Header ("Location:login.php?activationCode=".randomCodeGenerator(mt_rand(50,60)));			
				}
			}
		?>

		<form action="lab2.php" method="post">
			<div class="title">
				User Registration
			</div>
			<div class = "mainContainer">
				<div class = "question-pair">
					<div class = "question">
						First Name:
						<input type="text" maxlength = "50" value="<?php print $fn; ?>" name="firstName" placeholder="First Name" />
						<?php print $fnre; ?>
					</div>
					
					<div class = "question">
						Last Name: 
						<input type="text" maxlength = "50" value="<?php print $ln; ?>" name="lastName" placeholder="Last Name" /> 
						<?php print $lnre; ?>
					</div>
				</div>
				
				<div class = "question-pair">
					<div class = "question">
						Email: 
						<input type="text" maxlength = "50" value="<?php print $em; ?>" name="em" /> 
						<?php print $emre; ?>
					</div>
					
					<div class = "question">
						Confirm Email: 
						<input type="text" maxlength = "50" value="<?php print $alsoem; ?>" name="alsoem" /> 
						<?php print $emma; ?>
					</div>
				</div>
				
				<div class = "question">
					Gender: 
					<input type = "radio" name = "gender" value = "Male" <?php print $maleChecked; ?> checked 	/>Male
					<input type = "radio" name = "gender" value = "Female"  <?php print $femaleChecked; ?> />Female
				</div>
				
				<div class = "question-pair">
					<div class = "question">
						Password: 
						<input type="password" maxlength = "50" value="<?php print $ps; ?>" name="ps" /> 
						<?php print $psre; ?>
					</div>
					
					<div class = "question">
						Confirm Password: 
						<input type="password" maxlength = "50" value="<?php print $alsops; ?>" name="alsops" /> 
						<?php print $psma; ?>
					</div>
				</div>

				<div class = "question">
					Department:
					<select name = "dept">
						<option value = "Science">Science</option>
						<option value = "Business" selected>Business</option>
						<option value = "Law">Law</option>
						<option value = "Humanities">Humanities</option>
					</select>
				</div>

				<div class = "question">
					Status: <?php print $stre; ?>
					<select name = "st" >
						<option value = ""> Choose a status </option>
						<option value = "Full_Time" <?php if ($st == "Full_Time") echo "selected"; ?>> Full Time </option>
						<option value = "Part_Time" <?php if ($st == "Part_Time") echo "selected"; ?>> Part Time </option>
						<option value = "Student" <?php if ($st == "Student") echo "selected"; ?>> Student </option>
						<option value = "Intern" <?php if ($st == "Intern") echo "selected"; ?>> Intern </option>
					</select>
				</div>

				<div class = "question" style="width: 100%; align-items: center">
					By checking this box, you agree to the terms and conditions of XYZ Inc.
					<input type="checkbox" name="tnc" value=<?php print $tnc ?> <?php if ($tnc) echo "checked"; ?>>
					<?php print $tncre; ?>
				</div>

				<div class = "submitButton">
					<input name="enter" class="btn" type="submit" value="Submit" style="height: 30px; width: 60px; font-family: helvetica;"/> 
				</div>
			</div>
		</form>



	</body>
</html>


