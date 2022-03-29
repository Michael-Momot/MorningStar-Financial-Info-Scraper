from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait





class MorningstarScraper():

    MORNINGSTAR_BASE_URL = "https://www.morningstar.com/stocks/xnas/"  # xnas designates american markets

    def __init__(self, ticker):
        self.ticker = ticker
        self.driver = webdriver.Chrome()


    def test(self):
        self.driver.get(self.MORNINGSTAR_BASE_URL + self.ticker + "/quote")
        self.driver.refresh()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "keyStats").click()

        linkToOpen = self.driver.find_element(By.CLASS_NAME, "sal-full-key-ratios")
        linkToOpen.find_element(By.TAG_NAME, "a").get_attribute("href")

        self.driver.get(linkToOpen.find_element(By.TAG_NAME, "a").get_attribute("href"))

        # self.driver.find_element(By.LINK_TEXT, "Full Key Ratios Data").click


