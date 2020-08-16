"""使用函数嵌套，打印多行分隔符"""


def print_line(sign, count):
    """
    打印一行分割符
    :param sign: 符号
    :param count: 一行符号的个数
    """
    print(sign * count)


print_line("—— ", 10)


def print_lines(sign, count, lines):
    """
    打印多行分割符
    :param sign: 符号
    :param count: 一行符号的个数
    :param lines: 打印多少行
    """
    row = 0
    while row < lines:
        print_line(sign, count)
        row += 1


print_lines("-", 50, 3)



