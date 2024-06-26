# Hamster_Kombat_Morse

Automatically resolves Morse to Selenium for Hamster Kombat

![Hamster_Kombat_Morse](https://i.imgflip.com/8tcqyv.gif)


## Detailed Instructions

### Install Required Libraries

Ensure you have Selenium installed. You can install it using the following command:

pip install selenium

### Create `morse_clicker.py`

This file contains functions for clicking elements in Morse code using the Selenium library.

#### Functions

- `click_dot(element, driver)`: Simulates a dot click on the element.
- `click_dash(element, driver)`: Simulates a dash click on the element (click and hold).
- `click_morse_code(element, message, driver)`: Converts a message into Morse code and clicks the element accordingly.

### Modify `main.py`

1. Import the Morse code clicking function from `morse_clicker.py`.
2. Configure the Selenium web driver to open your target website.
3. Use `WebDriverWait` to ensure the element is clickable.
4. Call `click_morse_code(element, message, driver)` with the desired message.
5. Close the web driver after completion.

### Run Your Code

Run `main.py` to see the element being clicked according to the provided message in Morse code.

This setup ensures your code is modular and easy to maintain. The Morse code functionality is separated into its own file, making it reusable and easier to test.

