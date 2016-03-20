#coding:utf-8
import json
f=open('../extracted/json/full_dict')
d=json.loads(f.read())
f.close()
count = 0
for c in d['13']:
  if c[0] == c[2]:
    count += 1
    print c + ' '+str(len(d['13'][c]))+ '\t'+'|'.join(d['13'][c])
print count

