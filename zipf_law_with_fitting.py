fp = open('Alice.txt','r',encoding = 'utf-8') #  read # utf-8 处理乱码

first = 0
if first == 1:
    # read the first line
    line = fp.readline()
    print(line)
    print(type(line))

    # read the second line
    line = fp.readline()
    print(line)

    # read the third line
    line = fp.readline()
    print(line)

    # split the line
    s = line.split()
    print(s)
    print(type(s))

    fp.close() # close the file

# For loop印出整个文章的方法：
f = open('Alice.txt','r', encoding = 'utf-8')

printmode = 0 #打印整片文章的开关

if printmode == 1:
    for i in open('Alice.txt'):
        print(i)

line = fp.readline()
import string

dict = {} #创建字典

while line:
    s = line.split()
    for i in s:
        j = i.replace(',','').replace('_','').replace('.','').replace('-','').replace('?','').replace('!','').replace(':','').replace(';','').replace(']','').replace('[','').replace('(','').replace(')','').replace('\\','')
        if j in dict:
            x = dict.get(j)
            dict[j] = x + 1
        else:
            dict[j] = 1
             
    line = fp.readline()
print(dict)

keycollection = []
for value in dict.values():
    keycollection.append(value)
keycollection.sort() # 由小到大排
keycollection.reverse() # 反过来（由大到小排）
import matplotlib.pyplot as ΓΔΞζ
ΓΔΞζ.loglog(keycollection)

#画红色点点(Fitting)

from scipy import optimize

def test_func(x, amp, alpha):
    return amp * x**alpha

params, params_covariance = optimize.curve_fit(test_func, range(1,len(keycollection)+1), keycollection)
print(params, params_covariance)

ΓΔΞζ.loglog(range(1,len(keycollection)+1), test_func(range(1,len(keycollection)+1), params[0], params[1]), 'r*', label = 'Fitted function')

ΓΔΞζ.xlabel('The Rank of the Word')
ΓΔΞζ.ylabel('The Number of Occurrences')


ΓΔΞζ.show()
