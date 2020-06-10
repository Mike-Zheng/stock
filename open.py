# -*- coding: UTF-8 -*-
# python -m pip install twstock
# py stock.py


# https://twstock.readthedocs.io/zh_TW/latest/
import twstock
import json
from datetime import datetime
from random import randint
from time import sleep



# print( type(twstock.codes) )
twStockList = twstock.codes
# codes.codes 台灣上市上櫃股票代號
# codes.tpex 台灣上櫃股票代號
# codes.twse 台灣上市股票代號
# print(twStockList)

def genAllStockList(twStockList):
    allStock=[]
    for key in sorted(twStockList.keys()):
        stockInfo = twStockList[key]
        eachStackData = {}
        eachStackData["type"] = stockInfo.type
        eachStackData["code"] = stockInfo.code
        eachStackData["name"] = stockInfo.name
        eachStackData["ISIN"] = stockInfo.ISIN
        eachStackData["start"] = stockInfo.start
        eachStackData["market"] = stockInfo.market
        eachStackData["group"] = stockInfo.group
        eachStackData["CFI"] = stockInfo.CFI
        eachStackData["id"] = key
        allStock.append(eachStackData)

    stockDataFile = open("allcode.json", "w")
    stockDataFile.write(json.dumps(allStock, sort_keys=True,indent=4, separators=(',', ':')))
    stockDataFile.close()

# genAllStockList(twStockList)


def genLast3Day(twStockList):
    allStock = []
    for key in sorted(twStockList.keys()):
        stockInfo = twStockList[key]
        # 先只撈股票
        if stockInfo.type == '\u80a1\u7968' or stockInfo.type == '股票':
            sleep(randint(8, 10))
            eachStackData = {}
            eachStackData["type"] = stockInfo.type
            eachStackData["code"] = stockInfo.code
            eachStackData["name"] = stockInfo.name
            eachStackData["ISIN"] = stockInfo.ISIN
            eachStackData["start"] = stockInfo.start
            eachStackData["market"] = stockInfo.market
            eachStackData["group"] = stockInfo.group
            eachStackData["CFI"] = stockInfo.CFI
            eachStackData["id"] = key
            
            print("讀取中: " + stockInfo.name + "(" + stockInfo.code + ")")
            stock = twstock.Stock(str(stockInfo.code))

            # 取得各股一個月內有開盤的資料
            dataNear31 = stock.fetch_31()
            print(dataNear31)
            eachStackData["datas"] = []

            # 一個月內只取最新三天
            for i in dataNear31[-3:]:
                dayInfoTemp = {}
                dayInfoTemp["date"] = str(i.date)
                # capacity 總成交股數 (單位: 股)
                dayInfoTemp["capacity"] = i.capacity
                # turnover 總成交金額 (單位: 新台幣/元)
                dayInfoTemp["turnover"] = i.turnover
                # open 開盤價
                dayInfoTemp["open"] = i.open
                # high 盤中最高價
                dayInfoTemp["high"] = i.high
                # low 盤中最低價
                dayInfoTemp["low"] = i.low
                # close 收盤價
                dayInfoTemp["close"] = i.close
                # change 漲跌價差
                dayInfoTemp["change"] = i.change
                # transaction 成交筆數
                dayInfoTemp["transaction"] = i.transaction
                eachStackData["datas"].append(dayInfoTemp)
            print(eachStackData)
            allStock.append(eachStackData)


    #  寫檔案
    stockDataFile = open("stock.json", "w")
    stockDataFile.write(json.dumps(allStock, sort_keys=True,
                                indent=4, separators=(',', ':')))
    stockDataFile.close()





def genLastDay(twStockList):
    allStock = []
    for key in sorted(twStockList.keys()):
        stockInfo = twStockList[key]
        # 先只撈股票
        if stockInfo.type == '\u80a1\u7968' or stockInfo.type == '股票':
            sleep(randint(8, 10))
            eachStackData = {}
            eachStackData["type"] = stockInfo.type
            eachStackData["code"] = stockInfo.code
            eachStackData["name"] = stockInfo.name
            eachStackData["ISIN"] = stockInfo.ISIN
            eachStackData["start"] = stockInfo.start
            eachStackData["market"] = stockInfo.market
            eachStackData["group"] = stockInfo.group
            eachStackData["CFI"] = stockInfo.CFI
            eachStackData["id"] = key
            
            print("讀取中: " + stockInfo.name + "(" + stockInfo.code + ")")
            stock = twstock.Stock(str(stockInfo.code))

            # 取得各股一個月內有開盤的資料
            dataNear31 = stock.fetch_31()
            print(dataNear31)
            eachStackData["datas"] = []

            # 一個月內只取最新三天
            for i in dataNear31[-3:]:
                dayInfoTemp = {}
                dayInfoTemp["date"] = str(i.date)
                # capacity 總成交股數 (單位: 股)
                dayInfoTemp["capacity"] = i.capacity
                # turnover 總成交金額 (單位: 新台幣/元)
                dayInfoTemp["turnover"] = i.turnover
                # open 開盤價
                dayInfoTemp["open"] = i.open
                # high 盤中最高價
                dayInfoTemp["high"] = i.high
                # low 盤中最低價
                dayInfoTemp["low"] = i.low
                # close 收盤價
                dayInfoTemp["close"] = i.close
                # change 漲跌價差
                dayInfoTemp["change"] = i.change
                # transaction 成交筆數
                dayInfoTemp["transaction"] = i.transaction
                eachStackData["datas"].append(dayInfoTemp)
            print(eachStackData)
            allStock.append(eachStackData)


    #  寫檔案
    stockDataFile = open("stock.json", "w")
    stockDataFile.write(json.dumps(allStock, sort_keys=True,
                                indent=4, separators=(',', ':')))
    stockDataFile.close()


# genLast3Day(twStockList)