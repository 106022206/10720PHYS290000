import numpy as np
import matplotlib.pyplot as plt

m = int(input('每人初始金额/Initial amount: '))      #初始金额
n = int(input('学生人数/How many students: '))       #学生数量
k = int(input('回合数/Round: '))                     #回合
dm = 1      #赌钱金额
no_money_mode = int(input('是否开启可负债模式？(输入1开启)/Open no money mode? (enter 1 to open) ')) #是否开启负债模式
if no_money_mode == 1:
    print('负债模式开启 "No money" mode activated')
money_array = []

for i in range(0,n):
    money_array.append(m)

for i in range(0,k):
    snum = n
    for j in range(0,len(money_array)):
        
        if money_array[j] <= 0:
            snum -= 1                  #还没破产的人数
    
    
    result = np.random.randint(0,3) #猜猜拳
    
    if no_money_mode == 1:
        people1_in_game = np.random.randint(0,n) #挑第一个人
    
        people2_in_game = np.random.randint(0,n) #挑第二个人
        
        while people2_in_game == people1_in_game:
            people2_in_game = np.random.randint(0,n) #重挑第二个人
    else:
        money_array = sorted(money_array,reverse = True)    #大到小排序
        
        people1_in_game = np.random.randint(0,snum) #挑第一个人
    
        people2_in_game = np.random.randint(0,snum) #挑第二个人
    
        while people2_in_game == people1_in_game and snum > 1:
            people2_in_game = np.random.randint(0,snum) #重挑第二个人
    
        if snum == 1:       #只剩一人，停止游戏
            print('！！终极富豪诞生，游戏结束！！')
            break
    
    if result == 1:
        money_win = dm + money_array[people1_in_game]
        money_lose = money_array[people2_in_game] - dm
        
        money_array[people1_in_game]= money_win
        money_array[people2_in_game]= money_lose
        
    elif result == 2:
        money_win = dm + money_array[people2_in_game]
        money_lose = money_array[people1_in_game] - dm
        money_array[people2_in_game] = money_win
        money_array[people1_in_game] = money_lose
    
money_array = sorted(money_array,reverse = True) 
print(money_array)
plt.hist(money_array)
plt.show()