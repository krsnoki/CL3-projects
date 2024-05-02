# Import the library Selenium 
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains 
options = webdriver.ChromeOptions() 
options.add_argument('headless') 

chrome_driver_path = "\home\kalyani\Downloads\chromedriver_linux64"
browser = webdriver.Chrome( executable_path=chrome_driver_path, options=options) 

url = ["https://www.google.com/maps/place/Shri+Guru+Gobind+Singhji+Institute+of+Engineering+and+Technology/@19.1120892,77.2896565,17z/data=!4m15!1m8!3m7!1s0x3bce29f0b2e43199:0xe11b84ac3144b2b4!2sSGGS,+Vishnupuri,+Nanded,+Maharashtra+431606!3b1!8m2!3d19.1120015!4d77.2924127!16s%2Fg%2F11g1gt0047!3m5!1s0x3bce29b9903d053d:0x2c5238a90ab55c03!8m2!3d19.1124662!4d77.2924383!16s%2Fm%2F027z39w?entry=ttu"] 

i = 0

for i in range(len(url)): 

	# Open the Google Map URL 
	browser.get(url[i]) 
	title = browser.find_element_by_class_name( 
		"x3AX1-LfntMc-header-title-title") 
	print(i+1, "-", title.text) 
	stars = browser.find_element_by_class_name("aMPvhf-fI6EEc-KVuj8d") 
	print("The stars of restaurant are:", stars.text) 
	description = browser.find_element_by_class_name("uxOu9-sTGRBb-T3yXSc") 
	print("Description: ", description.text) 

	# Obtain the address of that place 
	address = browser.find_elements_by_class_name("CsEnBe")[0] 
	print("Address: ", address.text) 

	# Obtain the contact number of that place 
	phone = browser.find_elements_by_class_name("CsEnBe")[-2] 
	print("Contact Number: ", phone.text) 

	# Obtain the reviews of that place 
	review = browser.find_elements_by_class_name("OXD3gb") 
	print("------------------------ Reviews --------------------") 
	for j in review: 
		print(j.text) 
	print("\n") 
