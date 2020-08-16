"""
逻辑运算符
                  在python中                在js中         （在C语言和java语言中  逻辑运算符和js中相同）
     且              and                      &&

     或              or                       \\

     非              not                      !

"""
# 练习一：定义一个年龄，判断年龄是否输入正确（0-120之间）
# 练习二：定义三个模块A、B、C，只要有一个模块的分数小于60分，就挂科
# 练习三：定义一个布尔值变量，判断是否是本公司员工（如果不是提示不允许入内）

is_employee = True  # True表示是本公司人员
if not is_employee:
    print("非公司人员，禁止入内")

is_employee = False  # False表示非本公司人员
if not is_employee:
    print("非公司人员，禁止入内，滚得远远地")

