---
title: C++ String删除所有的某个特定字符
date: 2018-03-16 08:41:13
categories:
- C/C++
tags:
- C
- C++
- 字符串
---
#### 1.remove和erase函数实现
我们利用std::remove和boost::algorithm::erase函数实现从String中删除所有的某个特定字符，代码如下：
`s.erase(std::remove(s.begin(), s.end(), ':'), s.end());`
其中std::remove模板函数
``` cpp
template< class ForwardIt, class T >
ForwardIt remove( ForwardIt first, ForwardIt last, const T& value );
template< class ForwardIt, class UnaryPredicate >
ForwardIt remove_if( ForwardIt first, ForwardIt last, UnaryPredicate p );
```
从范围 [first, last) 移除所有满足特定判别标准的元素，并返回**范围新结尾的尾后迭代器**。
1) 移除所有等于 value 的元素。2) 移除所有 p 对于它返回 true 的元素。

代码示例：
```cpp
#include <boost/algorithm/string.hpp>
#include <iostream>
#include <string>

using namespace boost::algorithm;

int main() 
{
  std::string s = "08:EF:13:AB:88:BI";
  s.erase(std::remove(s.begin(), s.end(), ':'), s.end());
  std::cout << s << '\n';
}
```

运行结果：
``` bash
08EF13AB88BI
```

#### 2.remove_erase函数实现
boost库remove_erase函数源码是采用remove和erase方法实现。
代码示例：
```cpp
#include <boost/range/algorithm_ext.hpp>
#include <iostream>
#include <string>

int main() 
{
  std::string s = "08:EF:13:AB:88:BI";
  boost::range::remove_erase(s, ':');
  std::cout << s << '\n';
}
```

运行结果：
``` bash
08EF13AB88BI
```

#### 3.参考链接
1.[C++从string中删除所有的某个特定字符](http://lzl124631x.github.io/2017/01/22/remove-char-in-string-cpp.html)
2.[std::remove, std::remove_if](http://zh.cppreference.com/w/cpp/algorithm/remove)
3.[remove_erase documentation](http://www.boost.org/doc/libs/1_46_0/libs/range/doc/html/range/reference/algorithms/new/remove_erase.html)
4.[remove_erase source code](http://www.boost.org/doc/libs/1_60_0/boost/range/algorithm_ext/erase.hpp)

