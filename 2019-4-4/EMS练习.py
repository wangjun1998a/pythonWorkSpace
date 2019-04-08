# EMS 员工管理系统
flag = True
my_list = []
x = 0
# my_list.append(['ID', 'Name', 'Age', 'Sex', 'Address'])
# my_list.append(['孙悟空', '18', '男', '花果山'])
print('=' * 20, '欢迎使用员工管理系统', '=' * 20)
while flag:
    result = input('请选择要做的操作：\n \t'
                   '1、查询员工\n \t'
                   '2、添加员工\n \t'
                   '3、删除员工\n \t'
                   '4、退出系统\n'
                   '请选择（1-4）： ')
    # while flag:
    if (result == '1'):
        # 查询员工
        print('\t编号\t姓名\t年龄\t性别\t住址')
        while x < len(my_list):
            # for x in my_list:
            temp = f'\t{x + 1}\t'
            for value in my_list[x]:
                temp += str(value)
                temp += '\t'
            print(temp)
            x += 1
        x = 0
    elif (result == '2'):
        # 添加员工
        emp = []
        name = input('请输入名字：')
        age = input('请输入年龄：')
        sex = input('请输入性别：')
        address = input('请输入地址：')
        emp.extend([name, age, sex, address])
        my_list.append(emp)
    elif (result == '3'):
        # 删除员工
        user_input = int(input('请输入要删除的用户序号 : '))
        if 0 < user_input <= len(my_list) :
            del my_list[user_input - 1]
        else:
            print('输入有误')
    elif (result == '4'):
        flag = False
        print('成功退出系统!')
        break
    else:
        print('请输入正确的操作指令!')
        pass
    print('=' * 50)
