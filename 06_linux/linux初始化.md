# linux 初始化

## bash初始化
### PS
```
export PS1="\[\e[0;32m\]\u\[\e[0;32m\]@\[\e[0;32m\]\h\[\e[0;32m\]:\[\e[0;36m\]\w\[\e[0;37m\]\\$ \[\e[0m\]"
export PS1="\[$(tput setaf 2)\]\u@\[$(tput setaf 6)\]\h:\w\\$ \[$(tput sgr0)\]"
```

### alias
```
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
#alias diff='colordiff'      # apt-get install colordiff
#alias apt-get='apt-fast' # apt-get install apt-fast
#alias vi='vim'


# new-command
alias py='python'
alias py3='python3'
alias cc='clear'
alias cdnet='cd /etc/sysconfig/network-scripts/'
alias da='date "+%A, %B %d, %Y [%T]"'
alias du1='du --max-depth=1'
alias hist='history | grep $1'      # requires an argument
alias openports='ss --all --numeric --processes --ipv4 --ipv6'
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

