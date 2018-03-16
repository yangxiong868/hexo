---
title: C/C++字符串分隔方法
date: 2018-03-11 22:04:52
categories:
- C/C++
tags:
- C
- C++
- 字符串
---
#### 1.用strtok函数实现
原型：char *strtok(char *str, const char *delim);
功能：分解字符串为一组字符串。
参数说明：str为要分解的字符串，delim为分隔符字符串。
返回值：从str开头开始的一个个被分割的串。当没有被分割的串时则返回NULL。

 示例代码和运行结果：
```cpp
#include <stdio.h>
#include <string.h>

int main() {
  char s[] = "aaa/bbb,ccc/ddd";
  const char *d = ",/";
  char *p;
  p = strtok(s, d);
  while (p) {
    printf("%s\n", p);
    p = strtok(NULL, d);
  }

  return 0;
}
```

``` bash
运行结果
aaa
bbb
ccc
ddd
```

#### 2.用boost库的split函数实现
boost库在头文件<boost/algorithm/string.hpp>中提供了split函数处理字符串分隔。
原型：template<typename SequenceSequenceT, typename RangeT, typename PredicateT> 
  SequenceSequenceT & 
  split(SequenceSequenceT & Result, RangeT & Input, PredicateT Pred, 
        token_compress_mode_type eCompress = token_compress_off);
功能：以Pred为分隔符分隔Input字符串。
参数说明：如果eCompress参数设置为token_compress_on，则相邻分隔符合并在一起。 否则，每两个分隔符分隔一个标记。str为要分解的字符串，delim为分隔符字符串。
返回值：分割后的字符串存放在Result容器中。

 示例代码和运行结果：
```cpp
#include <boost/algorithm/string/classification.hpp>                                                                             
#include <boost/algorithm/string/split.hpp>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string s = "aaa/bbb,ccc/ddd";
  vector<string> vStr;
  boost::split(vStr, s, boost::is_any_of(",/"), boost::token_compress_on);
  for (vector<string>::iterator it = vStr.begin(); it != vStr.end(); ++it){
    cout << *it << endl;
  }
  return 0;
}
```

``` bash
运行结果
aaa
bbb
ccc
ddd
```