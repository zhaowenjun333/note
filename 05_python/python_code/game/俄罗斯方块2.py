from random import randint
import appuifw
import e32
import graphics

appuifw.app.screen='full'

img=graphics.Image.new((240,320))
img.clear(0xa0ff)
body=[(x+10,y+70) for y in range(0,240,12) for x in range(0,120,12)]+[(0,0)]*40
Body=[]
x=4
y=0
game=1
Piece=randint(1,19)
Piece1=randint(1,19)
Piece2=randint(1,19)
FRACTION=0
EVENT={}

for xx in body: b,c=xx[0],xx[1];img.rectangle((b,c,b+13,c+13),0xff,fill=0xa0ff)

def cn(x): return x.decode('utf-8')

img.text((145,88),u'%s' %(cn('俄罗斯方块')),0xff,u'')
img.text((140,108),u'%s' %(cn('御风学习制作')),0xff,u'')
img.text((145,128),u'%s' %(cn('QQ:669805604')),0xff,u'')

def decide(a,b,c):
    aa=piece1(a,c)
    bb=b<20
    a=piece2(a,b,c,0,0,0)
    cc=Body.count(a[0]) or Body.count(a[1]) or Body.count(a[2]) or Body.count(a[3])
    cc=cc is 0
    return aa and bb and cc

def piece(c): return {1: ((0, 0), (0, -1), (1, -1), (1, 0)), 2: ((0, 0), (-1, 0), (2, 0), (1, 0)), 3: ((0, 0), (0, -1), (0, -2), (0, -3)), 4: ((0, -1), (0, -2), (1, -1), (1, 0)), 5: ((-1, 0), (0, 0), (0, -1), (1, -1)), 6: ((0, 0), (0, -1), (1, -1), (1, -2)), 7: ((-1, -1), (0, -1), (0, 0), (1, 0)), 8: ((0, -2), (1, -2), (1, -1), (1, 0)), 9: ((-1, 0), (0, 0), (1, 0), (1, -1)), 10: ((0, 0), (0, -1), (0, -2), (1, 0)), 11: ((-1, -1), (-1, 0), (0, -1), (1, -1)), 12: ((0, 0), (0, -1), (0, -2), (1, -2)), 13: ((-1, -1), (0, -1), (1, -1), (1, 0)), 14: ((0, 0), (1, 0), (1, -1), (1, -2)), 15: ((-1, -1), (-1, 0), (0, 0), (1, 0)), 16: ((-1, 0), (0, 0), (0, -1), (1, 0)), 17: ((0, 0), (0, -1), (0, -2), (1, -1)), 18: ((-1, -1), (0, -1), (0, 0), (1, -1)), 19: ((0, -1), (1, 0), (1, -1), (1, -2))}[c]

def piece1(a,b): return {1:0<=a<=8,2:1<=a<=7,3:0<=a<=9,4:0<=a<=8,5:1<=a<=8,6:0<=a<=8,7:1<=a<=8,8:0<=a<=8,9:1<=a<=8,10:0<=a<=8,11:1<=a<=8,12:0<=a<=8,13:1<=a<=8,14:0<=a<=8,15:1<=a<=8,16:1<=a<=8,17:0<=a<=8,18:1<=a<=8,19:0<=a<=8}[b]

def piece2(a,b,c,d=0xff,e=0x0,f=1):
    aa=piece(c)
    aa=[aa[0][0]+(aa[0][1]+b)*10+a,aa[1][0]+(aa[1][1]+b)*10+a,aa[2][0]+(aa[2][1]+b)*10+a,aa[3][0]+(aa[3][1]+b)*10+a]
    for xx in aa:
        if f: draw(xx,d,e)
    return aa

def draw(a,b,c):
    global img
    xx=body[a]
    xx,yy=xx[0],xx[1]
    img.rectangle((xx,yy,xx+13,yy+13),b,fill=c)

def treat():
    global Body,img
    BODY=[[]]*20
    for a in Body:
        if 0<=a<=9: BODY[0]=BODY[0]+[a]
        if 10<=a<=19: BODY[1]=BODY[1]+[a]
        if 20<=a<=29: BODY[2]=BODY[2]+[a]
        if 30<=a<=39: BODY[3]=BODY[3]+[a]
        if 40<=a<=49: BODY[4]=BODY[4]+[a]
        if 50<=a<=59: BODY[5]=BODY[5]+[a]
        if 60<=a<=69: BODY[6]=BODY[6]+[a]
        if 70<=a<=79: BODY[7]=BODY[7]+[a]
        if 80<=a<=89: BODY[8]=BODY[8]+[a]
        if 90<=a<=99: BODY[9]=BODY[9]+[a]
        if 100<=a<=109: BODY[10]=BODY[10]+[a]
        if 110<=a<=119: BODY[11]=BODY[11]+[a]
        if 120<=a<=129: BODY[12]=BODY[12]+[a]
        if 130<=a<=139: BODY[13]=BODY[13]+[a]
        if 140<=a<=149: BODY[14]=BODY[14]+[a]
        if 150<=a<=159: BODY[15]=BODY[15]+[a]
        if 160<=a<=169: BODY[16]=BODY[16]+[a]
        if 170<=a<=179: BODY[17]=BODY[17]+[a]
        if 180<=a<=189: BODY[18]=BODY[18]+[a]
        if 190<=a<=199: BODY[19]=BODY[19]+[a]
    
    COUNT=0
    aa=0

    if len(BODY[0])==10: COUNT=COUNT+1;BODY[0]=[];aa=0
    if len(BODY[1])==10: COUNT=COUNT+1;BODY[1]=[];aa=1
    if len(BODY[2])==10: COUNT=COUNT+1;BODY[2]=[];aa=2
    if len(BODY[3])==10: COUNT=COUNT+1;BODY[3]=[];aa=3
    if len(BODY[4])==10: COUNT=COUNT+1;BODY[4]=[];aa=4
    if len(BODY[5])==10: COUNT=COUNT+1;BODY[5]=[];aa=5
    if len(BODY[6])==10: COUNT=COUNT+1;BODY[6]=[];aa=6
    if len(BODY[7])==10: COUNT=COUNT+1;BODY[7]=[];aa=7
    if len(BODY[8])==10: COUNT=COUNT+1;BODY[8]=[];aa=8
    if len(BODY[9])==10: COUNT=COUNT+1;BODY[9]=[];aa=9
    if len(BODY[10])==10: COUNT=COUNT+1;BODY[10]=[];aa=10
    if len(BODY[11])==10: COUNT=COUNT+1;BODY[11]=[];aa=11
    if len(BODY[12])==10: COUNT=COUNT+1;BODY[12]=[];aa=12
    if len(BODY[13])==10: COUNT=COUNT+1;BODY[13]=[];aa=13
    if len(BODY[14])==10: COUNT=COUNT+1;BODY[14]=[];aa=14
    if len(BODY[15])==10: COUNT=COUNT+1;BODY[15]=[];aa=15
    if len(BODY[16])==10: COUNT=COUNT+1;BODY[16]=[];aa=16
    if len(BODY[17])==10: COUNT=COUNT+1;BODY[17]=[];aa=17
    if len(BODY[18])==10: COUNT=COUNT+1;BODY[18]=[];aa=18
    if len(BODY[19])==10: COUNT=COUNT+1;BODY[19]=[];aa=19
    if COUNT:
        fraction(COUNT)
        for xx in body: b,c=xx[0],xx[1];img.rectangle((b,c,b+13,c+13),0xff,fill=0xa0ff)
    Body=[]
    for xx in BODY:
        for xxx in xx:
            if xxx<aa*10: xxx=xxx+10*COUNT
            Body.append(xxx)
    for xx in Body: xx=body[xx];b,c=xx[0],xx[1];img.rectangle((b,c,b+13,c+13),0xff,fill=0x0)

def fraction(a=0):
    global img,FRACTION
    FRACTION=FRACTION+a
    img.rectangle((185,30,240,50),0xa0ff,fill=0xa0ff)
    img.text((153,50),u'%s%i' %(cn('分数: '),(FRACTION*10)),0xff0000,u'')

    
fraction()
def time():
    global x,y,Body,Piece
    a=piece2(x,y,Piece,0,0,0)
    aa=piece2(x,y+1,Piece,0,0,0)
    for xx in [1]:
        if y>18: piece2(x,y,Piece,0xff,0x0);y=0;x=4;generate();Body=Body+a;treat();break
        else:
            for xx in aa:
                piece2(x,y,Piece,0xff,0x0)
                if Body.count(xx):
                    y=0;x=4
                    generate()
                    for xxx in a:
                        Body.append(xxx)
                    treat()
                    break
                else: piece2(x,y,Piece,0xff,0xa0ff)
    y=y+1
    e32.ao_sleep(0.49,time)
def generate():
    global Piece,Piece1,Piece2,img
    Piece=Piece1
    Piece1=Piece2
    Piece2=randint(1,19)
    a=piece(Piece1)
    bb=piece(Piece2)
    img.rectangle((0,0,153,65),0xa0ff,fill=0xa0ff)
    for xx in a:
        a,b=58+xx[0]*12,45+xx[1]*12
        img.rectangle((a,b,a+13,b+13),0xff,fill=0xff)
    for xx in bb:
        a,b=60+12*4+xx[0]*12,45+xx[1]*12
        img.rectangle((a,b,a+13,b+13),0xff00,fill=0xff00)

generate()
def callback(event={'keycode':0}):#按键控制
    global x,y,Piece,EVENT
    EVENT=event
    if event['keycode']==63495:#左
        if decide(x-1,y,Piece): piece2(x,y,Piece,0xff,0xa0ff);x=x-1;piece2(x,y,Piece,0xff,0x0)
    elif event['keycode']==63496:#右
        if decide(x+1,y,Piece): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;piece2(x,y,Piece,0xff,0x0)
    elif event['keycode']==63497:#上
        if Piece==1 and decide(x,y,1): piece2(x,y,Piece,0xff,0xa0ff);Piece=1;piece2(x,y,Piece,0xff,0x0)
        if Piece==2 and decide(x,y,3): piece2(x,y,Piece,0xff,0xa0ff);Piece=3;piece2(x,y,Piece,0xff,0x0)
        elif Piece==3 and decide(x,y,2): piece2(x,y,Piece,0xff,0xa0ff);Piece=2;piece2(x,y,Piece,0xff,0x0)
        elif Piece==3 and decide(x+1,y,2): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=2;piece2(x,y,Piece,0xff,0x0)
        elif Piece==3 and decide(x-1,y,2): piece2(x,y,Piece,0xff,0xa0ff);x=x-1;Piece=2;piece2(x,y,Piece,0xff,0x0)
        elif Piece==3 and decide(x-2,y,2): piece2(x,y,Piece,0xff,0xa0ff);x=x-2;Piece=2;piece2(x,y,Piece,0xff,0x0)
        if Piece==4 and decide(x,y,5): piece2(x,y,Piece,0xff,0xa0ff);Piece=5;piece2(x,y,Piece,0xff,0x0)
        elif Piece==4 and decide(x+1,y,5): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=5;piece2(x,y,Piece,0xff,0x0)
        elif Piece==5 and decide(x,y,4):piece2(x,y,Piece,0xff,0xa0ff);Piece=4;piece2(x,y,Piece,0xff,0x0)
        if Piece==6 and decide(x,y,7):piece2(x,y,Piece,0xff,0xa0ff);Piece=7;piece2(x,y,Piece,0xff,0x0)
        elif Piece==6 and decide(x+1,y,7):piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=7;piece2(x,y,Piece,0xff,0x0)
        elif Piece==7 and decide(x,y,6):piece2(x,y,Piece,0xff,0xa0ff);Piece=6;piece2(x,y,Piece,0xff,0x0)
        if Piece==8 and decide(x,y,11):piece2(x,y,Piece,0xff,0xa0ff);Piece=11;piece2(x,y,Piece,0xff,0x0)
        elif Piece==8 and decide(x+1,y,11):piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=11;piece2(x,y,Piece,0xff,0x0)
        elif Piece==9 and decide(x,y,8):piece2(x,y,Piece,0xff,0xa0ff);Piece=8;piece2(x,y,Piece,0xff,0x0)
        elif Piece==10 and decide(x,y,9): piece2(x,y,Piece,0xff,0xa0ff);Piece=9;piece2(x,y,Piece,0xff,0x0)
        elif Piece==10 and decide(x+1,y,9): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=9;piece2(x,y,Piece,0xff,0x0)
        elif Piece==11 and decide(x,y,10): piece2(x,y,Piece,0xff,0xa0ff);Piece=10;piece2(x,y,Piece,0xff,0x0)
        if Piece==12 and decide(x,y,15): piece2(x,y,Piece,0xff,0xa0ff);Piece=15;piece2(x,y,Piece,0xff,0x0)
        elif Piece==12 and decide(x+1,y,15): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=15;piece2(x,y,Piece,0xff,0x0)
        elif Piece==13 and decide(x,y,12): piece2(x,y,Piece,0xff,0xa0ff);Piece=12;piece2(x,y,Piece,0xff,0x0)
        elif Piece==14 and decide(x,y,13): piece2(x,y,Piece,0xff,0xa0ff);Piece=13;piece2(x,y,Piece,0xff,0x0)
        elif Piece==14 and decide(x+1,y,13): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=13;piece2(x,y,Piece,0xff,0x0)
        elif Piece==15 and decide(x,y,14): piece2(x,y,Piece,0xff,0xa0ff);Piece=14;piece2(x,y,Piece,0xff,0x0)
        if Piece==16 and decide(x,y,19): piece2(x,y,Piece,0xff,0xa0ff);Piece=19;piece2(x,y,Piece,0xff,0x0)
        elif Piece==17 and decide(x,y,16): piece2(x,y,Piece,0xff,0xa0ff);Piece=16;piece2(x,y,Piece,0xff,0x0)
        elif Piece==17 and decide(x+1,y,16): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=16;piece2(x,y,Piece,0xff,0x0)
        elif Piece==18 and decide(x,y,17): piece2(x,y,Piece,0xff,0xa0ff);Piece=17;piece2(x,y,Piece,0xff,0x0)
        elif Piece==19 and decide(x,y,18): piece2(x,y,Piece,0xff,0xa0ff);Piece=18;piece2(x,y,Piece,0xff,0x0)
        elif Piece==19 and decide(x+1,y,18): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=18;piece2(x,y,Piece,0xff,0x0)

    while EVENT['keycode']==63498:#下
         if decide(x,y+1,Piece): piece2(x,y,Piece,0xff,0xa0ff);y=y+1;piece2(x,y,Piece,0xff,0x0)
         m.blit(img)
         e32.ao_yield()
         e32.ao_sleep(0.0051)
    if event['keycode']==50:#上
        if Piece==1 and decide(x,y,1): piece2(x,y,Piece,0xff,0xa0ff);Piece=1;piece2(x,y,Piece,0xff,0x0)
        if Piece==2 and decide(x,y,3): piece2(x,y,Piece,0xff,0xa0ff);Piece=3;piece2(x,y,Piece,0xff,0x0)
        elif Piece==3 and decide(x,y,2): piece2(x,y,Piece,0xff,0xa0ff);Piece=2;piece2(x,y,Piece,0xff,0x0)
        elif Piece==3 and decide(x+1,y,2): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=2;piece2(x,y,Piece,0xff,0x0)
        elif Piece==3 and decide(x+2,y,2): piece2(x,y,Piece,0xff,0xa0ff);x=x+2;Piece=2;piece2(x,y,Piece,0xff,0x0)
        if Piece==4 and decide(x,y,5): piece2(x,y,Piece,0xff,0xa0ff);Piece=5;piece2(x,y,Piece,0xff,0x0)
        elif Piece==4 and decide(x+1,y,5): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=5;piece2(x,y,Piece,0xff,0x0)
        elif Piece==5 and decide(x,y,4):piece2(x,y,Piece,0xff,0xa0ff);Piece=4;piece2(x,y,Piece,0xff,0x0)
        if Piece==6 and decide(x,y,7):piece2(x,y,Piece,0xff,0xa0ff);Piece=7;piece2(x,y,Piece,0xff,0x0)
        elif Piece==6 and decide(x+1,y,7):piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=7;piece2(x,y,Piece,0xff,0x0)
        elif Piece==7 and decide(x,y,6):piece2(x,y,Piece,0xff,0xa0ff);Piece=6;piece2(x,y,Piece,0xff,0x0)
        if Piece==8 and decide(x,y,11):piece2(x,y,Piece,0xff,0xa0ff);Piece=11;piece2(x,y,Piece,0xff,0x0)
        elif Piece==8 and decide(x+1,y,11):piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=11;piece2(x,y,Piece,0xff,0x0)
        elif Piece==9 and decide(x,y,8):piece2(x,y,Piece,0xff,0xa0ff);Piece=8;piece2(x,y,Piece,0xff,0x0)
        elif Piece==10 and decide(x,y,9): piece2(x,y,Piece,0xff,0xa0ff);Piece=9;piece2(x,y,Piece,0xff,0x0)
        elif Piece==10 and decide(x+1,y,9): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=9;piece2(x,y,Piece,0xff,0x0)
        elif Piece==11 and decide(x,y,10): piece2(x,y,Piece,0xff,0xa0ff);Piece=10;piece2(x,y,Piece,0xff,0x0)
        if Piece==12 and decide(x,y,15): piece2(x,y,Piece,0xff,0xa0ff);Piece=15;piece2(x,y,Piece,0xff,0x0)
        elif Piece==12 and decide(x+1,y,15): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=15;piece2(x,y,Piece,0xff,0x0)
        elif Piece==13 and decide(x,y,12): piece2(x,y,Piece,0xff,0xa0ff);Piece=12;piece2(x,y,Piece,0xff,0x0)
        elif Piece==14 and decide(x,y,13): piece2(x,y,Piece,0xff,0xa0ff);Piece=13;piece2(x,y,Piece,0xff,0x0)
        elif Piece==14 and decide(x+1,y,13): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=13;piece2(x,y,Piece,0xff,0x0)
        elif Piece==15 and decide(x,y,14): piece2(x,y,Piece,0xff,0xa0ff);Piece=14;piece2(x,y,Piece,0xff,0x0)
        if Piece==16 and decide(x,y,19): piece2(x,y,Piece,0xff,0xa0ff);Piece=19;piece2(x,y,Piece,0xff,0x0)
        elif Piece==17 and decide(x,y,16): piece2(x,y,Piece,0xff,0xa0ff);Piece=16;piece2(x,y,Piece,0xff,0x0)
        elif Piece==17 and decide(x+1,y,16): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=16;piece2(x,y,Piece,0xff,0x0)
        elif Piece==18 and decide(x,y,17): piece2(x,y,Piece,0xff,0xa0ff);Piece=17;piece2(x,y,Piece,0xff,0x0)
        elif Piece==19 and decide(x,y,18): piece2(x,y,Piece,0xff,0xa0ff);Piece=18;piece2(x,y,Piece,0xff,0x0)
        elif Piece==19 and decide(x+1,y,18): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;Piece=18;piece2(x,y,Piece,0xff,0x0)
    elif event['keycode']==52:#左
        if decide(x-1,y,Piece): piece2(x,y,Piece,0xff,0xa0ff);x=x-1;piece2(x,y,Piece,0xff,0x0)
    elif event['keycode']==54:#右
        if decide(x+1,y,Piece): piece2(x,y,Piece,0xff,0xa0ff);x=x+1;piece2(x,y,Piece,0xff,0x0)
    while EVENT['keycode']==56:#下
         if decide(x,y+1,Piece): piece2(x,y,Piece,0xff,0xa0ff);y=y+1;piece2(x,y,Piece,0xff,0x0)
         m.blit(img)
         e32.ao_yield()
         e32.ao_sleep(0.0051)


m=appuifw.Canvas(event_callback=callback)
appuifw.app.body=m

time()
#decide(x,y,Piece)
while game:
    piece2(x,y,Piece)
    if Body.count(4): game=0

    
    img.rectangle((0,0,13,13),0xa0ff,fill=0xa0ff)
    m.blit(img)
    e32.ao_sleep(0.05)
    
    e32.ao_yield()

m.clear(0xff)
m.text((80,160),'%s' %(cn('游戏结束')),0xff0000,u'')

m.text((80,180),'%s%i' %(cn('得分: '),FRACTION*10),0xff0000,u'')