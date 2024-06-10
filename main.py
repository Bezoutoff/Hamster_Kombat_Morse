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
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    click_morse_code(element, message, driver)
    time.sleep(1)  # Adjust this duration if necessary

    try:
        # Wait for the confirmation element to appear
        confirm_wait = WebDriverWait(driver, 20)
        confirm_element = confirm_wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__nuxt"]/div/div[4]/div/div[7]/button/span'))
        )
        confirm_element.click()
        break  # Break the loop if the confirmation element is found and clicked
    except TimeoutException:
        attempts += 1
        print(f"Attempt {attempts} failed: Confirmation element not found, retrying Morse code clicks...")

if attempts == max_attempts:
    print("Max attempts reached. Confirmation element not found.")       

time.sleep(3)

# Close the driver after completion
driver.quit()
