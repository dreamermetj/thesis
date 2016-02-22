#coding:utf-8
f=open('../extracted/tri_slot/1234_1')
t=f.read().decode('utf-8').strip().split('\n')
f.close()
d=dict()
for w in t:
  for i in range(4):
    char = w[i]+str(i+1)
    if char not in d:
      d[char] = [w]
    else:
      d[char].append(w)
s=sorted(d.iteritems(),key=lambda x:len(x[1]),reverse=True)
f=open('../extracted/tri_slot/detail_1','wb')
for i in s:
  f.write(i[0].encode('utf-8')+'\t'+str(len(i[1]))+'\t')
  for j in i[1]:
    f.write(j.encode('utf-8')+' ')
  f.write('\n')
f.close()
