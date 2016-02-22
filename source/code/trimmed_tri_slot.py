#coding:utf-8
import json
f=open('../extracted/tri_slot/explicit_result.py')
t=f.read().decode("utf-8").split('\n')
f.close()
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
count = 0
s = []
def isDel(arr):
  s = sorted(arr)
  if s[3] > 10 * s[1]:
    return False
  return True
for w in t:
  count += 1
  if count > 100:
    break
  l = 0
  idx = int(w[1]) - 1
  for ins in rev:
    if ins[idx] != w[0] or rev[ins] == 0:
      continue
    l += 1
  s.append([w,l])
s=sorted(s,key=lambda x:x[1],reverse=True)
f=open('../extracted/tri_slot/trimmed_result_05.py','wb')
for p in s:
  f.write(p[0].encode('utf-8')+'\t'+str(p[1])+'\n')
f.close()
