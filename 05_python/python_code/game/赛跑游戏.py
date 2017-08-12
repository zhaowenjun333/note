import appuifw,e32,key_codes
import random
from graphics import *
def ch(x):return x.decode('utf8')
def exit():
    global run
    run=0
    e32.Ao_lock().signal()
appuifw.app.exit_key_handler=exit
zi=u'CombinedChinesePlain12'
s0=s1=s2=s3=0
choose=0
num=0
start=0
reach=0
win=0
win1=0
win2=0
win3=0
win4=0
fail=0.000001
fail1=0.000001
fail2=0.000001
fail3=0.000001
fail4=0.000001
winper=0
winper1=0
winper2=0
winper3=0
winper4=0
all=0
color=[0xff0000,0xff00ff,0xee33aa,0x00ff00]
def main(rect):
    global s,color,choose,num,start,s0,s1,s2,s3,reach,win,fail,winper,win1,win2,win3,win4,fail1,fail2,fail3,fail4,winper1,winper2,winper3,winper4,all
    img.clear(0xffffff)
    img.text((5,20),ch('战绩: ')+ch('胜:')+str(win)+u' '+ch('败:')+str(int(fail)),0,zi)
    winper=round((win*100)/(win+fail))
    img.text((105,20),ch('胜率: ')+str(winper)+u'%',0,zi)
    img.text((105,40),ch('局数: ')+str(all),0,zi)
    if start==1:
        s0+=random.random()
        s1+=random.random()
        s2+=random.random()
        s3+=random.random()
        if s0>=150.00 or s1>=150.00 or s2>=150.00 or s3>=150.00 :
            all+=1
            if s0>=150.00:
                reach=1
                win1+=1
                fail2+=1
                fail3+=1
                fail4+=1
            elif s1>=150.00:
                reach=2
                fail1+=1
                win2+=1
                fail3+=1
                fail4+=1
            elif s2>=150.00:
                reach=3
                fail1+=1
                fail2+=1
                win3+=1
                fail4+=1
            elif s3>=150.00:
                reach=4
                fail1+=1
                fail2+=1
                fail3+=1
                win4+=1
            if reach==num:
                win+=1
                choose=2
            else:
                fail+=1
                choose=3
            start=0
    if choose==0:
        img.text((18,140),ch('请按1-4的任意键开始游戏'),0,zi)
    elif choose==1:
        img.text((5,40),ch('你选择的是')+str(num)+ch('号'),0,zi)
    elif choose==2:
        img.text((5,40),ch('你选择的是')+str(num)+ch('号'),0,zi)
        img.text((48,80),str(reach)+ch('号到达了'),0,zi)
        img.text((50,100),ch('你胜利了'),0,zi)
        img.text((40,120),ch('请按0键返回'),0,zi)
    elif choose==3:
        img.text((5,40),ch('你选择的是')+str(num)+ch('号'),0,zi)
        img.text((45,80),str(reach)+ch('号先到达'),0,zi)
        img.text((50,100),ch('你失败了'),0,zi)
        img.text((40,120),ch('请按0键返回'),0,zi)
    img.ellipse((2+s0,54,14+s0,66),fill=color[0])
    img.ellipse((2+s1,74,14+s1,86),fill=color[1])
    img.ellipse((2+s2,94,14+s2,106),fill=color[2])
    img.ellipse((2+s3,114,14+s3,126),fill=color[3])
    for i in range(4):
        img.line((0,65+20*i,176,65+20*i),0,width=2)
        img.text((4,65+20*i),str(i+1)+u'',0)
        img.polygon((166,50+20*i,166,58+20*i,174,60+20*i),0,fill=0xff0000)
        img.line((166,50+20*i,166,65+20*i),0)
    for j in range(2):
        img.line((13+150*j,50,13+150*j,138),0,width=1)
    img.text((5,160),ch('1号: ')+ch('胜: ')+str(win1)+ch(' 败: ')+str(int(fail1)),0,zi)
    winper1=round((win1*100)/(win1+fail1))
    img.text((105,160),ch('胜率: ')+str(winper1)+u'%',0,zi)
    img.text((5,175),ch('2号 :')+ch('胜: ')+str(win2)+ch(' 败: ')+str(int(fail2)),0,zi)
    winper2=round((win2*100)/(win2+fail2))
    img.text((105,175),ch('胜率: ')+str(winper2)+u'%',0,zi)
    img.text((5,190),ch('3号: ')+ch('胜: ')+str(win3)+ch(' 败: ')+str(int(fail3)),0,zi)
    winper3=round((win3*100)/(win3+fail3))
    img.text((105,190),ch('胜率: ')+str(winper3)+u'%',0,zi)
    img.text((5,205),ch('4号: ')+ch('胜: ')+str(win4)+ch(' 败: ')+str(int(fail4)),0,zi)
    winper4=round((win4*100)/(win4+fail4))
    img.text((105,205),ch('胜率: ')+str(winper4)+u'%',0,zi)
    can.blit(img)
def keys(event):
    global choose,num,start,s0,s1,s2,s3
    en=event['keycode']
    if en==key_codes.EKey0:
        if start==0:
            choose=0
            s0=s1=s2=s3=0
    if en==key_codes.EKey1:
        if choose==0:
            num=1
            choose=1
            start=1
    if en==key_codes.EKey2:
        if choose==0:
            num=2
            choose=1
            start=1
    if en==key_codes.EKey3:
        if choose==0:
            num=3
            choose=1
            start=1
    if en==key_codes.EKey4:
        if choose==0:
            num=4
            choose=1
            start=1
    if en==key_codes.EKey5:
        pass
    if en==key_codes.EKey6:
        pass
    if en==key_codes.EKey7:
        pass
    if en==key_codes.EKey8:
        pass
    if en==key_codes.EKey9:
        pass
appuifw.app.screen='full'
can=appuifw.Canvas(event_callback=keys)
appuifw.app.body=can
w,h=can.size
img=Image.new((w,h))
appuifw.app.menu=[]
run=1
while run:
    main(())
    e32.ao_yield()