#coding:utf-8
import os

union = set()

for dp,dn,fns in os.walk("../lexDic/1234"):
  for fn in fns:
    if fn[-5:] != '.pure':
      continue
    f = open(dp+'/'+fn,'rb')
    print('processing '+fn+' ...')
    ls = f.read().split('\n')
    f.close()
    if ls[-1] == '':
      ls = ls[:-1]
    union |= set(ls)

f = open("../lexDic/union/united_dict.pure","wb")
for i in sorted(list(union)):
  f.write(i+'\n')
f.close()
