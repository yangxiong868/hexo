---
title: 'Linux基础-rpm和yum常用命令'
date: 2017-10-06 21:31:01
categories:
- Linux基础
tags:
- Linux
- Linux基础
---
### rpm常用命令
安装一个rpm包
rpm -ivh file.rpm 

参数说明：
-i ：安装的意思
-v ：可视化
-h ：显示安装进度
另外在安装一个rpm包时常用的附带参数有：
--force 强制安装，即使覆盖属于其他包的文件也要安装
--nodeps 当要安装的rpm包依赖其他包时，即使其他包没有安装，也要安装这个包

查看包依赖关系
rpm -qpR file.rpm　 

卸载一个rpm包
rpm -e file.rpm

查找是否已经安装了某个包
rpm -qa | grep htop

查看安装的软件包安装了哪些文件
rpm -ql htop

想知道本地文件来自那个软件包
rpm -qf /usr/bin/htop

rpm包下载网址：
- https://pkgs.org/
- http://rpm.pbone.net
- https://rpmfind.net/

参考链接：
http://achuan.blog.51cto.com/102/60869

### yum常用命令
从 repo 中查找某个软件包
yum search htop

查看yum安装源中包的版本信息
yum info htop

从 repo 中查找哪个包提供了哪个文件
yum provides /usr/bin/htop

安装软件包的最新或指定版本
yum install  [-y]  htop
yum install  [-y]  htop-2.0.1-1.el7

查看软件包所有可用的版本
yum --showduplicate list htop

卸载软件包
yum remove  [-y]  htop

升级软件包
yum update [-y] htop

降级软件包到指定版本（软件包的新版本已经安装）
yum downgrade htop-2.0.0-2.el7

删除 yum cache
yum clean all

