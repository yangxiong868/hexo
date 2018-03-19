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
