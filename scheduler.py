import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def submit_form():
    driver = None
    try:
        # Setup Chrome for Render
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service("/usr/local/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get("YOUR_GOOGLE_FORM_URL_HERE")
        time.sleep(2)

        # --- AGE ---
        age_options = ["18–24", "25–34", "35–44", "45 and above"]
        chosen_age = random.choice(age_options)
        age_input = driver.find_element(By.XPATH, '//input[@aria-label="Age"]')
        age_input.clear()
        age_input.send_keys(chosen_age)
        time.sleep(0.5)

        # --- GENDER ---
        gender_options = ["Male", "Female", "Prefer not to say"]
        chosen_gender = random.choice(gender_options)
        gender_input = driver.find_element(By.XPATH, '//input[@aria-label="Gender"]')
        gender_input.clear()
        gender_input.send_keys(chosen_gender)
        time.sleep(0.5)

        # --- YES/NO: Seen wildlife photographs? ---
        seen_options = ["Yes", "No"]
        chosen_seen = random.choice(seen_options)
        seen_input = driver.find_element(By.XPATH, '//input[@aria-label="Have you seen photographs of endangered wildlife or conservation efforts?"]')
        seen_input.clear()
        seen_input.send_keys(chosen_seen)
        time.sleep(0.5)

        # --- FREQUENCY ---
        freq_options = ["Never", "Rarely", "Sometimes", "Often", "Very often"]
        chosen_freq = random.choice(freq_options)
        freq_input = driver.find_element(By.XPATH, '//input[@aria-label="How often do you see wildlife photographs?"]')
        freq_input.clear()
        freq_input.send_keys(chosen_freq)
        time.sleep(0.5)

        # --- AGREEMENT with conservation impact ---
        agree_options = ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"]
        chosen_agree = random.choice(agree_options)
        agree_input = driver.find_element(By.XPATH, '//input[@aria-label="Do you agree that wildlife photographs raise conservation awareness?"]')
        agree_input.clear()
        agree_input.send_keys(chosen_agree)
        time.sleep(0.5)

        # --- EFFECTIVENESS scale 1–5 ---
        chosen_effect = str(random.randint(1, 5))
        effect_input = driver.find_element(By.XPATH, '//input[@aria-label="On a scale of 1–5, how effective are photographs in promoting conservation?"]')
        effect_input.clear()
        effect_input.send_keys(chosen_effect)
        time.sleep(0.5)

        # --- PLATFORMS (multiple choice) ---
        platforms = ["Social Media", "News Websites", "Magazines", "TV", "Other"]
        chosen_platforms = random.sample(platforms, random.randint(1, len(platforms)))
        platforms_input = driver.find_element(By.XPATH, '//input[@aria-label="Which platforms do you usually see wildlife photographs on?"]')
        platforms_input.clear()
        platforms_input.send_keys(", ".join(chosen_platforms))
        time.sleep(0.5)

        # --- MOST IMPACTFUL PLATFORM ---
        chosen_best_platform = random.choice(platforms)
        best_platform_input = driver.find_element(By.XPATH, '//input[@aria-label="Which platform is the most impactful for conservation awareness?"]')
        best_platform_input.clear()
        best_platform_input.send_keys(chosen_best_platform)
        time.sleep(0.5)

        # --- REACTION to wildlife photos ---
        reaction_options = ["Inspired", "Sad", "Angry", "Motivated", "No reaction"]
        chosen_reaction = random.choice(reaction_options)
        reaction_input = driver.find_element(By.XPATH, '//input[@aria-label="What is your reaction when you see wildlife photographs?"]')
        reaction_input.clear()
        reaction_input.send_keys(chosen_reaction)
        time.sleep(0.5)

        # --- AGREEMENT to support conservation due to photographs ---
        chosen_support = random.choice(agree_options)
        support_input = driver.find_element(By.XPATH, '//input[@aria-label="Do photographs make you more likely to support conservation efforts?"]')
        support_input.clear()
        support_input.send_keys(chosen_support)
        time.sleep(0.5)

        # --- SUBMIT ---
        submit_button = driver.find_element(By.XPATH, '//span[text()="Submit"]')
        submit_button.click()
        print(f"✅ Submitted with Age={chosen_age}, Gender={chosen_gender}")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        if driver:
            driver.quit()
