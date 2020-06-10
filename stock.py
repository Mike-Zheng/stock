# -*- coding: UTF-8 -*-
# python -m pip install twstock
# py stock.py


# https://twstock.readthedocs.io/zh_TW/latest/
import twstock
import json
from datetime import datetime
from random import randint
from time import sleep
import pandas_datareader as pdr
from ids import stockIds
twStockList = twstock.codes
# twstock.codes 台灣上市上櫃股票代號
# twstock.tpex 台灣上櫃股票代號
# twstock.twse 台灣上市股票代號
# print(twStockList)


# ------- 取得股市代碼  ----

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
    


# ------- 生成前三天資料  ----

def genLast3Day(twStockList):
    allStock = []
    for key in sorted(twStockList.keys()):
        stockInfo = twStockList[key]
        # 先只撈股票
        if stockInfo.type == '\u80a1\u7968' or stockInfo.type == '股票':
    
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

            try:

                df = pdr.DataReader(str(stockInfo.code)+'.TW', 'yahoo')
                # df['High']
                # df['Low']
                # df['Open']
                # df['Close']
                # df['Volume']
                # df['Adj Close']

                # 取得各股3天內有開盤的資料
                eachStackData["datas"] = {}
                eachStackData["datas"]['date']=[str(df.index[-1]),str(df.index[-2]),str(df.index[-3])]
                eachStackData["datas"]['open']=[df['Open'][-1],df['Open'][-2],df['Open'][-3]]

                print(eachStackData)
                allStock.append(eachStackData)
            except:
                print("Yahoo 不存在該股資料: " + stockInfo.name + "(" + stockInfo.code + ")")


    #  寫檔案
    stockDataFile = open("stock.json", "w")
    stockDataFile.write(json.dumps(allStock, sort_keys=True,
                                indent=4, separators=(',', ':')))
    stockDataFile.close()
    return allStock





def nowOpenMoreThanlast3Days(now, last3days):
    print('及時開盤:'+now)
    print('前三天開盤:'+ str(last3days))
    if float(now) > float(last3days[0]) and float(now) > float(last3days[1]) and float(now) > float(last3days[2]):
        return True
    else:
        return False


def getLast3Day():
    with open('stock.json') as data_file:    
        return json.load(data_file)





# ------- 主程式


# 生成清單 (你用不到吧)
# genAllStockList(twStockList)

# print(stockIds)


# 取得前三天的資料(開盤)
# last3DayData = genLast3Day(twStockList)
last3DayData = getLast3Day()



twstock.realtime.mock = False

# for eachId in stockIds:
#     stock=twstock.realtime.get(eachId)
#     sleep(5)
#     print(stock["realtime"]["open"])



targetList=[]


for eachStock in last3DayData:

    print("及時個股資料獲取中:" + eachStock['name'] +" ("+eachStock['code']+")")
    stock=twstock.realtime.get(eachStock['code'])
    nowOpen=stock["realtime"]["open"]

    if nowOpenMoreThanlast3Days(nowOpen,eachStock['datas']['open']):
        tempObj={}
        tempObj["name"]=eachStock['name']
        tempObj["code"]=eachStock['code']
        targetList.append(tempObj)
    sleep(5)



print("個股今天開盤大於前三天開盤:")
print(str(targetList))
