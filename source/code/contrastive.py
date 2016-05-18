#coding:utf-8

import re
from nlpir import *
f=open('../lexDic/1234/c30175.pure')
t=f.read().strip().decode('utf-8').split('\n')
f.close()
tag = 0
expand = 0
for w in t:
  temp = re.split(r'[ ]+',ParagraphProcess(' '.join(w).encode('utf-8'),c_int(1)).strip())
  tags = map(lambda x:x.split('/')[1][0],temp)
  if not all(map(lambda x:x in ['n','v','a'],tags)):
    continue
  if tags[0] == tags[2] and tags[1] == tags[3]:
    tag += 1
  elif tags[1] == tags[3]:
    biw = w[0]+w[2]
    if len(ParagraphProcess(biw.encode('utf-8'),c_int(1)).split('/')) == 2:
      expand += 1
      continue
    biw = w[2]+w[0]
    if len(ParagraphProcess(biw.encode('utf-8'),c_int(1)).split('/')) == 2:
      expand += 1
      continue
  elif tags[0] == tags[2]:
    biw = w[1]+w[3]
    if len(ParagraphProcess(biw.encode('utf-8'),c_int(1)).split('/')) == 2:
      expand += 1
      continue
    biw = w[3]+w[1]
    if len(ParagraphProcess(biw.encode('utf-8'),c_int(1)).split('/')) == 2:
      expand += 1
      continue
  else:
    biw1 = w[0]+w[2]
    biw2 = w[1]+w[3]
    if len(ParagraphProcess(biw1.encode('utf-8'),c_int(1)).split('/')) + len(ParagraphProcess(biw2.encode('utf-8'),c_int(1)).split('/')) == 4:
      expand += 1
      continue
    biw1 = w[2]+w[0]
    biw2 = w[3]+w[1]
    if len(ParagraphProcess(biw1.encode('utf-8'),c_int(1)).split('/')) + len(ParagraphProcess(biw2.encode('utf-8'),c_int(1)).split('/')) == 4:
      expand += 1
print tag #=13369;5788
print expand #=7779;4985
'''
import json
f=open('../extracted/json/full_dict_30175')
d=json.loads(f.read())
f.close()
d2={}
for mode in ['13','24']:
  for c in d[mode]:
    for i in d[mode][c]:
      if i not in d2:
        d2[i] = True
print len(d2)
'''
