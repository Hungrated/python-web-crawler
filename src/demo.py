# -*-coding:utf-8-*-

import requests
from lxml import html

cookie = {}

raw_cookies = ''

# for line in raw_cookies.split(';'):
#     key, value = line.split("=", 1)
#     cookie[key] = value

page = requests.get('https://github.com/Hungrated', cookies=cookie)

tree = html.fromstring(page.text)

print(tree)

intro_raw = tree.xpath('//span[@id="intro_display"]/text()')
