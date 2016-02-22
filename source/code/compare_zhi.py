#coding:utf-8
import json
f=open('../extracted/json/full_dict')
d=json.loads(f.read())
f.close()
rev = dict()
for mode in d:
  for construction in d[mode]:
    l = len(d[mode][construction])
    if l > 5:
      for instance in d[mode][construction]:
        rev[instance] = 0
    else:
      for instance in d[mode][construction]:
        if instance not in rev:
          rev[instance] = 1
print "lenrev:"+str(len(rev))
#trimmed
zhi='之'.decode('utf-8')
idx=2
l=0
for ins in rev:
  if ins[idx] != zhi or rev[ins] == 0:
    continue
  l += 1
#easy_trimmed
s=[]
for i in rev:
  if rev[i]:
    s.append(i)
print "len:"+str(len(s))
d=dict()
for w in s:
  for i in [0,1,2,3]:
    if w[i] not in d:
      d[w[i]] = [0,0,0,0]
    d[w[i]][i] += 1
print "trimmed:"+str(l)
print "easy_trimmed:"+str(d[zhi][idx])