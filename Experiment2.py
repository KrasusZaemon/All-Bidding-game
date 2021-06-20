from Algorithm import Unifom
from sys import argv
import tkinter as tk

import tkinter.messagebox
import random
from tkinter.constants import NO
from tkinter import Canvas, Scale, ttk
from Algorithm import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlwt

def play(p1,p2,budge1, budge2):
    pp1=0
    pp2=0
    while(True):
        place1 = Random(budge1,0)
        place2 = Random(budge2,p2-pp2)
        budge1-=place1
        budge2-=place2
        if(place1>=place2):
            pp1+=1
        else:
            pp2+=1
        if(pp1==p1):
            return True
        if(pp2==p2):
            return False
    
    return 
#  2 1 0~4000 1000
def play2(p1,p2,budge1, budge2):
    #print("start")
    #print(str(budge1)+"  "+str(budge2))
    player1_win=0
    player2_win=0
    if(budge1==0):
        return 0,budge2
    for i in range(budge1):
        #print("i"+i)
        for j in range(budge2):
            #print("j"+j)
            if(i==j):
                pass
            bb1 =budge1-i
            bb2 =budge2-j
            pp1=p1
            pp2=p2
            if(i>=j):
                pp1-=1
            else:
                pp2-=1
            if(pp1==0):
                player1_win+=1
            elif(pp2==0):
                player2_win+=1
            else:
                #print(111)
                a,b = play2(pp1,pp2,bb1,bb2)
                
                player1_win+=a
                player2_win+=b
    return player1_win,player2_win

            

epsilo = 1
#Round_player1_to_win=[1,2,2]
#Round_player2_to_win=[2,1,2]

aaa = [0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]

Round_player1_to_win=[1,3,2,3,3]
Round_player2_to_win=[3,1,3,2,3]

#Round_player1_to_win=[1,2,3,4,4,4,4]
#Round_player2_to_win=[4,4,4,4,3,2,1]


budge_player2 = 1000
"""
for i in range(len(Round_player1_to_win)):
    x=[]
    y=[]
    for j in aaa:
        #if(j%100==0):
        #    print(str(i)+" "+str(j))
        win=0
        round=10000
        for k in range(round):
            if(play(Round_player1_to_win[i],Round_player2_to_win[i],j,budge_player2)):
                win+=1
        x.append(j/budge_player2)
        y.append(win/round)
    plt.plot(x, y)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
"""

x=[]
y=[]
for i in range(1,200):
    print(i)
    a,b = play2(3,1,i,50)
    x.append(i/100)
    y.append(a/(a+b))

plt.plot(x, y)
plt.xlabel('Ratio')
plt.ylabel('Probability')
plt.savefig("11.png")
plt.show()

plt.scatter(x,y)
plt.xlabel('Ratio')
plt.ylabel('Probability')
plt.savefig("22.png")
plt.show()
"""
A = np.array([[1, 2], [3, 2], [1, 1], [3, 5], [5,2]])
data = pd.DataFrame(A)

writer = pd.ExcelWriter('A.xlsx')		# 写入Excel文件
data.to_excel(writer, 'page_1', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
writer.save()

writer.close()
"""
def saveMatrix2Excel(data, path):
    f = xlwt.Workbook()  # 创建工作簿
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    #[h, l] = data.size  # h为行数，l为列数
    l=len(data)
    h=len(data[0])
    for i in range(h):
        for j in range(l):
            sheet1.write(i, j, data[j][i])
    f.save(path)

W =[x,y]
pathW = "3_1.xls"   # 保存在当前文件夹下，你也可以指定绝对路径
saveMatrix2Excel(W,pathW)