"""
    习题1:
    有1,2,3,4 四个数字,能组成多少个互不相同且无重复数字的三位数?都是多少
"""


def answer():
    """
        思路: 循环三次,分别获取个位十位百位
    :return:
    """

    main_list = list(range(1,5))
    total_num = 0
    #白位
    for i in main_list:
        ten_list = main_list.copy()
        ten_list.remove(i)
        #十位
        for j in ten_list:
            hundred_list = ten_list.copy()
            hundred_list.remove(j)
            #个位
            for k in hundred_list:
                print(i*100+j*10+k)
                total_num += 1

    print("共有",total_num,"个")

#调用
answer()



