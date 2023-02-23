from selenium import webdriver

#Selenium code to open the browser
driver = webdriver.Chrome()
driver.get("https://libcal.bc.edu/reserve/oneill")

#Testing selenium run
print(driver.title)
 