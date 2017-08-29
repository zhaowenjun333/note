#!/bin/bash

#sudo apt-get install -y aria2 git
#
#if ! [[ -f /usr/bin/apt-fast ]]; then
#    git clone https://github.com/ilikenwf/apt-fast /tmp/apt-fast
#    sudo cp /tmp/apt-fast/apt-fast /usr/bin
#    sudo chmod +x /usr/bin/apt-fast
#    sudo cp /tmp/apt-fast/apt-fast.conf /etc
#fi

# Linux Init
# 1.PS1
# 2.alias
# 3.souce list

declare -x PS1="\[$(tput setaf 2)\]\u@\[$(tput setaf 6)\]\h:\w\\$ \[$(tput sgr0)\]"

cat>/tmp/bash_base<<EOF
# sys command
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
#alias vi='vim'

# new-command
alias py='python'
alias py3='python3'
alias cc='clear'
alias da='date "+%A, %B %d, %Y [%T]"'
alias du1='du --max-depth=1'
alias hist='history | grep $1'      # requires an argument
alias openports='ss --all --numeric --processes --ipv4 --ipv6 | column -t'
alias pg='ps -Af | grep $1'         # requires an argument (note: /usr/bin/pg is installed by the util-linux package; maybe a different alias name should be used)

# lsdir plus
alias ls='ls -hF --color=auto'
alias lr='ls -R'                    # 递归显示
alias ll='ls -l'
alias la='ll -A'
alias ld='ll -d'
alias lx='ll -BX'                   # sort by extension
alias lz='ll -rS'                   # 按大小排序
alias lt='ll -rt'                   # 按日期排序
alias lm='la | more'

# sec plus
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -I'                    # 'rm -i' 每个文件提示
# rm: remove 4 arguments? y/n
alias ln='ln -i'
alias chown='chown --preserve-root'
alias chmod='chmod --preserve-root'
alias chgrp='chgrp --preserve-root'

# perm plus
if [ $UID -ne 0 ]; then
    alias sudo='sudo '
    alias scat='sudo cat'
    alias svim='sudo vim'
    alias root='sudo su'
    alias reboot='sudo systemctl reboot'
    alias poweroff='sudo systemctl poweroff'
    #alias update='sudo pacman -Su'
    #alias netcfg='sudo netcfg2'
fi
EOF

cat>/tmp/bash_rpm<<EOF
alias cdnet='cd /etc/sysconfig/network-scripts/'
EOF

cat>/tmp/bash_deb<<EOF
#alias diff='colordiff'      # apt-get install colordiff
#alias apt-get='apt-fast'    # apt-get install apt-fast
EOF


cat>/tmp/bash_arch<<EOF
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
EOF

# 2. install alias
if [ -f /etc/bashrc ]; then
    cat /tmp/bash_base >> /etc/bashrc
    cat /tmp/bash_rpm >> /etc/bashrc
    . /etc/bashrc
fi

if [ -f /etc/bash.bashrc ]; then
    # install apt-fast
    sudo apt-get install aria2 wget
    wget https://github.com/ilikenwf/apt-fast/archive/master.zip
    unzip master.zip
    cd apt-fast-master
    sudo cp apt-fast /usr/bin
    sudo cp apt-fast.conf /etc/
    sudo cp ./man/apt-fast.8 /usr/share/man/man8
    sudo gzip /usr/share/man/man8/apt-fast.8
    sudo cp ./man/apt-fast.conf.5 /usr/share/man/man5
    sudo gzip /usr/share/man/man5/apt-fast.conf.5

    cat /tmp/bash_base >> /etc/bash.bashrc
    cat /tmp/bash_deb >> /etc/bash.bashrc
    . /etc/bash.bashrc
fi

if [ -d /etc/yum.repos.d/ ]; then
    cd /etc/yum.repos.d/
    rename .repo .repo.bak *.repo &>/dev/null
    which firewall-cmd &>/dev/null
    if [ $? -eq 0 ]; then
	echo -n "install aliyun repo ..."
        wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo &>/dev/null
    else
	echo -n "install aliyun repo ..."
        wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo &>/dev/null
    fi
    yum clean all
fi


rm -rf /tmp/bash_*
