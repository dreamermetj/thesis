#coding:utf-8
import json
f=open('../extracted/tri_slot/full_result.py')
t=f.read().decode("utf-8").split('\n')
f.close()
f=open('../extracted/json/full_dict')
d=json.loads(f.read())
f.close()
rev = dict()
for mode in d:
  for construction in d[mode]:
    l = len(d[mode][construction])
    for instance in d[mode][construction]:
      if instance not in rev:
        rev[instance] = [[construction, l]]
      else:
        rev[instance].append([construction, l])
f=open('../extracted/tri_slot/trimmed_result_10.py','wb')
count = 0
def isDel(arr):
  s = sorted(arr)
  if s[3] > 10 * s[1]:
    return False
  return True
for w in t:
  count += 1
  if count > 300:
    break
  if w[0] == '#':
    continue
  l = [0,0,0,0]
  for i in range(4):
    for ins in rev:
      if ins[i] != w[0]:
        continue
      ist = True
      for pair in rev[ins]:
        if pair[1] > 10:
          ist = False
          break
      if ist:
        l[i] += 1
  if isDel(l):
    f.write('#')
  f.write(w[:2].encode('utf-8')+str(l)+'\n')
f.close()