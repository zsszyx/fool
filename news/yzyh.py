# 有知有行
import requests
from bs4 import BeautifulSoup


def get_soup(url, need_assert=True):
    response = requests.get(url)
    if not need_assert:
        print(f"url: {url} code: {response.status_code} don't need assert")
        return BeautifulSoup(response.text, 'html.parser')
    assert response.status_code == 200, "Response status code is not 200"
    assert response.text is not None, "Response text is None"
    return BeautifulSoup(response.text, 'html.parser')


class yzyh():
    def __init__(self):
        self.url = "https://youzhiyouxing.cn/data"
        self.soup = get_soup(self.url)

    def get_temperature(self):
        temperature_element = self.soup.find('div', class_='tw-text-[40px] tw-font-semibold')
        if temperature_element:
            print("全市场温度:", temperature_element.text)
        else:
            print("未找到温度元素")

yzyh_instance = yzyh()
