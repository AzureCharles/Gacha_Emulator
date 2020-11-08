# -*- coding: utf-8 -*-
"""
    #This is a simple gacha simulator without consolation prize:)

    #Set target probability as:1%
    #Capacity of the simulated pool is 100 and maximum of operand is 10
"""
import random as rd
import time
pool_capacity = 100
max_operand = 10

def pool_initial():
    gacha_pool = []
    gacha_pool.append(time.time())  #表首放置时间戳标识卡池序号
    for index in range(1,pool_capacity+1):
        gacha_pool.append(False)

    treasure = rd.randint(1,pool_capacity)
    gacha_pool[treasure] = True     #随机放置目标
    return gacha_pool
"""
def get_print_list(gacha_result):
    result_list = []
    result_list.append(gacha_result)
    return result_list
"""
def gacha():
    #单次抽卡操作，结束后马上释放卡池并报告结果
    gacha_pool = pool_initial()
    gacha_result = gacha_pool[rd.randint(1,pool_capacity)]
    del gacha_pool
    return gacha_result

def gacha_multi(gacha_times = 10):
    #执行多次的单次抽卡，并输出结果列表。默认值是10
    if gacha_times <= max_operand:
        result_list = []
        for index in range(1,gacha_times+1):
            result_list.append(gacha())
        print(result_list)
        gacha_congratulate(result_list) #祝贺信息or出货特效
    else:
        print("Incorrect usage!\n")

def gacha_congratulate(result_list):
    for result in result_list:
        if result:
            print("Congratulations!")
            
#The MAIN function of simple gacha simulator is as follow:
active = True
while active:
    test_times = int(input("Please specify the times of lottery:\n"))
    
    if test_times >= max_operand:
        for try_num in range(1,int(test_times/max_operand)+1):
            gacha_multi()
        if test_times%max_operand:
            gacha_multi(test_times%max_operand)
    else:gacha_multi(test_times)
    
    end_flag = input("Do you want to end the gacha?(Y/N)\n")
    if end_flag == 'Y' or 'y':
        break
    
