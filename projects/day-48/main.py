from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/darrenleith/Documents/WebDriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# 1. Getting price of item from Amazon
# driver.get("https://www.amazon.co.uk/Apple-iPhone-11-Pro-64GB/dp/B07XRPD4TV/ref=sr_1_1_sspa?crid=1G4TQ589KJ333&dchild=1&keywords=iphone+11&qid=1614607264&sprefix=iphone%2Caps%2C151&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVTBETlhLTDBRQzROJmVuY3J5cHRlZElkPUEwODA4NjE0MTU5WjYwSjhXR0E3WSZlbmNyeXB0ZWRBZElkPUEwMjQ4OTgzM09VSURTSEpNVEZWUCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
# price = driver.find_element_by_id('priceblock_ourprice')


# 2. getting stock price from TradingView
# driver.get("https://www.tradingview.com/symbols/NASDAQ-AAPL/")
# price = driver.find_element_by_class_name('js-symbol-ext-hrs-close')
# # making use of x-path. If all else fails, x-path wont !
# price = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[2]/div/div/div[1]/div[1]/div[1]')
# print(float(price.text))
#
# if float(price.text) > 123.56:
#     print("123.57 alert")


# 3. get the next 5 upcoming events on python.org
# driver.get("https://www.python.org/")
# events_dict = {}
# for i in range(1, 6):
#     date = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/time')
#     event = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/a')
#     events_dict[i-1] = {
#         'time': date.text,
#         'name': event.text
#     }
# print(events_dict)

# alternatively...
# event_times = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
# events = {}

# 4. clicking
# driver.get("http://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_elements_by_css_selector('#articlecount a')
# all_portals = driver.find_element_by_link_text('All portals')
# # all_portals.click()
# # 5. searching, using keys
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# # 6. hitting enter
# search.send_keys(Keys.ENTER)

# 7. Filling in a form
driver.get("http://lethalapps.com/contact.html")
name = driver.find_element_by_id('name')
email = driver.find_element_by_id('email')
message = driver.find_element_by_id('message')
submit = driver.find_element_by_css_selector("form button")

name.send_keys("user name")
email.send_keys("a@a.com")
message.send_keys("lorem text")
submit.click()

#
# driver.quit()

