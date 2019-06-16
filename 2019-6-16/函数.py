# 定义一个函数，可以求任意两个数的和。
def sumNumber(a, b):
    print("SUM : ", a + b)


sumNumber(1, 8)


# 定义一个函数 求 三个数的乘积
def cheng(a, b, c):
    if isinstance(a, int) & isinstance(b, int) & isinstance(c, int):
        result = a * b * c
        print("乘积为 ： ", result)
    else:
        print("Error input type")


cheng(1, 2, 3)
cheng(2, 5, 3)
cheng(1, 2, '3')


# 根据不同的用户名显示不一样的欢迎信息
def welcome(loginName):
    print("欢迎", loginName, "登陆系统！")

welcome("小花")
welcome("崽崽")
