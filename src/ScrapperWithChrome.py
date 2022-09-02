from selenium import webdriver
from bs4 import BeautifulSoup


def load_page(page_url):
    driver = webdriver.Chrome("/Users/santhoshkalisamy/Downloads/chromedriver")
    driver.get(page_url)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    print(soup)
    return page_url

print(load_page("https://www.amazon.in/Sparx-Black-Brown-Flip-Flops-Slippers/dp/B00IZ94LHG/?th=1&psc=1"));
