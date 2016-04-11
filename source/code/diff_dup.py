#coding:utf-8
f=open('../extracted/expand/auto_diff')
out=open('../extracted/expand/duplicated_alternative','w')
d=dict()
tmp=dict()
VARSIGN = '…'.decode("utf-8")
while 1:
  l=f.readline().strip()
  if l == '' or l[0] == '=':
    if len(tmp):
      oddCon = []
      evnCon = []
      for i in tmp.iteritems():
        if i[0][0] == VARSIGN:
          evnCon.append(i)
        else:
          oddCon.append(i)
        if i[0] not in d:
          d[i[0]] = i[1]
        else:
          d[i[0]] += i[1]
      tmp=dict()
      out.write('odd constants:\n')
      s=sorted(oddCon,key=lambda x:x[1],reverse=True)
      for i in s:
        out.write(i[0].encode('utf-8')+': '+str(i[1])+'\n')
      out.write('even constants:\n')
      s=sorted(evnCon,key=lambda x:x[1],reverse=True)
      for i in s:
        out.write(i[0].encode('utf-8')+': '+str(i[1])+'\n')
    if l == '':
      break
    else:
      out.write(l+'\n')
  elif l[0] < '\x7f':
    continue
  else:
    p=l.split('\t')
    if p[1] != '2':
      continue
    try:
      c=p[2][2:14].decode("utf-8")
    except:
      print p[2][2:14]
      exit(-1)
    if c not in tmp:
      tmp[c] = 1
    else:
      tmp[c] += 1
out.write('==== total ====\n')
oddCon = []
evnCon = []
for i in d.iteritems():
  if i[0][0] == VARSIGN:
    evnCon.append(i)
  else:
    oddCon.append(i)
out.write('odd constants:\n')
s=sorted(oddCon,key=lambda x:x[1],reverse=True)
for i in s:
  out.write(i[0].encode('utf-8')+': '+str(i[1])+'\n')
out.write('even constants:\n')
s=sorted(evnCon,key=lambda x:x[1],reverse=True)
for i in s:
  out.write(i[0].encode('utf-8')+': '+str(i[1])+'\n')
out.close()

