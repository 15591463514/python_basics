"""
    创建两个函数函数
    第一个函数：计算一月的工资（ =  一天的工资 * 25）
    第二个函数：计算一年的工资（ =  一个月的工资 * 10 ）
    将第一个函数的结果，作为第二个函数的实参
    用户输入一天的工资，打印一个月的工资，打印一年的工资
"""


def money_month(money):
    """
    计算一月的工资
    :param money: 一天的工资
    """
    moneyMonth = money * 26

    return moneyMonth


def money_year(moneyM):
    """

        :param money: 一天的工资
        """
    moneyYear = moneyM * 11

    return moneyYear


a = int(input("请输入你一天的工资："))

print("你一月的工资为：%d" % money_month(a))

print("你一年的工资为：%d" % money_year(money_month(a)))



