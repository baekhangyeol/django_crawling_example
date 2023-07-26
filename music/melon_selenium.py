import os
import sys

current_path = os.path.abspath(os.path.dirname(__file__))

project_path = os.path.abspath(os.path.join(current_path, ".."))

sys.path.append(project_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django

django.setup()

from selenium import webdriver
from selenium.webdriver.common.by import By
from music.models import Music

def crawling_melon():
    driver = webdriver.Chrome()
    driver.get("https://www.melon.com/chart/index.htm")

    for row in driver.find_elements(By.XPATH, "//tbody/tr"):
        rank = int(row.find_element(By.CLASS_NAME, "rank").text)
        title = row.find_element(By.CLASS_NAME, "ellipsis.rank01").text.strip()
        artist = row.find_element(By.CLASS_NAME, "ellipsis.rank02").text.strip()
        album = row.find_element(By.CLASS_NAME, "ellipsis.rank03").text.strip()

        music = Music(rank=rank, title=title, artist=artist, album=album)
        music.save()

    driver.quit()


if __name__ == "__main__":
    crawling_melon()
