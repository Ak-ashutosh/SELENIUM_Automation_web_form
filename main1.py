from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Start browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    driver.get("https://formsmarts.com/html-form-example")
    wait = WebDriverWait(driver, 15)

    # Switch to iframe (FormSmarts form is inside iframe)
    iframe = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)

    # -------- Fill First Name --------
    wait.until(EC.visibility_of_element_located((By.NAME, "u_kT8_4607"))).send_keys("John")

    # -------- Fill Last Name --------
    driver.find_element(By.NAME, "u_kT8_338354").send_keys("Doe")

    # -------- Fill Email --------
    driver.find_element(By.NAME, "u_kT8_4608").send_keys("john.doe@example.com")

    # -------- Select Subject (Dropdown) --------
    subject_dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
    subject_dropdown.select_by_visible_text("Support Inquiry")

    # -------- Fill Inquiry (Textarea) --------
    driver.find_element(By.TAG_NAME, "textarea").send_keys(
        "This is a test inquiry submitted using Selenium automation."
    )

    # -------- Click CONTINUE button --------
    driver.find_element(By.NAME, "submit").click()

    # Wait to observe result
    wait.until(EC.url_changes("https://formsmarts.com/html-form-example"))

finally:
    driver.quit()