# coding=utf-8
# CodeFilePath = /ImageDownloadHelper/find_imageurls.py

# Copyright (c) 2025 HuangZiJinCoding. All rights reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.

# This is the key code. Editing it may lead to errors. Please do not make any changes to this file unless you understand what the code does.



import urllib.request
from bs4 import BeautifulSoup
from getHtmlString import *

def find_imageurls(html):
    sp = BeautifulSoup(html,"html.parser")
    imgtaglist = sp.find_all("img")
    srclist = list(map(lambda u:u.get("src"),imgtaglist))
    filtered_srclist = filter(lambda u:u.lower().endswith(".png") or u.lower().endswith(".jpg"),srclist)
    return filtered_srclist

if __name__ == "__main__":
    html = getHtmlString()
    url_list = find_imageurls(html)
    for url in url_list:
        print(url)