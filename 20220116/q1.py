"""
输出99乘法表
"""


def get_answer():
    """
        嵌套循环即可
        一个循环行,一个循环列
        格式化输出,%-3d占三位
    """
    for i in range(1, 10):
        for j in range(1, 10):
            print("%d*%d=%-3d" % (i, j, i * j), end="")
        print()


if __name__ == '__main__':
    get_answer()
