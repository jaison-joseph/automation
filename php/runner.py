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

adminItems = [
    Item('New admin username', True, 'text', 'newAdminUsername')
]

productItems = [
    Item('Product category', True, 'select', 'category', ['', 'Food', 'Electronics', 'Household']),
    Item("Product name", True, 'text', 'name'),
    Item("Product price", True, 'number', 'price'),
    Item("Product description", False, 'text', 'description'),
]

categoryItems = [
    Item("Category name", True, 'text', 'name'),
    Item("Category description", True, 'text', 'description')
]

inventoryItems = [
    Item('Product ID', True, 'select', 'productID', ['', '123', '456', '789']),
    Item('Seller ID', True, 'select', 'sellerID', ['', 'abc', 'def', 'ghi']),
    Item('Date stocked', True, 'date', 'dateStocked'),
    Item('Quantity remaining', True, 'number', 'qtyRemaining')
]

sellerItems = [
    Item('Seller name', True, 'text', 'name'),
    Item('Email', True, 'text', 'email'),
    Item('Phone number', True, 'number', 'phoneNumber'),
    Item('Address', True, 'text', 'address'),
    Item('Username', True, 'text', 'username'),
    Item('Password', True, 'text', 'password')
]

userItems = [
    Item("Username", True, 'text', 'username'),
    Item("Password", True, 'text', 'password'),
    Item("First Name", True, 'text', 'firstName'),
    Item("Middle Name", False, 'text', 'middleName'),
    Item("Last Name", True, 'text', 'lastName'),
    Item("Age", True, 'number', 'age'),
    Item('Gender', True, 'radio', 'gender', ['male', 'female', 'other']),
    Item('Address', True, 'text', 'address'),
    Item('Account Type', True, 'radio', 'accType', ['Admin', 'Customer', 'Seller'])
]

countryItems = [
    Item("Country name", True, 'text', 'countryName')
]

newAdminForm = List('Add admin', 'newAdminInput.php', 'table.php', ['dbconnect.php', 'util.php'], adminItems, 'ADMIN', False, 2)
productForm = List('New product', 'newProductInput.php', 'table.php', ['dbconnect.php', 'util.php'], productItems, 'PRODUCT', False, 5)
categoryForm = List('New category', 'newCategoryInput.php', 'table.php', ['dbconnect.php', 'util.php'], categoryItems, 'PRODUCT_CATEGORY', False, 3)
inventoryForm = List('New inventory', 'newInventoryInput.php', 'table.php', ['dbconnect.php', 'util.php'], inventoryItems, 'INVENTORY', False, 6)
sellerForm = List('New seller', 'newSellerInput.php', 'table.php', ['dbconnect.php', 'util.php'], sellerItems,'SELLER', False, 4)
userItems = List('New User', 'newUserInput.php', 'table.php', ['dbconnect.php', 'util.php'], userItems, 'USER', 10)
userItems = List('New Country', 'newCountryInput.php', 'table.php', ['dbconnect.php', 'util.php'], countryItems, 'COUNTRY', False, 2)
