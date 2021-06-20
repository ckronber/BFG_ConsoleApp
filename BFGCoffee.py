import time
import os
import http.client
import ssl
import json

def getToken():
	token = "bearer C9FRY-1Fs-CJuzr2szOg1OPco5bNMA0rxLs7M2TbobH7MiqoMjsFI-JygZc1A87nhKYLblE6iFAXGXZuhoq4k0TPVeVA3F4GmkO-Vp6PehsFCyIJT1X5rZzu5FRLJZqnqWhvEEL5BNknCuyZ2ranUtUyWbBj6chBB0vUz5CxWP0i2H6K7EAe3ib0UybSQQLQ6MmVF3ACR0dh1x8oJTWq7P4Wz8D2-UKyuCUQV3go-7DRiZFpLUivUjQJXgcJ-JGf8mN1yqddyVQHQXsC5noNyhWeqirdxo93Hlvxpi9p-A8ZFLuHFolY6ld4tMFnXUCzIBtCq6Is2Mf63dvgWw22TlhXe_ioacHrOzFxmTaAjAWE90arWJffZNDMmDyOQm2ABgtxe1vE2O1vMxPFnEbPbXQQ0TxvyIDv5BTYqUVw5SnWqRfAfXkP8U4V9AN0x-bK0cQdXWj-YnBYqrFld1YwRfMJZ5-rNCFIzCleY8RhfLU"
	return token
	
def clearConsole():
    command = 'cls'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def asciiDoom():
	print("""
				
		____________ _____      _____        __  __              _____ _                 
		| ___ \  ___|  __ \    /  __ \      / _|/ _|            /  ___| |                
		| |_/ / |_  | |  \/    | /  \/ ___ | |_| |_ ___  ___    \ `--.| |__   ___  _ __  
		| ___ \  _| | | __     | |    / _ \|  _|  _/ _ \/ _ \    `--. \ '_ \ / _ \| '_ \ 
		| |_/ / |   | |_\ \    | \__/\ (_) | | | ||  __/  __/   /\__/ / | | | (_) | |_) |
		\____/\_|    \____/     \____/\___/|_| |_| \___|\___|   \____/|_| |_|\___/| .__/ 
											  | |    
											  |_|    
			
		""")

class CoffeeShop:
	
	def AddCoffeeshop(self,name,location,number,website):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'ShopName='+name+'&Location='+location+'&PhoneNumber='+number+'&Website='+website
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("POST", "/api/CoffeeShop", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def getCoffeeshops(self):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET", "/api/CoffeeShop", payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def getCoffeeShop(self,id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET","/api/CoffeeShop/"+str(id), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def UpdateCoffeeshop(self,Shopid,name,location,number,website):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'CoffeeShopId='+Shopid+'&ShopName='+name+'&Location='+location+'&PhoneNumber='+number+'&Website='+website
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("PUT", "/api/CoffeeShop", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def RemoveCoffeeShop(self,id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("DELETE","/api/CoffeeShop/"+str(id), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

class CoffeeOrder:
	#CoffeeOrder Crud
	def AddCoffeeOrder(self,country,barista,shopid):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'Country='+country+'&Barista='+barista+'&CoffeeShopId='+shopid
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("POST", "/api/CoffeeOrder", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def getCoffeeOrders(self):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET", "/api/CoffeeOrder", payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def getCoffeeOrder(self,Orderid):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET","/api/CoffeeOrder/"+str(Orderid), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def UpdateCoffeeOrder(self,Orderid,country,barista):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'CoffeeOrderId='+Orderid+'&Country='+country+'&Barista='+barista
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("PUT", "/api/CoffeeOrder", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def RemoveCoffeeOrder(self,Orderid):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("DELETE","/api/CoffeeOrder/"+str(Orderid), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

class MenuItem:
	#Menu Crud
	def AddMenuItem(self,itemName,itemPrice,orderId):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'ItemName='+itemName+'&ItemPrice='+itemPrice+'&CoffeeOrderId='+orderId
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("POST", "/api/Menu", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def getMenuItems(self):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET", "/api/Menu", payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def getMenuItem(self,id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET", "/api/Menu/"+str(id), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def UpdateMenuItem(self,menuId,itemName,itemPrice):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'MenuId='+menuId+'&ItemName='+itemName+'&ItemPrice='+itemPrice
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("PUT", "/api/Menu", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def RemoveMenuItem(self,id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("DELETE", "/api/Menu/"+str(id), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

class Addition:
	#Addition Crud
	def AddAdditionItem(self,itemName,itemPrice,orderId):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'Name='+itemName+'&Price='+itemPrice+'&CoffeeOrderId='+orderId
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("POST", "/api/Addition", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def getAdditions(self):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET", "/api/Addition", payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def UpdateAdditionItem(self,Addid,itemName,itemPrice):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'AdditionId='+Addid+'&Name='+itemName+'&Price='+itemPrice
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("PUT", "/api/Addition", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def RemoveAddition(self,Addid):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("DELETE", "/api/Addition/"+str(Addid), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")
	
class Customer:
	
	tolken = getToken()

	#Register
	def AddRegister(self,userName,password,passConfirm):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'Email='+userName+'&Password='+password+'&ConfirmPassword='+passConfirm
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("POST", "/api/Register", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	#Login
	def AddLogin(self,userName,password):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'grant_type=password&Email='+userName+'&Password='+password
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("GET", "/token", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	#Customeer Crud
	def AddCustomer(self,firstName,lastName,paymentType,orderId):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'FirstName='+firstName+'&LastName='+lastName+'&PaymentType='+paymentType+'&CoffeeOrderId='+orderId
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain","Authorization": self.tolken}
		conn.request("POST", "/api/Customer", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))
		
	def getCustomers(self):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {"Authorization": self.tolken}
		conn.request("GET", "/api/Customer", payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def getCustomer(self,Custid):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {"Authorization": self.tolken}
		conn.request("GET", "/api/Customer/"+str(Custid), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def UpdateCustomer(self,Custid,firstName,lastName,paymentType):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'CustomerId='+Custid+'&FirstName='+firstName+'&LastName='+lastName+'&PaymentType='+paymentType
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain","Authorization": self.tolken}
		conn.request("PUT", "/api/Customer", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def RemoveCustomer(self,Custid):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {"Authorization": self.tolken}
		conn.request("DELETE", "/api/Customer/"+str(Custid), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")
	
class CRUD:

	Shop = CoffeeShop()
	Order = CoffeeOrder()
	Menu = MenuItem()
	AddTo = Addition()
	Cust = Customer()
		
	#Display
	def DisplayAll(self,ListValues,Name,values):
		#clearConsole()
		print("\n\nDisplay All " + Name)
		print("========================")
		i = 0
		
		for i in range(len(ListValues)):
			if(i%values == 0):
				print("\n")
			print(ListValues[i])
		
		print("\n")
		
	def DisplayById(self,ListValues,Name):
		#clearConsole()
		print("\n\nDisplay By ID " + Name)
		print("========================")
		i = 0
		
		for i in range(len(ListValues)):
			print(ListValues[i])
		
		print("\n")
		
	#Posting
	def CoffeeShopPost(self):
		Name = input("Enter Name for CoffeeShop: ")
		Location = input("Enter Location CoffeeShop: ")
		Number = input("Enter Phone Number for CoffeeShop: ")
		Website = input("Enter Website for CoffeeShop: ")
		
		self.Shop.AddCoffeeshop(Name,Location,Number,Website)
		
	def CoffeeOrderPost(self):
		CoffeeOrderList = self.Order.getCoffeeOrders().split(",")
		self.DisplayAll(CoffeeOrderList,"CoffeeShops",5)

		ShopId = input("Enter Id for the CoffeeShop: ")
		Barista = input("Enter Barista Fulfilling this Order: ")
		Country = input("Enter The Origin Coutry for the Beans: ")
		
		self.Order.AddCoffeeOrder(Country,Barista,ShopId)

	def MenuItemPost(self):
		CoffeeOrderList = self.Order.getCoffeeOrders().split(",")
		self.DisplayAll(CoffeeOrderList,"CoffeeOrders",4)

		OrderId = input("Enter Id for the CoffeeOrder: ")
		ItemName = input("Enter The Menu Item Name: ")
		ItemPrice = input("Enter the Menu Item Price: ")
		
		self.Menu.AddMenuItem(ItemName,ItemPrice,OrderId)

	def AdditionItemPost(self):
		CoffeeOrderList = self.Order.getCoffeeOrders().split(",")
		self.DisplayAll(CoffeeOrderList,"CoffeeOrders",4)

		OrderId = input("Enter Id for the CoffeeShop: ")
		ItemName = input("Enter The Addition Item Name: ")
		ItemPrice = input("Enter the Addition Item Price: ")
		
		self.AddTo.AddAdditionItem(ItemName,ItemPrice,OrderId)

	def CustomerPost(self):
		OrderList = self.Order.getCoffeeOrders().split(",")
		self.DisplayAll(OrderList,"CoffeeOrders",4)

		OrderId = input("Enter Id for the CoffeeOrder: ")
		FirstName = input("Enter First Name: ")
		LastName = input("Enter The Last  Name: ")
		PaymentType = input("Enter Payment Type: ")
		
		self.Cust.AddCustomer(FirstName,LastName,PaymentType,OrderId)

	#Updating
	def CoffeeShopUpdate(self):	
		CoffeeShopList = self.Shop.getCoffeeshops().split(",")
		self.DisplayAll(CoffeeShopList,"CoffeeShops",5)

		ShopId = input("Enter the Id for The CoffeeShop to Edit: ")
		Name = input("Enter Name for CoffeeShop: ")
		Location = input("Enter Location CoffeeShop: ")
		Number = input("Enter Phone Number for CoffeeShop: ")
		Website = input("Enter Website for CoffeeShop: ")
		
		self.Shop.UpdateCoffeeshop(ShopId,Name,Location,Number,Website)

	def CoffeeOrderUpdate(self):
		CoffeeOrderList = self.Order.getCoffeeOrders().split(",")
		self.DisplayAll(CoffeeOrderList,"CoffeeOrders",4)

		print("\nAdding a CoffeeOrder")
		OrderId = input("Enter Id for the CoffeeOrder: ")
		Barista = input("Enter Barista Fulfilling this Order: ")
		Country = input("Enter The Origin Coutry for the Beans: ")
		
		self.Order.UpdateCoffeeOrder(OrderId,Country,Barista)
	
	def MenuItemUpdate(self):
		MenuList = self.Menu.getMenuItems().split(",")
		self.DisplayAll(MenuList,"MenuItems",3)

		MenuId = input("Enter Id for the MenuItem: ")
		ItemName = input("Enter The Menu Item Name: ")
		ItemPrice = input("Enter the Menu Item Price: ")
		
		self.Menu.UpdateMenuItem(MenuId,ItemName,ItemPrice)

	def AdditionItemUpdate(self):
		AdditionList = self.AddTo.getAdditions().split(",")
		self.DisplayAll(AdditionList,"CoffeeOrders",3)

		AddId = input("Enter Id for the Addition to Update: ")
		ItemName = input("Enter The Addition Item Name: ")
		ItemPrice = input("Enter the Addition Item Price: ")
		
		self.AddTo.UpdateAdditionItem(AddId,ItemName,ItemPrice)

	def CustomerUpdate(self):
		CustomerList = self.Cust.getCustomers().split(",")
		self.DisplayAll(CustomerList,"Customers",4)

		CustId = input("Enter Customer Id to Update: ")
		FirstName = input("Enter First Name: ")
		LastName = input("Enter Last Name: ")
		PaymentType = input("Enter Payment Type: ")
		
		self.Cust.UpdateCustomer(CustId,FirstName,LastName,PaymentType)

	#Delete
	def CoffeeShopRemove(self):
		ShopId = input("Enter the CoffeeShop Id to Remove: ")
		self.Shop.RemoveCoffeeShop(ShopId)

	def CoffeeOrderRemove(self):
		OrderId = input("Enter the CoffeeOrder Id to Remove: ")
		self.Order.RemoveCoffeeOrder(OrderId)

	def CustomerRemove(self):
		CustId = input("Enter the Customer Id to Remove: ")
		self.Cust.RemoveCustomer(CustId)
	
	def MenuItemRemove(self):
		MenuID= input("Enter the MenuItem Id to Remove: ")
		self.Menu.RemoveMenuItem(MenuID)

	def AdditionRemove(self):
		AddId = input("Enter the Additon Id to Remove: ")
		self.AddTo.RemoveAddition(AddId)

class DisplayMenu:

	Shop = CoffeeShop()
	Order = CoffeeOrder()
	Menu = MenuItem()
	AddTo = Addition()
	Cust = Customer()
	CrudWork = CRUD()
	token = getToken()

	# this method is used to select which to do	
	def displayMenu(self):
		clearConsole()
		print("BFG CoffeeShopMenu")
		print("===================")
		print("1. CoffeeShop")
		print("2. CoffeeOrder")
		print("3. Customer")
		print("4. MenuItems")
		print("5. Additions")
		
		menuValue = input("\nMake a selection: ")
		
		if(menuValue == str(1)):
			self.displayCRUD("CoffeeShop")
		elif(menuValue == str(2)):
			self.displayCRUD("CoffeeOrder")
		elif(menuValue == str(3)):
			self.displayCRUD("Customer")
		elif(menuValue == str(4)):
			self.displayCRUD("MenuItem")
		elif(menuValue == str(5)):
			self.displayCRUD("Addition")
		else:
			print("This is not a Selection. Try Again")

	def displayCRUD(self,MainValue):
		print("\n\n"+MainValue)
		print("===================")
		print("1. Add")
		print("2. Update")
		print("3. Display")
		print("4. Display By Id")
		print("5. Delete")

		crudVal = input("\n Select an Option: ")

		if(crudVal == str(1)):
			print("\n\nAdd " + MainValue)
			if( MainValue== "CoffeeShop"):
				self.CrudWork.CoffeeShopPost()
			elif(MainValue == "CoffeeOrder"):
				self.CrudWork.CoffeeOrderPost()
			elif(MainValue == "MenuItem"):
				self.CrudWork.MenuItemPost()
			elif(MainValue == "Addition"):
				self.CrudWork.AdditionItemPost()
			elif(MainValue == "Customer"):
				self.CrudWork.CustomerPost()
			else:
				print("Not a valid option")
		elif(crudVal == str(2)):
			print("Update " + MainValue)
			if( MainValue== "CoffeeShop"):
				self.CrudWork.CoffeeShopUpdate()
			elif(MainValue == "CoffeeOrder"):
				self.CrudWork.CoffeeOrderUpdate()
			elif(MainValue == "MenuItem"):
				self.CrudWork.MenuItemUpdate()
			elif(MainValue == "Addition"):
				self.CrudWork.AdditionItemUpdate()
			elif(MainValue == "Customer"):
				self.CrudWork.CustomerUpdate()
			else:
				print("Not a valid option")
		elif(crudVal == str(3)):
			print("\n\nDisplay " + MainValue)
			if( MainValue== "CoffeeShop"):
				CoffeeShopList = self.Shop.getCoffeeshops().split(",")
				self.CrudWork.DisplayAll(CoffeeShopList,"CoffeeShops",5)
			elif(MainValue == "CoffeeOrder"):
				CoffeeOrderList = self.Order.getCoffeeOrders().split(",")
				self.CrudWork.DisplayAll(CoffeeOrderList,"CoffeeOrder",4)
			elif(MainValue == "MenuItem"):
				MenuItemList = self.Menu.getMenuItems().split(",")
				self.CrudWork.DisplayAll(MenuItemList,"MenuItems",3)
			elif(MainValue == "Addition"):
				AdditionItemList = self.AddTo.getAdditions().split(",")
				self.CrudWork.DisplayAll(AdditionItemList,"AdditionItems",3)
			elif(MainValue == "Customer"):
				CustomerList = self.Cust.getCustomers().split(",")
				self.CrudWork.DisplayAll(CustomerList,"Customers",4)
			else:
				print("Not a valid option")
		elif(crudVal == str(4)):
			print("\n\nDisplay By ID " + MainValue)
			if( MainValue== "CoffeeShop"):
				CoffeeShopList = self.Shop.getCoffeeshops().split(",")
				self.CrudWork.DisplayAll(CoffeeShopList,"CoffeeShops",5)
				
				getId = input("Enter the Id # of the CoffeeShop To Display: ")
				CoffeeShopList = self.Shop.getCoffeeShop(getId).split(",")
				self.CrudWork.DisplayById(CoffeeShopList,"CoffeeShop")

			elif(MainValue == "CoffeeOrder"):
				CoffeeOrderList = self.Order.getCoffeeOrders().split(",")
				self.CrudWork.DisplayAll(CoffeeOrderList,"CoffeeOrder",4)

				getId = input("Enter the Id # of the CoffeeOrder To Display: ")
				CoffeeOrderList = self.Order.getCoffeeOrder(getId).split(",")
				self.CrudWork.DisplayById(CoffeeOrderList,"CoffeeOrder")

			elif(MainValue == "MenuItem"):
				MenuItemList = self.Menu.getMenuItems().split(",")
				self.CrudWork.DisplayAll(MenuItemList,"MenuItems",3)

				getId = input("Enter the Id # of the Menu To Display: ")
				MenuItemList= self.Menu.getMenuItem(getId).split(",")
				self.CrudWork.DisplayById(MenuItemList,"MenuItem")

			elif(MainValue == "Addition"):
				print("Not needed")

				input("Press Enter To Continue")

			elif(MainValue == "Customer"):
				CustomerList = self.Cust.getCustomers().split(",")
				self.CrudWork.DisplayAll(CustomerList,"Customers",4)

				getId = input("Enter the Id # of the Customer To Display: ")
				CustomerList= self.Cust.getCustomer(getId).split(",")
				self.CrudWork.DisplayById(CustomerList,"Customer")
			else:
				print("Not a valid option")
		elif(crudVal == str(5)):
			print("\n\nDelete " + MainValue)
			
			if( MainValue== "CoffeeShop"):
				CoffeeShopList = self.Shop.getCoffeeshops().split(",")
				self.CrudWork.DisplayAll(CoffeeShopList,"CoffeeShops",5)

				self.CrudWork.CoffeeShopRemove()
			elif(MainValue == "CoffeeOrder"):
				CoffeeOrderList = self.Order.getCoffeeOrders().split(",")
				self.CrudWork.DisplayAll(CoffeeOrderList,"CoffeeOrder",4)

				self.CrudWork.CoffeeOrderRemove()
			elif(MainValue == "MenuItem"):
				MenuItemList = self.Menu.getMenuItems().split(",")
				self.CrudWork.DisplayAll(MenuItemList,"MenuItems",3)

				self.CrudWork.MenuItemRemove()
			elif(MainValue == "Addition"):
				AdditionItemList = self.AddTo.getAdditions().split(",")
				self.CrudWork.DisplayAll(AdditionItemList,"AdditionItems",3)

				self.CrudWork.AdditionRemove()
			elif(MainValue == "Customer"):
				CustomerList = self.Cust.getCustomers().split(",")
				self.CrudWork.DisplayAll(CustomerList,"Customers",4)

				self.CrudWork.CustomerRemove()
			else:
				print("Not a valid option")
		else:
			print("This is not a Selection")

			

	
keepRunning = True
	
asciiDoom()
time.sleep(3)
token = getToken()
	
while(keepRunning):
	

	menuDisplay = DisplayMenu() #displays the men to select from different classes
	myCrud = CRUD()

	#clearConsole()
	menuDisplay.displayMenu()
	#AdditionItemPost()
	
	#myCoffeeShop = CoffeeShop()
	

	#cust = Customer()

	#print("Login")
	#userName = input("Enter an Email for Username: ")
	#password = input("Enter a password: ")

	#newToken = cust.Login(userName,password)
	#print(newToken)

	#answer = input("Would you like to add a CoffeeShop? (y/n): ")

	#if(answer == 'y'):
	#	myCrud.CoffeeShopPost()

	#print("\n\n")

	#CoffeeShopList = myCrud.Shop.getCoffeeshops().split(",")
	#CoffeeOrderList = myCrud.Order.getCoffeeOrders().split(",")
	#CoffeeOrderItem = myCrud.Order.getCoffeeOrder(2).split(",")
	#CustomerList = getCustomers(token).split(",")
	#MenuItemList = getMenuItems().split(",")
	#AdditionList = getAdditions().split(",")
	
	#myCrud.DisplayAll(CoffeeShopList,"CoffeeShops",5)
	#myCrud.DisplayAll(CoffeeOrderList,"CoffeeOrders",2)
	#myCrud.DisplayById(CoffeeOrderItem,"CoffeeOrders")
	#DisplayById(CoffeeOrderList,"CoffeeOrders",2)
	#DisplayAll(CustomerList,"Customers",4)
	#DisplayAll(MenuItemList,"MenuItems",3)
	#DisplayAll(AdditionList,"AdditonItems",3)
	
	value1 = input("Do You want to Continue?(Enter y or n):")

	if(value1 == 'n'):
		keepRunning = False