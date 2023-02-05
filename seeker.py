"""
Author:Saba Konjaria
Created at: 06-Feb-2023 02:04. Poti, Georgia
"""
# first improve only necessary libraries
from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


# url of the form that builds our spreadsheet
form_url = "https://forms.gle/C1kd4nVxmVHGt8wy7"
# get the response in order to work on raw html and then cook so much beautiful soup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en,ka;q=0.9"
}
response = requests.get(
    url="https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.54502520766381%2C%22east%22%3A-122.31431231703881%2C%22south%22%3A37.66956567780267%2C%22north%22%3A37.80477697968697%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A628633%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    headers=headers)
raw_html = response.text
soup = BeautifulSoup(raw_html, 'lxml')
addresses = soup.find(name="div", id="grid-search-results").find_all(name='li')


# define a function to get only decimal part from a junk string we have
def extract_number(string):
    extracted_number = ''
    we_got_digit = False
    comma = ','
    dot = '.'
    for char in string:
        if char.isdigit() or we_got_digit and char == comma or char == dot:
            extracted_number += char
            we_got_digit = True
        else:
            break
    return extracted_number


# lists of the things we want to tackle
url_links = []
prices_list = []
addresses_list = []
# put all the variables into the lists
for i, address in enumerate(addresses):
    try:
        current_url = address.find(name="a").get("href")
        if not current_url.__contains__('https://'):
            current_url = "https://www.zillow.com" + current_url
        current_address = address.find(name="address").text
        if address.find(name="span").text.__contains__('$') is False:
            continue
        current_span_text = extract_number(address.find(name="span").text.split('$')[1])
        url_links.append(current_url)
        addresses_list.append(current_address)
        prices_list.append(current_span_text)
    except AttributeError:
        continue

# tackle selenium webdriver


# build web-driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# access the url we've copied over
driver.get(form_url)



time.sleep(10)
for i, curr_url in enumerate(url_links):
    in_form_address = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    in_form_price = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    in_form_url = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(2)
    in_form_address.send_keys(addresses_list[i])
    in_form_price.send_keys(prices_list[i])
    in_form_url.send_keys(curr_url)

    send_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    send_button.click()
    time.sleep(3)

    once_again = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    once_again.click()
    time.sleep(3)

