#coding:utf-8
path = '../extracted/tri_slot/'
f=open(path+'explicit_result.py')
t=f.read().split('\n')
f.close()
#d={}
a=[0,0,0,0]
c=0
for l in t:
  if c >= 100:
    break
  p=l.split('\t')[0][-1]
  a[int(p)-1] += 1
  c += 1
print a