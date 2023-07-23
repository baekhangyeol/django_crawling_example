import os
import sys

# 현재 파일의 경로를 가져옴
current_path = os.path.abspath(os.path.dirname(__file__))

# 프로젝트 폴더(config 폴더의 상위 폴더)의 경로를 가져옴
project_path = os.path.abspath(os.path.join(current_path, ".."))

# 프로젝트 경로를 시스템 경로에 추가
sys.path.append(project_path)

# DJANGO_SETTINGS_MODULE 환경 변수 설정
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
