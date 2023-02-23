from selenium import webdriver

#Selenium code to open the browser
driver = webdriver.Chrome(executable_path='/Users/andyjung/Downloads/chromdriver1')


driver.get("https://libcal.bc.edu/reserve/oneill")

#Testing selenium run
print(driver.title)

#Test