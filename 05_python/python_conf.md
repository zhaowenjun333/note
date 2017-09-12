

## linux下多版本python环境配置

### 1. 依赖
pyenv安装使用git
```
# yum install git -y
# yum -y install gcc make patch gdbm-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel
```

### 2. 创建用户python
```
# useradd python
# passwd python
```

### 3. 使用python用户登录
`su - python`

### 4. 开始部署pyenv
```
pyenv安装方式：
- pyenv git方式安装 https://github.com/pyenv/pyenv
- pyenv-installer 脚本自动安装 https://github.com/pyenv/pyenv-installer

以下将介绍使用 pyenv-installer 方式安装 pyenv
$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

在python用户的~/.bash_profile中追加
export PATH="/home/python/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

$ source ~/.bash_profile

开始使用 pyenv
$ python -V
$ pyenv versions
```


### 5. pyenv 使用介绍
$ pyenv     # 显示 pyenv 帮助
$ pyenv global  x.x.x    # 设置全局 python版本（应用到整个系统）
$ pyenv local  x.x.x     # 设置本地 python版本（子目录下会继承此设置）
$ pyenv shell  x.x.x    # 设置会话 python版本（作用于当前shell会话）
$ pyenv help install    # 查看子命令帮助


$ pyenv install --list  # 列出 pyenv 支持的所有版本

#### 5.1 安装特定的 python 版本
5.1.1 online 安装指定 python 版本
$ pyenv install 3.5.3
$ pyenv versions

5.1.2. 使用缓存方式安装指定 python 版本
$ pyenv install 3.5.3 -v

> cache目录，如果目录不存在，就自己创建，在~/.pyenv目录下，新建cache目录，放入下载好的 python 文件。
> 不确定要哪一个文件，把下载的3个文件都放进去。



### 6. pyenv 使用 virtualenv 虚拟环境设置
> pyenv已经自带 Virtualenv插件，在plugins/pyenv-virtualenv

#### 6.1 创建一个指定版本的虚拟环境空间
$ pyenv virtualenv 3.6.1 magedu361  # 创建出一个3.6.1版本的虚拟环境
$ pyenv versions        # 真实目录在.pyenv/versions/
* system (set by /home/python/.pyenv/version)
  3.5.3
  3.6.1
  3.6.1/envs/magedu361
  magedu361

#### 6.2 使用虚拟环境空间
$ mkdir -p magedu361/projects/cmdb
[python@node ~]$ cd magedu361/projects/cmdb
[python@node cmdb]$ pyenv local magedu361
(magedu361) [python@node cmdb]$ cd ..
[python@node projects]$ cd cmdb/



### 7. 部署 ipython 与 jupyter

#### 7.1 配置pip
```
vi ~/.pip/pip.conf
[global]
index-url=https://mirrors.aliyun.com/pypi/simple/
trusted-host=mirrors.aliyun.com
```

在不同的虚拟环境中，安装redis包，使用pip list看看效果。
$ pip -V


#### 7.2 安装ipython
$ pip install ipython
$ ipython

#### 7.3 部署 jupyter
```
安装Jupyter，也会自动安装ipython
$ pip install jupyter
$ jupyter notebook help

生成配置文件
$ jupyter notebook --generate-config
$ jupyter notebook password         # 设置 jupyter 登录密码（也可以写入到配置文件中）
$ jupyter notebook --ip=0.0.0.0 --no-browser    

生成密码
$ ipython
In [1]: from notebook.auth import passwd
In [2]: passwd()
Enter password:
Verify password:
Out[2]: 'sha1:ce23d945972f:34769685a7ccd3d08c84a18c63968a41f1140274'    # 复制密码‘sha:ce…’

修改默认配置文件
vim ~/.jupyter/jupyter_notebook_config.py
c.NotebookApp.ip='*'        # 在所有IP上侦听
# c.NotebookApp.password = 'string'
# The string should be of the form type:salt:hashed-password
c.NotebookApp.password = 'sha:ce...刚才复制的那个密文'
c.NotebookApp.open_browser = False      # 禁止自动打开浏览器
c.NotebookApp.port =8888                #随便指定一个端口

启动jupyter notebook
jupyter notebook

参考地址： <http://jupyter-notebook.readthedocs.io/en/latest/public_server.html>
```

### 8. python环境移植
pip freeze > requirement
pip install -r requirement


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
关于windows下安装，大同小异。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~