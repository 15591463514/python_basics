"""
使用if的嵌套  判断一个人是否可以乘坐列车
满足两个条件  一、过安检（有违规物品禁止进入）
              二、检票（凭票上车）
"""
# 定义某个人有车票
has_ticket = True

# 定义某个人没有带违规物品
knife_length = 9

# 首先检查这个人是否带了车票，有车票才允许进行安检
if has_ticket:
    print("车票检查通过，请进行安检")
# 安检时，需要检查刀的长度，判断是否超过10厘米
# 如果超过10厘米，则提示刀的长度，不允许上车
    if knife_length >= 10:
        print("你的刀有%d厘米，不能上车" % knife_length)
# 如果不超过，则可以上车
    else:
        print("安检通过，可以上车了")
# 如果没票，不准进门
else:
    print("没票，先去买票")