name = "小明"
age = 18
gender = "男"
# 使用+进行拼串，不过python中的+不会进行强制类型转换 在js中可以直接拼串 在这里需要先转化数据类型再拼串
print("我是" + name + "，今年" + str(age) + "岁，是一个" + gender + "孩子")
# 格式化输出，类似c语言中的语法
print("我是%s" % name)  # %s表示字符串
print("我是%s，今年%d岁，是一个%s孩子" % (name,age,gender))  # 多个变量要加括号
student_num = 255
print("学号是%06d" % student_num)  # %06d表示一共输出6位整数 不足的地方用0补全
price = 19.98
print("价钱为%.6f" % price)  # %.6f表示小数点后保留6位
bili = 0.2512496587
print("数据比例是%0.2f%%" % bili*3)  # %%表示%  不加括号表示输出三次
print("数据比例是%0.2f%%" % (bili*100))  # 加括号表示值乘以100
print("得奖的概率为12.28%")  # 注意：这里不需要写两个%
print("我是%s，今年%d岁，是一个%s孩子" % (name*3,age,gender)*2)  # 注意*的用法
