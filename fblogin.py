from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Welcome to Omar Hegazy's Auto Facebook Login Bot.")
print("")
time.sleep(2)
class FacebookBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")
        time.sleep(5)
        user_name_elem = driver.find_element_by_name("email")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_name("pass")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

omarFB = FacebookBot(input("Enter Username: "),input("Enter Password: "))
omarFB.login()