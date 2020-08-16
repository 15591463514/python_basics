hello_str1 = "hello world"

# 判断是否以指定字符串开始
print(hello_str1.startswith("hello"))  # True

# 判断是否以指定字符串结束
print(hello_str1.endswith("world"))  # True

# 查找指定的字符串
print(hello_str1.find("llo"))  # 2

# 替换字符串
print(hello_str1.replace("world", "python"))  # hello python
print(hello_str1)  # hello world
# ##### 注意：replace（）方法不会修改原字符串，会返回一个新的字符串

# 切片
str = "0123456789"
print(str[1:2])  # 1
print(str[:5])  # 01234
print(str[-2:])  # 89
print(str[::2])  # 02468
