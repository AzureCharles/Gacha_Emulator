#import pandas as pd
import random as rd
import time

#Gacha emulator from Arknights
"""
    Key points of card pool design:
     ①Support multiple sets of prize number imported from outside
     ②Support weighted probability output
     ③Support set-accessible probability
     ④Support built-in guarantee prize

    关键字说明：
    @TOTAL_STORE：Prizes类型的一个实例，总卡池
    @PR: 设定抽取概率
"""
#本次测试仅仅使用内置参数


class Prizes:   #卡池基本模板

    def __init__(self,ur_list,ssr_list,sr_list,r_list):
        self.ur = ur_list
        self.ssr = ssr_list
        self.sr = sr_list
        self.r = r_list


def range_list(start,amount):
    #生成一系列连续编号并返回列表
    return [item for item in range(start,start+amount)]
    #[exp for iter_var in iterable]
"""
等效于
    lst = []
    for num in range(start,start+amount):
        lst.append(num)
    return lst
"""

TOTAL_STORE = Prizes(range_list(6001,10), range_list(5001,20),
                     range_list(4001,30), range_list(3001,15))
#仓库初始化，这是一个全局Prizes类，包含10个ur，20个ssr，30个sr，15个r
#卡池内容从该仓库中取得

PR = (('ur',0.02),('ssr',0.08),('sr',0.35),('r',0.55))
#设定概率


def selectPrize(ur_list,ssr_list,prizes=TOTAL_STORE):
    #选取卡池内容
    selected_prizes = Prizes(ur_list, ssr_list,
                             prizes.sr,
                             prizes.r)
    #当期卡池
    print_current_prizes(selected_prizes)
    return selected_prizes


def print_current_prizes(selected_prizes, pbty=PR):
    #打印当期卡池与概率
    pass
    prizes_dict = selected_prizes.__dict__
    print(prizes_dict)


def test_function():
    test = selectPrize([6002,6005],[5001,5006,5009])
    print(test)


test_function()


def getPoolContent(Selected_Prize):
    pass
    prizeRates = []
    for index in prizeList:
        poolContent[prizeList[index]] = prizeRates[index]
    return poolContent

    #卡池列表初始化，key-value:编号-数量比例
    #为便于测试，


gachaResultDict = {}


"""class GachaPool:
    def __init__(self,poolContent,):
        self.pool = poolContent
        


def pool_initial(pool_capacity=100,prizeDict):
    gacha_pool = []
    gacha_pool.append(time.time())  #表首放置时间戳标识卡池序号
    for index in range(1,pool_capacity+1):
        gacha_pool.append(False)

    treasure = rd.randint(1,pool_capacity)
    gacha_pool[treasure] = True     #随机放置目标
    return gacha_pool"""

def gacha():
    #单次抽卡操作，结束后马上释放卡池并报告结果
    gacha_pool = pool_initial()
    gacha_result = gacha_pool[rd.randint(1,pool_capacity)]
    del gacha_pool
    return gacha_result

def gacha_congratulate(result_list):
    for result in result_list:
        if result:
            print("Congratulations!")
