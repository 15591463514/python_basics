"""
石头剪刀布游戏 对战电脑
你和电脑出石头剪刀布
比一比 你会赢吗
"""
# 首先，导入随机数模块
import random

# 产生随机的结果
item=["石头","剪刀","布"]
result = random.choice(item)

# 玩家输入自己想出的结果
player = input("你出：")

# 电脑选择随机数，代表石头剪刀布
computer = result

# 首先检查玩家输入是否是石头剪刀布
if player != "石头" and player != "剪刀" and player != "布":

    # 不是，则提示输入石头剪刀布
    print("请输入石头剪刀布")

# 是，显示电脑出的是什么，并判断是否会赢
else:
    print("电脑出的是：%s" % computer)

    # 赢的情况：
    #   player    computer
    #   石头      剪刀
    #   剪刀      布
    #   布        石头
    if ( player == "石头" and computer == "剪刀") \
            or( player == "剪刀" and computer == "布")\
            or( player == "布" and computer == "石头"):
        print("恭喜你，你赢了")

    # 输的情况：
    #   player    computer
    #   布      剪刀
    #   石头      布
    #   剪刀       石头
    elif ( player == "布" and computer == "剪刀" )\
            or( player == "石头" and computer == "布" )\
            or( player == "剪刀" and computer == "石头"):
        print("你输了")

    # 平局条件为 玩家和电脑一样的
    # elif ( player == "石头" and computer == "石头" )\
    #         or( player == "剪刀" and computer == "剪刀" )\
    #         or( player == "布" and computer == "布"):
    else:
        print("这局是平局")


