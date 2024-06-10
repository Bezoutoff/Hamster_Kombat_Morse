from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from morse_clicker import click_morse_code  # Import the Morse code click function

# Configure the web driver
driver = webdriver.Chrome()
driver.get('https://your-website-url.com')  # Replace with your URL

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".user-tap-button-inner")))

# Call morse mode
# Waiting until the item becomes clickable
morse_mode = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__nuxt"]/div/main/div/ul/li/div[1]')))
# Cycle to click on the item three times with a 2 second delay between clicks
for _ in range(3):
  morse_mode.click()
  time.sleep(.5)
print("Entered morse mode!")
time.sleep(4)


# Example usage
message = "WEB3"
click_morse_code(element, message, driver)

time.sleep(2)
wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/div[7]/button/span')))
element.click()
print("Claim 1k for solving the morse!")
time.sleep(2)

# Close the driver after completion
driver.quit()
