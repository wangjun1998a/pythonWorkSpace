# 练习1 100以内所有的奇数的和
# i = 0
# sumNumber = 0
# while i < 100:
#     if i % 2 != 0:
#         print(i)
#         sumNumber = sumNumber + i
#     i = i + 1
# print("SUM : ", sumNumber)

# 练习2 100以内所有的7的倍数 以及个数
# i = 0
# count = 0
# while i < 100:
#     if i % 7 == 0 and i != 0:
#         print(i)
#         count += 1
#     i += 1
# print("COUNT : ", count)

# 练习3 水仙花数z
# i = 100
# WHILE I < 1000:
#     if i >= 100:
#         length = len(str(i))
#         a = int(i / 100)
#         b = int(i % 100 / 10)
#         c = i % 100 % 10
#         if (a ** length + b ** length + c ** length) == i:
#             print(i)
#     i += 1

# 练习4 获取用户输入的数 判断是不是质数
number = int(input("Please input a number : "))
i = 2
flag = True
while i < number:
    b = number % i
    if b == 0:
        flag = False
    else:
        pass
    i += 1
if flag:
    print("是质数")
else:
    print("不是质数")
