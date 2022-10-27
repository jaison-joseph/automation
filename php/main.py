start_string_ = \
'''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="EN" dir="ltr" xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>User Registration</title>
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>
    
	<body>
'''

end_string_ = \
'''
    </body>
</html>'''

class Item:
    def __init__(self, qn: str, required: bool, inputType: str, varName: str, inputTypeOptions = None, fkArgs = None) -> None:
        self.qn = qn
        self.required = required
        if inputType not in ['text', 'radio', 'select', 'checkbox', 'date', 'number', 'fkSelect']:
            print("question type " + inputType + " is invalid")
            return
        self.inputType = inputType
        self.varName = varName
        if self.inputType in ['radio', 'select']:
            if type(inputTypeOptions) is not list:
                print("for question types of radio or select, strings for options must be provided")
                return
            self.inputTypeOptions = inputTypeOptions[:]
        if inputType == 'fkSelect':
            if fkArgs is None:
                print("for fkSelect type, you are requied to pass in an array of arguments for the custom select function")
                return
            self.fkArgs = fkArgs[:]

class List:
    def __init__(self, title: str, fileName: str, resultFileName: str, requiredFiles: list, items: list, tableName: str, makeOutputPage = False, tableFieldCount = -1) -> None:
        self.title = title
        self.fileName = fileName
        self.resultFileName = resultFileName
        self.makeOutputPage = makeOutputPage        # we might not always need to create output pages
        self.tableName = tableName                  # the table for which we are going to insert the records
        self.tableFieldCount = tableFieldCount      # the table's # of columns
        self.requiredFiles = requiredFiles[:]
        self.items = items[:]
        self.genPHP()
        self.genHTML()
        if self.makeOutputPage:
            self.genResultsHTML()
        self.writeFiles()

    def genPHP(self):
        self.php = []
        
        for i in self.requiredFiles:
            self.php.append('require_once("' + i + '");')

        self.php.append('')

        self.php.append('// variables for form fields')
        for i in self.items:
            if i.inputType == 'checkbox':
                self.php.append('$' + i.varName + " = FALSE;")
            else:
                self.php.append('$' + i.varName + ' = "";')

        self.php.append('')
        self.php.append("// variables to enforce reuqired fields")
        for i in self.items:
            if i.required:
                self.php.append('$' + i.varName + '_re = "*";')

        self.php.append('')

        self.php.append("$flag = FALSE;	// flag that's set to TRUE if any of the required fields are not filled")

        self.php.append('')

        self.php.append("if (isset($_POST['enter'])) {")

        for i in self.items:
            self.php.append('if (isset($_POST[\'' + i.varName + '\'])) {')
            self.php.append('$' + i.varName + ' = trim($_POST[\'' + i.varName + '\']);')
            self.php.append('}')
            if i.required:
                self.php.append('if ($' + i.varName + ' == "") {')
                self.php.append('$flag = TRUE;')
                # $tncre = "<span style=\"color:red\">*</span>";
                self.php.append('$' + i.varName + "_re = '<span style=\"color:red\">*</span>';")
                self.php.append('}')

            self.php.append("")

        '''
        if ($agreeok) {
            //enter data into the database
            
            $stmt = $con->prepare("insert into EMPLOYEE values(null, ?, ?, ?, ?)");
            if ($stmt->execute(array($fn, $ln, $gender, $deptID ))==TRUE)
                $msg = '<font color = "red">Thank you for registering. Please login.</font><br/>';
            else
                $msg = "Your information cannot be entered this time. Please try again later.";
        }            
        '''
        if self.makeOutputPage is False:
            self.php.append('//enter data into the database')
            self.php.append('$stmt = $con->prepare("insert into ' + self.tableName + ' values(null' + (', ?'*(self.tableFieldCount-1)) + ')");')
            foo = 'if ($stmt->execute(array('
            foo += '$' + self.items[0].varName
            for item in self.items[1:]:
                foo += ', $' + item.varName
            foo += '))==FALSE) {'
            self.php.append(foo)
            self.php.append('$flag = TRUE;')
            self.php.append('''echo "<script type='text/javascript'>''')
            self.php.append('''alert('Failed to insert entries into table. Please try again later or contact the sysadmin');''')
            self.php.append('''</script>"; ''')
            self.php.append("}")

        if self.makeOutputPage:
            # Header ("Location: process.php ? firstName =".$ fn ."&lastName=".$ln."&email=".$em."&gender=".$gender."&dept=".$dept."&st=".$st);
            # Header ("Location: process.php ? firstName =".$ fn ."&lastName=".$ln."&email=".$em."&gender=".$gender."&dept=".$dept."&st=".$st);
            nextPageURL = self.resultFileName + '?' + self.items[0].varName + '=".$' + self.items[0].varName
            for i in self.items[1:]:
                nextPageURL += '."&' + i.varName + '=".$' + i.varName
        else:
            nextPageURL = self.resultFileName + "?tableName=" + self.tableName + '"'
        
        self.php.append('if (!$flag) {')
        self.php.append('Header ("Location:' + nextPageURL + ');')			
        self.php.append('}') # for the if flag
        self.php.append('}') # for the isset

    def genQnHTML(self, qn: Item):
        result = []
        
        result.append('<div class = "question">')
        
        # 'text', 'radio', 'select', 'checkbox'
        foo = qn.qn + ": "
        if qn.required:
            foo += '<?php print $' + qn.varName + '_re' + '; ?>'
        result.append(foo)

        foo = []
        if qn.inputType == 'text':
            foo.append('<input type="text" maxlength = "50" value="<?php print $' + qn.varName + '; ?>" name="' + qn.varName + '" />')
        elif qn.inputType == 'radio':
            for j in qn.inputTypeOptions:
                foo.append('<input type = "radio" name = "' + qn.varName + '" value = "' + j + '" <?php if ($' + qn.varName + '=="' + j + '") echo "checked";?> >' + j)
        elif qn.inputType == 'select':
            foo.append('<select name = "' + qn.varName + '">')
            for j in qn.inputTypeOptions:
                foo.append('<option value = "' + j + '">' + j + '</option>')
            foo.append('</select>')
        elif qn.inputType == 'checkbox':
            foo.append('<input type="checkbox" name="' + qn.varName + '" value=<?php print $' + qn.varName + ' ?> <?php if ($' + qn.varName + ') echo "checked"; ?>>')
        elif qn.inputType == 'date':
            foo.append('<input type="date" name="' + qn.varName + '" + value=<?php print $' + qn.varName + '?>>')
        elif qn.inputType == 'number':
            foo.append('<input type="number" value="<?php print $' + qn.varName + '; ?>" name="' + qn.varName + '" />')
        elif qn.inputType == 'fkSelect':
            #       makeDropdown($selectName, $tableName, $columnIDName, $columnDataName);
            # <?php makeDropdown('country_name', 'COUNTRY', 'CountryID', 'CountryName');?>
            foo.append(
                "<?php makeDropdown("\
                +\
                "'" + qn.varName + "'" +\
                ''.join([", '" + i +"'" for i in qn.fkArgs]) +\
                ");?>"
            )

        else:
            print("invalid question type found: ", qn)
        result += foo
        result.append('</div>')

        return result

    def genHTML(self):
        self.html = []

        self.html.append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">')
        self.html.append('<html lang="EN" dir="ltr" xmlns="http://www.w3.org/1999/xhtml">')
        self.html.append('<head>')
        self.html.append('<title>User Registration</title>')
        self.html.append('<link rel="stylesheet" type="text/css" href="style.css">')
        self.html.append('</head>')
        self.html.append('')
        self.html.append('<body>')
        self.html.append('')
        self.html.append('<?php')
        self.html += self.php
        self.html.append('?>')
        self.html.append('')

        self.html.append('<form action=' + self.fileName + ' method="post">')
        self.html.append('<div class="title">')
        self.html.append(self.title)
        self.html.append('</div>')

        self.html.append('<div class = "mainContainer">')
        for i in self.items:
            self.html += self.genQnHTML(i)
        
        self.html.append('<div class = "submitButton">')
        self.html.append('<input name="enter" class="btn" type="submit" value="Submit" style="height: 30px; width: 60px; font-family: helvetica;"/> ')
        self.html.append('</div>')

        self.html.append('</div>') # for the mainContainer
        self.html.append('</form>') # for the form
        self.html.append('</body>')
        self.html.append('</html>')

    def genResultsHTML(self):
        if self.makeOutputPage is False:
            return
        self.results_html = []

        self.results_html.append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">')
        self.results_html.append('<html lang="EN" dir="ltr" xmlns="http://www.w3.org/1999/xhtml">')
        self.results_html.append('<head>')
        self.results_html.append('<title>Form inputs</title>')
        self.results_html.append('<link rel="stylesheet" type="text/css" href="style.css">')
        self.results_html.append('</head>')
        self.results_html.append('')
        self.results_html.append('<body>')
        self.results_html.append('')
        self.results_html.append('<?php')
        
        for i in self.items:
            self.results_html.append("$" + i.varName + " =  $_GET['" + i.varName + "'];")

        self.results_html.append('?>')
        self.results_html.append('')

        self.results_html.append('<div class="title">')
        self.results_html.append('Form entries')
        self.results_html.append('</div>')

        self.results_html.append('<div class = "mainContainer">')
        for i in self.items:
            self.results_html.append('<div class="answer">')
            self.results_html.append(i.varName + ': <?php print $' + i.varName + '?>')
            self.results_html.append('</div>')
    

        self.results_html.append('</div>') # for the mainContainer
        self.results_html.append('</body>')
        self.results_html.append('</html>')

    def writeFiles(self):
        tabCount = 0
        print("number of lines: ", len(self.html))
        with open(self.fileName, "w+") as f:
            for i in self.html:
                s = '\t' * tabCount
                if '</html' in i or '</body' in i or '</form' in i or '</select' in i or '</div' in i or '}' in i or '?>' in i:
                    s = '\t' * (tabCount - 1)
                s += i
                s += '\n'
                f.write(s)

                if '<html' in i or '<body' in i or '<form' in i or '<select' in i or '<div' in i or '{' in i or '<?php' in i:
                    tabCount += 1
                if '</html' in i or '</body' in i or '</form' in i or '</select' in i or '</div' in i or '}' in i or '?>' in i:
                    tabCount -= 1

        # if we were not asked to create output HTML pages, then we are done
        if self.makeOutputPage is False:
            return
        tabCount = 0
        print("number of lines: ", len(self.results_html))
        with open(self.resultFileName, "w+") as f:
            for i in self.results_html:
                s = '\t' * tabCount
                if '</html' in i or '</body' in i or '</form' in i or '</select' in i or '</div' in i or '}' in i:
                    s = '\t' * (tabCount - 1)
                s += i
                s += '\n'
                f.write(s)

                if '<html' in i or '<body' in i or '<form' in i or '<select' in i or '<div' in i or '{' in i or '<?php' in i:
                    tabCount += 1
                if '</html' in i or '</body' in i or '</form' in i or '</select' in i or '</div' in i or '}' in i or '?>' in i:
                    tabCount -= 1
                

'''
['text', 'radio', 'select', 'checkbox']

questions are suffixed with a ': ' automatically
'''

if __name__ == "__main__":
    # a = Item('Enter UserID', True, 'text', 'userID')
    # b = Item('Enter listID', False, 'radio', 'listID', ['male', 'female'])
    a = Item("Number", True, 'number', 'num')
    b = Item("Date", True, 'date', 'date')

    form = List('test', 'test.php', 'output.php', [], [a, b])
