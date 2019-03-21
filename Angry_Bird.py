import numpy as np
import matplotlib.pyplot as plt
import math
#from matplotlib import animation
from colorama import  init, Fore, Back, Style
init(autoreset=True)
class Colored(object):
    def red(self, s):
        return Fore.RED + s + Fore.RESET
color = Colored()

g = 9.8
zt = 0                                        #状态标识符
pig_location = np.random.random(2,)
print(pig_location)

plt.figure()                                  #创建窗口
#plt.style.use('dark_background')
plt.plot(100*pig_location[0],50*pig_location[1],'o',color = 'g')
plt.axis([0,100,0,70])
plt.show()

n = int(input('Bullets per one shot: '))
while zt == 0:
    v = float(input('Initial Velocity: '))
    theta = float(input('Angle:'))

    r_the = np.radians(theta)                      #角度转弧度
    for i in range(0,n):
        x = np.arange(0,100,0.01)
        y = ((v**2)*math.sin(2*(r_the + i*math.pi/96*(-1)**i))*x-g*x**2)/(2*(v*math.cos(r_the + i*math.pi/96*(-1)**i))**2) #霰弹

        
        disx = x-100.*pig_location[0]
        disy = y-50.*pig_location[1]
        dist =np.sqrt(disx**2 + disy**2)

        cpd = min(dist)           #critical point
        print('The Min distance:',cpd)
    
        if min(dist) <=2:                 #猪的大小
            zt = 1
            print(color.red('命中!'))
            plt.plot([100*pig_location[0],x[np.where(dist == min(dist))]],[50*pig_location[1],y[np.where(dist == min(dist))]],':')#辅助线
            plt.plot(x,y,c = 'r')         #弹道
        else:
            plt.plot([100*pig_location[0],x[np.where(dist == min(dist))]],[50*pig_location[1],y[np.where(dist == min(dist))]],':')#辅助线
            plt.plot(x,y,c = 'y')         #弹道
 
        plt.plot(100*pig_location[0],50*pig_location[1],'o',color = 'g')                #猪的位置
    plt.axis([0,100,0,70])
    plt.show()


