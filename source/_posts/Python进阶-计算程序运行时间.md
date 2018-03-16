---
title: Python进阶-计算程序运行时间
date: 2018-03-11 21:30:23
categories:
- Python
tags:
- Python
- Python进阶
---
#### 计算程序运行时间方法1
Python的time模块包含很多与时间相关函数。我们可通过它获得当前的时间和格式化时间输出。
``` python
from time import time

def timeTest():
    start = time()
    print("Start: " + str(start))
    
    for i in range(1, 100000000):
        pass
    stop = time()
    
    print("Stop: " + str(stop))
    print(str(round(stop-start, 2)) + "秒")

def main():
    timeTest()

if __name__=='__main__':
    main()
```

#### 计算程序运行时间方法2
[Python: 使用装饰器“@”取得函数执行时间](https://blog.oldj.net/2010/05/22/decorator-get-execution-time/)
