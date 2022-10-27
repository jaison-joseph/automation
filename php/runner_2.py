'''
tables that are fillable
	user
		has dropdown for account type
	account type
	admin
		search/dropdown to add admin
	product
		dropdown for category
	category
	inventory
		dropdown for product
		dropdown for seller
	seller
'''

'''
input types: ['text', 'radio', 'select', 'checkbox']
'''

from main import Item, List
# <?php makeDropdown('country_name', 'COUNTRY', 'CountryID', 'CountryName');?>

adminItems = [
    Item('New admin username', True, 'fkSelect', 'newAdminUsername', None, ['USER', 'UserID', 'Username'])
]

productItems = [
    Item('Product category', True, 'fkSelect', 'category', None, ['PRODUCT_CATEGORY', 'ProductCategoryID', 'CategoryName']),
    Item("Product name", True, 'text', 'name'),
    Item("Product price", True, 'number', 'price'),
    Item("Product description", False, 'text', 'description'),
]

categoryItems = [
    Item("Category name", True, 'text', 'name'),
    Item("Category description", True, 'text', 'description')
]

inventoryItems = [
    Item('Product ID', True, 'fkSelect', 'productID', None, ['PRODUCT', 'ProductID', 'Name']),
    Item('Seller ID', True, 'fkSelect', 'sellerID', None, ['SELLER', 'SellerID', 'Name']),
    Item('Date stocked', True, 'date', 'dateStocked'),
    Item('Quantity remaining', True, 'number', 'qtyRemaining')
]

sellerItems = [
    Item('Seller name', True, 'text', 'name'),
    Item('Email', True, 'text', 'email'),
    Item('LineOne', True, 'text', 'lineOne'),
    Item('LineTwo', True, 'text', 'lineTwo'),
    Item('City', True, 'text', 'city'),
    Item('State', True, 'text', 'state'),
    Item('Zip', True, 'number', 'zip'),
    Item('POBox', True, 'number', 'pobox'),
    Item('Country', True, 'fkSelect', 'country', None, ['COUNTRY', 'CountryID', 'CountryName'])
]

userItems = [
    Item("Username", True, 'text', 'username'),
    Item("Password", True, 'text', 'password'),
    Item("First Name", True, 'text', 'firstName'),
    Item("Middle Name", False, 'text', 'middleName'),
    Item("Last Name", True, 'text', 'lastName'),
    Item("Age", True, 'number', 'age'),
    Item('Gender', True, 'radio', 'gender', ['male', 'female', 'other']),
    Item('LineOne', True, 'text', 'lineOne'),
    Item('LineTwo', True, 'text', 'lineTwo'),
    Item('City', True, 'text', 'city'),
    Item('State', True, 'text', 'state'),
    Item('Zip', True, 'number', 'zip'),
    Item('POBox', True, 'number', 'pobox'),
    Item('Country', True, 'fkSelect', 'country', None, ['COUNTRY', 'CountryID', 'CountryName']),
    Item('Account Type', True, 'fkSelect', 'accType', None, ['ACCOUNT_TYPE', 'AccTypeID', 'TypeName'])
]

countryItems = [
    Item("Country name", True, 'text', 'countryName')
]

newAdminForm = List('Add admin', 'newAdminInput.php', 'table.php', ['dbconnect.php', 'alsoutil.php'], adminItems, 'ADMIN', False, 2)
productForm = List('New product', 'newProductInput.php', 'table.php', ['dbconnect.php', 'alsoutil.php'], productItems, 'PRODUCT', False, 5)
categoryForm = List('New category', 'newCategoryInput.php', 'table.php', ['dbconnect.php', 'alsoutil.php'], categoryItems, 'PRODUCT_CATEGORY', False, 3)
inventoryForm = List('New inventory', 'newInventoryInput.php', 'table.php', ['dbconnect.php', 'alsoutil.php'], inventoryItems, 'INVENTORY', False, 6)
sellerForm = List('New seller', 'newSellerInput.php', 'table.php', ['dbconnect.php', 'alsoutil.php'], sellerItems,'SELLER', False, 4)
userForm = List('New User', 'newUserInput.php', 'table.php', ['dbconnect.php', 'alsoutil.php'], userItems, 'USER', False, 10)
countryForm = List('New Country', 'newCountryInput.php', 'table.php', ['dbconnect.php', 'alsoutil.php'], countryItems, 'COUNTRY', False, 2)
