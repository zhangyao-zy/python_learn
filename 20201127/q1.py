"""
用*输出C的图案
"""


def get_answer():

    for i in range(5):
        print(" "*(10-(i*2)), "**")

    print("**")
    print("**")
    print("**")

    for i in range(5):
        print(" "*((i+1)*2), "**")


get_answer()
