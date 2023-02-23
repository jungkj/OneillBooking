from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new service object for Chromedriver
service = Service('/Users/andyjung/chromedriver1/chromedriver')


# Start Chromedriver
driver = webdriver.Chrome(executable_path='/Users/andyjung/chromedriver1/chromedriver', service=service)

# Go to the O'Neill Library Reserve Room page
driver.get("https://libcal.bc.edu/reserve/oneill")

# Wait for time table window to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.ID, "eq-time-grid")))

# Find Date Picker window and click it twice 
element = driver.find_element(By.CLASS_NAME, "fc-next-button btn btn-default btn-sm")
element.click() 



# Wait for the clickable container to load:
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fc-event-title-container")))

# # Click on containers for 3-6 pm on the next week  
# driver.find_element_by_class_name("fc-event-title-container").click()
