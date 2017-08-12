#'''海上飞马'''
import random,appuifw
def ru(x):
  return x.decode('utf-8')
def exit():
    if appuifw.query(ru('是否退出？'),'query'):
        appuifw.note(ru('正在退出…！！'),'info')
        appuifw.app.set_exit()
global a,b
a=[ru('大'),ru('小'),ru('豹子')]
appuifw.app.body=n=appuifw.Text(ru('猜大小游戏\n海上飞马\nQQ506339531\n按导航键开始游戏'))
def play():
  n.clear()
  b=random.randint(0,2)
  cho=appuifw.popup_menu(a,ru('选择'))
  if (b==cho):
    appuifw.note(ru('你猜赢了！！'),'info')
    n.add(ru('你猜赢了！！'))
  else:
    appuifw.note(ru('你猜输了'),'error')
    n.add(ru('你猜输了'))
  n.add(ru('\n电脑开出了:')+a[b]+ru('\n你猜了:')+a[cho])
def about():
  n.set(ru('猜大小游戏\n海上飞马\nQQ506339531\n按导航键开始游戏'))
appuifw.app.menu=[(ru('开大小'),play),(ru('关于'),about),(ru('退出'),exit)]
n.bind(63557,play)
appuifw.app.exit_key_handler = exit

#####结束,以下打包程序时再去掉
import e32
Lock=e32.Ao_lock()
appuifw.app.exit_key_handler=Lock.signal
Lock.wait()