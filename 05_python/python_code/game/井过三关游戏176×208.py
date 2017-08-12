import appuifw,e32
from graphics import *

def cn(x):return x.decode('utf8')

def ao():
  global a,turn
  if a!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.point((42,27),0,width=25)
    img.point((42,27),0xe0e0ff,width=20)
    a=1
    turn+=1
    game()
def bo():
  global b,turn
  if b!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.point((87,27),0,width=25)
    img.point((87,27),0xe0e0ff,width=20)
    b=1
    global turn
    turn+=1
    game()
def co():
  global c,turn
  if c!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.point((135,27),0,width=25)
    img.point((135,27),0xe0e0ff,width=20)
    c=1
    turn+=1
    game()
def do():
  global d,turn
  if d!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.point((42,70),0,width=25)
    img.point((42,70),0xe0e0ff,width=20)
    d=1
    turn+=1
    game()
def eo():
  global e,turn
  if e!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.point((87,70),0,width=25)
    img.point((87,70),0xe0e0ff,width=20)
    e=1
    turn+=1
    game()
def fo():
  global f,turn
  if f!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.point((135,70),0,width=25)
    img.point((135,70),0xe0e0ff,width=20)
    f=1
    turn+=1
    game()
def go():
  global g,turn
  if g!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.point((42,115),0,width=25)
    img.point((42,115),0xe0e0ff,width=20)
    g=1
    global turn
    turn+=1
    game()
def ho():
  global h,turn
  if h!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.point((87,115),0,width=25)
    img.point((87,115),0xe0e0ff,width=20)
    h=1
    turn+=1
    game()
def io():
  global i,turn
  if i!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.point((135,115),0,width=25)
    img.point((135,115),0xe0e0ff,width=20)
    i=1
    turn+=1
    game()


def ax():
  global a,turn
  if a!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.line((35,20,50,35),0,width=5)
    img.line((50,20,35,35),0,width=5)
    a=2
    turn+=1
    game()
def bx():
  global b,turn
  if b!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.line((80,20,95,35),0,width=5)
    img.line((95,20,80,35),0,width=5)
    b=2
    turn+=1
    game()
def cx():
  global c,turn
  if c!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.line((125,20,140,35),0,width=5)
    img.line((140,20,125,35),0,width=5)
    c=2
    turn+=1
    game()
def dx():
  global d,turn
  if d!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.line((35,63,50,78),0,width=5)
    img.line((50,63,35,78),0,width=5)
    d=2
    turn+=1
    game()
def ex():
  global e,turn
  if e!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.line((80,63,95,78),0,width=5)
    img.line((95,63,80,78),0,width=5)
    e=2
    turn+=1
    game()
def fx():
  global f,turn
  if f!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.line((125,63,140,78),0,width=5)
    img.line((140,63,125,78),0,width=5)
    f=2
    turn+=1
    game()
def gx():
  global g,turn
  if g!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.line((35,105,50,120),0,width=5)
    img.line((50,105,35,120),0,width=5)
    g=2
    turn+=1
    game()
def hx():
  global h,turn
  if h!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.line((80,105,95,120),0,width=5)
    img.line((95,105,80,120),0,width=5)
    h=2
    turn+=1
    game()
def ix():
  global i,turn
  if i!=0:
        appuifw.note(cn('此格被占用…'),'info')
        game()
  else:
    img.line((125,105,140,120),0,width=5)
    img.line((140,105,125,120),0,width=5)
    i=2
    turn+=1
    game()

def desk():
    global img
    img.clear(0xe0e0ff)
    img.line((61,5,61,135),0,width=5)
    img.line((115,5,115,135),0,width=5)
    img.line((24,45,154,45),0,width=5)
    img.line((24,94,154,94),0,width=5)

def vs():
    global a,b,c,d,e,f,g,h,i,img
    desk()
    a,b,c,d,e,f,g,h,i=0,0,0,0,0,0,0,0,0
    global turn
    turn=0
    game()

def game():
    def handle_redraw(rect):
         canvas.blit(img)
    appuifw.app.body=canvas=appuifw.Canvas(event_callback=None,redraw_callback=handle_redraw)
    handle_redraw(())
    delta()
    global turn
    if turn%2==0:
       appuifw.app.body.bind(49,ao)
       appuifw.app.body.bind(50,bo)
       appuifw.app.body.bind(51,co)
       appuifw.app.body.bind(52,do)
       appuifw.app.body.bind(53,eo)
       appuifw.app.body.bind(54,fo)
       appuifw.app.body.bind(55,go)
       appuifw.app.body.bind(56,ho)
       appuifw.app.body.bind(57,io)
    elif turn%2!=0:
       appuifw.app.body.bind(49,ax)
       appuifw.app.body.bind(50,bx)
       appuifw.app.body.bind(51,cx)
       appuifw.app.body.bind(52,dx)
       appuifw.app.body.bind(53,ex)
       appuifw.app.body.bind(54,fx)
       appuifw.app.body.bind(55,gx)
       appuifw.app.body.bind(56,hx)
       appuifw.app.body.bind(57,ix)

def delta():
       global a,b,c,d,e,f,g,h,i
       if a==1 and b==1 and c==1:
         appuifw.note(cn('先手胜利！'),'conf')
         img.line((24,27,154,27),0xff0000,width=5)
       elif a==2 and b==2 and c==2:
         appuifw.note(cn('后手胜利！'),'conf')
         img.line((24,27,154,27),0x3366ff,width=5)
       elif d==1 and e==1 and f==1:
         appuifw.note(cn('先手胜利！'),'conf')
         img.line((24,70,154,70),0xff0000,width=5)
       elif d==2 and e==2 and f==2:
         appuifw.note(cn('后手胜利！'),'conf')
         img.line((24,70,154,70),0x3366ff,width=5)
       elif g==1 and h==1 and i==1:
         appuifw.note(cn('先手胜利！'),'conf')
         img.line((24,115,154,115),0xff0000,width=5)
       elif g==2 and h==2 and i==2:
         appuifw.note(cn('后手胜利！'),'conf')
         img.line((24,112,154,112),0x3366ff,width=5)
       elif a==1 and d==1 and g==1:
         appuifw.note(cn('先手胜利！'),'conf')
         img.line((42,5,42,135),0xff0000,width=5)
       elif a==2 and d==2 and g==2:
         appuifw.note(cn('后手胜利！'),'conf')
         img.line((43,5,43,135),0x3366ff,width=5)
       elif b==1 and e==1 and h==1:
         appuifw.note(cn('先手胜利！'),'conf')
         img.line((88,5,88,135),0xff0000,width=5)
       elif b==2 and e==2 and h==2:
         appuifw.note(cn('后手胜利！'),'conf')
         img.line((88,5,88,135),0x3366ff,width=5)
       elif c==1 and f==1 and i==1:
         appuifw.note(cn('先手胜利！'),'conf')
         img.line((135,5,135,135),0xff0000,width=5)
       elif c==2 and f==2 and i==2:
         appuifw.note(cn('后手胜利！'),'conf')
         img.line((133,5,133,135),0x3366ff,width=5)
       elif a==1 and e==1 and i==1:
         appuifw.note(cn('先手胜利！'),'conf')
         img.line((24,5,154,135),0xff0000,width=5)
       elif a==2 and e==2 and i==2:
         appuifw.note(cn('后手胜利！'),'conf')
         img.line((24,5,154,135),0x3366ff,width=5)
       elif c==1 and e==1 and g==1:
         appuifw.note(cn('先手胜利！'),'conf')
         img.line((24,135,154,5),0xff0000,width=5)
       elif c==2 and e==2 and g==2:
         appuifw.note(cn('后手胜利！'),'conf')
         img.line((24,135,154,5),0x3366ff,width=5)
       elif a!=0 and b!=0 and c!=0 and d!=0 and e!=0 and f!=0 and g!=0 and h!=0 and i!=0:appuifw.note(cn('打成平手！'),'info')

def about():
    appuifw.note(cn('编写：◣絶恋◢卍◤莳绱◥'))

def quit():
       appuifw.app.set_exit()

def main():
    appuifw.app.title=cn('\n井字过三关')
    appuifw.app.screen='normal'
    appuifw.app.menu=[(cn('开始游戏'),vs),(cn('关于'),about),(cn('退出'),quit)]
    appuifw.app.exit_key_handler=quit
    global img
    img=Image.new((176,208))
    desk()
    def handle_redraw(rect):
         canvas.blit(img)
    appuifw.app.body=canvas=appuifw.Canvas(event_callback=None,redraw_callback=handle_redraw)
    handle_redraw(())
main()
e32.Ao_lock().wait()