from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import time

def submit_form():
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        service = Service("/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfLijis5Y40ribPKLDwocm8EnfJXYyPATrU-G9i07AzHBqsAw/viewform")
        time.sleep(2)

        # === Age ===
        age_choices = ["18-24", "25-34", "35-44", "45 and above"]
        age = random.choice(age_choices)
        age_input = driver.find_element(By.XPATH, '//input[@type="text" and @aria-label="Age"]')
        age_input.clear()
        age_input.send_keys(age)

        # === Gender ===
        gender_choices = ["Male", "Female", "Prefer not to say"]
        gender = random.choice(gender_choices)
        gender_input = driver.find_element(By.XPATH, '//input[@type="text" and @aria-label="Gender"]')
        gender_input.clear()
        gender_input.send_keys(gender)

        # === Seen photographs? ===
        seen_input = driver.find_element(By.XPATH, '//input[@type="text" and contains(@aria-label,"photographs of endangered wildlife")]')
        seen_input.clear()
        seen_input.send_keys(random.choice(["Yes", "No"]))

        # === Frequency ===
        freq_input = driver.find_element(By.XPATH, '//input[@type="text" and contains(@aria-label,"Frequency")]')
        freq_input.clear()
        freq_input.send_keys(random.choice(["Daily", "Weekly", "Monthly", "Rarely", "Never"]))

        # === Awareness impact ===
        agree_choices = ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"]
        impact_input = driver.find_element(By.XPATH, '//input[@type="text" and contains(@aria-label,"awareness impact")]')
        impact_input.clear()
        impact_input.send_keys(random.choice(agree_choices))

        # === Effectiveness scale ===
        scale_input = driver.find_element(By.XPATH, '//input[@type="text" and contains(@aria-label,"effectiveness")]')
        scale_input.clear()
        scale_input.send_keys(str(random.randint(1, 5)))

        # === Platforms ===
        platforms_choices = ["Facebook", "Instagram", "Twitter", "YouTube", "Newspapers", "Magazines", "Websites"]
        platforms_input = driver.find_element(By.XPATH, '//input[@type="text" and contains(@aria-label,"Platforms")]')
        platforms_input.clear()
        platforms_input.send_keys(", ".join(random.sample(platforms_choices, random.randint(1, 3))))

        # === Most impactful platform ===
        impactful_input = driver.find_element(By.XPATH, '//input[@type="text" and contains(@aria-label,"most impactful")]')
        impactful_input.clear()
        impactful_input.send_keys(random.choice(platforms_choices))

        # === Reaction ===
        reactions = ["Sadness", "Inspiration", "Anger", "Motivation", "Indifference"]
        reaction_input = driver.find_element(By.XPATH, '//input[@type="text" and contains(@aria-label,"Reaction")]')
        reaction_input.clear()
        reaction_input.send_keys(random.choice(reactions))

        # === Support for conservation ===
        support_input = driver.find_element(By.XPATH, '//input[@type="text" and contains(@aria-label,"support for conservation")]')
        support_input.clear()
        support_input.send_keys(random.choice(agree_choices))

        # === Submit ===
        submit_button = driver.find_element(By.XPATH, '//span[text()="Submit"]')
        submit_button.click()
        time.sleep(2)

    finally:
        if driver:
            driver.quit()
