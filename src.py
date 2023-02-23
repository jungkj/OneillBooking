from selenium import webdriver

#selenimum code here: 
driver = webdriver.Chrome(executable_path="/Users/andyjung/chromedriver")
driver.get("http://www.google.com")
driver.quit()
