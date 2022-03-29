import requests
from bs4 import BeautifulSoup
import os
from morningstar_scraper import MorningstarScraper
from array import *

import guru_scraper
import logging

DEBUG = True


class Scraper():
    GURUFOCUS_BASE_URL = "https://www.gurufocus.com/stock/"
    MORNINGSTAR_BASE_URL = "https://www.morningstar.com/stocks/xnas/"  # xnas designates american markets


    CELLS = [["Stock Ticker", "B9"],
             ["Stock Price", "B10"],
             ["Enterprise Value", "B13"],
             ["F-Score", "B15"],
             ["Z-Score", "B16"],
             ["M-Score", "B17"],
             ["Required Margin of Safety", "B18"],
             ["Desired Discount Rate %", "B19"],
             ["20 AA Corporate bond Rate % ", "B20"],
             ["Discount Rate 10y Fed Note %", "B21"]
             ]

    def __init__(self, ticker):
        self.ticker = ticker

    def getGuruFields(self) :
        guru_url = self.GURUFOCUS_BASE_URL + self.ticker + "/summary"
        req = requests.get(guru_url)

        if req.status_code != 200:
            logging.error("Status Code {} for URL {}".format(req.status_code, guru_url))
            return -1

        text = req.text
        soup = BeautifulSoup(text, 'html.parser')

        with open("./sample/{}_guru.txt".format(self.ticker), "w+", encoding="utf-8") as f:
            f.write(soup.getText())

        with open("./sample/{}_guru.txt".format(self.ticker), "r", encoding="utf-8") as f:
            lines = f.readlines()

        print("Price: {}".format(lines[361]))

        if not DEBUG:
            os.remove("{}_guru.txt".format(self.ticker))

        return 1


def main():
    ticker = input("Enter Ticker: ")

    morningstar_scraper = MorningstarScraper(ticker)

    morningstar_scraper.test()



    # scraper = Scraper(ticker)
    #
    # scraper.getGuruFields()


if __name__ == '__main__':
    main()
