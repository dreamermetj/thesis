#coding:utf-8
import json
f=open('../extracted/json/full_dict')
d=json.loads(f.read())
f.close()
f=open('../extracted/expand/duplicated_alternate_detail','wb')
oddCon = []
evnCon = []
for mode in ['13','24']:
  for c in d[mode]:
    if c[:2] == c[2:]:
      if mode == '13':
        oddCon.append([c,d[mode][c]])
      else:
        evnCon.append([c,d[mode][c]])
s=sorted(oddCon,key=lambda x:len(x[1]),reverse=True)
f.write('oddCon:\n')
for i in s:
  f.write((i[0]+'\t'+','.join(i[1])+'\n').encode("utf-8"))
s=sorted(evnCon,key=lambda x:len(x[1]),reverse=True)
f.write('evnCon:\n')
for i in s:
  f.write((i[0]+'\t'+','.join(i[1])+'\n').encode("utf-8"))
f.close()
