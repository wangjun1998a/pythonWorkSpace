# # 九九乘法表
# i = 1;
# while i < 10:
#     j = 1
#     while j <= i:
#         print(j, " * ", i, " = ", i * j, '  ', end=' ')
#         j += 1
#     print()
#     i += 1

# 100以内所有的质数
i = 2
while i <= 100:
    j = 2
    flag = False
    while j <= i:
        if (i % j == 0 and i != j):
            flag = False
            break
        else:
            flag = True
        j += 1
    if flag == True:
        print(i)
    i += 1
