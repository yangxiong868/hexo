---
title: 'Python基础-枚举类'
date: 2017-12-19 23:03:35
categories:
- Python
tags:
- Python
- Python基础
---
Python基础枚举类有两种实现方法
第一种方法：定义常量，变量名称大写，例如月份：
``` python
JAN = 1
FEB = 2
MAR = 3
...
NOV = 11
DEC = 12
```
第二种方法：从Enum派生出自定义枚举类，unique装饰器可以帮助我们检查保证没有重复值，例如星期：
```python
from enum import Enum, unique
 
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```
访问枚举类型的若干方法如下，可见在实际使用中既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
```python
>>> print (Weekday.Mon)
Weekday.Mon
>>> print (Weekday['Tue'])
Weekday.Tue
>>> type(Weekday.Mon)
<enum 'Weekday'>
>>> print(Weekday.Mon.value)
1
>>> print(Weekday(1))
Weekday.Mon
>>> for name, member in Weekday.__members__.items():
...      print(name, '=>', member)
... 
('Sun', '=>', <Weekday.Sun: 0>)
('Mon', '=>', <Weekday.Mon: 1>)
('Tue', '=>', <Weekday.Tue: 2>)
('Wed', '=>', <Weekday.Wed: 3>)
('Thu', '=>', <Weekday.Thu: 4>)
('Fri', '=>', <Weekday.Fri: 5>)
('Sat', '=>', <Weekday.Sat: 6>)
>>> 
```
