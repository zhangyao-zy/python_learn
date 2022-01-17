"""
题目: 输出国际象棋棋盘
"""


def get_answer():
    """
    输出国际象棋棋盘
    棋盘规则: 横竖都是8 64个格子 黑白间隔
    其实还是一个嵌套循环问题
    通过取余判断应该是黑还是白
    """
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                print("黑", end="")
            else:
                print("白", end="")
        print()


if __name__ == '__main__':
    get_answer()
