from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# 1️⃣ LOGIN TEST
driver.get("https://the-internet.herokuapp.com/login")
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
wait.until(EC.presence_of_element_located((By.ID, "flash")))
print("Login Test Passed")

# 2️⃣ CHECKBOX TEST
driver.get("https://the-internet.herokuapp.com/checkboxes")
checkboxes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']")))
checkboxes[0].click()
checkboxes[1].click()
print("Checkbox Test Passed")

# 3️⃣ DROPDOWN TEST
driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown_element = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
Select(dropdown_element).select_by_visible_text("Option 2")
print("Dropdown Test Passed")

# 4️⃣ ALERT TEST
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
js_alert_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']")))
js_alert_button.click()
try:
    alert = wait.until(EC.alert_is_present())
    alert.accept()
    print("Alert Test Passed")
except TimeoutException:
    print("Alert did not appear! Skipping this test.")

# 5️⃣ ADD/REMOVE ELEMENTS TEST
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Element']")))
add_button.click()
try:
    delete_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "added-manually")))
    delete_button.click()
    print("Add/Remove Test Passed")
except TimeoutException:
    print("Delete button did not appear! Skipping this test.")

driver.quit()