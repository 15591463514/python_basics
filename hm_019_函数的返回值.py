"""
    在017py中没有设置返回值，在函数外部就无法访问到
    这和求和的结果，所以一般给函数添加返回值用于外界
    能对函数计算接结果进行操作
"""


def fun1(count):
    """计算你的平时分"""

    # 平时分数 = 交作业次数 * 10（最多交过10次作业）

    # if count - int(count) != 0:

    usual_score = 0
    # 判断用户输入的次数是不是一个小数
    # 如果是小数，提示用户输入错误
    if not isinstance(count, int):
        print("不能输入小数！！！")
    # 若果不是小数，在进行次数范围的判断
    else:
        # 进行判断，交作业次数必须少于等于10次，大于0次
        # 如果输入次数范围正常，打印用户的平时分
        if 0 <= count <= 10:
            usual_score = count * 10
            # print("你的平时分数为：%d" % usual_score)

        # 如果输入的次数不在要求范围内，则提示用户次数不对
        else:
            print("你输入的次数不对！！！")


    return usual_score


def fun2(objective, subjective):
    """计算你的期末考试分数"""

    # 期末考试分数 = 客观题分数(60分) + 主观题分数(40分)
    exam_score = objective + subjective

    return exam_score

# 计算总成绩
score = fun1(8) * 0.3 + (fun2(60, 40)) * 0.7

print("你的总分为：%d" % score)




























