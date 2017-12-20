#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import csv
import sys
from time import time

def cvs_file_read(filename): 
    if not os.path.isfile(filename):
        print ("%s is not file." % filename)
        return None

    try:
        csvfile = file(filename, 'rb')
        reader = csv.reader(csvfile)
    except:
        print ("read %s open error." % filename)
        return None
	
    headers = next(reader)
    row_contents = []
    for i, line in enumerate(reader):
    	print i, line
	row_contents.append(line)

    csvfile.close()
    return row_contents

def csv_file_write(filename, row_title, row_contents):
    try:
        csvfile = file(filename, 'wb')
        writer = csv.writer(csvfile)
    except:
        print ("write %s open error." % filename)
        return

    writer.writerow(row_title)
    writer.writerows(row_contents)

    csvfile.close()

def get_opt_init(argv):
    if len(argv) < 3:
        print "python cvs_handler.py inputfile outputfile"
        return None

    if len(argv) >= 3:
        inputfile = argv[1]
        outputfile = argv[2]
                   
    return inputfile, outputfile 

if __name__=="__main__" :
    start = time()

    inputfile, outputfile = get_opt_init(sys.argv)
    if not inputfile and outputfile:
        sys.exit(0)

    row_contents = cvs_file_read(inputfile)
    if not row_contents:
        sys.exit(0)
		
    row_title = ["姓名", "年龄", "电话"]
    csv_file_write(inputfile[:-4]+"_result.csv", row_title, row_contents)

    print "Time cost %.2fs." % (time() - start)
