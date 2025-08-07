import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

def submit_form():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-gpu")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform")
        time.sleep(3)

        # Random values
        ages = ['18–24', '25–34', '35–44', '45 and above']
        genders = ['Male', 'Female', 'Prefer not to say']
        selected_age = random.choice(ages)
        selected_gender = random.choice(genders)

        # Find and type into the first "Age" field
        age_field = driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"] div[contenteditable="true"]')[0]
        age_field.click()
        age_field.send_keys(selected_age)
        time.sleep(1)

        # Find and type into the second "Gender" field
        gender_field = driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"] div[contenteditable="true"]')[1]
        gender_field.click()
        gender_field.send_keys(selected_gender)
        time.sleep(1)

        # Click submit
        submit_button = driver.find_element(By.XPATH, '//span[contains(text(), "Submit")]')
        submit_button.click()
        time.sleep(3)

    finally:
        driver.quit()
