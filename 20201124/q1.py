"""
输入某年某月某日,判断是本年的哪一天
"""
import time


def get_answer():
    """
        使用time模块转换为时间元组

    :return:
    """
    date = input("请输入日期,格式为20201124\n")
    print("输入日期为=", date)

    struct_time = time.strptime(date, "%Y%m%d")
    print(struct_time)

    print("输入日期是本年第", struct_time[7], "天")


get_answer()
