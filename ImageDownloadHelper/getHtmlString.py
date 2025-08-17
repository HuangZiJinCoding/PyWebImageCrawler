# coding=utf-8
# CodeFilePath = /ImageDownloadHelper/getHtmlString.py

# Copyright (c) 2025 HuangZiJinCoding. All rights reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.

# This is the key code. Editing it may lead to errors. Please do not make any changes to this file unless you understand what the code does.

import urllib.request
import ssl
import certifi

url = str(input("Please enter the website you want to operate:"))

def getHtmlString():
    # Create SSL context with certifi certificates
    context = ssl.create_default_context(cafile=certifi.where())

    # Create request with headers to mimic browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)

    # Open URL with SSL context
    with urllib.request.urlopen(req, context=context) as response:
        data = response.read()
        htmlstr = data.decode(encoding="utf-8",errors="ignore")
        return htmlstr

if __name__ == "__main__":
    html = getHtmlString()
    print(html)