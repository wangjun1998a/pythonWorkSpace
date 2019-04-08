emps = []
emps.append([1, 1, 1, 1 ,1])
emps.append([2, 1, 1, 2])

print(emps)
print(len(emps))
print(emps[1])

for x in emps:
    result = '\t'
    for y in x:
        result += str(y)
        result += '\t'
    print(result)
    print(' ')
