"""
从101-200有多少个素数,输出全部素数
"""


def get_answer():
    """
    素数: 只能被1和他本身整除的数
    还是嵌套循环问题,首先循环 101 -200
    再嵌套循环 每次从2到被循环的数字有没有可以整除的,如果有说明这个数字不符合要求,结束循环
    """
    for i in range(101, 200):
        temp = True
        for j in range(2, i):
            if i % j == 0:
                temp = False
                break
        if temp:
            print(i)


if __name__ == '__main__':
    get_answer()
