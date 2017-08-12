# pastriang.py - (c) Goetz Schwandtner
# schwandtner@googlemail.com
# 18-01-2008
# V1.0 with class structure

import appuifw
from graphics import *
import e32
from key_codes import *

STDCOLORS=((255,0,0),(0,0,255),(0,255,0),(255,255,0))
def getcolor(i):
    if i<4:
        return STDCOLORS[i]
    return 10*i,10*i,10*i

class Pascal(object):
    def __init__(self,n,mod=1):
        self.BORDER=4
        self.vals=[]
        self.mod=mod
        self.setsize(n)
        self.labels=0
        self.nums=0
        
    def setsize(self,n):
        self.n=n
        if n>9:
            self.nums=0
        st=len(self.vals)
        for i in range(st,n):
            self.vals.append([1])
            for j in range(1,i+1):
                self.vals[-1].append(self.vals[-2][j-1]+self.vals[-2][j])
            self.vals[-1].append(1)
        self.setcolmod()
    
    def setcolmod(self,mod=None):
        if mod:
            self.mod=mod
        self.cols=[]
        for r in self.vals:
           self.cols.append([])
           for c in r:
               self.cols[-1].append(c%self.mod)
             
    def printme(self):
       for r in self.vals:
           print
           for c in r:
               print c,

    def draw(self,image):
        w,h=image.size
        image.clear()
        if self.labels:
            image.text((0,20),u"n:"+str(self.n)+" mod:"+str(self.mod))
        cw,ch=w//(self.n+1),h//self.n
        for y in range(self.n):
            for x in range(y+2):
                c=getcolor(self.cols[y][x])
                image.rectangle(((w-(y+2)*cw)//2+x*cw,y*ch,(w-(y+2)*cw)//2+(x+1)*cw-self.BORDER,(y+1)*ch-self.BORDER),outline=c,fill=c)
                if self.nums:
                    tx=unicode(self.vals[y][x])
                    tm= image.measure_text(tx)[0]
                    image.text(((w-(y+1)*cw-tm[2])//2+x*cw,(y+1)*ch-(ch+tm[1]-self.BORDER)//2),tx)

class Main(object):
    def __init__(self):
        self.running=1
        self.tr=Pascal(15)
        appuifw.app.exit_key_handler=self.quit
        appuifw.app.menu=[("帮助".decode('utf8'),self.help),("关于".decode('utf8'),self.about),("退出".decode('utf8'),self.quit)]
        appuifw.app.screen='full'
        self.img=None
        self.canvas=appuifw.app.body=appuifw.Canvas(event_callback=self.handle_event,redraw_callback=self.handle_redraw)
        self.img=Image.new(self.canvas.size)

    def quit(self):
        self.running=0
    
    def mainLoop(self):
        self.redraw()
        while self.running:
            e32.ao_yield()

    def redraw(self):
        self.tr.draw(self.img)
        self.handle_redraw(())

    def handle_event(self,event):
        if event['type'] == appuifw.EEventKeyUp:
            key=event['scancode']
            if key==EScancodeUpArrow:
                self.tr.setcolmod(self.tr.mod+1)
                self.redraw()
            if key==EScancodeDownArrow:
                self.tr.setcolmod(max(self.tr.mod-1,1))
                self.redraw()
            if key==EScancodeLeftArrow:
                self.tr.setsize(max(1,self.tr.n-1))
                self.redraw()
            if key==EScancodeRightArrow:
                self.tr.setsize(self.tr.n+1)
                self.redraw()
            if key==EScancodeHash:
                self.tr.labels=1-self.tr.labels
                self.redraw()
            if key==EScancode0:
                self.tr.nums=1-self.tr.nums
                self.redraw()            

    def handle_redraw(self,rect):
        if self.img:
            self.canvas.blit(self.img)

    def about(self):
        appuifw.note(u'Pascal triangle demo \n (c) 01-2008 Goetz schwandtner@googlemail.com')

    def help(self):
        appuifw.note('帮助 (按键):\n左,右 大小\上,下 颜色 (mod)\n显示: # par, 0 vals'.decode('utf8'))
m=Main()
m.mainLoop()