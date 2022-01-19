"""
题目: 有一对兔子,从出生后三个月起每个月都生一对兔子,小兔子长到三个月后又生一对兔子,假如兔子都不死,那么每个月的兔子总数为多少?
"""


def get_answer():
    """
    我们需要最终输出的是每个月的数字,可以人为先算一下兔子的对数
    1 1 2 3 5 8 .....
    可以看到其实每个月兔子的对数都是=前面的数字相加
    所以其实是一个数学问题
    只要三个数字来交替赋值就行
    """
    first_month, second_month = 1, 1
    print(first_month, second_month, end="")
    for i in range(20):
        print(" ", first_month + second_month, end="")
        temp_month = second_month
        second_month = first_month + second_month
        first_month = temp_month

if __name__ == '__main__':
    get_answer()
