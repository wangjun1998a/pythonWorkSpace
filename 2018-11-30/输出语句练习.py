# 输出下面的语句
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
# 方法1
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
# 方法2
print()
# 想用一个输出并且换行 可以使用sep'\n'来进行换行
print(n , f , s1 , s2 , s3 , s4 , sep='\n')
