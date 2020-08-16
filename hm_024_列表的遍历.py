phone_number = [110, 119, 120, 114, 10086, 12580, 10010]

# 使用while循环遍历列表
i = 0

while i< len(phone_number):

    print(phone_number[i])

    i += 1

# 使用for进行迭代遍历
for x in phone_number:

    print(x,phone_number.index(x))