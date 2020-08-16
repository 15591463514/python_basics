"""列表的方法"""

name_list = ['zhangsan', 'lisi', 'wangwu', 'xiaoming', 'lisi']
ming_list = ['shiqisheng', 'shihang']

# 取
print("取索引为2处的值：", name_list[2])  # 根据索引取值
print("取“小明”索引：", name_list.index('xiaoming'))  # 根据值取索引：index（）

# 改
name_list[2] = 'lele'
print("修改元素后：", name_list)

# 增
name_list.append('huahua')  # 向列表的末尾添加‘一个’元素：append（）
name_list.insert(1, 'xiaomeimei')  # 向列表的指定索引‘前’添加‘一个’元素：insert（）
name_list.extend(ming_list)  # 向列表的末尾添加另一个序列中的多个值：exten（）
print("增加元素后：", name_list)

# 删
name_list.remove('shiqisheng')  # 删除列表中的指定元素：remove（）
name_list.pop(1)  # 删除列表中指定位置的元素：pop（）
name_list.pop()  # 不写索引，默认删除最后一个元素
del name_list[0]  # 删除指定位置的元素：del关键字（一般不用）
# name_list.clear()  # 清空列表：clear（）
print("删除元素后：", name_list)

# 统计
print("列表长度为", len(name_list))  # 统计列表中的元素的个数：len(list)函数
print("lisi出现了%d次" % name_list.count('lisi'))  # 统计某个元素在列表中共出现过几次：count（）

# 排序
age_list = [13, 24, 9, 34, 10]
print("原列表为：", age_list)
age_list.reverse()  # 对列表进行逆序排列：reverse（）
print("逆序后：", age_list)
age_list.sort()  # 对列表进行升序排列：sort（）
print("升序后：", age_list)
age_list.sort(reverse=True)  # 对列表进行降序排列：sort（reverse=True）
print("降序后：", age_list)





