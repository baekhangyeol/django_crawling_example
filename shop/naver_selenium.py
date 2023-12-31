import ssl

from selenium import webdriver
from urllib.parse import quote_plus
from urllib.request import urlopen
from selenium.webdriver.common.by import By
import os


def save_images(images , save_path):
    for index, image in enumerate(images[:10]):
        src = image.get_attribute('src')
        t = urlopen(src).read()
        file = open(os.path.join(save_path, str(save_path), str(index + 1) + ".jpg"), "wb")
        file.write(t)
        print("img save " + save_path + str(index + 1) + str(index + 1) + ".jpg")


def create_folder_if_not_exists(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('message: Creating directory. ' + directory)

def make_url(search_term):
    base_url = 'https://search.naver.com/search.naver?where=image&section=image&query='

    return base_url + quote_plus(search_term)

def crawl_images(search_term):
    ssl._create_default_https_context = ssl._create_unverified_context

    url = make_url(search_term)

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(url)
    images = driver.find_elements(By.CLASS_NAME, "_image")
    save_path = "/Users/hangyeol/" + search_term + "/"
    create_folder_if_not_exists(save_path)

    save_images(images, save_path)

    print(search_term + "저장 성공")
    driver.quit()


if __name__ == '__main__':
    crawl_images(input('원하는 검색어: '))

