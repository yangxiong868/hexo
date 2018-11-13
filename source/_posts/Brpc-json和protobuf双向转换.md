---
title: Brpc json和protobuf双向转换
date: 2018-10-20 20:09:56
categories:
- Brpc
tags:
- Brpc
- Json
---
### json2pb介绍
brpc支持json和protobuf间的双向转化，实现于[json2pb](https://github.com/brpc/brpc/tree/master/src/json2pb/)。

### json2pb接口
json2pb提供json到protobuf接口函数：`JsonToProtoMessage`，包含头文件：`<json2pb/json_to_pb.h>`，下面列举一个接口定义如下：
``` cpp
bool JsonToProtoMessage(const std::string& json,
                        google::protobuf::Message* message,
                        const Json2PbOptions& options,
                        std::string* error = NULL);
```
json2pb提供protobuf到json接口函数：`ProtoMessageToJson`，包含头文件：`<json2pb/pb_to_json.h>`，下面列举一个接口定义如下：
``` cpp
bool ProtoMessageToJson(const google::protobuf::Message& message,
                        std::string* json,
                        const Pb2JsonOptions& options,
                        std::string* error = NULL);
```

### json2pb应用
brpc json2pb的接口应用示例如下，addressbook.proto在brpc源码test文件中。
```cpp
#include <gflags/gflags.h>
#include <glog/logging.h>
#include <iostream>
#include <string>

#include <json2pb/json_to_pb.h>
#include <json2pb/pb_to_json.h>

#include "ads/serving/Json/addressbook.pb.h"
#include "butil/iobuf.h"

using addressbook::AddressBook;
using addressbook::Person;

void PopulateAddressBookMessage(AddressBook* address_book) {
  Person* person = address_book->add_person();

  person->set_id(100);
  person->set_name("Test");
  person->set_data(-240000000);
  person->set_data32(6);
  person->set_data64(-1820000000);
  person->set_datadouble(123.456);
  person->set_datadouble_scientific(1.23456789e+08);
  person->set_datafloat_scientific(1.23456789e+08);
  person->set_datafloat(8.6123);
  person->set_datau32(60);
  person->set_datau64(960);
  person->set_databool(0);
  person->set_databyte("welcome to china");
  person->set_datafix32(1);
  person->set_datafix64(666);
  person->set_datasfix32(120);
  person->set_datasfix64(-802);
}

bool JsonToProtoMessageTest(const butil::IOBuf input,
                            google::protobuf::Message* message) {
  std::string error;
  json2pb::Json2PbOptions options;
  options.base64_to_bytes = true;

  butil::IOBufAsZeroCopyInputStream stream(input);
  if (!json2pb::JsonToProtoMessage(&stream, message, options, &error)) {
    LOG(ERROR) << "Failed to JsonToProtoMessage err:" << error;
    return false;
  }

  return true;
}

bool ProtoMessageToJsonTest(const google::protobuf::Message& message,
                            butil::IOBuf* output) {
  std::string error;
  json2pb::Pb2JsonOptions options;
  options.enum_option = json2pb::OUTPUT_ENUM_BY_NUMBER;
  options.bytes_to_base64 = true;

  butil::IOBufAsZeroCopyOutputStream stream(output);
  if (!json2pb::ProtoMessageToJson(message, &stream, options, &error)) {
    LOG(ERROR) << "Failed to ProtoMessageToJson err:" << error;
    return false;
  }

  return true;
}

void Json2PbTest() {
  bool result;
  butil::IOBuf buf;

  // ProtoMessageToJsonTest
  LOG(ERROR) << "ProtoMessageToJsonTest......";
  AddressBook address_book;
  PopulateAddressBookMessage(&address_book);
  LOG(ERROR) << "ProtoBuf:" << address_book.DebugString();

  result = ProtoMessageToJsonTest(address_book, &buf);
  LOG(ERROR) << "result: " << result << " Json:" << buf;

  // ProtoMessageToJsonTest
  LOG(ERROR) << "JsonToProtoMessageTest......";
  AddressBook address_book1;
  result = JsonToProtoMessageTest(buf, &address_book1);
  LOG(ERROR) << "result: " << result
             << "ProtoBuf:" << address_book1.DebugString();
}

int main(int argc, char* argv[]) {
  google::InitGoogleLogging(argv[0]);
  FLAGS_logtostderr = 1;

  Json2PbTest();

  return 0;
}
```
程序运行结果如下：
```
E1019 16:09:41.195989 26059 json2pb_test.cpp:73] ProtoMessageToJsonTest......
E1019 16:09:41.196545 26059 json2pb_test.cpp:76] ProtoBuf:person {
  name: "Test"
  id: 100
  data: -240000000
  data32: 6
  data64: -1820000000
  datadouble: 123.456
  datafloat: 8.6123
  datau32: 60
  datau64: 960
  databool: false
  databyte: "welcome to china"
  datafix32: 1
  datafix64: 666
  datasfix32: 120
  datasfix64: -802
  datafloat_scientific: 1.2345679e+08
  datadouble_scientific: 123456789
}
E1019 16:09:41.196682 26059 json2pb_test.cpp:78] result: 1 Json:{"person":[{"name":"Test","id":100,"data":-240000000,"data32":6,"data64":-1820000000,"datadouble":123.456,"datafloat":8.612299919128418,"datau32":60,"datau64":960,"databool":false,"databyte":"d2VsY29tZSB0byBjaGluYQ==","datafix32":1,"datafix64":666,"datasfix32":120,"datasfix64":-802,"datafloat_scientific":123456792.0,"datadouble_scientific":123456789.0}]}
E1019 16:09:41.196696 26059 json2pb_test.cpp:81] JsonToProtoMessageTest......
E1019 16:09:41.196838 26059 json2pb_test.cpp:84] result: 1ProtoBuf:person {
  name: "Test"
  id: 100
  data: -240000000
  data32: 6
  data64: -1820000000
  datadouble: 123.456
  datafloat: 8.6123
  datau32: 60
  datau64: 960
  databool: false
  databyte: "welcome to china"
  datafix32: 1
  datafix64: 666
  datasfix32: 120
  datasfix64: -802
  datafloat_scientific: 1.2345679e+08
  datadouble_scientific: 123456789
}
```

### 参考链接
1.[brpc json2pb 介绍](https://github.com/brpc/brpc/blob/master/docs/cn/json2pb.md)
2.[brpc json2pb 源码](https://github.com/brpc/brpc/tree/master/src/json2pb/)