#coding:utf-8
d=dict()
c=0
for i in ['','_20','_10','_5','_1']:
  path = '../extracted/tri_slot/explicit_result'
  f=open(path+i+'.py')
  t=f.read().strip().split('\n')
  f.close()
  c2=0
  lastc=0
  lastn=0
  for j in t:
    c2 += 1
    p=j.split('\t')
    if p[0] not in d:
      d[p[0]] = [0,0,0,0,0]
    d[p[0]][c] = p[1]
    if not c:
      continue
    if p[1] != lastn:
      d[p[0]][c] += '('+str(c2)+')'
      lastn = p[1]
      lastc = c2
    else:
      d[p[0]][c] += '('+str(lastc)+')'
  c+=1
s=sorted(d.iteritems(),key=lambda x:int(x[1][0]),reverse=True)
'''
f=open(path+'_matrix.py','w')
for i in s:
  f.write(i[0]+'\t'+str(i[1])+'\n')
f.close()
'''
m=[[0,0,0,0] for i in range(4)]
for i in [0,1,2,3]:#20+10+5,20,10,5
  j=0
  for top in [10,20,50,100]:
    out=0
    for k in range(top):
      if i != 0:
        p = s[k][1][i].find('(')
        if int(s[k][1][i][p+1:-1]) > top:
          out += 1
      else:
        isOut = False
        for l in range(1,4):
          p = s[k][1][l].find('(')
          if int(s[k][1][l][p+1:-1]) > top:
            isOut = True
            break
        if isOut:
          out += 1
    m[i][j] = out
    j+=1
for i in range(4):
  for j in range(4):
    print m[i][j],
    if j != 3:
      print '\t',
  print '\n',