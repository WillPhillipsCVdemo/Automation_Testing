from selenium import webdriver
import time
import os


##Driver
driver = webdriver.Firefox()

##website search
driver.get("http://www.google.com")

##search field
input_element = driver.find_element_by_name("q")

##search inquiry
input_element.send_keys("lego sets")
input_element.submit()


##create directory

if not os.path.exists("Results"):
    os.makedirs("Results")


##Pause for 4 seconds
time.sleep(4)

##Take screenshot
driver.save_screenshot("Results/results1.png")

##Close driver
driver.close()
