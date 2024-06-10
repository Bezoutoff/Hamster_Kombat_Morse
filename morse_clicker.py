import time
import random
from selenium.webdriver.common.action_chains import ActionChains

# Define durations
DOT_DURATION = 0.1  # Duration of a dot
DASH_DURATION = 0.6  # Duration of a dash
LETTER_PAUSE = 4  # Pause between letters

# Create Morse code dictionary
MORSE_CODE_DICT = {
    'A': '•-', 'B': '-•••', 'C': '-•-•', 'D': '-••',
    'E': '•', 'F': '••-•', 'G': '--•', 'H': '••••',
    'I': '••', 'J': '•---', 'K': '-•-', 'L': '•-••',
    'M': '--', 'N': '-•', 'O': '---', 'P': '•--•',
    'Q': '--•-', 'R': '•-•', 'S': '•••', 'T': '-',
    'U': '••-', 'V': '•••-', 'W': '•--', 'X': '-••-',
    'Y': '-•--', 'Z': '--••',
    '1': '•----', '2': '••---', '3': '•••--', '4': '••••-', '5': '•••••',
    '6': '-••••', '7': '--•••', '8': '---••', '9': '----•', '0': '-----'
}

def click_dot(element, driver):
    ActionChains(driver).move_to_element_with_offset(element, random.uniform(0, element.size['width'] * 0.3), random.uniform(0, element.size['height'] * 0.3)).click().perform()
    time.sleep(DOT_DURATION)

def click_dash(element, driver):
    action = ActionChains(driver)
    action.move_to_element_with_offset(element, random.uniform(0, element.size['width'] * 0.3), random.uniform(0, element.size['height'] * 0.3))
    action.click_and_hold().perform()
    time.sleep(DASH_DURATION)
    action.release().perform()
    time.sleep(DOT_DURATION)

def click_morse_code(element, message, driver):
    for letter in message:
        if letter == ' ':
            time.sleep(LETTER_PAUSE)
        else:
            morse_code = MORSE_CODE_DICT.get(letter.upper(), '')
            for symbol in morse_code:
                if symbol == '•':
                    click_dot(element, driver)
                elif symbol == '-':
                    click_dash(element, driver)
            time.sleep(LETTER_PAUSE)  # Pause between letters
