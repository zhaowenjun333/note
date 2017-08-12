import appuifw,random,e32
import globalui
#定义初始变量
level=1
gold=0
attack=4
defen=2
dofor=2
sheel=2
exp=0
maxexp=7
life=8
maxlife=8
molife=0
moatt=0
mowat=0
modo=0
moshe=0
mogo=0
moexp=0
moitem=''
#####################
def ch(x):return x.decode('utf8')
#退出游戏
def exit():
    if appuifw.query(ch('要退出吗?'),'query'):
        appuifw.app.set_exit()
def gailu(ten1,ten2,five1,five2,shu1,shu2):
    global expka
    global goldka
    global life
    global maxlife
    global attack
    global defen
    global gold
    ran=int(random.random()*10000)
    if ran>ten1 and ran<ten2:
        if appuifw.query(ch('获得10倍经验,是否装备,按否出售,售价:50000'),'query'):
            expka=10
            appuifw.note(ch('装备成功'),'conf')
        else:
            gold+=50000
            appuifw.note(ch('出售成功'),'conf')
    if ran>five1 and ran<five2:
        if appuifw.query(ch('获得5倍经验,是否装备,按否出售,售价:10000'),'query'):
            expka=5
            appuifw.note(ch('装备成功'),'conf')
        else:
            gold+=10000
            appuifw.note(ch('出售成功'),'conf')
    if ran>shu1 and ran<sht2:
        if appuifw.query(ch('获得全属性+30,是否使用,按否出售,售价:2000'),'query'):
            life+=300
            maxlife+=300
            attack+=30
            defen+=30
            appuifw.note(ch('已经使用'),'conf')
        else:
            gold+=4000
            appuifw.note(ch('出售成功'),'conf')
def mopro(heart,gong,fang,bao,shan):
    global molife
    global moatt
    global mowat
    global modo
    global moshe
    molife=heart
    moatt=gong
    mowat=fang
    modo=bao
    moshe=shan
    return molife
    return moatt
    return mowat
    return modo
    return moshe
#怪物更新系统
def monster():
    mon=[ch('彻里吉'),ch('夏侯渊'),ch('庞德'),ch('徐晃'),ch('张辽'),ch('许诸'),ch('司马懿'),ch('曹操'),ch('吕布之魂')]
    monum=appuifw.popup_menu(mon,ch('挑战BOSS'))
    if monum==0:
        if appuifw.query(ch('准备好了吗?'),'query'):
            mopro(3600,160,130,3,4)
            warring()
            gailu(0,2,5001,5102,7000,7600)
    elif monum==1:
        if appuifw.query(ch('准备好了吗?'),'query'):
            mopro(7200,280,164,9,8)
            warring()
            gailu(0,4,5001,5202,7000,7800)
    elif monum==2:
        if appuifw.query(ch('准备好了吗?'),'query'):
            mopro(18000,610,524,12,13)
            warring()
            gailu(0,6,5001,5302,7000,8000)
    elif monum==3:
        if appuifw.query(ch('准备好了吗?'),'query'):
            mopro(45000,1420,1240,8,21)
            warring()
            gailu(0,36,5001,5602,7000,8200)
    elif monum==4:
        if appuifw.query(ch('准备好了吗?'),'query'):
            mopro(140000,1990,1840,18,20)
            warring()
            gailu(0,72,5001,5902,7000,8400)
    elif monum==5:
        if appuifw.query(ch('准备好了吗?'),'query'):
            mopro(270000,2800,2600,21,29)
            warring()
            gailu(0,144,5001,6202,7000,8600)
    elif monum==6:
        if appuifw.query(ch('准备好了吗?'),'query'):
            mopro(400000,1600,4500,30,31)
            warring()
            gailu(0,288,5001,6502,7000,8800)
    elif monum==7:
        if appuifw.query(ch('准备好了吗?'),'query'):
            mopro(450000,4600,4400,35,35)
            warring()
            gaiku(0,400,5001,6802,7000,9000)
    elif monum==8:
        if appuifw.query(ch('准备好了吗?'),'query'):
            mopro(950000,9000,8500,45,45)
            warring()
def warring():
    global life
    global molife
    global level
    global gold
    global exp
    global maxexp
    global attack
    global defen
    global dofor
    global sheel
    global maxlife
    global moatt
    global mowat
    global modo
    global moshe
    global fuatt
    global fudef
    for i in range(1000):
        if molife<=0:
            if exp<maxexp:
                getgold=(random.randint((int((4.0/5.0)*moatt)),(int((6.0/5.0)*moatt))))*goldka
                getexp=(int(moatt+mowat)*2)*expka
                gold+=getgold
                exp+=getexp
                globalui.global_msg_query((ch('获得经验值 %s')%getexp+ch('\n获得金钱 %s')%getgold),ch('战斗胜利'))
            if exp>=maxexp:
                exp=0
                maxexp=((level**2)*level)+(random.randint(level+1,level+3)*level*level)
                getlife=(int(random.random()*level)+level//3+2)*2
                getatt=(int(random.random()*(level//3))+level//3+2)
                getwat=(int(random.random()*(level//3))+level//4+2)
                getdo=int(random.random()*2)
                getsh=int(random.random()*2)
                attack+=getatt
                defen+=getwat
                dofor+=getdo
                sheel+=getsh
                life+=getlife
                maxlife+=getlife
                level+=1
                globalui.global_msg_query((ch('目前等级为%s')%level+ch('\n生命最大值上升了%s')%getlife+ch('\n攻击力上升了%s')%getatt+ch('\n防御力升了%s')%getwat+ch('\n暴击率上升了%s')%getdo+ch('\n幸运上升了%s')%getsh),(ch('你升级了')))
            break
        elif life<=0:
            gold=int((1.0/2.0)*gold)
            exp=0
            life=int((1.0/2.0)*maxlife)
            globalui.global_msg_query((ch('失去所有经验值,经验值为0\n失去金钱,变为原来的一半\n生命变为一半')),ch('战斗失败'))
            break
        else:
            cha1=moatt-defen
            if cha1>0:
                cha=random.randint(int((4.0/5.0)*cha1),int((6.0/5.0)*cha1))
            else:
                cha=1
            mocha1=attack-mowat
            if mocha1>0:
                mocha=random.randint(int((4.0/5.0)*mocha1),int((6.0/5.0)*mocha1))
            else:
                mocha=1
            life-=cha
            molife-=mocha
            if life<=0:
                life=0
            if molife<=0:
                molife=0
            globalui.global_msg_query((ch('受到攻击,失去生命%s')%cha+ch('\n命中目标,失去生命%s')%mocha),ch('生命:%s')%life+' [%s'%(i+1)+']'+ch(' 生命:%s')%molife)
#睡觉的地方
def slehouse():
    if appuifw.query(ch('休息一晚可以回复生命,需要%s')%(level**2)+ch('金,要休息吗'),'query'):
        global gold
        global life
        if gold>=(level**2):
            gold-=level**2
            life=maxlife
            appuifw.note(ch('谢谢光顾'),'conf')
        else:
            appuifw.note(ch('金钱不够,再见'),'info')
    else:
        appuifw.note(ch('欢迎下次再来'),'info')
#买东西的去处
def shop():
    global life
    global attack
    global defen
    global expka
    global goldka
    global maxlife
    global gold
    shopping=[ch('药草                15'),ch('肉包                30'),ch('鸡腿                90'),ch('回复草            360'),ch('全药草            1200'),ch('烧鸡                2400'),ch('烤卤猪            5000'),ch('完复草            10000'),ch('2倍经验          2000'),ch('3倍经验          8000'),ch('2倍金钱          2000'),ch('3倍金钱          8000'),ch('全属性+20     6000')]
    shopnum=appuifw.popup_menu(shopping,ch('物品                价格'))
    if shopnum==0:
        syshop(15,45)
    elif shopnum==1:
        syshop(30,95)
    elif shopnum==2:
        syshop(90,250)
    elif shopnum==3:
        syshop(360,800)
    elif shopnum==4:
        syshop(1200,2000)
    elif shopnum==5:
        syshop(2400,4000)
    elif shopnum==6:
        syshop(5000,8000)
    elif shopnum==7:
        syshop(10000,15000)
    elif shopnum==8:
        expgo(2000,2)
    elif shopnum==9:
        expgo(8000,3)
    elif shopnum==10:
        goldgo(2000,2)
    elif shopnum==11:
        goldgo(8000,3)
    elif shopnum==12:
        if gold>=6000:
            life+=200
            maxlife+=200
            attack+=20
            defen+=20
            gold-=6000
            appuifw.note(ch('购买成功'),'conf')
        else:
            appuifw.note(ch('金钱不够,再见'),'info')
def expgo(expadd,kanum):
    global expka
    global gold
    if gold>=expadd:
        expka=kanum
        gold-=expadd
        appuifw.note(ch('购买成功'),'conf')
    else:
        appuifw.note(ch('金钱不够,再见'))
def goldgo(goldad,goka):
    global gold
    global goldka
    if gold>=goldad:
        gold-=goldad
        goldka=goka
        appuifw.note(ch('购买成功'),'conf')
    else:
        appuifw.note(ch('金钱不够,再见'),'info')
def syshop(goldnum,lifeadd):
    global gold
    global life
    if gold>=goldnum and life<maxlife:
        life+=lifeadd
        gold-=goldnum
        appuifw.note(ch('谢谢光顾'),'conf')
        if life>=maxlife:
            life=maxlife
    else:
        appuifw.note(ch('金钱不够或者已经满血,再见'),'info')
        
#主角状态一览
def state():
    globalui.global_msg_query(((ch('生命: %s')%life+u' / %s'%maxlife)+(ch('\n攻击: %s')%attack+ch('          防御: %s')%defen)+(ch('\n暴击: %s')%dofor+ch('          幸运: %s')%sheel)+(ch('\n经验值: %s')%exp)+(ch('\n升级经验值: %s')%maxexp)),(ch('等级: %s')%level+ch('          金钱: %s')%gold))
#出城打怪
allmon=[ch('小混混'),ch('打手'),ch('流寇'),ch('强盗'),ch('山贼'),ch('海盗')]
def moname(mcon,s1,s2,s3,s4,s5):
    global level
    global allmon
    if level>10 and level<=25:
        allmon[mcon]=s1
    elif level>25 and level<=40:
        allmon[mcon]=s2
    elif level>40 and level<=60:
        allmon[mcon]=s3
    elif level>60 and level<=90:
        allmon[mcon]=s4
    elif level>90:
        allmon[mcon]=s5
def gate():
    global level
    ranmo=int(random.random()*6)
    if ranmo==0:
        moname(0,ch('弓兵'),ch('长弓兵'),ch('弩兵'),ch('连弩兵'),ch('重弩兵'))
        if appuifw.query(ch('遇到%s')%allmon[0]+ch(',要进入战斗吗?'),'query'):
            if level<=10:
                mopro(6,2,0,0,0)
                warring()
                gailu(10002,0,0,9000,9002)
            elif level>10 and level<=25:
                mopro(36,12,6,0,0)
                warring()
                gailu(10002,0,0,9000,9025)
            elif level>25 and level<=40:
                mopro(150,36,18,0,0)
                warring()
                gailu(10002,0,0,9000,9040)
            elif level>40 and level<=60:
                mopro(780,140,80,0,0)
                warring()
                gailu(10002,0,0,9000,9060)
            elif level>60 and level<=90:
                mopro(2600,270,155,0,0)
                warring()
            else:
                mopro(9200,510,240,0,0)
                warring()
    elif ranmo==1:
        moname(1,ch('短兵'),ch('长枪兵'),ch('双剑客'),ch('轻车兵'),ch('诸侯车'))
        if appuifw.query(ch('遇到%s')%allmon[1]+ch(',要进入战斗吗?'),'query'):
            if level<=10:
                mopro(6,2,1,0,0)
                warring()
            elif level>10 and level<=25:
                mopro(54,15,9,0,0)
                warring()
            elif level>25 and level<=40:
                mopro(234,56,36,2,3)
                warring()
            elif level>40 and level<=60:
                mopro(1300,112,72,7,5)
                warring()
            elif level>60 and level<=90:
                mopro(6700,300,200,12,11)
                warring()
            else:
                mopro(15000,652,404,18,14)
                warring()
    elif ranmo==2:
        moname(2,ch('道士'),ch('风水师'),ch('算命师'),ch('军师'),ch('名军师'))
        if appuifw.query(ch('遇到%s')%allmon[2]+ch(',要进入战斗吗?'),'query'):
            if level<=10:
                mopro(12,3,1,0,0)
                warring()
            elif level>10 and level<=25:
                mopro(72,18,12,0,0)
                warring()
            elif level>25 and level<=40:
                mopro(450,72,50,3,4)
                warring()
            elif level>40 and level<=60:
                mopro(2900,160,112,14,12)
                warring()
            elif level>60 and level<=90:
                mopro(11000,579,440,17,15)
                warring()
            else:
                mopro(23800,815,574,15,16)
                warring()
    elif ranmo==3:
        moname(3,ch('参谋'),ch('参谋长'),ch('副将'),ch('总参谋'),ch('丞相'))
        if appuifw.query(ch('遇到%s')%allmon[3]+ch(',要进入战斗吗?'),'query'):
            if level<=10:
                mopro(16,4,2,0,0)
                warring()
            elif level>10 and level<=25:
                mopro(96,24,12,0,0)
                warring()
            elif level>25 and level<=40:
                mopro(840,190,150,4,5)
                warring()
            elif level>40 and level<=60:
                mopro(5200,396,260,8,9)
                warring()
            elif level>60 and level<=90:
                mopro(21350,921,774,13,15)
                warring()
            else:
                mopro(45200,1320,921,17,18)
                warring()
    elif ranmo==4:
        moname(4,ch('侦察骑兵'),ch('轻骑'),ch('重骑'),ch('近卫骑兵'),ch('白马将军'))
        if appuifw.query(ch('遇到%s')%allmon[4]+ch(',要进入战斗吗?'),'query'):
            if level<=10:
                mopro(28,7,3,0,0)
                warring()
            elif level>10 and level<=25:
                mopro(168,49,36,0,0)
                warring()
            elif level>25 and level<=40:
                mopro(2170,376,250,5,6)
                warring()
            elif level>40 and level<=60:
                mopro(8690,520,489,6,7)
                warring()
            elif level>60 and level<=90:
                mopro(39000,1350,1010,12,14)
                warring()
            else:
                mopro(68000,1840,1520,15,16)
                warring()
    elif ranmo==5:
        moname(5,ch('中尉'),ch('太尉'),ch('大将军'),ch('英雄'),ch('霸王'))
        if appuifw.query(ch('遇到%s')%allmon[5]+ch(',要进入战斗吗?'),'query'):
            if level<=10:
                mopro(40,12,9,1,2)
                warring()
            elif level>10 and level<=25:
                mopro(360,72,54,3,5)
                warring()
            elif level>25 and level<=40:
                mopro(4450,505,384,9,12)
                warring()
            elif level>40 and level<=60:
                mopro(11500,820,660,14,13)
                warring()
            elif level>60 and level<=90:
                mopro(64200,1600,1480,17,18)
                warring()
            else:
                mopro(120000,2100,1820,12,20)
                warring()
expka=1
goldka=1
def equ():
    globalui.global_msg_query(((ch('\n经验: %s')%expka+ch('倍'))+(ch('\n金钱: %s')%goldka+ch('倍'))),ch('装备一览'))
#####################
appuifw.app.body=infor=appuifw.Text()
infor.set(ch('                  游戏介绍\n敌人在26级,41级,61级,91级更新.\n在挑战时可以打到10倍经验值，但概率小.打到5倍概率会高一些.\n如果难,就修改下初识变量.'))
#定义菜单选项
appuifw.app.menu=[(ch('探险'),gate),(ch('状态'),state),(ch('装备'),equ),(ch('商店'),shop),(ch('客栈'),slehouse),(ch('挑战'),monster),(ch('退出'),exit)]
e32.Ao_lock().wait()