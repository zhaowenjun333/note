
#RHEL环境使用文档
##RHEL7.2 实验环境使用介绍：
启动server计算机     rht-vmctl start server
查看“物理控制台”以进行登录并操作server     rht-vmctl view server
将server重置为之前的状态，并重新启动虚拟机        rht-vmctl reset server

- desktopX.example.com        172.25.X.10     学生客户端     student/student;redhat/redhat
- serverX.example.com         172.25.X.11     学生服务器     student/student;redhat/redhat
- classroom.example.com       172.25.254.254  教室环境使用服务器     root/Asimov

系统要求：
1. vmware12
2. 内存：8G



1. 登录系统（无密码）
    # su -
    # passwd: redhat
