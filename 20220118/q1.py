"""
打印十阶楼梯,同时在楼梯上方打印两个笑脸
ヽ(°◇° )ノヽ(°◇° )ノ
￣|
￣|￣|
￣|￣|￣|
￣|￣|￣|￣|
￣|￣|￣|￣|￣|
￣|￣|￣|￣|￣|￣|
￣|￣|￣|￣|￣|￣|￣|
￣|￣|￣|￣|￣|￣|￣|￣|
￣|￣|￣|￣|￣|￣|￣|￣|￣|
"""


def get_answer():
    """
    还是嵌套循环问题
    需要考虑的是,内层循环的次数其实是外层循环的变量
    """
    print("ヽ(°◇° )ノ" * 2)
    for i in range(10):
        for j in range(i):
            print("￣|", end="")
        if i > 0:
            print("")


if __name__ == '__main__':
    get_answer()
