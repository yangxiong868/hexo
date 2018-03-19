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
