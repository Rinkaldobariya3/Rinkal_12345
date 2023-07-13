# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.google.com/")
time.sleep(2)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","APjFqb") old syntax
search_bar = driver.find_element("id", "APjFqb")
search_bar.send_keys("dress")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(2)

# Verifying that the search results page has loaded
assert "dress" in driver.title
images = driver.find_element(By.XPATH, "//div[contains(text(),'Images')]")
images.click()

#time.sleep(2)
#
shopping = driver.find_element(By.XPATH, "//a[normalize-space()='Shopping']")
shopping.click()

Map = driver.find_element(By.XPATH, "//a[normalize-space()='Maps']")
Map.click()
#
#


#
# # Waiting for the dress details page to load
# time.sleep(5)
#
# # Adding the dress to the cart
# add_to_cart_button = driver.find_element("id","add-to-cart-button")
# add_to_cart_button.click()
#
# # Waiting for the cart to update
# time.sleep(5)
#
#
# go_to_checkout= driver.find_element("xpath","/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div/div[1]/span/span/a")
# go_to_checkout.click()
# time.sleep(2)
#
# Proceed_to_checkout= driver.find_element("xpath","/html/body/div[1]/div[2]/div[3]/div[5]/div/div[1]/div[1]/div/form/div/div[3]/span/span/span/input")
# Proceed_to_checkout.click()
# time.sleep(2)
#
# Closing the webdriver
driver.close()
