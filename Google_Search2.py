from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
time.sleep(1)

##Take screenshot
driver.save_screenshot("Results/results3.png")



###Output results
RESULTS_LOCATOR = "//div/h3/a"


page1_results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)

for item in page1_results:
    print(item.text)

    ## Item text in lower case
    if "lego" in str(item.text).lower():
        print("Pass")
    else:
        print("Fail")


##Close driver
driver.close()
