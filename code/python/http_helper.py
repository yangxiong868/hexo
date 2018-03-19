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
