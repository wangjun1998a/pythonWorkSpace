# 使用input函数
# 在命令行输入一个用户名 获取用户的输入 进行判断
# 如果用户输入了admin 输出欢迎语句
# 不是admin就不用欢迎了
a = input("please input a name : ");

if a == "admin":
    print("welcome ! costomer!")
else:
    print("sorry no welcome service.")
