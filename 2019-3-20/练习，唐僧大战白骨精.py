# 身份选择
# 欢迎信息  欢迎   XXX  进入游戏！
#                     请选择身份 ：
# 1 ：
# 2 ：

playerName = "唐僧"
bossName = "白骨精"
print(f"欢迎光临 《{playerName}大战{bossName}》 游戏 ！")
a = input(f"请选择你的身份：  \n 1 : {playerName} \n 2 : {bossName} \n 请选择 ： ")
# print(a)
# 根据用户选择身份来分配身份（显示不同的信息）
if a == '1':
    print(f"当前已选择用户 --> {playerName} <-- ")
elif a == '2':
    print(f"无法选择用户-- > {bossName} <-- 系统自动分配角色为 --> {playerName} <-- ")
else:
    print(f"无效的输入 ！ 系统自动分配角色为 --> {playerName} <--")

# 游戏进行操作 ：
# 显示玩家信息 ：
attack = 2
hp = 2
emeryAttack = 8
emeryHp = 8
print(f"当前角色为 ： --> {playerName} <-- 攻击力 ：", attack, " 生命值 ：  ", hp)
# 显示可以进行的操作
while True:
    do = input(f"选择你需要进行的操作 : \n 1 : 练级\n 2 : 打{bossName} \n 3 : 逃跑 \n 选择你需要进行的操作 ： ")
    print(" ")
    if do == '1':
        attack += 2
        hp += 2
        print(f"当前角色为 ： --> {playerName} <-- 攻击力 ：", attack, " 生命值 ：  ", hp)
        print(" ")
    elif do == '2':
        emeryHp = emeryHp - attack
        print(f"攻击{bossName}!   对{bossName}造成伤害 : ", attack, f"  {bossName}剩余生命值为 : ", emeryHp)
        print(" ")
        if emeryHp > 0:
            hp = hp - emeryAttack
            print(f"{bossName}反击!   对{playerName}造成伤害 : ", emeryAttack, f"  {playerName}剩余生命值为 : ", hp)
            print(" ")
            if hp <= 0:
                print("游戏失败！你输了！")
                print(" ")
                break
        else:
            print(f"胜利！{bossName}被击败了！")
            print(" ")
            break
    elif do == '3':
        print("退出游戏！ 游戏结束！")
        print(" ")
        break
    else:
        print("输入有误 ！请重新输入！")
        print(" ")
