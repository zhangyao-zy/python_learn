"""
    企业发放的奖金跟据利润提成,
    利润(i)小于等于10w元时,奖金可提10%;
    利润高于10w元时小于等于20w,高于10w的部分可提成7.5%;
    利润高于20w元时小于等于40w,高于20w的部分可提成5%;
    利润高于40w元时小于等于60w,高于40w的部分可提成3%;
    利润高于60w元时小于等于100w,高于60w的部分可提成1.5%;
    利润高于100w,高于100w的部分可提成1%;
"""


def get_bonus():

    # 定义奖金
    bonus = 0

    # 获取输入利润
    profit = int(input("请输入利润"))
    bonus1 = 100000 * 0.1
    bonus2 = bonus1 + (profit-100000) * 0.075
    bonus3 = bonus2 + (profit-200000) * 0.05
    bonus4 = bonus3 + (profit-400000) * 0.03
    bonus5 = bonus4 + (profit-600000) * 0.015
    bonus6 = bonus5 + (profit-1000000) * 0.01

    if profit > 1000000:
        bonus = bonus6
    elif profit > 600000:
        bonus = bonus5
    elif profit > 400000:
        bonus = bonus4
    elif profit > 200000:
        bonus = bonus3
    elif profit > 100000:
        bonus = bonus2
    elif profit <= 100000:
        bonus = bonus1
    else:
        print("非法数字")
        return

    print("奖金金额为", bonus)


get_bonus()
