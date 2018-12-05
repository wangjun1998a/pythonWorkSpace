# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。
# 提示：计算平方根可以调用math.sqrt()函数：

from math import pow, sqrt


def quadratic(a, b, c):
    for item in [a, b, c]:
        if not isinstance(item, (int, float)):
            raise TypeError('bad operand type')

    result = pow(b, 2) - 4 * a * c

    if result < 0:
        print('方程无解')
        return
    elif result > 0:
        x1 = (-b + sqrt(result)) / (2 * a)
        x2 = (-b - sqrt(result)) / (2 * a)
        return x1, x2
    else:
        return -b / (2 * a)

    # 测试:


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
