import urllib

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from HouseData import HouseData

BASE_URL = "https://www.yad2.co.il/realestate/forsale"
ITEM_CLASS = "feeditem table"
ITEM_TITLE = "title"
ITEM_SUBTITLE = "subtitle"
HOUSE_DATA = "middle_col"
ROOMS_DATA_ID = "data_rooms_"
FLOOR_DATA_ID = "data_floor_"
SQUARE_METER_DATA_ID = "data_SquareMeter_"
PRICE_DATA_CLASS = "price"
NUM_OF_PAGES = 1


def getHtml():
    # S = requests.Session()

    # option one - todo after a couple of times we get captcha - not good
    with urllib.request.urlopen(BASE_URL) as response:
        htmlData = response.read().decode('utf-8')
        return htmlData
    # browser = webdriver.Chrome()
    # browser.get(BASE_URL)
    # html = browser.page_source

    # session = requests.Session()

    # r = session.get(BASE_URL)
    # htmlString = r.html

    # print(htmlString)
    #
    # for curParam in range(NUM_OF_PAGES):
    #     curParam += 1
    #     curParam = {
    #         "page": str(curParam),
    #     }
    #     R = S.get(url=BASE_URL)
    #     DATA = R.content
    #     print(DATA)


def parseHtmlData(htmlData):
    soup = BeautifulSoup(htmlData, "lxml")
    homes_result = soup.findAll("div", {"class": ITEM_CLASS})
    i = 0
    for home_data_html in homes_result:
        cur_rooms_data_id = ROOMS_DATA_ID + str(i)
        cur_home_data = HouseData()

        # parse html data into data object
        cur_home_data.number_of_rooms = \
            home_data_html.find(id=cur_rooms_data_id).contents[0]
        cur_home_data.price = home_data_html.find("div",
                                                  {"class": ITEM_CLASS})
        i += 1

    print("finished")


if __name__ == "__main__":
    html = getHtml()
    parseHtmlData(html)

    # print(curParam["page"])

# unused options:
#     browser = webdriver.PhantomJS()
#     S.get(BASE_URL)
#     html = browser.page_source
#     soup = BeautifulSoup(html, 'lxml')
#
#     a = soup.find('section', 'wrapper')
