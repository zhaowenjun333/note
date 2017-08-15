# python使用指南

## 1 配置

### 1.1 pip配置

国内pip源

`http://pypi.douban.com/simple/`
`http://pypi.mirrors.ustc.edu.cn/simple/`
`http://mirrors.aliyun.com/pypi/simple/`

### 1.2 pip命令行

`pip install --upgrade pip`

```
pip list
pip install packages -i http://pypi.douban.com/simple/
pip install packages -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com
pip install packages
```

### 1.3 pip配置参数介绍

```bash
# 官方参考地址： <https://pip.pypa.io/en/stable/user_guide/>
# 多配置文件读取顺序
# 1. firstly the site-wide file is read, then
# 2. the per-user file is rad, and finally
# 3. the virtualenv-specific file is read.
# 
# site-wide
Mac OS: /Library/Application Support/pip/pip.conf
linux and Unix: /etc/pip.conf
windos 7: C:\ProgramData\pip\pip.ini
# 
# per-user configuration file
Mac OS : $HOME/Library/Application Support/pip/pip.conf
linux and Unix:~/.pip/pip.conf 
windows: %APPDATA%\pip\pip.ini or %HOME%\pip\pip.ini
```

### 1.4 pip配置举例

```bash
# [global]
# index-url = http://<mirror>/simple
# find-links =
#	http://pypi.douban.com/simple/
#	http://mirrors.aliyun.com/pypi/simple/

[global]
trusted-host = pypi.douban.com
index-url = http://pypi.douban.com/simple/
[install]
ignore-installed = true
```

### 1.5 pip使用

```
两个版本的Python: 
$ python -V
Python 2.7.10
$ python3 -V
Python 3.5.2

可以使用:
$ python -m pip install requests
$ python3 -m pip install requests

或者使用:
$ pip install requests
$ pip3 install requests
```





## 2 py版本管理

### 2.1 virtualenv

> pypi download <https://pypi.python.org/pypi/virtualenv>

```
pip install virtualenv
mkdir microblog
virtualenv microblog
# virtualenv --no-site-packages microblog
microblog\Scripts\activate
deactivate
```

