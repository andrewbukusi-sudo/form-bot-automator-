import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def random_delay(min_seconds=1, max_seconds=3):
    time.sleep(random.uniform(min_seconds, max_seconds))

def submit_form():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/chromium"

    driver = None
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform")

        # Wait for page to load
        time.sleep(2)

        # Simulate typing into custom editable fields
        editable_fields = driver.find_elements(By.CSS_SELECTOR, 'div[contenteditable="true"]')
        responses = [
            "25–34",  # Age
            "Male",   # Gender
            "Yes",    # Seen wildlife photos?
            "Weekly", # Frequency
            "Agree",  # Impact agreement
            "4",      # Effectiveness rating
            "Instagram, YouTube", # Platforms
            "YouTube",            # Most impactful
            "Shocked",            # Reaction
            "Agree"               # Support due to photos
        ]

        for field, response in zip(editable_fields, responses):
            field.click()
            field.clear()
            field.send_keys(response)
            random_delay()

        # Submit
        submit_button = driver.find_element(By.XPATH, '//span[text()="Submit"]/ancestor::div[@role="button"]')
        submit_button.click()

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if driver:
            driver.quit()