#coding:utf-8
import os
s=set()
for dp, dns, fns in os.walk('../lexDic/1234/'):
  for fn in fns:
    f=open(dp+fn)
    ns=set(f.read().strip().split('\n'))
    if not len(s):
      s = ns
    else:
      s = s & ns
    f.close()
f=open('../extracted/expand/intersect','w')
for i in s:
  f.write(i+'\n')
f.close()
