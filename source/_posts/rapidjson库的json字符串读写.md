---
title: rapidjson库的json字符串读写
date: 2018-03-12 08:42:16
categories:
- C/C++
tags:
- C++
- Json
---
#### 1.rapidjson简介
rapidjson是腾讯的开源json解析框架，用c++实现。由于全部代码仅用header file实现，所以很容易集成到项目中。
* [RapidJSON GitHub](https://github.com/miloyip/rapidjson/)                                                                      
* RapidJSON 文档 ：[English](http://rapidjson.org/)，[简体中文](http://rapidjson.org/zh-cn/)，[GitBook](https://www.gitbook.com/book/miloyip/rapidjson/) ，[rapidjson代码剖析](http://miloyip.com/rapidjson/)
rapidjson安装
``` bash
unzip rapidjson-1.1.0.zip
cd rapidjson-1.1.0
cp -a include/rapidjson /usr/include/
```

#### 2.json字符串读写
最近在工作中使用rapidjson库实现json字符串操作，下面以读写json字符串为例进行整理。

``` cpp
#include <rapidjson/document.h>
#include <rapidjson/prettywriter.h>
#include <rapidjson/stringbuffer.h>
#include <rapidjson/writer.h>
#include <iostream>
#include <string>

std::string JsonToString(const rapidjson::Value &json) {
  rapidjson::StringBuffer str_buf;
  rapidjson::PrettyWriter<rapidjson::StringBuffer> writer(str_buf);
  json.Accept(writer);
  return str_buf.GetString();
}

bool JsonCheckField(const rapidjson::Value &json, const char *field_key,
                    bool (rapidjson::Value::*validator)() const,
                    bool is_required) {
  if (!json.HasMember(field_key)) {
    if (is_required) {
      std::cout << "Invalid json: " << JsonToString(json) << " , miss key "
                << field_key << std::endl;
    }
    return false;
  }

  if (!(json[field_key].*validator)()) {
    std::cout << "Invalid json: " << JsonToString(json) << " , invalid key "
              << field_key << std::endl;

    return false;
  }

  return true;
}

bool JsonParse(const std::string &data) {
  rapidjson::Document doc;
  if (doc.Parse(data.c_str()).HasParseError()) {
    std::cout << "Failed to parse json string: " << data
              << ", error is: " << doc.GetParseError() << std::endl;
    return false;
  }

  std::cout << "JsonParse data:" << std::endl;
  // Int64
  if (JsonCheckField(doc, "Int64", &rapidjson::Value::IsInt64, true)) {
    std::cout << "Int64 = " << doc["Int64"].GetInt64() << std::endl;
  }

  // Object
  if (JsonCheckField(doc, "Object", &rapidjson::Value::IsObject, true)) {
    const rapidjson::Value &object = doc["Object"];

    if (JsonCheckField(object, "name", &rapidjson::Value::IsString, true)) {
      std::cout << "Object.name = " << object["name"].GetString() << std::endl;
    }
    if (JsonCheckField(object, "age", &rapidjson::Value::IsInt, true)) {
      std::cout << "Object.age = " << object["age"].GetInt() << std::endl;
    }
  }
  // StringArray
  if (JsonCheckField(doc, "StringArray", &rapidjson::Value::IsArray, true)) {
    const rapidjson::Value &array = doc["StringArray"];
    size_t len = array.Size();
    for (size_t i = 0; i < len; i++) {
      std::cout << "StringArray[" << i << "] = " << array[i].GetString()
                << std::endl;
    }
  }

  // ObjectArray
  if (JsonCheckField(doc, "ObjectArray", &rapidjson::Value::IsArray, true)) {
    const rapidjson::Value &array = doc["ObjectArray"];
    size_t len = array.Size();
    for (size_t i = 0; i < len; i++) {
      const rapidjson::Value &object = array[i];
      if (object.IsObject()) {
        std::cout << "ObjectArray[" << i << "]:";
        if (JsonCheckField(object, "name", &rapidjson::Value::IsString, true)) {
          std::cout << "name = " << object["name"].GetString();
        }
        if (JsonCheckField(object, "age", &rapidjson::Value::IsInt, true)) {
          std::cout << ", age = " << object["age"].GetInt() << std::endl;
        }
      }
    }
  }

  return true;
}

void JsonSerialize(std::string *data) {
  rapidjson::StringBuffer str_buf;
  rapidjson::Writer<rapidjson::StringBuffer> writer(str_buf);

  writer.StartObject();

  // Int64
  writer.Key("Int64");
  writer.Int64(123456789);

  // Object
  writer.Key("Object");
  writer.StartObject();
  writer.Key("name");
  writer.String("zhangsan");
  writer.Key("age");
  writer.Int(28);
  writer.EndObject();

  // StringArray
  writer.Key("StringArray");
  writer.StartArray();
  writer.String("one");
  writer.String("tow");
  writer.String("three");
  writer.EndArray();

  // ObjectArray
  writer.Key("ObjectArray");
  writer.StartArray();
  for (int i = 0; i < 3; i++) {
    writer.StartObject();
    writer.Key("name");
    writer.String("wangwu");
    writer.Key("age");
    writer.Int(20 + i);
    writer.EndObject();
  }
  writer.EndArray();

  writer.EndObject();

  *data = str_buf.GetString();
  std::cout << "Json data: " << *data << std::endl;
}

int main(int argc, char *argv[]) {
  std::string data;

  JsonSerialize(&data);
  JsonParse(data);

  return 0;
}
```
```
程序运行结果如下：
JsonSerialize data: {"Int64":123456789,"Object":{"name":"zhangsan","age":28},"StringArray":["one","tow","three"],"ObjectArray":[{"name":"wangwu","age":20},{"name":"wangwu","age":21},{"name":"wangwu","age":22}]}

JsonParse data:
Int64 = 123456789
Object.name = zhangsan
Object.age = 28
StringArray[0] = one
StringArray[1] = tow
StringArray[2] = three
ObjectArray[0]:name = wangwu, age = 20
ObjectArray[1]:name = wangwu, age = 21
ObjectArray[2]:name = wangwu, age = 22
```

#### 3.参考资料
[RapidJSON 文档-简体中文](http://rapidjson.org/zh-cn/)
[rapidjson库的基本使用](http://blog.csdn.net/qq849635649/article/details/52678822)