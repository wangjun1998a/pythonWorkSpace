# if_elif_else练习

# (1)编写一个程序 检查任意一个年份是不是为闰年
# 一个年份可以被4整除 但是不能被100整除 或者这个年份可以被400整除 就是闰年

# year = input("please input a year : ")
# year = int(year)
#
# if year % 4 == 0 and year % 100 != 0:
#     print("闰年")
# elif year % 400 == 0:
#     print("闰年")
# else:
#     print("非闰年")


# (2)我家狗五岁了 5岁的狗等于多大年龄的人？
#         计算公式是 前两年每一年都等于人的10.5岁 然后每增加一年都相当于人的4岁
# 所以五岁的狗等于 10.5+10.5+4+4+4 = 33岁

# humanYear = 0
# dogsYear = int(input("Please input dog year : "))
# if dogsYear < 0:
#     print("error!")
# else:
#     while dogsYear > 0:
#         if dogsYear > 2:
#             humanYear += 4
#             dogsYear -= 1
#         else:
#             humanYear += 10.5
#             dogsYear -= 1
#     print(humanYear)

# (3)键盘输入小明的期末成绩
# 需求直接写在代码里 太多了懒得敲 看不懂是人才
# personGrade = int(input("input this student grades : "))
#
# if personGrade == 100:
#     print("give a car ")
# elif personGrade >= 80:
#     print("give a IPhone")
# elif personGrade >= 60:
#     print("give a book ")
# else:
#     print("give nothing")

# (4) 男大当婚女大当嫁 女方家长要嫁女儿 提出了一些条件
height = float(input("Input human height : "))
money = float(input("Input human money : "))
sex = float(input("Input human sex : "))
if height  > 180 and money > 1000 and sex > 500 :
    print("must merry he")
elif height > 180 or money > 1000 or sex > 500:
    print("just merry it ")
else:
    print("won't merry he!")
