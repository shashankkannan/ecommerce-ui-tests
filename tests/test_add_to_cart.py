from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_product_to_cart(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    add_button = driver.find_element(By.CSS_SELECTOR, ".inventory_item button")
    product_name = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    add_button.click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_item_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    ).text

    assert product_name == cart_item_name
