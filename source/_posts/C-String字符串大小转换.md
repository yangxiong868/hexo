---
title: C++ String字符串大小转换
date: 2018-03-16 07:34:05
categories:
- C/C++
tags:
- C
- C++
- 字符串
---
#### 1.Boost.StringAlgorithms库大小转换函数
大小写转换API：
boost::algorithm::to_upper_copy()  
boost::algorithm::to_lower_copy() 
boost::algorithm::to_upper() //修改原string字符串
boost::algorithm::to_lower() //修改原string字符串

代码示例：
```cpp
#include <boost/algorithm/string.hpp>
#include <string>
#include <iostream>

using namespace boost::algorithm;

int main()
{
  std::string s = "Boost C++ Libraries";
  std::cout << to_upper_copy(s) << std::endl;
}
```

运行结果：
``` bash
BOOST C++ LIBRARIES
```

#### 2.STL库transform模板函数实现
我们利用STL库提供transform模板函数，动作是toupper或tolower，完成std::string大(小)写转换的功能。

代码示例：
```cpp
#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>

int main() 
{
  std::string s = "Boost C++ Libraries";
  std::transform(s.begin(), s.end(), s.begin(), ::toupper);
  // std::transform(s.begin(), s.end(), s.begin(), ::tolower);
  std::cout << s << std::endl;
}
```

运行结果：
``` bash
BOOST C++ LIBRARIES
```

#### 3.参考链接
1.[Chapter 5. Boost.StringAlgorithms](https://theboostcpplibraries.com/boost.stringalgorithms)
2.[string转化大小写(C++)](http://www.vimer.cn/archives/495.html)
3.[std::transform](http://zh.cppreference.com/w/cpp/algorithm/transform)
