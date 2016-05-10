#coding:utf-8
import json
f=open('../extracted/json/full_dict_30175')
d=json.loads(f.read())
f.close()
strict = []
others = []
for mode in d:
  if len(mode) == 3:
    continue
  for c in d[mode]:
    if len(d[mode][c]) >= 10:
      strict.append(c)
    else:
      others.append([c,len(d[mode][c])])
f=open('../extracted/dict/strict','w')
for c in strict:
  f.write(c.encode("utf-8")+'\n')
f.close()
s=sorted(others,key=lambda x:x[1],reverse=True)
f=open('../extracted/dict/others','w')
for c in s:
  f.write(c[0].encode('utf-8')+'\t'+str(c[1])+'\n')
f.close()