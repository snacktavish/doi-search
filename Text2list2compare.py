# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:18:36 2019

@author: jvela
"""

import sys
inFile = sys.argv[1]
inFile2= sys.argv[2]

import json

with open(inFile, "r") as read_file:
    data = json.load(read_file) 

lit = []

for study in data['matched_studies']:
	if u'ot:studyPublication' in study:
	  x = study[u'ot:studyPublication']
	  lit.append(x)


with open(inFile2, "r") as read_fil:
    data2 = json.load(read_fil) 
    
lit2 = []

for studi in data2['matched_studies']:
	if u'ot:studyPublication' in studi:
	  y = studi[u'ot:studyPublication']
	  lit2.append(y)  
      
a = lit
b = lit2

def returnMatches(a,b):
  if len(list(set(a) & set(b))) > 0:
      return list(set(a) & set(b))
  else :
      print "no matches :("

print "These are the matches:" 
print ("\n".join(map(str, returnMatches(a,b))))
