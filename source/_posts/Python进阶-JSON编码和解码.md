---
title: Python进阶-JSON编码和解码
date: 2018-03-24 21:53:54
categories:
- Python
tags:
- Python
- Python进阶
- JSON
---
#### Python的JSON模块
JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。
Python内置类型和JSON数据类型的对应如下：
|   Python类型      |  JSON类型 |
| :--------------- | :-------- | 
| dict             |  object{} |
| list, tuple      |  array[]  |
| str, unicode     |  string   |
| int, long, float |  number   |
| True             |  true     |
| False            |  false    |
| None             |  null     |

#### JSON编码
json.dumps 用于将 Python 对象编码成 JSON 字符串。
**语法**
```python
json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)
```
- 如果ensure_ascii为true（默认值），则输出将保证所有传入的非ASCII字符都转义。如果ensure_ascii为false，则这些字符将按原样输出。
- 如果indent是非负整数或字符串，那么JSON数组元素和对象成员将以该缩进级别打印。缩进级别0，负数或""将只插入换行符。None（默认值）选择最紧凑的表示。使用正整数缩进缩进，每个级别有许多空格。
- 如果sort_keys为真（默认值：False），则字典的输出将按键排序。

**实例**
以下实例将数组编码为 JSON 格式数据：
``` python
#!/usr/bin/python
import json

data = { 'a' : 1, 'b' : 2.0, 'c' : False, 'd' : True, 'e' : None, 'f' : [1, 2, 'str']}      

json = json.dumps(data)
print json
```

以上代码执行结果为：
``` bash
{"a": 1, "c": false, "b": 2.0, "e": null, "d": true, "f": [1, 2, "str"]}
```

使用参数让 JSON 数据格式化输出：
``` python
#!/usr/bin/python
import json

data = {"foo" : 1, "bar" : 2}

json = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
print json
```

以上代码执行结果为：
``` python
{
    "bar": 2,
    "foo": 1
}
```

#### JSON解码
json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
**语法**
```python
json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])
```
第一步：将json文本转换为python数据结构
第二步：按照操作字典的方法取值，取值之前先检查key和类型正确

**实例**
以下实例展示了Python 如何解码 JSON 对象：
``` python
#!/usr/bin/python                                                                                                                
import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print text
```

以上代码执行结果为：
``` bash
{u'a': 1, u'c': 3, u'b': 2, u'e': 5, u'd': 4}
```

以下实例展示了Python 解码 JSON 对象后检查key和操作字典：
``` python
#!/usr/bin/python
import json

def check_json_field(value, key):                                                                                                
    if not value.has_key(key): #检查key是否存在
        print("Invalid json missing key %s" % key)
        return False
    
    if not isinstance(value[key], dict): #检查key的value类型
        print("Invalid json invalid key %s" % key)
        return False

    return True

def main():
    jsonData = '{"test":{"a":1,"b":2.0,"c":false,"d":null,"e":"string"}}';

    text = json.loads(jsonData)
    print text
    if check_json_field(text, "test") is True:
        test = text.get("test")
        print("a=%d, b=%d, c=%d, d=%s, e=%s" % \
                (test.get("a"), test.get("b"), test.get("c"), test.get("d"), test.get("e")))

if __name__ == "__main__":
    main()
```

以上代码执行结果为：
``` bash
{u'test': {u'a': 1, u'c': False, u'b': 2.0, u'e': u'string', u'd': None}}
a=1, b=2, c=0, d=None, e=string
```

#### requests模块

以下实例展示了Python 解码 JSON 对象后检查key和操作字典：
``` python
#!/usr/bin/python
import json
import requests

def json_request():
    url = 'https://github.com/timeline.json'
    r = requests.get(url)
    data = r.json()
    for key, value in data.items():
        print("%s=%s" % (key, value))
		
json_request()
```

以上代码执行结果为：
``` bash
documentation_url=https://developer.github.com/v3/activity/events/#list-public-events
message=Hello there, wayfaring stranger. If you’re reading this then you probably didn’t see our blog post a couple of years back announcing that this API would go away: http://git.io/17AROg Fear not, you should be able to get what you need from the shiny new Events API instead.
```

#### 参考资料 
1.[Python JSON教程](http://www.runoob.com/python/python-json.html)
2.[python 读写 json文件](https://zhuanlan.zhihu.com/p/27917664)
3.[运维那点事-Python模块：json](http://www.ywnds.com/?p=10415)
4.[Python JSON Documentation](https://docs.python.org/2/library/json.html)
5.[python-requests快速上手](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html#json)