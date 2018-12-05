# 所谓的函数可以返回多个值的问题 其实python返回的是一个tuple
# 在有多个变量同时接收参数的时候 可以按照位置
# 一一赋值 但当只有一个变量去接收参数的时候 会明显的看出是一个tuple
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)

print(x, y, r, sep='\n')
