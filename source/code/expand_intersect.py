#coding:utf-8
import os
inter = set(open('../extracted/expand/intersect').read().strip().split('\n'))
for dp, dns, fns in os.walk('../lexDic/1234/'):
  for fn in fns:
    f=open(dp+fn)
    ns=set(f.read().strip().split('\n'))
    f.close()
    f=open('../extracted/expand/'+fn.split('.')[0]+'.diff','w')
    for w in (ns - inter):
      f.write(w+'\n')
    f.close()

