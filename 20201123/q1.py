"""
    题目：10w以内的一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少?
"""


def get_answer():
    """
    思路: 先对一个数开平方,开完平方再求平方,看等不等与他本身
    :return:
    """
    for i in range(1, 100000):
        x = int((i+100) ** 0.5)
        y = int((i+268) ** 0.5)
        if x**2 == (i+100) and y**2 == (i+268):
            print(i)


get_answer()
