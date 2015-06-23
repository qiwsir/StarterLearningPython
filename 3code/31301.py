#! /usr/bin/env python
# coding = utf-8

import pandas
import pandas.io.data
import datetime
import urllib2
import csv

YAHOO = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sd1ohgl1vl1"

def get_quote_today(symbol):
    response = urllib2.urlopen(YAHOO % symbol)
    reader = csv.reader(response, delimiter=",", quotechar='"')
    for row in reader:
        if row[0] == symbol:
            return row

def main():
    symbol = "BABA"
    
    history = pandas.io.data.DataReader(symbol, "yahoo", start="2014/11/11")
    print history.tail(3)

    today = datetime.date.today()
    df = pandas.DataFrame( columns=["Open", "High", "Low", "Close", "Volume", "Adj Close"], dtype=float)

    row = get_quote_today(symbol)
    df.ix[0] = map(float, row[2:])

    history = history.append(df)

    print "today is %s" % today
    print history.tail(2)

if __name__ == "__main__":
    main()
