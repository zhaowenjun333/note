#
#扫雷
import appuifw,e32,sysinfo,key_codes,random
from graphics import*
def cn(x):return x.decode("utf8")
appuifw.app.body=m=appuifw.Canvas()
a=sysinfo.display_pixels()
a5=[a[0],a[1]]
appuifw.app.screen="full"
img=Image.new((a[0],a[1]))
img.clear(0x0)
img.text((40,20),cn("作者：刀剑㏑入梦"),0xffaaca,u'LatinBold12')

m1,n1,k1=12,12,20#行竖线条，格子大小
f=[a[0]/2-k1,a[1]/2-k1,a[0]/2,a[1]/2]#ѡ���
def h():#��ʼ������
  for m2 in range(m1):
    img.rectangle(((a5[0]/2-m1/2*k1)+k1*m2,a5[1]/2-m1/2*k1,a5[0]/2+m1/2*k1,a5[1]/2+m1/2*k1),0xffffff,width=2)
  for n2 in range(n1):  
    img.rectangle((a5[0]/2-n1/2*k1,a5[1]/2-n1/2*k1,a5[0]/2+n1/2*k1,(a5[1]/2-n1/2*k1)+k1*n2),0xffffff,width=2)
def h2():#h2-h5ѡ�����ƶ�  
  for u in [0,2]:
    f[u]=f[u]-k1;h()
  img.rectangle((f[0],f[1]-1,f[2]+1,f[3]),0x0000ff,width=2)
  redraw(())
#  print "w",f[0],f[2]
def h3():  
  for u in [0,2]:
    f[u]=f[u]+k1;h()
  img.rectangle((f[0],f[1]-1,f[2]+1,f[3]),0x0000ff,width=2)
  redraw(())
def h4():  
  for u in [1,3]:
    f[u]=f[u]-k1;h()
  img.rectangle((f[0],f[1]-1,f[2]+1,f[3]),0x0000ff,width=2)
  redraw(())
def h5():  
  for u in [1,3]:
    f[u]=f[u]+k1;h()    
  img.rectangle((f[0],f[1]-1,f[2]+1,f[3]),0x0000ff,width=2)
  redraw(())

b2=[(858,558)]
def h6():
  global b3
  if (f[0]+k1/2,f[1]+k1/2) in b:
    img.text((60,40),cn("����Ϸ������游戏结束"),0x11fafa,u'LatinBold12')
    i()
    redraw(())  
  elif (f[0]+k1/2,f[1]+k1/2) in b3:
      zu=b3.count((f[0]+k1/2,f[1]+k1/2))
      img.text((f[0]+k1/2-4,f[1]+k1/2+10),u"%d"%zu,0xff0000,u'LatinBold12')
      b2.append((f[0]+k1/2,f[1]+k1/2))
      redraw(())
      del b2[1:]
  else:
    x1=f[0]+k1/2;y1=f[1]+k1/2;c=0
    while(c<len(b2)):      
      bc,bd=0,2
      fy=[x1-k1,x1,x1+k1,y1-k1,y1,y1+k1]
      for a in range(1,10):
        if a==4 or a==7:
          bc=bc+1
          bd=bd-3
        bd=bd+1
        if (fy[bc],fy[bd]) in b2:#����
          continue
        if fy[bc]<a5[0]/2-m1/2*k1 or fy[bc]>a5[0]/2+m1/2*k1 or fy[bd] <a5[1]/2-n1/2*k1 or fy[bd]>a5[1]/2+n1/2*k1:#����
           continue
        b2.append((fy[bc],fy[bd]))#���괢��
         
      if (b2[c][0],b2[c][1]) not in b3:  
        x1,y1=b2[c][0],b2[c][1]
      c=c+1 
    z1=0
  
    while(z1<len(b2)):#��������

      x2=b2[z1][0];y2=b2[z1][1]
      zu=b3.count((x2,y2))
      z1=z1+1
      if (x2,y2) in b:
        continue  
      img.text((x2-4,y2+10),u"%d"%zu,0xff00ff,u'LatinBold12')        
      redraw(())
    del b2[1:]#ɾ��b2�����꣬�����ظ�д����  
h()
bx=[]  
def h8():
  if (f[0],f[1]) not in bx:
    if (f[0]+k1/2,f[1]+k1/2) not in b2:
      bx.append((f[0],f[1]))#���괢��
      img.text((f[0]+6,f[1]+20),u"X",0x00ffff,u'LatinBold12')
  else:
    img.text((f[0]+6,f[1]+20),u"X",0x0,u'LatinBold12')
    bx.remove((f[0],f[1]))
  redraw(())    

img.rectangle((f[0],f[1]-1,f[2]+1,f[3]),0x0000ff,width=2)#ѡ���
m.bind(key_codes.EKeyLeftArrow,h2)      
m.bind(key_codes.EKeyRightArrow,h3)      
m.bind(key_codes.EKeyUpArrow,h4)
m.bind(key_codes.EKeyDownArrow,h5)
m.bind(key_codes.EKeySelect,h6)
m.bind(48,h8)#������

def h7():#�ж�ѡ����Ƿ�Խ��
  if f[0]==140:
    f[0]=f[0]-60
    f[2]=f[2]-60
    print "w"

o=range(1,m1*n1+1)
o1=25#地雷数
b=[];b3=[]
while(o1>0):
  t=int(random.random()*m1*n1)#���
  if o[t]!=0:#�жϴ˸���û��
    o[t]=0#����
    o1=o1-1
    x=(a5[0]/2-n1/2*k1+k1/2)+k1*((t+m1)%m1);y=(a5[1]/2-n1/2*k1+k1/2)+k1*int(t/n1)
    b.append((x,y))
    fx=[x-k1,x,x+k1,y-k1,y,y+k1]
    bc,bd,c=0,2,0
    for a in range(1,10):
      if a==4 or a==7:
        bc=bc+1
        bd=bd-3
      bd=bd+1
      if (fx[bc],fx[bd])==(x,y):
        continue
      if fx[bc]<a5[0]/2-m1/2*k1 or fx[bc]>a5[0]/2+m1/2*k1 or fx[bd] <a5[1]/2-n1/2*k1 or fx[bd]>a5[1]/2+n1/2*k1:#����
        continue
      b3.append((fx[bc],fx[bd]))#���괢��
    
def i():
  z=0
  z1=-1
  while z<o.count(0):#ȡ����
    x,y=b[z][0],b[z][1] 
    img.point((x,y),0xffffff,width=(k1)/2)
    z=z+1

def redraw(rect):
  m.blit(img)
redraw(())  

import e32
lock=e32.Ao_lock()
appuifw.app.exit_key_handler=lock.signal
lock.wait()
