import time
import os
import http.client
import ssl

def getToken():
	token = "bearer yF_QYzobJCQX-ueCSN7zsva3EdgTr9iZU6zeZLLSbwkgIVKBI2vq_LunK8EETJB6XN7yBG1nqu2dhGOIzLJIklCNWU9KWBT4Dvk7dUNshFkaCnK_U1Ox64NaljOVCPd6D1N1mQQ0G-4Qx__vUf2S7WR7BPypRssKtz6h0pUcEL3TR4LtFG5iRIisLtVtfKAACe4ZCldEZ7XE9SCF4r8grEgVwTeT26sa8-RqZgcOcHj8xAomnUqxYtNWwayJRNWh4jJLDiBOQZ7vLEkRDftjBbf-cJhjzcPBYCamUSMVN-aykHgkBo0a-pv50xb_cYsznObhMsRrLalwvkp5obT3i4btuQYy2ugDCRkKV3NrZdP8nJf5G4r_rHPxVaMyfsrvzYqmvnQ6itTiR_6OcTrIn_nzjhAavcmtugJz_nwTSrn0_1mnk8yqbqsZ03YB16jsHtCnHtKg9h_v_9K82_ILO61zblzgZtZOg0OAfAIcALVlHTxFenX0GWyzNJIlHTTF"
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
	#def __init__(self) -> None:
	#	pass
	#CoffeeShop Crud
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

	def getCoffeeOrder(self,id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET","/api/CoffeeOrder/"+str(id), payload, headers)
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

	def RemoveCoffeeOrder(self,id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("DELETE","/api/CoffeeOrder/"+str(id), payload, headers)
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

	def getAddition(self,id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET", "/api/Addition/"+str(id), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def UpdateAdditionItem(self,Addid,itemName,itemPrice):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'AdditionId'+Addid+'&Name='+itemName+'&Price='+itemPrice
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("PUT", "/api/Addition", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def RemoveAddition(self,id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("DELETE", "/api/Addition/"+str(id), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")
	
class Customer:
	def __init__(self):
		self.tolken = getToken()

	#Register
	def AddRegister(self,userName,password,passConfirm):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'Email='+userName+'&Password='+password+'ConfirmPassword'+passConfirm
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
		payload = 'FirstName='+firstName+'&LastName='+lastName+'PaymentType'+paymentType+'&CoffeeOrderId='+orderId
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

	def getCustomer(self,id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {"Authorization": self.tolken}
		conn.request("GET", "/api/Customer/"+str(id), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def UpdateCustomer(self,Custid,firstName,lastName,paymentType):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'CustomerId='+Custid+'&FirstName='+firstName+'&LastName='+lastName+'PaymentType'+paymentType
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain","Authorization": self.tolken}
		conn.request("PUT", "/api/Customer", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def RemoveCustomer(self,id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {"Authorization": self.tolken}
		conn.request("DELETE", "/api/Customer/"+str(id), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")
	
class DisplayMenu:
	def __init__(self):
		self.Shop = CoffeeShop()
		self.Order = CoffeeOrder()
		self.Menu = MenuItem()
		self.AddTo = Addition()
		self.Cust = Customer()
		self.CrudWork = CRUD()

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
		
		if(menuValue == 1):
			self.displayCRUD("CoffeeShop")
		elif(menuValue == 2):
			self.displayCRUD("CoffeeOrder")
		elif(menuValue == 3):
			self.displayCRUD("Customer")
		elif(menuValue == 4):
			self.displayCRUD("MenuItem")
		elif(menuValue == 5):
			self.displayCRUD("Addition")
		else:
			print("This is not a Selection. Try Again")

	def displayCRUD(self,MainValue):
		print("Select an Option for " + MainValue)
		print("===================")
		print("1. Add")
		print("2. Update")
		print("3. Display")
		print("3. Display By Id")
		print("4. Delete")

		crudVal = input("\n Select an Option: ")

		if(crudVal == 1):
			print("Add " + MainValue)
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
		elif(crudVal == 2):
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
		elif(crudVal == 3):
			print("Display " + MainValue)
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
		elif(crudVal == 4):
			print("Display By ID " + MainValue)
			print("Add " + MainValue)
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
		elif(crudVal == 5):
			print("Delete " + MainValue)
			print("Add " + MainValue)
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
		else:
			print("This is not a Selection")
		
		
class CRUD:
	def __init__(self):
		self.Shop = CoffeeShop()
		self.Order = CoffeeOrder()
		self.Menu = MenuItem()
		self.AddTo = Addition()
		self.Cust = Customer()
		self.CrudWork = CRUD()
	
	#Display
	def DisplayAll(ListValues,Name,values):
		#clearConsole()
		print("Display All " + Name)
		print("========================")
		i = 0
		
		for i in range(len(ListValues)):
			if(i%values == 0):
				print("\n")
			print(ListValues[i])
		
		print("\n")
		
	def DisplayById(ListValues,Name):
		#clearConsole()
		print("Display All " + Name)
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
		self.DisplayAll(CoffeeOrderList,"CoffeeOrders",2)

		OrderId = input("Enter Id for the CoffeeOrder: ")
		ItemName = input("Enter The Menu Item Name: ")
		ItemPrice = input("Enter the Menu Item Price: ")
		
		self.Menu.AddMenuItem(ItemName,ItemPrice,OrderId)

	def AdditionItemPost(self):
		CoffeeOrderList = self.Order.getCoffeeOrders().split(",")
		self.DisplayAll(CoffeeOrderList,"CoffeeOrders",2)

		OrderId = input("Enter Id for the CoffeeShop: ")
		ItemName = input("Enter The Addition Item Name: ")
		ItemPrice = input("Enter the Addition Item Price: ")
		
		self.AddTo.AddAdditionItem(ItemName,ItemPrice,OrderId)

	def CustomerPost(self):
		CustomerList = self.Cust.getCustomers().split(",")
		self.DisplayAll(CustomerList,"CoffeeOrders",2)

		FirstName = input("Enter Id for the CoffeeShop: ")
		LastName = input("Enter The Menu Item Name: ")
		PaymentType = input("Enter the Menu Item Price: ")
		
		self.Cust.AddCustomer(FirstName,LastName,PaymentType)

	#Updating
	def CoffeeShopUpdate(self):


		ShopId = input("Enter the Id for The CoffeeShop to Edit: ")
		Name = input("Enter Name for CoffeeShop: ")
		Location = input("Enter Location CoffeeShop: ")
		Number = input("Enter Phone Number for CoffeeShop: ")
		Website = input("Enter Website for CoffeeShop: ")
		
		self.Shop.UpdateCoffeeshop(ShopId,Name,Location,Number,Website)

	def CoffeeOrderUpdate(self):
		print("Updating a CoffeeOrder")
		CoffeeOrderList = self.Order.getCoffeeOrders().split(",")
		self.DisplayAll(CoffeeOrderList,"CoffeeShops",5)

		print("\nAdding a CoffeeOrder")
		OrderId = input("Enter Id for the CoffeeOrder: ")
		Barista = input("Enter Barista Fulfilling this Order: ")
		Country = input("Enter The Origin Coutry for the Beans: ")
		
		self.Order.UpdateCoffeeOrder(OrderId,Country,Barista)
	
	def MenuItemUpdate(self):
		CoffeeOrderList = self.Order.getCoffeeOrders().split(",")
		self.DisplayAll(CoffeeOrderList,"CoffeeOrders",2)

		print("\nAdding a MenuItem")
		OrderId = input("Enter Id for the CoffeeOrder: ")
		ItemName = input("Enter The Menu Item Name: ")
		ItemPrice = input("Enter the Menu Item Price: ")
		
		self.Menu.UpdateMenuItem(OrderId,ItemName,ItemPrice)

	def AdditionItemUpdate(self):
		CoffeeOrderList = self.Order.getCoffeeOrders().split(",")
		self.DisplayAll(CoffeeOrderList,"CoffeeOrders",2)

		print("\nUpdating an Addition to CoffeeOrder")
		AddId = input("Enter Id for the Addition to Update: ")
		ItemName = input("Enter The Addition Item Name: ")
		ItemPrice = input("Enter the Addition Item Price: ")
		
		self.AddTo.UpdateAdditionItem(AddId,ItemName,ItemPrice)

	def CustomerUpdate(self):
		CustomerList = self.Cust.getCustomers().split(",")
		self.DisplayAll(CustomerList,"CoffeeOrders",2)

		print("\nUpdating Customer")
		CustId = input("Enter Customer Id to Update: ")
		FirstName = input("Enter First Name: ")
		LastName = input("Enter Last Name: ")
		PaymentType = input("Enter Payment Type: ")
		
		self.Cust.UpdateCustomer(CustId,FirstName,LastName,PaymentType)

	#Delete
	


keepRunning = True
	
asciiDoom()
time.sleep(3)
token = getToken()
	
while(keepRunning):
	

	menuDisplay = DisplayMenu() #displays the men to select from different classes
	
	menuDisplay.displayMenu()
	#AdditionItemPost()

	#cust = Customer()

	#print("Login")
	#userName = input("Enter an Email for Username: ")
	#password = input("Enter a password: ")

	#newToken = cust.Login(userName,password)
	#print(newToken)

	#getCoffeeshops()
	#CoffeeShopList = getCoffeeshops().split(",")
	#CoffeeOrderList = CoffeeOrder.getCoffeeOrder(2).split(",")
	#CustomerList = getCustomers(token).split(",")
	#MenuItemList = getMenuItems().split(",")
	#AdditionList = getAdditions().split(",")
	
	#DisplayAll(CoffeeShopList,"CoffeeShops",5)
	#DisplayById(CoffeeOrderList,"CoffeeOrders")
	#DisplayAll(CustomerList,"Customers",4)
	#DisplayAll(MenuItemList,"MenuItems",3)
	#DisplayAll(AdditionList,"AdditonItems",3)
	
	value1 = input("Do You want to Continue?(Enter y or n):")

	if(value1 == 'n'):
		keepRunning = False