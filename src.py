from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new service object for Chromedriver
service = Service('/Users/andyjung/chromedriver1/chromedriver')

# timetable wait function
def wait_for_time_table():
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "eq-time-grid"))
    )




# Start Chromedriver
driver = webdriver.Chrome(executable_path='/Users/andyjung/chromedriver1/chromedriver', service=service)

# Go to the O'Neill Library Reserve Room page
driver.get("https://libcal.bc.edu/reserve/oneill")

# Find Date Picker window and click it twice 
element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div/div/div/div[4]/div[1]/div[1]/div[1]/div/button[2]")
element.click() 
wait_for_time_table()
element.click()
