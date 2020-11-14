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
        email.clear()
        email.send_keys(self.username)
        password.clear()
        password.send_keys(self.pw)
        log.click()
        time.sleep(5)

    def like_tweet(self, hashtag):
        bot = self.bot

        bot.get('https://www.twitter.com/search?q='+ hashtag +'&src=typed_query')
        time.sleep(3)

        """
        the range() determines how many times the bot scrolls...
        by default it's 10 times...
        """
        for i in range(1, 10):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)


twitter = SocialBot('<username>', '<password>')
twitter.login()
twitter.like_tweet('<search title>')