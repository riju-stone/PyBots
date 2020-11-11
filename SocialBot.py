from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:/Program Files (x86)/msedgedriver.exe'

class SocialBot:
    def __init__(self, username, pw):
        self.bot = webdriver.Edge(PATH)
        self.username = username
        self.pw = pw

    def login(self):
        bot = self.bot
        bot.get('https://www.twitter.com/')
        bot.maximize_window()
        time.sleep(3)

        email = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[1]/div/label/div/div[2]/div/input')
        password = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[2]/div/label/div/div[2]/div/input')
        log = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[3]/div/div/span/span')
        email.send_keys(self.username)
        password.send_keys(self.pw)
        log.click()
        time.sleep(5)


twitter = SocialBot('<username>', '<password>')
twitter.login()