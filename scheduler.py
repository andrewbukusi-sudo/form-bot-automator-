import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def submit_form():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/chromium"

    service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform")
        time.sleep(3)

        # Fill Age (simulated typing)
        age_field = driver.find_element(By.XPATH, '//div[@aria-label="Age"]')
        age_field.click()
        age_field.send_keys(random.choice(["18–24", "25–34", "35–44", "45 and above"]))
        time.sleep(1)

        # Fill Gender (simulated typing)
        gender_field = driver.find_element(By.XPATH, '//div[@aria-label="Gender"]')
        gender_field.click()
        gender_field.send_keys(random.choice(["Male", "Female", "Prefer not to say"]))
        time.sleep(1)

        # Click Submit
        submit_button = driver.find_element(By.XPATH, '//span[contains(text(), "Submit")]')
        submit_button.click()
        time.sleep(2)

    finally:
        driver.quit()
