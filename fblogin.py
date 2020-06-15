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
        userelement = driver.find_element_by_name("email")
        userelement.clear()
        userelement.send_keys(self.username)
        passelement = driver.find_element_by_name("pass")
        passelement.clear()
        passelement.send_keys(self.password)
        passelement.send_keys(Keys.RETURN)
        time.sleep(2)

omarFB = FacebookBot(input("Enter Username: "),input("Enter Password: "))
omarFB.login()
