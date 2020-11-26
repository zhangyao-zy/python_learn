"""
输入三个整数,将三个整数按从大到小的顺序输出
"""


def get_answer():
    number1 = int(input("请输入第一个整数"))
    number2 = int(input("请输入第二个整数"))
    number3 = int(input("请输入第三个整数"))

    total_list = [number1,number2,number3]
    total_list.sort()

    print(total_list)


get_answer()

