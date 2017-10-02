

## linux 多版本 python 配置

### 依赖
pyenv安装使用git
`# yum install git -y`
Python安装依赖
`# yum -y install gcc make patch gdbm-devel openssl-devel sqlite-devel readline-devel zlib-devel bzip2-devel`


创建用户python
`# useradd python`


使用python用户登录
$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

在python用户的~/.bash_profile中追加
export PATH="/home/python/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

$ source ~/.bash_profile

python 版本及path路径
$ python --version
$ python -V
$ echo $PATH

pyenv 命令
$ pyenv
$ pyenv global      # 影响全局
$ pyenv local       # 影响本地
$ pyenv shell       # 影响会话
$ pyenv help install

列出所有可用版本
$ pyenv install --list
安装指定版本
$ pyenv install 3.5.3
$ pyenv versions


使用缓存方式安装
$ pyenv install 3.5.3 -v
cache目录，如果目录不存在，就自己创建
在~/.pyenv目录下，新建cache目录，放入下载好的版本文件。
不确定要哪一个文件，把下载的3个文件都放进去。



设置Python版本
$ pyenv global 3.5.3
切记，这里用global是因为是在非root用户python用户下
如果是root用户安装，请不要使用global，否则影响太大
使用pyenv local设置从当前工作目录开始向下递归都继承这个设置。
pyenv shell只作用于当前会话
$ pyenv shell system

Virtualenv
插件，在plugins/pyenv-virtualenv
$ pyenv virtualenv 3.6.1 magedu361
创建出一个3.6.1版本的独立空间。
$ pyenv versions
* system (set by /home/python/.pyenv/version)
  3.5.3
  3.6.1
  3.6.1/envs/magedu361
  magedu361
真实目录在.pyenv/versions/

$ mkdir works/magedu361 -p
[python@node ~]$ cd works/magedu361/
[python@node magedu361]$ pyenv local magedu361
(magedu361) [python@node magedu361]$ cd ..
[python@node works]$ cd magedu361/



pip通用配置
```
vi ~/.pip/pip.conf
[global]
index-url=https://mirrors.aliyun.com/pypi/simple/
trusted-host=mirrors.aliyun.com
```

在不同的虚拟环境中，安装redis包，使用pip list看看效果。
$ pip -V


安装ipython
$ pip install ipython
$ ipython



```
安装Jupyter，也会安装ipython的
$ pip install jupyter
$ jupyter notebook help
生成配置文件
$ jupyter notebook --generate-config
$ jupyter notebook --ip=0.0.0.0 --no-browser

生成密码
In [1]: from notebook.auth import passwd
In [2]: passwd()
Enter password:
Verify password:
Out[2]: 'sha1:ce23d945972f:34769685a7ccd3d08c84a18c63968a41f1140274'
把生成的密文‘sha:ce…’复制下来

修改默认配置文件

vim ~/.jupyter/jupyter_notebook_config.py
c.NotebookApp.ip='*'        # 就是设置所有ip皆可访问
c.NotebookApp.password = 'sha:ce...刚才复制的那个密文'
c.NotebookApp.open_browser = False      # 禁止自动打开浏览器
c.NotebookApp.port =8888                #随便指定一个端口


启动jupyter notebook
jupyter notebook

参考地址： <http://jupyter-notebook.readthedocs.io/en/latest/public_server.html>
```


pip freeze > requirement
pip install -r requirement

- EOF

