---
title: Python进阶-urllib2模块http请求
date: 2018-03-19 23:32:40
categories:
- Python
tags:
- Python
- Python进阶
- urllib2
---
#### Python的http请求类
最近工作基于urllib2模块实现一个httpHelper类，该类的使用方法：
1.设置http header，URL，timeout，RetryTimes等；
2.调用get，post，put，delete方法；

``` python
#!/usr/bin/env python
# -*-coding:utf-8 -*-
import logging
import urllib2
import time

__metaclass = type

class HttpHelper:
    def __init__(self):
        pass

    name = 'http helper'
    __reqHeader = {}
    __reqUrl = ''
    __reqTimeOut = 30
    __reqRetryTimes = 5
    __reqRetryIntervalTime = 5

    def headers(self, headers):
        self.__reqHeader = headers
        return self
    
    def url(self, url):
        logging.debug("request url: %s" % url)
        self.__reqUrl = url
        return self

    def timeOut(self, time=30):
        self.__reqTimeOut = time
        return self

    def retryTime(self, times=3, interval_time=5):
        self.__reqRetryTimes = times
        self.__reqRetryIntervalTime = interval_time
        return self

    def debug(self):
        httpHandler = urllib2.HTTPHandler(debuglevel=1)
        httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
        opener = urllib2.build_opener(httpHandler, httpsHandler)
        urllib2.install_opener(opener)
        return self
    
    def __buildGetRequest(self):
        if len(self.__reqHeader) == 0:
            request = urllib2.Request(self.__reqUrl)
        else:
            request = urllib2.Request(self.__reqUrl, headers=self.__reqHeader)
        return request

    def __buildPostPutDeleteRequest(self, postData):
        if len(self.__reqHeader) == 0:
            request = urllib2.Request(self.__reqUrl, data=postData)
        else:
            request = urllib2.Request(self.__reqUrl, headers=self.__reqHeader, data=postData)
        return request

    def __handleResponse(self, request, func):
        for _ in range(self.__reqRetryTimes):
            try:
                if self.__reqTimeOut == 0:
                    res = urllib2.urlopen(request)
                else:
                    res = urllib2.urlopen(request, timeout=self.__reqTimeOut)
            except urllib2.HTTPError, e:
                logging.error("urlopen HTTPError code:%s. url:%s" % (e.code, e.geturl()))
                time.sleep(self.__reqRetryIntervalTime)
            except urllib2.URLError, e:
                logging.error("urlopen URLError code:%s. reason:%s" % (e.code, e.reason))
                time.sleep(self.__reqRetryIntervalTime)
            except Exception, e:
                logging.error("urlopen Exception Error:%s." % str(e))
                time.sleep(self.__reqRetryIntervalTime)
            else:
                func(res.read())
                break
        else:
            logging.error("urlopen over retry time %d error. url:%d." % (self.__reqRetryTimes, self.__reqUrl))
            return False 
        
        return True

    def get(self, func):
        request = self.__buildGetRequest()
        return self.__handleResponse(request, func)

    def post(self, postData, func):
        request = self.__buildPostPutDeleteRequest(postData=postData)
        return self.__handleResponse(request, func)

    def put(self, putData, func):
        request = self.__buildPostPutDeleteRequest(postData=putData)
        request.get_method = lambda: 'PUT'
        return self.__handleResponse(request, func)

    def delete(self, putData, func):
        request = self.__buildPostPutDeleteRequest(postData=putData)
        request.get_method = lambda: 'DELETE'
        return self.__handleResponse(request, func)

```

#### Python的http请求类示例
基于httpHelper类实现一个简单的get请求代码如下：
``` python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import os
from http_helper import HttpHelper 


def init_log():
    log_file = os.path.join("/tmp/", 'http_help_%d.log' % os.getpid())
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=log_file,
                        filemode='w')

class HttpHelperTest():
    def __init__(self):
        self.httpHelper = HttpHelper() 
        self.httpHelper.debug()

    def __handlerResponse(self, data):
        logging.debug("response data: %s" % data)

    def httpGet(self):
        url = "https://www.baidu.com/" 
        result = self.httpHelper.url(url).get(self.__handlerResponse)

def main():
    init_log()
    test = HttpHelperTest() 
    test.httpGet()

if __name__ == "__main__":
    main()

```

#### 3.参考链接
1.[urllib2 document](https://docs.python.org/2/library/urllib2.html)
2.[Retrying a web request in Python](https://codereview.stackexchange.com/questions/112868/retrying-a-web-request-in-python)