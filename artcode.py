# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:13:14 2019

@author: jvela
"""
import sys
inFile = sys.argv[1]

from xlrd import open_workbook

book = open_workbook(inFile)
sheet = book.sheet_by_index(0) 

column1 = []
column2 = []

for row in range(0, 6): 
    column1.append(str(sheet.cell(row, 0)))
    column2.append(str(sheet.cell(row, 1)))


a = column1
b = column2

def returnMatches(a,b):
  return list(set(a) & set(b))

print "These are the matches:" 
print ("\n".join(map(str, returnMatches(a,b))))
