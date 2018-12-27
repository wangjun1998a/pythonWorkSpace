# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if L is None or L == []:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
    for x in L:
        if min == 0 and max == 0:
            min = x
            max = x
        if x > max:
            max = x
        if x < min:
            min = x
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
