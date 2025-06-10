from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_proceed_to_checkout(driver):
    driver.get("https://www.saucedemo.com/")

    # Wait for login form elements and enter credentials
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    # Wait for URL to change to inventory page
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

    # Debug print and screenshot
    print("Current URL after login:", driver.current_url)
    try:
        driver.save_screenshot("debug_inventory_screen.png")
    except Exception as e:
        print("Screenshot failed:", e)

    # Check for login error message
    error = driver.find_elements(By.CLASS_NAME, "error-message-container")
    if error:
        print("Login failed:", error[0].text)
        try:
            driver.save_screenshot("login_failed.png")
        except Exception as e:
            print("Login screenshot failed:", e)
        assert False, "Login failed"

    # Wait for inventory items to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    # Check how many inventory items were found
    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print("Found", len(inventory_items), "items.")
    assert len(inventory_items) > 0
