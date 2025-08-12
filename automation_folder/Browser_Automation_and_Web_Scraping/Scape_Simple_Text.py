from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

print("Script is running...")

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/")
    return driver

def clean_text(text):
    """Extract only the temp from text"""
    output = float(text.split(": ")[1])
    return output

def write_to_file(text):
    """Write the text to a file"""
    filename = f"{dt.now().strftime("%Y-%m-%d-%H-%M-%S")}.txt"
    with open(filename, "w") as file:
        file.write(text)

def main():
    driver = get_driver()
    while True:
        time.sleep(3)
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        text = str(clean_text(element.text))
        write_to_file(text)



print(main())