---
title: Python进阶-Pyinotify文件系统监控
date: 2018-03-17 00:23:27
categories:
- Python
tags:
- Python
- Python进阶
- Pyinotify
---
#### Pyinotify介绍
Pyinotify 是一个简单而有用的 Python 模块，它可用于在 Linux 中实时监控文件系统更改。它依赖于 inotify（在内核 2.6.13 中纳入的 Linux 内核功能），它是一个事件驱动的通知程序，其通知通过三个系统调用从内核空间导出到用户空间。Pyinotify 既可以监视文件，也可以监视目录。
#### Pyinotify示例
最近在工作中有个需求：监控业务数据文件的创建事件。在网上查找用 pyinotify模块可以很容易的实时监控文件系统更改或修改。
``` python
#!/usr/bin/env python
#coding = utf-8
import os
from pyinotify import WatchManager, Notifier, ProcessEvent
from pyinotify import IN_DELETE, IN_CREATE, IN_MODIFY

class EventHandler(ProcessEvent):
     def process_IN_CREATE(self, event): 
         event_file = os.path.join(event.path, event.name)
         print "create file: %s " % event_file 

     def process_IN_DELETE(self, event): 
         event_file = os.path.join(event.path, event.name)
         print "delete file: %s " % event_file 

     def process_IN_MODIFY(self, event): 
         event_file = os.path.join(event.path, event.name)
         print "modify file: %s " % event_file 

def FSMonitor(path='.'):
     wm = WatchManager()
     mask = IN_DELETE | IN_MODIFY | IN_CREATE
     notifier = Notifier(wm, EventHandler())
     wm.add_watch(path, mask, rec=True, auto_add=True)
     print "now starting monitor %s." % path

     while True:
          try:
               notifier.process_events()
               if notifier.check_events():
                   notifier.read_events()
          except KeyboardInterrupt:
               notifier.stop()
               break

if __name__ == "__main__":
     FSMonitor()
```
