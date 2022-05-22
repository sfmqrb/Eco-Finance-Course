from re import S
import pytse_client as tse
import csv
from persiantools.jdatetime import JalaliDate
from datetime import datetime as clock
import json

class Sheet:

    def __init__(self):
        pass

    def getAllContent(self):
        data = []
        with open('./output/Trades.csv')as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                data.append(row)
        return data
    def getCurrentMoneyLeft(self):
        data = self.getAllContent()
        return float(data[-1][-3])
    def getAmountsSection(self):
        data = self.getAllContent()
        return data[-1][9:14]

 
class Stock:

    sheet = Sheet()

    low = 0
    high = 0

    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
        self.ticker = tse.Ticker(symbol=self.sign)
        self.amount = self.getCurrentAmount()

    def setHight(self, high):
        self.high = high
    def setLow(self, low):
        self.low = low
    def downloadPrice(self):
        tse.download(symbols=self.sign, write_to_csv=True)
    def getCurrentPrice(self):
        return self.ticker.last_price
    def getYesterdaysPrice(self):
        return self.ticker.yesterday_price
    def getIndexInCSV(self):
        data = self.sheet.getAllContent()
        index = 0
        for idx, i in enumerate(data[0]):
            if self.sign in i:
                index = idx

        return index
    def getSignCSV(self):
        self.downloadPrice()
        path = f"./tickers_data/{self.sign}.csv"
        data = []
        with open(path) as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
        
    def getCurrentCandle(self):
        return 'green' if self.getCurrentPrice() > self.getYesterdaysPrice() else 'red'
    def isGreenCandle(self):
        return True if 'green' in self.getCurrentCandle() else False 
    def isRedCandle(self):
        return True if 'red' in self.getCurrentCandle() else False
        
    def getCurrentAmount(self):
        index = self.getIndexInCSV()
        data = self.sheet.getAllContent()
        return int(data[-1][index])

    def sell(self, amount):
        with open("./output/Trades.csv", 'a') as file:
            writter = csv.writer(file)
            date = JalaliDate.today()
            _time = clock.now()
            time = _time.strftime("%H:%M")
            trade_worth = amount * self.getCurrentPrice() 
            trade_cost = amount * self.getCurrentPrice() * 0.006
            money_left = self.sheet.getCurrentMoneyLeft() + ( trade_worth + trade_cost )
            self.amount -= amount
            quantity = self.sheet.getAmountsSection()
            quantity[self.getIndexInCSV() - 9] = self.amount
            row = [self.sign, -1, amount, self.getCurrentPrice(), trade_worth, trade_cost, money_left, date, time] + quantity
            writter.writerow(row)
    def buy(self, amount):
        with open("./output/Trades.csv", 'a') as file:
            writter = csv.writer(file)
            date = JalaliDate.today()
            _time = clock.now()
            time = _time.strftime("%H:%M")
            trade_worth = amount * self.getCurrentPrice() 
            trade_cost = amount * self.getCurrentPrice() * 0.006
            money_left = self.sheet.getCurrentMoneyLeft() - (trade_cost + trade_worth )
            self.amount += amount 
            quantity = self.sheet.getAmountsSection()
            quantity[self.getIndexInCSV() - 9] = self.amount
            row = [self.sign, 1, amount, self.getCurrentPrice(), trade_worth, trade_cost, money_left, date, time] + quantity
            writter.writerow(row)
    def getAverage(self):
        data = self.getSignCSV()
        prices = []
        for d in data[-90:]:
            prices.append(d[-1])
        highs = prices.sort()[:10]
        high = sum(highs) / len(highs)
        lows = prices.sort(reverse=True)[:10]
        low = sum(lows) / len(lows)
        return low, high