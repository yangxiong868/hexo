---
title: 'C/C++时间结构体与获取函数'
date: 2017-10-06 21:27:35
categories:
- C/C++
tags:
- C
- C++
- Linux系统编程
---
### 时间结构体
C/C++中常用的时间结构体有三种：time_t、struct tm、struct timeval。
#### time_t时间值
time_t时间值在time.h中定义如下：
```cpp
#ifndef __TIME_T  
#define __TIME_T  
typedef  long  time_t;  
#endif  
```
time_t是一个long型，表示从UTC时间(1970年1月1日00时00分00秒)到当前系统时刻的秒数。使用`time()`函数可以获取当前系统时间time_t的值。
#### struct tm时间结构体
由于time_t以秒为单位表示可读性差，所以需要一个可以表示当前系统时间（年、月、日、时、分、秒）方式的数据结构struct tm。struct tm结构体也在time.h中定义如下：
```cpp
struct tm {
   int tm_sec;    /* 秒,取值范围(0~59)，但当遇到闰秒时则会有60秒的取值。 */
   int tm_min;    /* 分钟数，取值范围(0-59) */
   int tm_hour;   /* 小时数，取值范围(0-23) */
   int tm_mday;   /* 当天在这个月中是第几天，取值范围(1-31) */
   int tm_mon;    /* 当前月份是第几个月，取值范围(0-11) */
   int tm_year;   /* 从1900年开始至今的年数，即(Year - 1900)的值 */
   int tm_wday;   /* 当天在本周是第几天，取值范围(0-6, Sunday = 0) */
   int tm_yday;   /* 当天在今年是第几天，取值范围(0-365, 1 Jan = 0) */
   int tm_isdst;  /* 夏令时标记，值大于0表示夏令时生效；等于0表示夏令时失效；小于0表示数据不可用。 */
   char	*tm_zone; /* 时区名称，根据系统不同可能不被声明或不同全名。 */
};
```
使用`localtime()`和`gmtime()`函数可以把time_t时间值转换成struct tm。
#### struct timeval结构体
由于time_t只能表示秒级时间粒度，而struct timeval结构体可以表示微秒级，其中tv_sec表示当前系统时刻的秒数，tv_usec表示当前系统时刻的微秒数，1秒 = 1000000微秒。struct timeval结构体在time.h中定义如下：
```cpp
/* A time value that is accurate to the nearest
   microsecond but also has a range of years.  */
struct timeval
{
    __time_t tv_sec;		/* Seconds.  */
    __suseconds_t tv_usec;	/* Microseconds.  */
};
```
使用`gettimeofday()`函数获取当前系统时间struct timeval结构体的值。
### 时间获取函数
主要介绍四个常用的时间获取函数：`time()`、`gmtime()`、`localtime()`、`gettimeofday()`。
#### time()函数
**头文件**：`#include <time.h>`
**函数定义**：`time_t time (time_t *t)`
**功能描述**：该函数返回从UTC时间(1970年1月1日00时00分00秒)到当前系统所经过的秒数。
**返回值**：成功则返回秒数，失败则返回((time_t)-1)值，错误原因存于errno中。
#### gmtime()函数
**头文件**：`#include <time.h>`
**函数定义**：`struct tm *gmtime(time_t const *timep)`
**功能描述**：该函数将参数timep指向的time_t时间值转换成以tm结构体表示的世界标准时间UTC。
**返回值**：返回结构体tm代表目前UTC 时间。
#### localtime()函数
**头文件**：`#include <time.h>`
**函数定义**：`struct tm *localtime(time_t const *timep)`
**功能描述**：该函数将参数timep指向的time_t时间值转换成以tm结构体表示的本地时间（如北京时间）。
**返回值**：返回结构体tm代表目前UTC 时间。
>说明：以北京时间为例，gmtime()得到的结果比localtime()要提前(早)8小时。

#### gettimeofday()函数
**头文件**：`#include <time.h>`
**函数定义**：`int gettimeofday (struct timeval *__restrict __tv, __timezone_ptr_t __tz)`
**功能描述**：该函数把当前的时间信息存入tv指向的结构体中，把当前时区信息存入tz指向的结构体中，如果tz为NULL则不向tz写入。
**返回值**：成功则返回0，失败则返回-1值，错误原因存于errno中。
### 时间格式化字符串
时间格式化字符串三个常用的函数有： `ctime()`、`asctime()`、`strftime()`、`strptime()`。
#### ctime()函数
**头文件**：`#include <time.h>`
**函数定义**：`char *ctime(const time_t *timep)`
**功能描述**：将参数timep时间值转换成实际使用的时间日期表示方法。
**返回值**：以字符串形式返回。字符串格式为："Wed Jun 20 21:00:00 2012\n"。
#### asctime()函数
**头文件**：`#include <time.h>`
**函数定义**：`char *asctime(const struct tm *tm)`
**功能描述**：将参数tm结构体转换成实际使用的时间日期表示方法。
**返回值**：以字符串形式返回。字符串格式为："Wed Jun 20 21:00:00 2012\n"。
>说明：`ctime()`和`asctime()`的区别是函数的入参不同，返回的字符串格式化相同。

#### strftime()函数
**头文件**：`#include <time.h>`
**函数定义**：`size_t strftime(char *s, size_t max, const char *format, const struct tm *tm)`
**功能描述**：格式化时间字符串，可以根据format指向字符串中格式命令把tm中保存的时间信息放在s指向的字符串中，最多向s中存放max个字符。 
**返回值**：向s指向的字符串中放置的字符数。

`strftime()`函数的操作有些类似于`sprintf()`：识别以百分号(%)开始的格式命令集合，格式化输出结果放在一个字符串中。
下面仅挑几个常用的来说：

| 格式化参数  |    含义  |
| :--------: | :--------: |
|%Y | 完整的年数字 |
|%m | 月份，如月份是1~9,则数字前填充一个’0’ |
|%d | 日子 |
|%F | 等同于“%Y-%m-%d” |
|%H | 小时数 |
|%M | 分钟数 |
|%S | 秒数 |
|%_m | 月份，如果月份是1~9，则数字前有一个空格填充 |
|%-m | 月份，如果月份是1~9，仍只显示该数字 |

#### strptime()函数
**头文件**：`#include <time.h>`
**函数定义**：` char *strptime(const char *s, const char *format, struct tm *tm)`
**功能描述**：将一个字符串格式化为一个tm结构，功能与strftime相反，根据format指向字符串中格式命令把s指向的字符串转换存储到tm中。 
**返回值**：指向转换过程处理的最后一个字符后面的那个字符。
### 时间代码示例
运用上述介绍的结构体和函数编写的C语言代码如下：
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>

int main(int argc, char *argv[])
{
    time_t calendar_time;
    struct tm *tm_local;
    struct timeval start,end;
    long dif_sec, dif_usec, j;
 
    time(&calendar_time);
    //calendar_time = time(NULL);

    printf("calendar_time: %ld\n", calendar_time);

    tm_local = localtime(&calendar_time);
    printf("\nlocaltime :year=%d mon=%d mday=%d hour=%d min=%d sec=%d\n",tm_local->tm_year + 1900, tm_local->tm_mon + 1, tm_local->tm_mday, tm_local->tm_hour, tm_local->tm_min, tm_local->tm_sec);

    printf("asctime: %s\n", asctime(tm_local));
    printf("ctime: %s\n", ctime(&calendar_time));

    char strtime[128];
    strftime(strtime, sizeof(strtime), "%Y-%m-%d %H-%M-%S", tm_local);
    printf("localtime format: %s\n", strtime);

    //下面代码可以计算程序部分代码执行的时间(微秒)
    gettimeofday(&start, NULL);

    for(int i = 0; i < 10000000; ++i)
	    j = 3.14 * i + 6.28 * i + 0.001 * i;

    gettimeofday(&end, NULL);
    dif_sec = end.tv_sec - start.tv_sec;
    dif_usec = end.tv_usec - start.tv_usec;
    printf("running time is %ld sec (%ld usec)\n", dif_sec, dif_sec*1000000 + dif_usec);

    return 0;
}
```
程序运行结果如下：
```
calendar_time: 1482079700

localtime :year=2016 mon=12 mday=18 hour=8 min=48 sec=20
asctime: Sun Dec 18 08:48:20 2016

ctime: Sun Dec 18 08:48:20 2016

localtime format: 2016-12-18 08-48-20

running time is 0 sec (97651 usec)
```

运用strftime和strptime函数编写的C语言代码如下：
```cpp
#include "stdio.h"  
int main(void)  
{  
    time_t lt = time(NULL);  
    struct tm* ptr = localtime(&lt);  
    char szBuffer[64] = {0};  
    const char* pFormat = "The time now is %Y-%m-%d %H:%M:%S";  
    strftime(szBuffer, 64, pFormat, ptr);  
    printf("%s\n", szBuffer);  
  
    struct tm tmTemp;  
    char tmBuffer[64] = {0};  
    strptime(szBuffer, pFormat, &tmTemp);//字符串转换成struct tm结构体
    strftime(tmBuffer, 64, "The time just was %Y-%m-%d %H:%M:%S", &tmTemp);  
    printf("%s\n", tmBuffer);  
    return 0;  
}  
```
程序运行结果如下：
```
The time now is 2016-12-19 10:39:24
The time just was 2016-12-19 10:39:24
```

获取当前时间戳和字符串形式时间转换时间戳代码如下：
``` cpp
#include <iostream>
#include <time.h>

time_t get_timestamp(const char *date = NULL,
                     const char *format = "%Y-%m-%d %H:%M:%S") {
  struct tm tm = {0};
  if (!date) {
    return time(NULL);
    // return absl::ToUnixMillis(absl::Now()); // 毫秒
    // return absl::ToTimeT(absl::Now()); // 秒
  }
  strptime(date, format, &tm);
  return mktime(&tm);
}

int main(void) {
  char date[] = "2018-02-10 19:00:00";
  time_t now = get_timestamp(date);
  std::cout << "date " << date << " to timestamp " << now << std::endl;
  
  now = get_timestamp();
  std::cout << "now timestamp " << now << std::endl;

  return 0;
}

```
程序运行结果如下：
```
date 2018-02-10 19:00:00 to timestamp 1518260400
now timestamp 1521676868
```

###参考链接：
1. http://sodino.com/2015/03/15/c-time/
2. http://blog.csdn.net/yasaken/article/details/7429506
3. Unix时间戳http://tool.chinaz.com/Tools/unixtime.aspx