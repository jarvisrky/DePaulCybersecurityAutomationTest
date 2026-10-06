''' Number 3 '''

import requests
import time
from selenium import webdriver


def capture(url):
    tops = requests.get(url).text.split()
    elites = tops[:10]

    browser = webdriver.Chrome()

    for site in elites:
        browser.get("https://" + site)
        time.sleep(5)

        name = site.replace("www.", "").split(".")[0]
        browser.save_screenshot(name + ".png")

    browser.quit()
    return elites

url = "https://raw.githubusercontent.com/bensooter/URLchecker/master/top-1000-websites.txt"
print(capture(url))
