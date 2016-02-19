#coding:utf-8
import json
f=open('../lexDic/93050/union/1234')
t=f.read().strip().decode("utf-8").split('\n')
f.close()
wd=dict()
for w in t:
  wd[w] = 1
f=open('../lexDic/93050/extracted/json/full_dict')
d=json.loads(f.read())
f.close()
for mode in d:
  for c in d[mode]:
    if len(d[mode][c]) >= 11:
      for ins in d[mode][c]:
        wd[ins] = 0
f=open('../extracted/tri_slot/1234_11','wb')
for i in wd:
  if wd[i]:
    f.write(i.encode('utf-8')+'\n')
f.close()
