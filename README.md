# Hamster_Kombat_Morse
Automatically resolves morse to selenium for Hamster Kombat
Detailed Instructions
Install Required Libraries:

Ensure you have selenium installed.
Install using: pip install selenium.
Create morse_clicker.py:

This file contains functions for clicking elements in Morse code using the selenium library.
Functions:

click_dot(element, driver): Simulates a dot click on the element.
click_dash(element, driver): Simulates a dash click on the element (click and hold).
click_morse_code(element, message, driver): Converts a message into Morse code and clicks the element accordingly.

Modify main.py:

Import the Morse code clicking function from morse_clicker.py.
Configure the Selenium web driver to open your target website.
Use WebDriverWait to ensure the element is clickable.
Call click_morse_code(element, message, driver) with the desired message.
Close the web driver after completion.
Run Your Code:

Run main.py to see the element being clicked according to the provided message in Morse code.
This setup ensures your code is modular and easy to maintain. The Morse code functionality is separated into its own file, making it reusable and easier to test.
