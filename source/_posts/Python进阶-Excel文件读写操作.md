---
title: Python进阶-Excel文件读写操作
date: 2017-12-20 23:46:37
categories:
- Python
tags:
- Python
- Python进阶
---
#### Python第三方库
Python读写Excel文件依赖第三方库：xlrd和xlwt。
xlrd：可以读取.xls、.xlsx文件
xlwt：可以写Excel文件，生成.xls格式后缀，但不可以直接修改Excel文件。
下面使用pip安装xlrd和xlwt第三方库如下：
```bash
pip install xlrd
pip install xlwt
```
Python在线手册：http://www.python-excel.org/

#### Excel文件组织方式
每一个Excel数据文件从上至下分为三个层级的对象：
workbook： 每一个Excel文件就是一个workbook。
sheet： 每一个workbook中可以包含多个sheet，具体就对应Excel中我们在左下脚所看到的“sheet1”,“sheet2”等。
cell： 每一个sheet就是我们通常所看到的一个表格，可以含有m行，n列，每个确定的行号，列号所对应的一个格子就是一个cell。

#### Python Excel文件读操作
1. 导入模块
  import xlrd   
  
2. 打开Excel文件
  book = xlrd.open_workbook('excelFile.xls')
  
  Book类的方法、属性等：
  book.nsheets: 在Book对象中的文件有多少个worksheet。
  book.sheet_by_index(sheetx): 根据提供的sheetx索引来获取对应的sheet表，返回一个Sheet类的对象。
  book.sheet_by_name(sheet_name): 根据提供的sheet_name来获取对应的sheet表，返回一个Sheet类的对象。
  book.sheet_names(): 返回Book对象中的所有sheet表的名称列表。
  book.sheets(): 返回在Book对象中所有的Sheet对象实例列表。

3. 获取Excel文件工作表
  sh = book.sheet_by_index(0) #通过索引顺序获取
  sh = book.sheet_by_name(u'Sheet1')#通过名称获取  
  
  Sheet类方法、属性等：
  sh.cell(rowx, colx): 根据给出的行和列的参数获取得到cell类，返回一个Cell类实例对象
  sh.cell_type(rowx, colx): 返回对应的cell对象的Type类型
  sh.cell_value(rowx, colx): 返回对应的cell对象的value值
  sh.col_values(colx): 返回指定列的所有cell对象的value值
  sh.row_values(rowx): 返回指定的行的所有cell对象的value值
  sh.name: 返回sheet对象的名称
  sh.ncols: 返回在sheet对象中的列的数目
  sh.nrows: 返回在sheet对象中的行的数目book = xlrd.open_workbook('excelFile.xls')

4. 获取Excel文件工作表cell的值：
  cell=sh.cell(rowx=1, colx=1)   #根据输入行和列获返回一个Cell类对象，cell.value获取值
  sh.cell_value(rowx=1, colx=1) ##根据输入行和列获返回一个Cell类对象的值

#### Python Excel文件写操作
1. 导入模块
import xlwt

2. 打开Excel文件
book = xlrd.Workbook('excelFile.xls')
    
3. 添加Excel文件工作表
sheet1 = wb.add_sheet('heet_name')

4. 写Excel文件工作表cell的值：
sheet1.write(0, 0, 'test1')
row1 = sheet1.row(1)
col1=sheet2.col(1)
row1.write(0, 'test2')
col1.write(1, 'test3')

5. 保存Excel文件
wb.save('excelFile.xls')

#### Python Excel文件读写操作示例
Excel文件读写操作excel_handler.py示例：
1.读取inputfile文件内容，并保存到row_contents列表中；
2.将row_title和row_contents列表重新写到outputfile文件中；
3.执行：`python excel_handler.py personInfo.xlsx result.xls`
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import os
import sys

import xlrd
import xlwt

from time import time

def excel_file_read(filename): 
    if not os.path.isfile(filename):
        print ("%s is not file." % filename)
        return None

    try:
        book = xlrd.open_workbook(filename)
        sh = book.sheet_by_index(0)
    except:
        print ("read %s open error." % filename)
        return None

    print("Sheet name:%s, nrows:%d, ncols:%d" % (sh.name, sh.nrows, sh.ncols))

    row_contents = []
    for rx in range(sh.nrows):
        row_content = []
        for cx in range(sh.ncols):
            #print sh.cell_value(rx, cx)
            row_content.append(sh.cell_value(rx, cx))
        row_contents.append(row_content)
    #print row_contents
    
    return row_contents[1:]

def excel_file_write(filename, row_title, row_contents):
    try:
        wb = xlwt.Workbook()
        ws = wb.add_sheet("Sheet1")
    except:
        print ("write %s open error." % filename)
        return

    for col, col_content in enumerate(row_title):
        #print col, col_content
        ws.write(0, col, col_content)

    for row, row_content in enumerate(row_contents):
        for col, col_content in enumerate(row_content):
            #print col, col_content
            ws.write(row + 1, col, col_content)

    wb.save(filename)

def get_opt_init(argv):
    if len(argv) < 3:
        print "python excel_handler.py inputfile outputfile"
        return None

    if len(argv) >= 3:
        inputfile = argv[1]
        outputfile = argv[2]
                   
    return inputfile, outputfile 

if __name__=="__main__" :
    start = time()

    inputfile, outputfile = get_opt_init(sys.argv)
    if not inputfile and outputfile:
        sys.exit(0)

    row_contents = excel_file_read(inputfile)
    if not row_contents:
        sys.exit(0)
		
    row_title = [u'姓名', u'年龄', u'电话']
    excel_file_write(outputfile, row_title, row_contents)

    print "Time cost %.2fs." % (time() - start)

```
**遇到问题**
问题现象：执行脚本，在save方法报编码错误
```bash
File "excel_handler.py", line 55, in excel_file_write
  wb.save(filename)
.......
File "/usr/local/lib/python2.7/site-packages/xlwt/UnicodeUtils.py", line 50, in upack2
  us = unicode(s, encoding)
```
解决方法：
row_title = ['姓名', '年龄', '电话']修改成row_title = [u'姓名', u'年龄', u'电话']

参考链接：
http://blog.sina.com.cn/s/blog_6babbcb8010182c3.html
http://blog.csdn.net/wangkai_123456/article/details/50457284