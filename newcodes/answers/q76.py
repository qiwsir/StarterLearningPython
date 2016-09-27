#!/usr/bin/env python
# coding=utf-8

import urllib.request, json


def weather(city):
    url = "http://apis.baidu.com/heweather/weather/free?city={}".format(city)

    req = urllib.request.Request(url)
    req.add_header("apikey", "3befccfb4dde4ef385a62a92e958a204")

    resp = urllib.request.urlopen(req)
    content = resp.read()
    if content:
        return content

if __name__ == "__main__":
    print("Search the weather, Please input the city name.")
    while True:
        city_name = input("input your city:")
        r = weather(city_name)
        r_str = r.decode(encoding='utf-8', errors='strict')
        r_dict = json.loads(r_str) 
        weather_values = r_dict["HeWeather data service 3.0"][0]
        basic_info = weather_values["basic"]
        city_name = basic_info['city']
        daily_forecast = weather_values['daily_forecast']
        #aqi = weather_values['aqi']
        today_forecast = daily_forecast[0]
        tomorrow_forecast = daily_forecast[1]
        today_date = today_forecast['date']
        tomorrow_date = tomorrow_forecast['date']
        today_pop = today_forecast['pop']
        tomorrow_pop = tomorrow_forecast['pop']
        print("{0}{1}:降水概率{2}%".format(today_date, city_name, today_pop))
        print("{0}{1}:降水概率{2}%".format(tomorrow_date, city_name, tomorrow_pop))
        
