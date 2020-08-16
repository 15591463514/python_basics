"""
打印如下图形：
    *
    **
    ***
    ****
    *****
"""
# ①使用嵌套循环

# 定义行变量
i = 1

while i <= 5:

    # 定义列变量
    j = 1

    while j <= i :

        print("*", end="")

        j += 1

    print("")

    i += 1




# ②使用循环&乘法

i = 1

while i <= 5:

    print("*" * i)

    i += 1
# end 的用法
print("(*", end = "_" )
print("*)")
