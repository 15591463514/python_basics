# break 结束本次循环

i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

# continue 可以跳过本次循环

j = 1
while j <= 5:
    if j == 3:
        # 为了不使j ==3 使成为死循环，在continue前给j加1
        j += 1
        continue
    print(j)
    j += 1
