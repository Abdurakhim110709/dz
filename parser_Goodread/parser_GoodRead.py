import requests
from bs4 import BeautifulSoup as BS

URL = 'https://www.goodreads.com/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}


# 1
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


# 2
def get_data(html):
    bs = BS(html, features="html.parser")
    items = bs.find_all('div', class_='b-content__inline_item')
    GoodRead_list = []
    for item in items:
        title = item.find('div', class_='b-content__inline_item-link').get_text()
        href = item.find('a').get('href')
        GoodRead_list.append(
            {
            'title': title,
            'href': href
            }
        )
    return GoodRead_list


# 3
def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        GoodRead_list2 = []
        for page in range(1, 2):
            response = get_html("https://www.goodreads.com/", params={'page': page})
            GoodRead_list2.extend(get_data(response.text))
        return GoodRead_list2
    else:
        raise Exception('Error in parsing')

print(parsing())
