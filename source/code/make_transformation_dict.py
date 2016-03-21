#coding:utf-8
import json
f=open('../lexDic/93050/union/1234')
t=f.read().strip().decode("utf-8").split('\n')
f.close()
d={}
for w in t:
  tr = ''.join(sorted(w))
  if tr in d:
    d[tr].append(w)
  else:
    d[tr] = [w]
print len(d)
f=open('../extracted/json/transformation_dict','w')
f.write(json.dumps(d))
f.close()