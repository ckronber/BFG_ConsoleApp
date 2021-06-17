import time
import os
import http.client
import ssl

def getToken():
	token = "bearer UMfe73d_n89Ps_rOx-QzZYe9WI2gl1lGd_ty1npOmPEtvfqHUvkZu3S1n1IwMWRPvlIUnKI_255-YM-ANZ19OnifFF4b4wDcTYJy3QlFOZAFgTPc6Rk1nbj9JeQkBHXWfbWl1YFPPikBn_-6W8n9HFd_BIao8rK8ltpPONvfF3lR93Z8FTWGRB8yc_CgmZ89UKnWktqVsZU-zn7jt5qypPn4YVwi5KPGl0s7AQnv2dcCciSy-WV_9P1UadG0hC40B1oW0rwqBrFwaLWecyuqFxVy4LvbKm-6xs8sIYWs1dy9zinOLTkKrSMz3U4OtuVTNdkLJ56jCVdShv3SSytcUwpFSxN1dYcAYWcPPUbObPz5WoQnAwqBn1sGZcx6A21zGr-oHxwVQw0n7rzkW-dJBE3xY3FXa0Z1giuIxs5NGzYxnYl67uo4Em9D2K51kUohgNeVFR8TxIkLRjQNvV0pG2qvMF53tqSpNKlnTgXXv0g"
	return token
	
def clearConsole():
    command = 'cls'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def asciiDoom():
	print("""
		____________ _____        _____        __  __                 _____ _                 
		| ___ \  ___|  __ \      /  __ \      / _|/ _|               /  ___| |                
		| |_/ / |_  | |  \/      | /  \/ ___ | |_| |_ ___  ___       \ `--.| |__   ___  _ __  
		| ___ \  _| | | __       | |    / _ \|  _|  _/ _ \/ _ \       `--. \ '_ \ / _ \| '_ \ 
		| |_/ / |   | |_\ \      | \__/\ (_) | | | ||  __/  __/      /\__/ / | | | (_) | |_) |
		\____/\_|    \____/       \____/\___/|_| |_| \___|\___|      \____/|_| |_|\___/| .__/ 
																					| |    
																					|_|    

																																								
				***********,,,***/**,.,                                              
				,,,,///,,,(((***((/*******/**////*,,,,,,,.,,,/////////////////////***   
			((..................,* .   *(((((*//***/*((((((/***//(/////(/****%*****  
		(((((((((((((((((((((/(/(%%((/(/((((((//////////(/*,/,,*******************,  
		/*//(/(//////////(///////###/*,,*,*,,/*******,,,,,,,,,,,    .,,,..,,,,**,,   
			*/.    ..  .....   .  ,,... ,..,,,,,,,,,*...,..,.,   ,.,,  , *,,******,,*   
			***,,,,,,,,,,,,,,,,,,,,****,,,,,,,,,,   ,.*..,..     .,,.    ,,***,,*.*    
					..................., ,....   .....,*,.,      ,,,,      ,,,,,**     
				. ..... ,.... ........,,,,,.,.,,,,,,,,,.,,/,,**....,,...*                  
			..,,.....    . ...........,,,,,,,,.,.,/,,,,,/.,,,,.,                   
					,,,,,...       ........,*, *....                                    
					...,,,,.............,                                             
									, .,.      """)

class CoffeeShop:
	#CoffeeShop Crud
	def AddCoffeeshop(name,location,number,website):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'ShopName='+name+'&Location='+location+'&PhoneNumber='+number+'&Website='+website
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("POST", "/api/CoffeeShop", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def getCoffeeshops():
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET", "/api/CoffeeShop", payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def getCoffeeShop(id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET","/api/CoffeeShop/"+id, payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def UpdateCoffeeshop(id,name,location,number,website):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'CoffeeShopId='+id+'&ShopName='+name+'&Location='+location+'&PhoneNumber='+number+'&Website='+website
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("PUT", "/api/CoffeeShop", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def RemoveCoffeeShop(id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("DELETE","/api/CoffeeShop/"+id, payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

class CoffeeOrder:
	#CoffeeOrder Crud
	def AddCoffeeOrder(country,barista,shopid):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'Country='+country+'&Barista='+barista+'&CoffeeShopId='+shopid
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("POST", "/api/CoffeeOrder", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def getCoffeeOrders():
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET", "/api/CoffeeOrder", payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def getCoffeeOrder(id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET","/api/CoffeeOrder/"+str(id), payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def UpdateCoffeeOrder(id,country,barista,shopid):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'CoffeeOrderId='+id+'&Country='+country+'&Barista='+barista+'&CoffeeShopId='+shopid
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("PUT", "/api/CoffeeOrder", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def RemoveCoffeeOrder(id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("DELETE","/api/CoffeeOrder/"+id, payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

class MenuItem:
	#Menu Crud
	def AddMenuItem(itemName,itemPrice,orderId):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'ItemName='+itemName+'&ItemPrice='+itemPrice+'&CoffeeOrderId='+orderId
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("POST", "/api/Menu", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def getMenuItems():
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET", "/api/Menu", payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def getMenuItem(id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET", "/api/Menu/"+id, payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def AddMenuItem(id,itemName,itemPrice,orderId):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'ItemName='+id+'&ItemName='+itemName+'&ItemPrice='+itemPrice+'&CoffeeOrderId='+orderId
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("PUT", "/api/Menu", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def RemoveMenuItem(id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("DELETE", "/api/Menu/"+id, payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

class Addition:
	#Addition Crud
	def AddAdditionItem(itemName,itemPrice,orderId):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'Name='+itemName+'&Price='+itemPrice+'&CoffeeOrderId='+orderId
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("POST", "/api/Addition", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def getAdditions():
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET", "/api/Addition", payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def getAddition(id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("GET", "/api/Addition/"+id, payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def UpdateAdditionItem(id,itemName,itemPrice,orderId):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'AdditionId'+id+'&Name='+itemName+'&Price='+itemPrice+'&CoffeeOrderId='+orderId
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("PUT", "/api/Addition", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def RemoveAddition(id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {}
		conn.request("DELETE", "/api/Addition/"+id, payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")
	
class Customer:
	#Register
	def Register(userName,password,passConfirm):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'Email='+userName+'&Password='+password+'ConfirmPassword'+passConfirm
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("POST", "/api/Register", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	#Login
	def Login(userName,password):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'grant_type=password&Email='+userName+'&Password='+password
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn.request("GET", "/token", payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	#Customeer Crud
	def AddCustomer(firstName,lastName,paymentType,orderId,tolken):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'FirstName='+firstName+'&LastName='+lastName+'PaymentType'+paymentType+'&CoffeeOrderId='+orderId
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain","Authorization": tolken}
		conn.request("POST", "/api/Customer", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))
		
	def getCustomers(tolken):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {"Authorization": tolken}
		conn.request("GET", "/api/Customer", payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def getCustomer(tolken,id):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {"Authorization": tolken}
		conn.request("GET", "/api/Customer/"+id, payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")

	def UpdateCustomer(id,firstName,lastName,paymentType,tolken):
		conn = http.client.HTTPSConnection("localhost", 44378,context = ssl._create_unverified_context())
		payload = 'CustomerId='+id+'&FirstName='+firstName+'&LastName='+lastName+'PaymentType'+paymentType
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain","Authorization": tolken}
		conn.request("PUT", "/api/Customer", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print(data.decode("utf-8"))

	def RemoveCustomer(id,tolken):
		conn = http.client.HTTPSConnection("localhost", 44378, context = ssl._create_unverified_context())
		payload = ''
		headers = {"Authorization": tolken}
		conn.request("DELETE", "/api/Customer/"+id, payload, headers)
		res = conn.getresponse()
		data = res.read()
		return data.decode("utf-8")
	
class Menu:
	# this method is used to select which to do	
	def displayMenu():
		clearConsole()
		print("BFG CoffeeShopMenu")
		print("===================")
		print("1. CoffeeShop")
		print("2. CoffeeOrder")
		print("3. Customer")
		print("4. MenuItems")
		print("5. Additions")
		
		menuValue = input("\nMake a selection: ")
		
		'''
		switch (menuValue):
		case 1:
			displayCRUD("CoffeeShop")
			break
		case 2: 
			displayCRUD("CoffeeOrder")
			break
		case 3:
			displayCRUD("Customer")
			break
		case 4:
			displayCRUD("MenuItems")
			break
		case 5:
			displayCRUD("AdditionItems")
			break
		default:
			print("Not a value from 1 to 5")
			break
	'''

	def displayCRUD(MainValue):
		print("Select an Option for " + MainValue)
		print("===================")
		print("1. Add")
		print("2. Update")
		print("3. Display")
		print("4. Delete")
		
		#crudVal = input("\n Select an Option: ")

class CRUD:
	
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
		
	def CoffeeShopPost():
		print("Adding a CoffeeShop")
		Name = input("Enter Name for CoffeeShop: ")
		Location = input("Enter Location CoffeeShop: ")
		Number = input("Enter Phone Number for CoffeeShop: ")
		Website = input("Enter Website for CoffeeShop: ")
		
		CoffeeShop.AddCoffeeshop(Name,Location,Number,Website)
		
	def CoffeeOrderPost(self):
		CoffeeOrderList = CoffeeOrder.getCoffeeOrders().split(",")
		self.DisplayAll(CoffeeOrderList,"CoffeeShops",5)

		print("\nAdding a CoffeeOrder")
		ShopId = input("Enter Id for the CoffeeShop: ")
		Barista = input("Enter Barista Fulfilling this Order: ")
		Country = input("Enter The Origin Coutry for the Beans: ")
		
		CoffeeOrder.AddCoffeeOrder(Country,Barista,ShopId)

	def MenuItemPost(self):
		CoffeeOrderList = CoffeeOrder.getCoffeeOrders().split(",")
		self.DisplayAll(CoffeeOrderList,"CoffeeOrders",2)

		print("\nAdding a MenuItem")
		OrderId = input("Enter Id for the CoffeeShop: ")
		ItemName = input("Enter The Menu Item Name: ")
		ItemPrice = input("Enter the Menu Item Price: ")
		
		Menu.AddMenuItem(ItemName,ItemPrice,OrderId)

	def AdditionItemPost(self):
		CoffeeOrderList = CoffeeOrder.getCoffeeOrders().split(",")
		self.DisplayAll(CoffeeOrderList,"CoffeeOrders",2)

		print("\nAdding a Addition to CoffeeOrder")
		OrderId = input("Enter Id for the CoffeeShop: ")
		ItemName = input("Enter The Addition Item Name: ")
		ItemPrice = input("Enter the Addition Item Price: ")
		
		Addition.AddAdditionItem(ItemName,ItemPrice,OrderId)

keepRunning = True
	
asciiDoom()
time.sleep(3)
token = getToken()
	
while(keepRunning):
	
	#displayMenu() #displays the men to select from different classes
	
	#AdditionItemPost()


	print("Enter A Username and Password")
	userName = input("Enter an Email for Username:")
	password = input("Enter a password to Login")

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