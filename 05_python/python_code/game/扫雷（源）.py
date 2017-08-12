# -*- coding: utf-8 -*-
#编程思想：
#形成一个00 01 02 03 04 05 06 07 08 09
#       10 11 12 13 14 15 16 17 18 19
#       20 21 22 23 24 25 26 27 28 29
#       .............................
#       80 81 82 83 84 85 86 87 88 89
#       90 91 92 93 94 95 96 97 98 99
#这样一个二维的列表，然后画一个8*8的方框图，对应于列表中的11~88,这样做的好处就在于
#在寻雷过程中不会对四个角与四个边作判断处理。

import e32
from appuifw import *
from key_codes import *
from graphics import *
import random

class Keyboard(object):
 #按键处理函数，抄自网上PYS60源码程序。
    def __init__(self):
        self.state = {}  
        self.buffer= {}  
    def handle_event(self, event): 
        code = event['scancode']
        if event['type'] == EEventKeyDown:
            self.buffer[code]= 1  
            self.state[code] = 1
        elif event['type'] == EEventKeyUp:
            self.state[code] = 0
    def pressing(self, code):     
        return self.state.get(code,0)
    def pressed(self, code):       
        if self.buffer.get(code,0):
            self.buffer[code] = 0  
            return 1
        return 0
    
def nei_rand(nei_n): 
#随机产生10个数，并将其存放在列表nei_num中
    i=0
    while i<nei_n:
        rand=random.randrange(0,63)
        if rand in nei_num:
            continue
        nei_num.append(rand)
        i=i+1

def nei_chick(neix,neiy):
#点击扫雷，递归扫描neix与neiy坐标的情况
    global running
    global z
    if nei[neix][neiy]==1:
#如果为1表示踩到雷则程序结束
        canvas.rectangle([(1,178), (22*8+22,178+22)], None, 0xef) 
        canvas.text((100,200),u"GAME OVER",fill=0xff00ee,font='normal')
    else:
        n=nei_check(neix,neiy)
        if n==0:
            nei_fan(neix,neiy)
        else:
            canvas.text((22*(neix-1)+8,22*(neiy-1)+20),u""+str(n)+"",fill=0xff00ee,font='normal')
                        
def nei_checkx(neix,neiy): 
#检查周围雷个数
    numbers=0
    for i in range(neix-1,neix+2):
        for j in range(neiy-1,neiy+2):
            if i!=neix or j!=neiy: 
#此过程写的时候，这句中的"or"我开始写成的"and",让我郁闷了半天。幸得群589626里的"哎呀我忘了"指点
                if nei[i][j]==1:
                    numbers=numbers+1
    return numbers #返回雷数

def nei_check(x,y): #检查周围雷个数。参考了一VB代码后，觉得他的算法更直观，好理解。所以改了一下。
    counts=0
    for i in range(-1,2):
        for j in range(-1,2):
            if nei[x+i][y+j]==1:
                counts=counts+1
    return counts

def nei_fan(neix,neiy):
    for i in range(-1,2):
        for j in range(-1,2):
            if j*i==0 and nei[neix+i][neiy+j]==0:
                nei[neix+i][neiy+j]=-2
                n=nei_check(neix+i,neiy+j)
                #canvas.rectangle([(22*(neix+i-1)+2, 22*(neiy+j-1)+2), (22*(neix+i-1)+20, 22*(neix+j-1)+20)], None, 0xffffff)
                canvas.text((22*(neix+i-1)+8,22*(neiy+j-1)+20),u""+str(n)+"",fill=0xffffff,font='normal')
                if n!=0:
                    canvas.text((22*(neix+i-1)+8,22*(neiy+j-1)+20),u""+str(n)+"",fill=0xff00ee,font='normal')
                else:
                    if n==0:
                        nei_fan(neix+i,neiy+j)

def quit():
    global running
    running = 0
def clear_box(color=0xffffff):#显示坐标的方格
    global x,y
    canvas.rectangle([(22*x, 22*y), (22*x+23, 22*y+23)], color)


#程序开始
app.screen='full'
app.body=None
nei_number=kill_nei_num=query('雷数目'.decode('utf-8'),'number')
key = Keyboard()
app.body = canvas = Canvas(event_callback=key.handle_event)
nei_num=[]#雷列表
nei=[]#定义一个列表，以便后面存放游戏中雷的排列。如其他语言中的二维数组,Python中可以用append对其增量。
app.exit_key_handler = quit
running = 1
if nei_number==None or nei_number>30:
    nei_number=10#雷数目
    kill_nei_num=nei_number
nei_rand(nei_number)#初始化雷列表
z=""
k=0
for j in range(10):   #初始化扫雷界面(画8*8个方格),并初始化排雷列表,（实际上是要画10*10个方格，主要是存放列表中10*10，
    #省掉后面判断其八个方向情况时的麻烦,这样不管怎么样都不会产生四角与四边的判断了。）
    nei.append([])
    for i in range(10):
        if j<9 and i<9:#这句是少画一行方框界面。因为我的手机是176*208的。多画出的列在手机屏幕不可见的地方，所以不作判断
                #如果你的手机屏幕大于176*208,可以写成 if j<9 and i<9:来测试，由于我没法测试。故保留此处
            canvas.rectangle([(22*(i-1)+1, 22*(j-1)+1), (22*(i-1)+22, 22*(j-1)+22)], None, 0x000000)
        if j>0 and i>0 and j<9 and i<9:
            if k in nei_num:#如果递增量K在nei_num列表中，就将当前nei列表设为1,反之为0
                nei[j].append(1)
            else:
                nei[j].append(0)
        else:
            nei[j].append(-1)#如果在游戏界面范围外的列表。递增量K保持不变。这样就保证所有的雷都会分布在游戏界面列表内。
            k=k-1
        k=k+1
canvas.rectangle([(1,178), (22*8+22,178+22)], None, 0xef)
x, y = 0, 0
black_white = 0
while running:
    if key.pressed(EScancodeLeftArrow):#左键
        clear_box()
        if x > 0: x -= 1
        else: x=7
    if key.pressed(EScancodeRightArrow):#右键
        clear_box()
        if x < 7: x += 1
        else: x=0
    if key.pressed(EScancodeUpArrow):#上键
        clear_box()
        if y > 0: y -= 1
        else:y=7
    if key.pressed(EScancodeDownArrow):#下键
        clear_box()
        if y < 7: y += 1
        else:y=0
    if key.pressed(EScancodeSelect):#选择键
        nei_chick(x+1,y+1)
    if key.pressed(EScancodeLeftSoftkey):#左功能键为标雷
        canvas.text((22*(x)+4,22*(y)+18),u''+"★".decode('utf-8')+'',fill=0xffffff,font='normal')
        if nei[x+1][y+1]==1:#如果猜对了的话。
            nei_number-=1
        kill_nei_num-=1 #用户标志出的雷
    if nei_number==0:
        canvas.rectangle([(1,178), (22*8+22,178+22)], None, 0xef) 
        canvas.text((120,200),u"WINER",fill=0xff00ee,font='normal')
    canvas.rectangle([(1,178), (100,178+22)], None, 0xef) 
    canvas.text((2,200),u'X'+str(x)+'Y'+str(y)+' mine:'+str(kill_nei_num)+'',fill=0xff00ee,font='normal')
    black_white ^= 0xffffff 
    clear_box(black_white)#让坐标方框背影色，令其闪烁
    e32.ao_sleep(0.2)
