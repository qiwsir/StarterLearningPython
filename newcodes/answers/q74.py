#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup
import time

def get_data(url):
    req = requests.get(url)
    
    soup = BeautifulSoup(req.text, 'lxml')
    try:
        table = soup.select("#ContentPlaceHolder1_lbldata table table")[0].find_all("td")
        province = table[0].find("b").string
        province = str(province)
        crop_name = str(table[6].string)
        crop_number = str(table[7].string)
        return province, crop_name, crop_number
    except:
        return False

if __name__ == "__main__":
    for i in range(11, 66): 
        url = "http://202.127.42.157/moazzys/nongqing_result.aspx?year=2015&prov={}%20%20%20&item=01&type=1&radio=1&order1=year_code&order2=prov_code&order3=item_code".format(i)
        result = get_data(url)
        if result:
            print(result)
        else:
            print("hahha")
            time.sleep(1)
