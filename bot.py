"""
Facebook Friend Request Automation Bot

Uses Selenium with a real Brave browser profile to
send Facebook friend requests based on keyword search.

Intended for educational or controlled internal use.
"""

import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# =======================
# CONFIG (Environment Variables)
# =======================

BRAVE_PATH = os.getenv("BRAVE_PATH")
USER_DATA_DIR = os.getenv("USER_DATA_DIR")
PROFILE_DIR = os.getenv("PROFILE_DIR", "Default")

if not all([BRAVE_PATH, USER_DATA_DIR]):
    raise RuntimeError(
        "Missing environment variables: BRAVE_PATH, USER_DATA_DIR"
    )


# =======================
# BROWSER SETUP
# =======================

def setup_browser():
    chrome_options = Options()
    chrome_options.binary_location = BRAVE_PATH

    chrome_options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
    chrome_options.add_argument(f"--profile-directory={PROFILE_DIR}")

    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver


def human_sleep():
    time.sleep(random.uniform(3, 7))


def open_people_search(driver, keyword):
    url = f"https://www.facebook.com/search/people/?q={keyword.replace(' ', '%20')}"
    driver.get(url)
    time.sleep(5)


def find_add_friend_buttons(driver):
    btns = []

    elements = driver.find_elements(By.XPATH, "//div[@aria-label='Add Friend']")
    btns.extend(elements)

    elements = driver.find_elements(
        By.XPATH,
        "//span[text()='Add friend']/ancestor::div[@role='button']"
    )
    btns.extend(elements)

    return list(dict.fromkeys(btns))


def main():
    keyword = input("Enter keyword: ").strip()

    driver = setup_browser()
    open_people_search(driver, keyword)

    print("🔥 Started friend request bot...")
    last_height = 0

    while True:
        buttons = find_add_friend_buttons(driver)
        print(f"🟢 Found {len(buttons)} Add Friend buttons...")

        for btn in buttons:
            try:
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", btn
                )
                time.sleep(1)
                driver.execute_script("arguments[0].click();", btn)
                print("🎯 Friend Request Sent")
                human_sleep()
            except Exception as e:
                print("⚠️ Click failed:", e)

        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(3)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("✔️ Reached end of results.")
            break
        last_height = new_height

    print("🎉 Finished sending friend requests.")
    input("Press ENTER to close browser...")
    driver.quit()


if __name__ == "__main__":
    main()
