# linux 配置指南

>适用于ubuntu、fedora、redhat、centos系列

## 1. 源配置

```bash
# DNF config for fedoraX
# 加速dnf镜像
# cat /etc/dnf/dnf.conf
echo fastestmirror=true >>/etc/dnf/dnf.conf

# PPA for ubuntu..
# 3rd Party Repository: GetDeb Apps
wget -q -O - http://archive.getdeb.net/getdeb-archive.key | sudo apt-key add -
sudo sh -c 'echo "deb http://archive.getdeb.net/ubuntu xenial-getdeb apps" >> /etc/apt/sources.list.d/getdeb.list'

sudo add-apt-repository ppa:saiarcot895/myppa	# apt-fast ubuntu1404 and later versions
sudo add-apt-repository ppa:lotem/rime	# ibus-rime
sudo add-apt-repository ppa:webupd8team/sublime-text-3	# sublimetext 3
sudo apt-add-repository ppa:otto-kesselgulasch/gimp		# gimp
sudo add-apt-repository ppa:mystic-mirage/pycharm	# pycharm commnuity
sudo add-apt-repository ppa:wine/wine-builds	# wine
sudo add-apt-repository ppa:gns3/ppa	# ubuntu-based dis(64bit-only)
sudo add-apt-repository ppa:jonathonf/vim	# vim8
sudo add-apt-repository ppa:webupd8team/y-ppa-manager	# y-ppa-manager
sudo add-apt-repository ppa:atareao/atareao	# touchpad-indicator
sudo add-apt-repository ppa:nathan-renniewaldock/flux	# flux
sudo add-apt-repository ppa:stebbins/handbrake-releases	# handbrake
sudo add-apt-repository ppa:i-nex-development-team/stable && sudo add-apt-repository ppa:gambas-team/gambas3	# i-nex hardinfo
sudo add-apt-repository ppa:plushuang-tw/uget-stable	# uget
sudo add-apt-repository ppa:plushuang-tw/uget-devel
apt://indicator-multiload	# touchpad


sudo add-apt-repository ppa:webupd8team/java
sudo apt update
sudo apt install oracle-java8-installer
# javaws -viewer    打开JAVA控制面板

sudo apt-get update
sudo apt-get -y install apt-fast ibus-rime sublime-text pycharm-community gimp 
sudo apt install --install-recommends winehq-devel
```



## 2. bash_conf

### 2.1 配置命令别名

> ubuntu or debian
>
> vi /.bash_aliases

```bash
# 替换系统命令
alias grep='grep --color=auto'
alias more='less'
alias df='df -h'
alias du='du -c -h'
alias du1='du --max-depth=1'
alias mkdir='mkdir -p -v'
alias nano='nano -w'
alias ping='ping -c 5'
alias ..='cd ..'
alias free='free -mh'
#alias diff='colordiff'      # apt-get install colordiff
#alias apt-get='apt-fast'	# apt-get install apt-fast
#alias vi='vim'


# 新命令
alias py='python'
alias py3='python3'
alias cc='clear'
alias da='date "+%A, %B %d, %Y [%T]"'
alias du1='du --max-depth=1'
alias hist='history | grep $1'      # requires an argument
alias openports='ss --all --numeric --processes --ipv4 --ipv6'
alias pg='ps -Af | grep $1'         # requires an argument (note: /usr/bin/pg is installed by the util-linux package; maybe a different alias name should be used)

# 列目录加强版
alias ls='ls -hF --color=auto'
alias lr='ls -R'                    # 递归显示
alias ll='ls -l'
alias la='ll -A'
alias ld='ll -d'
alias lx='ll -BX'                   # sort by extension
alias lz='ll -rS'                   # 按大小排序
alias lt='ll -rt'                   # 按日期排序
alias lm='la | more'

# 安全特性加强版
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -I'                    # 'rm -i' 每个文件提示
# rm: remove 4 arguments? y/n
alias ln='ln -i'
alias chown='chown --preserve-root'
alias chmod='chmod --preserve-root'
alias chgrp='chgrp --preserve-root'

# 特权访问
if [ $UID -ne 0 ]; then
    alias sudo='sudo '
    alias scat='sudo cat'
    alias svim='sudo vim'
    alias root='sudo su'
    alias reboot='sudo systemctl reboot'
    alias poweroff='sudo systemctl poweroff'
    alias update='sudo pacman -Su'
    alias netcfg='sudo netcfg2'
fi

# Pacman 是一个软件包管理器, 作为ArchLinux发行版的一部分.
# pacman aliases (if applicable, replace 'pacman' with 'yaourt'/'pacaur'/whatever)
alias pac="pacman -S"      # default action     - install one or more packages
alias pacu="pacman -Syu"   # '[u]pdate'         - upgrade all packages to their newest version
alias pacs="pacman -Ss"    # '[s]earch'         - search for a package using one or more keywords
alias paci="pacman -Si"    # '[i]nfo'           - show information about a package
alias pacr="pacman -R"     # '[r]emove'         - uninstall one or more packages
alias pacl="pacman -Sl"    # '[l]ist'           - list all packages of a repository
alias pacll="pacman -Qqm"  # '[l]ist [l]ocal'   - list all packages which were locally installed (e.g. AUR packages)
alias paclo="pacman -Qdt"  # '[l]ist [o]rphans' - list all packages which are orphaned
alias paco="pacman -Qo"    # '[o]wner'          - determine which package owns a given file
alias pacf="pacman -Ql"    # '[f]iles'          - list all files installed by a given package
alias pacc="pacman -Sc"    # '[c]lean cache'    - delete all not currently installed package files
alias pacm="makepkg -fci"  # '[m]ake'           - make package from PKGBUILD file in current directory
```

### 2.2 配置 bash提示符
vi /bashrc
```bash
# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi
```




## 3. 基本软件
### 3.1 小狼豪输入法

安裝更多輸入方案：

```
# 五筆86、袖珍簡化字拼音、五筆畫
sudo apt-get install librime-data-wubi librime-data-pinyin-simp librime-data-stroke-simp
# 朙月拼音（預裝）
sudo apt-get install librime-data-luna-pinyin
# 雙拼
sudo apt-get install librime-data-double-pinyin
# 宮保拼音
sudo apt-get install librime-data-combo-pinyin
# 注音、地球拼音
sudo apt-get install librime-data-terra-pinyin librime-data-bopomofo
# 倉頡五代（預裝）
sudo apt-get install librime-data-cangjie5
# 速成五代
sudo apt-get install librime-data-quick5
# IPA (X-SAMPA)
sudo apt-get install librime-data-ipa-xsampa
# 上海吳語
sudo apt-get install librime-data-wugniu
# 粵拼
sudo apt-get install librime-data-jyutping
# 中古漢語拼音
sudo apt-get install librime-data-zyenpheng
```

添加更多输入法方案（F4快捷键选择）
cd ~/.config/ibus/rime/
cp default.yaml default.custom.yaml

```bash
# default.custom.yaml
# save it to: 
#   ~/.config/ibus/rime  (linux)
#   ~/Library/Rime       (macos)
#   %APPDATA%\Rime       (windows)

patch:
  schema_list:
    - schema: luna_pinyin          # 朙月拼音
    - schema: luna_pinyin_simp     # 朙月拼音 简化字模式
    - schema: luna_pinyin_tw       # 朙月拼音 臺灣正體模式
    - schema: terra_pinyin         # 地球拼音 dì qiú pīn yīn
    - schema: bopomofo             # 注音
    - schema: bopomofo_tw          # 注音 臺灣正體模式
    - schema: jyutping             # 粵拼
    - schema: cangjie5             # 倉頡五代
    - schema: cangjie5_express     # 倉頡 快打模式
    - schema: quick5               # 速成
    - schema: wubi86               # 五笔86
    - schema: wubi_pinyin          # 五笔拼音混合輸入
    - schema: double_pinyin        # 自然碼雙拼
    - schema: double_pinyin_mspy   # 微軟雙拼
    - schema: double_pinyin_abc    # 智能ABC雙拼
    - schema: double_pinyin_flypy  # 小鶴雙拼
    - schema: wugniu        # 吳語上海話（新派）
    - schema: wugniu_lopha  # 吳語上海話（老派）
    - schema: sampheng      # 中古漢語三拼
    - schema: zyenpheng     # 中古漢語全拼
    - schema: ipa_xsampa    # X-SAMPA 國際音標
    - schema: emoji         # emoji表情
```


### 3.2 常用软件

```bash
# If your system is 64 bit, enable 32 bit architecture (if you haven't already):
sudo dpkg --add-architecture i386

sudo apt install guake git p7zip-rar cheese shutter vim colordiff unetbootin unity-tweak-tool


# git install exvim
git clone https://github.com/exvim/main
cd main/
sh unix/install.sh

# replace vim
sh unix/replace-my-vim.sh
​```
```
### 3.3  vim config
```bash
# vi .vimrc.local
# solarized scheme https://github.com/altercation/vim-colors-solarized
set relativenumber	"雇用相对行号 ex 10j, 4k
colorscheme solarized
hi Normal  ctermfg=252 ctermbg=none	"雇用背景透明，基于终端
hi Comment ctermfg=203	"修改注释文字颜色
```

> 相对行号
>
> 像很多用户一样，我也使用绝对行号，好吧，所有用户都使用它。然而，有天我偶然发现了[这篇文章](http://jeffkreeftmeijer.com/2012/relative-line-numbers-in-vim-for-super-fast-movement/)，令我陷入思考：万一相对行号更好用呢？我决定用用看。然后，就像 Ben 在[这个视频](https://www.youtube.com/watch?v=C0H-LyZy9Ko)中所言，绝对行号在我的生活中就是一个谎言。Vim的正宗用法是启用相对行号。
>
> 启用相对行号之前，我建议把下列命令行添加到 .vimrc 文件中：
>
> ```
> set number
> set relativenumber	"雇用相对行号
> ```
>
> 这两个命令行一起，使 Vim 对当前行显示绝对行号，而对其它行显示相对行号。
>
> 接下来，我要说明相对行号的用处。很多 Vim 命令都有一个数字作为前缀。例如，要移动当前行以下的 10 行，可以用 10j。要移动当前行以上的 4 行，使用 4k。要对当前行及以下 2 行缩进，使用 >2j。明白了吧？有了相对行号，其它行（距离当前行）有多远就一目了然了。如果你使用的是绝对行号，你要知道两行之间相距多少行就必须做口算，把两个行号（可能很大）相减。使用相对行号就可以减少这种数学运算。
>
> 同时，你仍然可以使用绝对行号。例如，你编译了一个源文件，然后编译器告知第 943 行有一个语法错误，这时你可以用 943G 或 :943 定位到这一行。
>
> Vim 的一个非常好的特性是，你可以设置[折行功能](http://vimcasts.org/episodes/soft-wrapping-text/)。很多用户包括我会把 j/k 键重映射为 gj/gk，使得按下它们时，光标按虚拟行而不是按物理行移动。然而，这种重映射影响了前文提到的计数功能。为了弥补这一不足，基于[这篇stackoverflow.com的博文](http://stackoverflow.com/a/21000307/2580955)，我们重新进行如下映射：
>
> ```
> noremap <silent> <expr> j (v:count == 0 ? 'gj' : 'j')
> noremap <silent> <expr> k (v:count == 0 ? 'gk' : 'k')
> ```
>
> 
>
> 这样之后，当遇到没有行号的行时，gj/gk 命令会使光标按虚拟行移动，而当遇到有行号的行时，光标则按物理行移动。这与相对行号一起，堪称绝配。

## 4. ubuntu热补丁

```bash
# https://ubuntu.com/livepatch
$ sudo snap install canonical-livepatch
$ sudo canonical-livepatch enable ceca1b8d487f4fda83e584e990a72036
```

## 5. gns3

```bash
sudo add-apt-repository ppa:gns3/ppa
sudo apt-get update
sudo apt-get install gns3-gui

# IOU support
sudo apt-get update
sudo apt-get install gns3-iou
```

## 6 conky

Harmattan Conky Pack is a lightweight system monitor, here's how to install it in Ubuntu14.04

```bash
# http://www.noobslab.com/2014/05/harmattan-conky-pack-offers-15.html
1. Open a terminal window.
2. Type in the following commands then hit Enter after each.
	sudo apt-get install conky curl
	cd && wget -O harmattan.sh http://drive.noobslab.com/data/conky/Harmattan/harmattan.sh
	cd && chmod +x harmattan.sh && ./harmattan.sh
3. You can uninstall it with these commands.
	cd && wget -O uninstall-harmattan.sh http://drive.noobslab.com/data/conky/Harmattan/uninstall-harmattan.sh
	chmod +x uninstall-harmattan.sh && ./uninstall-harmattan.sh
```

## 7 蓝牙卡顿

```bash
# http://blog.tkassembled.com/188/macbook-pro-83-bluetooth-issues-on-linux/#sthash.so5tqJLp.dpuf
$ sudo modprobe b43 btcoex=0
```

## 8 QQ

```
wget http://download.sourceforge.net/wine/wine_gecko-x.xx.x86_64.msi
wine msiexec /i wine_gecko-x.xx.x86_64.msi
or
sudo -i
sudo mkdir -p /usr/share/wine/gecko
sudo mv wine_gecko-x.xx.x86_64.msi /usr/share/wine/gecko/
ls /usr/share/wine/gecko/

wget http://www.kegel.com/wine/winetricks
chmod +x winetricks && sudo cp winetricks /usr/local/bin
winetricks
# 其他运行库，可以使用 winetricks 安装。
```



# 彩色 bash prompt PS1 设定

## 我的配置

```
PS1='${debian_chroot:+($debian_chroot)}\[\033[2;31m\]\u@\h\[\033[2;32m\]\w\$ \[\033[m\]'
```

配置网站： <http://xta.github.io/HalloweenBash/>



## 配置语法

   `PS1=\[ \e[<attr>;<fgcolor>;<bgcolor>m ]`

` PS1="\e[2;31m\u@\h\e[2;32m \w> \e[m"`

> 我们需要将全部非打印字符用专用的 bash 转义序列 `\[ `和` ] `括起来。这两个序列通知 bash，被括起来的字符不占用行上的任何空间，这样就使自动换行能够继续正常工作。没有这两个转义序列，尽管您有了一个很漂亮的提示行，但是假如您键入的命令恰好到达终端的最右端，就会造成显示混乱。


**实际例子**

 `PS1=’${debian_chroot:+($debian_chroot)}\[\033[01;32m][\u@\h] \[\033[01;34m]\w \$ \[\033[00m]’`



| 前景FF | 背景BB |  颜色  |
| :--: | :--: | :--: |
|  30  |  40  |  黑色  |
|  31  |  41  |  红色  |
|  32  |  42  |  绿色  |
|  33  |  43  |  黄色  |
|  34  |  44  |  蓝色  |
|  35  |  45  |  紫色  |
|  36  |  46  |  青色  |
|  37  |  47  |  白色  |



Bash中内置了PS1/PS2/PS3/PS4及PROMPT_COMMAND共5个变量，用于控制Bash shell中提示符的内容和格式。

例如一般意义上默认的：user@localhost~ $，本文的意图是让我们能控制、更改它。

 

如果你们需要在全局设置这些选项，请前往：

（全局的系统设置文件：）/etc/profile, /etc/bashrc

（用户的系统设置文件：）~/.bash_profile , ~/.bash_login , ~/.profile , ~/.bashrc, ~/.bash_logout

### PS设置的实例：

1. export PS1='\u@\h \w \$ ' (普通示例)
2. export PS1='\[\e[0;32m\][\u@\h \w \$]\[\e[m\]' (颜色示例)
3. export PS1='\t: ' (时间示例)
4. export PS1='\u@\h [\$(ls | wc -l)]:\$ ' (显示当前目录行下文件数量)

> PS1/PS2/PS3/PS4及PROMPT_COMMAND的意义：
> > - PS1 ：命令行提示符
> > - PS2 ：延续命令行提示符
> > - PS3 ：脚本中select语句提示符
> > - PS4 ：调试模式下脚本命令提示符("set -x"提示所执行命令)
> > - PROMPT_COMMAND ：Bash shell在显示PS1提示符前所执行的命令

### 1. 提示符转义码

Bash shell允许用户在提示符中使用以下转义符号：

| 转义符号       | 意义                                       |
| ---------- | ---------------------------------------- |
| \a         | 响铃(ASCII 0x07)                           |
| \d         | 日期(格式：星期 月 日)                            |
| \D{format} | 以指定格式显示当前日期(格式字符串将传递给strftime()函数，若为空则使用本机标准格式) |
| \e         | ESC,(ASCII 0x1B)                         |
| \h         | 本机名称(从左至右直到遇到'.')                        |
| \H         | 本机名称                                     |
| \j         | shell当前正在处理任务号                           |
| \l         | shell终端设备基本名称                            |
| \n         | 换行(ASCII 0x0A)                           |
| \r         | 回车(ASCII 0x0D)                           |
| \s         | shell名,$0的基本名                            |
| \t         | 当前时间,24小时制,格式为HH:MM:SS                   |
| \T         | 当前时间,12小时制,格式为HH:MM:SS                   |
| \@         | 当前时间,12小时制,格式为HH:MM am｜pm                |
| \A         | 当前时间,24小时制,格式为HH:MM                      |
| \u         | 当前用户名                                    |
| \v         | Bash版本                                   |
| \V         | Bash发行号(版本+补丁级别)                         |
| \w         | 当前路径,$HOME将会被缩写为'~'                      |
| \W         | 当前路径的基本名(最后一级文件夹),$HOME处理同上              |
| \!         | 当前命令的命令历史记录编号                            |
| \#         | 当前命令的编号                                  |
| \$         | 如果当前用户ID为0(超级用户),则显示'#';否则显示'$'          |
| \nnn       | 八进制数值nnn对应的ASCII字符                       |
| \\         | 反斜杠'\'                                   |
| \[         | 标识不打印字符串的开始                              |
| \]         | 标识不打印字符串的结束                              |

### 2. 在shell中使用不同颜色输出文字

在shell中，可以通过转义序列[<attr>;<fgcolor>;<bgcolor>m设置文字的显示属性(可选择分别或组合设置)。如果要还原字符显示方案为系统默认，可以使用'\e[m'完成。

| attr控制文字的修饰效果(终端并一定全部支持)                 |
| ---------------------------------------- |
| 0:默认; 1:加亮; 2:变暗; 4:下划线; 5:闪烁; 7:反色显示; 8:隐藏文字; 9:删除线 |
| fgcolor控制文本颜色                            |
| 30:黑色; 31:红色; 32:绿色; 33:黄色; 34:蓝色; 35:紫色; 36:青色; 37:白色 |
| bgcolor控制文本颜色                            |
| 40:黑色; 41:红色; 42:绿色; 43:黄色; 44:蓝色; 45:紫色; 46:青色; 47:白色 |

显示属性/前景色/背景色定义在不同的数值区间，这样作的好处是不用显示指明颜色的作用域，系统也会从颜色数值推断出用户想要设置的究竟是属性/前景色／背景色。例如，'\e[9;41m'是要设置显示属性和背景色，保持前景色不变;'\e34m‘仅设置前景色。

下面的脚本演示了各种姿色组合的显示效果

```
#!/bin/bash

for attr in 0 1 2 4 5 7 8 9; do
    for fgcolor in 30 31 32 33 34 35 36 37; do
        for bgcolor in 40 41 42 43 44 45 46 47; do
             printf '\e[%s;%s;%sm %1s;%02s;%02s ' $attr $fgcolor $bgcolor $attr $fgcolor $bgcolor
        done
        printf '\e[0;37;40m\n'
    done
    printf '\n'
done
```

   转义字符ESC的输入

1. shell中，如果想输入ESC(转义)字符，可以先按ctrl+v键后,再按下ESC键，系统会显示出'^['表示转义字符输入完成
2. echo命令中，使用-e选项允许转义字符后，可以输入'\033'或'\e'表示转义符ESC
3. printf命令中，直接使用'\033'即可表示转义符ESC

### 3. 光标控制

同样，通过转义序列我们可以控制光标移动到指定位置：

| 转义序列                       | 跳转位置          |
| -------------------------- | ------------- |
| \033[(L);(C)H\033[(L);(C)f | 跳转至第L行第C列     |
| \033[(N)A                  | 光标向上移动n行      |
| \033[(N)B                  | 光标向下移动n行      |
| \033[(N)C                  | 光标向前移动n列      |
| \033[(N)D                  | 光标向后移动n列      |
| \033[2J                    | 清除屏幕并移动至(0,0) |
| \033[K                     | 删除至行尾         |
| \033[s                     | 保存光标当前位置      |
| \033[u                     | 恢复光标至保存位置     |

### 4. 设置PS1

PS1控制着终端中系统默认提示符的格式 (一般系统默认为'\u@\h:\w \$ ')。我们可以在PS1控制字符串使用Bash预定义的转义符号加入如用户/当前路径/主机名等信息，还可以使用转义字符串控制提示符的颜色。

`export PS1='\[\e[0;32m\][\u@\h \w \$]\[\e[m\]'`

- 值得说明的是在颜色的（以及任何你所使用的转义字符串的）周围我们需要用'\['和'\]'来标记他们是不可见字符，否则会造成第二行重复输入在本行。

### 5. 设置PS2

PS2控制终端中命令延续行的格式，一般系统默认为单字符'>'。和PS1一样，可以使用字符/预定义转义字符/转义序列等进行定制。

`export PS2='\[\e[0;32m\]~>\[\e[m\]'`

比如你可以通过以下命令来实验：

```
$ ls \
~> -la /etc/
```

其中~>为我们的PS2的设置，它替换了一般意义上默认的'>'。

 

### 6. 设置PS3

PS3用于控制shell中提示用户进行选择的提示符，一般系统默认为'#?'。

ps3test.sh

```
[user @ dir] $ cat ps3test.sh
select i in mon tue wed thu fri exit
do
case $i in
mon) echo "Monday";;
tue) echo "Tuesday";;
wed) echo "Wednesday";;
thu) echo "Thusday";;
fri) echo "Friday";;
exit) exit;;
esac
done
[user @ dir] $ ./ps3test.sh
1) mon
2) tue
3) wed
4) thu
5) fri
6) exit
#? 6
[user @ dir] $ export PS3='Enter your choice: '
[user @ dir] $ ./ps3test.sh
1) mon
2) tue
3) wed
4) thu
5) fri
6) exit
Enter your choice: 6
```

### 7. 设置PS4

调试模式下脚本命令提示符，用以将命令和命令执行结果区分开。系统默认为'+'。同样，可以使用各种字符/预定义符号/转义控制序列去设置PS4，此外，系统还提供了两个可用于PS4的变量'$0'和'$LINENO'，分别表示脚本名和当前行号。

ps4test.sh

```
[user @ dir] $ cat ps4test.sh
#!/bin/bash
export PS4='\[\e[0;37;44m\]$LINENO@$0:\[\e[m\]'
set -x
ls -l ~ | wc -l
du -s ~/Music

[user @ dir] $ ./ps4test.sh
5@./ps4test.sh:ls -l /home/user
5@./ps4test.sh:wc -l
13
6@./ps4test.sh:du -s /home/user/Music
4 /home/user/Music
```

### 8. PROMPT_COMMAND

PROMPT_COMMAND是Bash shell在显示PS1提示符前所执行的命令字符串。

`export PROMPT_COMMAND="echo -n [$(date +%H:%M:%S)]"`

显示：`[23:25:38][user@~/workspace/temp] $`



# 故障处理

## 1. 无法开机

```
ctrl+alt+F1
sudo systemctl stop lightdm.service
sudo systemctl poweroff
```

### 2. wireshak权限

```
# http://www.cnblogs.com/craftor/p/3811733.html
sudo groupadd wireshark
sudo chgrp wireshark /usr/bin/dumpcap
sudo chmod 4755 /usr/bin/dumpcap
sudo gpasswd -a lite wireshark
```



# 引用

引用地址
- <http://blog.jobbole.com/103343/>
- <http://www.slblog.net/2014/04/configure-ibus-rime-wubi-schemas-on-ubuntu-14-04/>
- <http://xta.github.io/HalloweenBash/>
- [http://blog.xuyu.org/?p=940](http://blog.xuyu.org/?p=940)
- [http://linuxconfig.org/Bash_prompt_basics](http://linuxconfig.org/Bash_prompt_basics)
- [http://www.thegeekstuff.com/2008/09/bash-shell-take-control-of-ps1-ps2-ps3-ps4-and-prompt_command/](http://www.thegeekstuff.com/2008/09/bash-shell-take-control-of-ps1-ps2-ps3-ps4-and-prompt_command/)
