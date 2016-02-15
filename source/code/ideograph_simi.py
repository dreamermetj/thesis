#coding:utf-8
f=open('/Users/Dreamer/result.txt')
t=f.read().split('\n')
f.close()
l=[]
for i in range(14000):
  l.append([t[2*i], int(t[2*i+1])])
s=sorted(l,key=lambda x:x[1])
f=open('../extracted/similarity/similarity.txt')
t=f.read().strip().split('\n')
f.close()
d=dict()
for i in t:
  p = i.split('\t')
  d[p[0]] = p[1]
for i in range(len(s)):
  s[i].append(d[s[i][0]])
f=open('../extracted/similarity/ideograph_simi','w')
for i in s:
  f.write(i[0]+'\t'+str(i[1])+'\t'+i[2]+'\n')
f.close()