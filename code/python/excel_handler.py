#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import os
import sys

import xlrd
import xlwt

from time import time

def excel_file_read(filename): 
    if not os.path.isfile(filename):
        print ("%s is not file." % filename)
        return None

    try:
        book = xlrd.open_workbook(filename)
        sh = book.sheet_by_index(0)
    except:
        print ("read %s open error." % filename)
        return None

    print("Sheet name:%s, nrows:%d, ncols:%d" % (sh.name, sh.nrows, sh.ncols))

    row_contents = []
    for rx in range(sh.nrows):
        row_content = []
        for cx in range(sh.ncols):
            #print sh.cell_value(rx, cx)
            row_content.append(sh.cell_value(rx, cx))
        row_contents.append(row_content)
    #print row_contents
    
    return row_contents[1:]

def excel_file_write(filename, row_title, row_contents):
    try:
        wb = xlwt.Workbook()
        ws = wb.add_sheet("Sheet1")
    except:
        print ("write %s open error." % filename)
        return

    for col, col_content in enumerate(row_title):
        #print col, col_content
        ws.write(0, col, col_content)

    for row, row_content in enumerate(row_contents):
        for col, col_content in enumerate(row_content):
            #print col, col_content
            ws.write(row + 1, col, col_content)

    wb.save(filename)

def get_opt_init(argv):
    if len(argv) < 3:
        print "python excel_handler.py inputfile outputfile"
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

    row_contents = excel_file_read(inputfile)
    if not row_contents:
        sys.exit(0)
		
    row_title = [u'姓名', u'年龄', u'电话']
    excel_file_write(outputfile, row_title, row_contents)

    print "Time cost %.2fs." % (time() - start)
