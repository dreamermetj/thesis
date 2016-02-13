#coding:utf-8
from NLPIR.nlpir import *
zhi2 = []
zhi3 = []
er2 = []
er3 = []
f=open('../lexDic/union/1234')
t=f.read().strip().decode('utf-8').split('\n')
f.close()
zhi = '之'.decode('utf-8')
er = '而'.decode('utf-8')
zw = ''
ew = ''
for w in t:
  if w[1] == zhi:
    zhi2.append(w)
  elif w[1] == er:
    er2.append(w)
  if w[2] == zhi:
    zhi3.append(w)
  elif w[2] == er:
    er3.append(w)
f=open('../extracted/tri_slot/zhi_er','wb')
f.write('之2：'+str(len(zhi2)))
f.write('，之3：'+str(len(zhi3)))
f.write('，而2：'+str(len(er2)))
f.write('，而3：'+str(len(er3))+'\n')
def insert(t, d, sp=0):
  s = t.strip().split(' ')
  t = ''
  for i in s:
    t += i.split('/')[1][0]
  if sp == 1:
    t = t[0] + ' ' + t[1:]
  elif sp == 2:
    t = t[:-1] + ' ' + t[-1]
  if t not in d:
    d[t] = 1
  else:
    d[t] += 1
for ch in ['之', '而']:
  for indx in [1, 2]:
    arr = []
    if ch == '之':
      exec("arr = zhi"+str(indx+1))
    else:
      exec("arr = er"+str(indx+1))
    pred = {}
    postd = {}
    alld = {}
    for w in arr:
      if indx == 1:
        pre = w[0]
        post = w[2:]
      else:
        pre = w[:2]
        post = w[3]
      preTag = ParagraphProcess(pre.encode('utf-8'),c_int(1))
      postTag = ParagraphProcess(post.encode('utf-8'),c_int(1))
      allTag = preTag.strip() + ' ' + postTag.strip()
      insert(postTag,postd)
      insert(preTag,pred)
      insert(allTag,alld,indx)
    f.write(ch+str(indx+1)+':\n')
    def printf(d,sp=0):
      if sp == 1:
        s = sorted(d.iteritems(),key=lambda x:(x[0][0],x[1]),reverse=True)
      elif sp == 2:
        s = sorted(d.iteritems(),key=lambda x:(x[0][-1],x[1]),reverse=True)
      else:
        s = sorted(d.iteritems(),key=lambda x:x[1],reverse=True)
      for i in s:
        f.write('\t\t'+str(i[1])+'\t'+i[0]+'\n')
    f.write('\tPRETAG:\n')
    printf(pred)
    f.write('\tPOSTTAG:\n')
    printf(postd)
    f.write('\tFULLTAG:\n')
    printf(alld,indx)
f.close()