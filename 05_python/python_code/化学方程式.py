import appuifw
def cn(x):return x.decode("utf-8")
def _1():
    global cg
    cg=0
    fin()
    show=m.get()[:-1]
    if (len(show)<1):
        m.set(cn('很抱歉，未找到相关的方程式，您可以尝试交换物质AB的顺序'))
        return
    m.color = (255,0,0)
    m.set(wa+cn('、')+wb)
    m.color = (0)
    m.add(cn('的相关化学方程式：\n\n'))
    m.add(show)
def fin(temp=0,ga=0,gb=0):
    global wa,wb
    if (ga!=0):
        wa=ga
        wb=gb
    else:
        m.set(u'')
        wa=appuifw.query(cn('输入物质A'),'text')
        wb=appuifw.query(cn('输入物质B'),'text')
#    g=m.get()
    global x,s
    x=1
    s=temp
    try:
        while x==1:
            f=g.find(wa,s)
            f2=g.find(wb,f)
            if (f==-1)and(f2==-1):break
            fj=g[f:f2]
            ff=fj.find(u'\n')
            if (ff==-1):x=f
            else:s=f+1
        global ft,fd
        ft=0
        while ft!=-1:
            ft=g[:x].find(u'\n',ft+1)
            if (ft!=-1):fjg=ft
        fd=g.find(u'\n',x)
        be=g[fjg+1:fd]
    except:pass
    global cg
    try:
        if((x-fjg)<20):m.add(be+u'\n')
    except:cg=1
    if(cg!=1):fin(fd,wa,wb)
    if(len(m.get())<1):pass
    else:
        m.set_pos(0)
        m.focus = True
    return 0
def clear():
    m.set("")
def st():
    f=open('e:\\system\\chemistry.db','r')
    global g
    g=f.read()
    g=cn(g)
    m.set(cn('简介:本软件可以搜索化学方程式，只需要输入相关方反应物质即可智能搜索并列举符合条件的化学方程式，软件支持模糊匹配。'))
def exit():
    if appuifw.query(cn("要退出吗"),"query"):
        appuifw.app.set_exit()

appuifw.app.body = m = appuifw.Text()
#appuifw.app.screen = 'large'
m.focus = False
m.font = (u'Sans MT 936_s60', 16)
m.color = (0)

appuifw.app.menu = [(cn("查找"),_1),(cn("退出"),exit)]
st()