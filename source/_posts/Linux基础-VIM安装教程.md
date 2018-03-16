---
title: Linux基础-VIM安装教程
date: 2017-10-06 17:36:06
categories:
- Linux基础
tags:
- Linux
- Linux基础
---

### yum安装Vim
1.先卸载老的vim
```bash
yum remove vim-* -y
```
2.下载第三方yum源
```bash
wget -P /etc/yum.repos.d/  https://copr.fedorainfracloud.org/coprs/mcepl/vim8/repo/epel-7/mcepl-vim8-epel-7.repo
```
3.安装vim
```bash
yum -y install vim-enhanced sudo
```

4.验证vim版本
```bash
rpm -qa |grep vim
vim-enhanced-8.0.0704-1.1.26.el7.centos.x86_64
vim-common-8.0.0704-1.1.26.el7.centos.x86_64
vim-minimal-8.0.0704-1.1.26.el7.centos.x86_64
vim-filesystem-8.0.0704-1.1.26.el7.centos.x86_64
```

安装过程遇到的依赖问题“libc.so.6 is needed by XXX”解决方法
参考：http://www.cnblogs.com/think3t/p/4165102.html

### rpm包安装Vim
1.Vim安装需要的四个rpm包如下：
```bash
vim-filesystem-7.4.629-5.el6_8.1.x86_64.rpm
vim-common-7.4.629-5.el6_8.1.x86_64.rpm
vim-enhanced-7.4.629-5.el6_8.1.x86_64.rpm  
vim-minimal-7.4.629-5.el6_8.1.x86_64.rpm
```

2.登录[rpmfind网站](https://www.rpmfind.net/linux/rpm2html/search.php)，下载vim的rpm包，注：**centos只有7.4版本vim包**

vim有四个包，下面是按照顺序

3.使用rpm命令安装Vim包，按照1中的顺序依次安装。
``` bash
rpm -ivh 包名
```
4.查看vim版本号
``` bash
vim --version | head
```

### 源码安装Vim
1.安装依赖
``` bash
yum -y install ruby perl-devel python-devel ruby-devel perl-ExtUtils-Embed ncurses-devel
```

2.源码下载
源码下载方法一：克隆源码
``` bash
git clone https://github.com/vim/vim.git
cd vim/
```

源码下载方法二：下载压缩包
``` bash
wget https://github.com/vim/vim/archive/master.zip
unzip master.zip
cd vim-master
cd src/
```

3.源码编译
``` bash
./configure --prefix=/usr/local --enable-multibyte  --with-tlib=tinfo  --enable-pythoninterp --enable-rubyinterp \
--with-ruby-command=/usr/bin/ruby --with-features=huge
make
make install
```

4.查看vim版本号
``` bash
vim --version | head
```
