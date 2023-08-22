# login to programming.dev instance of lemmy federation

# Module Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
dpath = r"C:\Users\ranger\AppData\Local\chromedriver.exe"
driver = webdriver.Chrome(dpath)
driver.get("https://programming.dev/")
driver.implicitly_wait(3)

# Login Element - Clciking login button on main page
driver.find_element(By.XPATH, "//*[@title='Login']").click()

# Entering Input into Username Password
uNameElement = driver.find_element(By.ID, "login-email-or-username")
uNameElement.clear() # Erase pre-existing text
uNameElement.send_keys("homers")

# Entering Input into Password
passElement = driver.find_element(By.CSS_SELECTOR, 'input.form-control[type="password"]')
# passElement.clear() # Erase pre-existing text
passElement.send_keys("WoodLand1234")
passElement.send_keys(Keys.RETURN)
""" # Clicking Login Button on login page
driver.find_element(By.CSS_SELECTOR, 'input.btn btn-secondary[type="submit"]').click()
 """
time.sleep(6)

driver.close()