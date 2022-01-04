import requests
import json
import csv
from bs4 import BeautifulSoup

allStocks = []
stocksInfo = []
numOfStocks = int(input("Choose the number of stocks to view: "))
for i in range(numOfStocks):
    stock = input("Enter Stock (Ticker Symbol) " + str(i + 1) + ": ")
    allStocks.append(stock)



def getInfo(ticker_symbol):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
    url = 'https://www.marketwatch.com/investing/stock/' + ticker_symbol + '?'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    symbol = ticker_symbol
    price = soup.find('h2', {'class':'intraday__price'}).find_all('bg-quote')[0].text
    price_change = soup.find('span', {'class':'change--point--q'}).find_all('bg-quote')[0].text
    percent_change = soup.find('span', {'class':'change--percent--q'}).find_all('bg-quote')[0].text
    
    stock = [symbol, price, price_change, percent_change]

    return stock

for stock in allStocks:
    stocksInfo.append(getInfo(stock))
print(stocksInfo)
    
with open ('stocksData.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Symbol', 'Price', 'Price Change', 'Percent Change'])
    writer.writerows(stocksInfo)
    