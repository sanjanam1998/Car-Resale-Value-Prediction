# Python code to demonstrate working of unittest 
import unittest 
import requests

class TestStringMethods(unittest.TestCase): 
	def setUp(self): 
		pass

	# Validating the first api which is used to predict the resale value of the car
	# For an existing brand Audi. expected code 200
	def test_existing_brand(self): 
		response = requests.post("http://127.0.0.1:5000/",json = {"model":'a3',"brand":'audi',"fuel":'diesel',"vehicle":'small car',"damage":'nein',"gear":"manuell","date":'1998-12-19',"km":15000,"power":750})
		self.assertEqual( response.status_code , 200) 

	# For a non-existing brand Aux. expected code 400 and not an error code 500 
	def test_random_brand(self): 
		response = requests.post("http://127.0.0.1:5000/", json = {'brand':'aux','model':'a3','fuel':'diesel','vehicle':'small car','damage':'nein','gear':'manuell','date':'1998-12-19','km':15000,'power':750})
		self.assertEqual( response.status_code , 400) 
 
	# For a exceptionally high power. Expected 400
	def test_power(self): 
		response = requests.post("http://127.0.0.1:5000/", json = {'brand':'audi','model':'a3','fuel':'diesel','vehicle':'small car','damage':'nein','gear':'manuell','date':'1998-12-19','km':15000,'power':15550})
		self.assertEqual( response.status_code , 400)

	# For an invalid fuel type ( A drop down in the frontend ). Response body is expected
	def test_fuel_type(self): 
		response = requests.post("http://127.0.0.1:5000/", json = {'brand':'audi','model':'a3','fuel':'desel','vehicle':'small car','damage':'nein','gear':'manuell','date':'1998-12-19','km':15000,'power':750})
		self.assertEqual( response, "Choose One among the input field")

	# For a blank input field. Expected 400
	def test_blank(self): 
		response = requests.post("http://127.0.0.1:5000/", json = {'brand':' ','model':'a3','fuel':'diesel','vehicle':'small car','damage':'nein','gear':'manuell','date':'1998-12-19','km':15000,'power':750})
		self.assertEqual( response.status_code , 400) 

	# Validation of Date. Expected 400 (Input form "Date" in the frontend)
	def test_date(self): 
		response = requests.post("http://127.0.0.1:5000/", data = {'brand':'audi','model':'a3','fuel':'diesel','vehicle':'small car','damage':'nein','gear':'manuell','date':'1998-12-32','km':15000,'power':750})
		self.assertEqual( response.status_code , 400)

	#Validating the second api which is used to register the cars.
	# For a legitimate input. Expected 200
	def test_register(self): 
		response = requests.put("http://127.0.0.1:5000/",json = {"table":"cars","model":'a3',"brand":'audi',"fuel":'diesel',"vehicle":'small car',"damage":'nein',"gear":"manuell","date":'1998-12-19',"km":15000,"power":750})
		self.assertEqual( response.status_code , 200)

	#For negative values of km. Expected 400
	def test_km_negative(self):
		response = requests.put("http://127.0.0.1:5000/",json = {"table":"cars","model":'3er',"brand":'bmw',"fuel":'diesel',"vehicle":'small car',"damage":'nein',"gear":"manuell","date":'1998-12-19',"km":-1,"power":750})
		self.assertEqual( response.status_code , 400) 

	# For a junk input which has special characters to the parameter 'model', expected code 400
	# Since the user input is not being validated. It would return 200 and add the junk value to the DB 
	def test_junk_model(self): 
		response = requests.put("http://127.0.0.1:5000/", json = {"table":"cars",'brand':'ford','model':'a3#$','fuel':'diesel','vehicle':'small car','damage':'nein','gear':'manuell','date':'1998-12-19','km':15000,'power':750})
		self.assertEqual( response.status_code , 400)

	#Validating the third api subscribe. Expected 200
	def test_subscribe(self):
		response = requests.put("http://127.0.0.1:5000/",json = {"table":"sub","fname":"Abcd","lname":"xyz","email":"abcd@gmail.com","number":"987654321"})
		self.assertEqual( response.status_code , 200)

if __name__ == '__main__': 
	unittest.main() 