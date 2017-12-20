---
title: Python进阶-csv文件读写
date: 2017-12-20 00:23:13
categories:
- Python
tags:
- Python
- Python进阶
---
#### Python csv模块
Python的cvs模块可以实现csv文件读写操作，只需要在脚本中`import csv`模块。
Python的cvs模块在线手册：https://docs.python.org/2/library/csv.html

#### Python读csv文件
``` python
import csv

csvfile = file(filename, 'rb')
reader = csv.reader(csvfile)
for line in reader:
	print line
	
csvfile.close() 
```
获取csv文件行数：`lines = sum(1 for line in reader)`

#### Python写csv文件
``` python
import csv

csvfile = file(filename, 'wb')
writer = csv.writer(csvfile)
'''写一行'''
writer.writerow(['姓名', '年龄', '电话'])
data = [
	('张三', '20', '18645674567'),
	('李四', '22', '13511224567'),
	('王五', '24', '18833444567')
]
'''写多行'''
writer.writerows(data)

csvfile.close()
```

#### Python读写csv文件示例
读写csv文件 cvs_handler.py示例：
1.读取inputfile文件内容，并保存到row_contents列表中；
2.将row_title和row_contents列表重新写到outputfile文件中；
3.执行：`python cvs_handler.py personInfo.csv result.csv`
```python
#!/usr/bin/env python                                                                                                            
# -*- coding:utf-8 -*-
import os
import csv
import sys
from time import time

def cvs_file_read(filename): 
    if not os.path.isfile(filename):
        print ("%s is not file." % filename)
        return None

    try:
        csvfile = file(filename, 'rb')
        reader = csv.reader(csvfile)
    except:
        print ("read %s open error." % filename)
        return None
	
    headers = next(reader)
    row_contents = []
    for i, line in enumerate(reader):
    	print i, line
	row_contents.append(line)

    csvfile.close()
    return row_contents

def csv_file_write(filename, row_title, row_contents):
    try:
        csvfile = file(filename, 'wb')
        writer = csv.writer(csvfile)
    except:
        print ("write %s open error." % filename)
        return

    writer.writerow(row_title)
    writer.writerows(row_contents)

    csvfile.close()

def get_opt_init(argv):
    if len(argv) < 3:
        print "python cvs_handler.py inputfile outputfile"
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

    row_contents = cvs_file_read(inputfile)
    if not row_contents:
        sys.exit(0)
		
    row_title = ["姓名", "年龄", "电话"]
    csv_file_write(outputfile, row_title, row_contents)

    print "Time cost %.2fs." % (time() - start)
```
personInfo.csv文件内容如下所示：
```bash
[root@10.127.20.32 cvs]# cat personInfo.csv 
姓名,年龄,电话
张三,20,18645674567
李四,22,13511224567
王五,24,18833444567
```
