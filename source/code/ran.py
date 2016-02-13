#coding:utf-8
from NLPIR.nlpir import *
ran2 = []
ran4 = []
f=open('../lexDic/union/1234')
t=f.read().strip().decode('utf-8').split('\n')
f.close()
ran = '然'.decode('utf-8')
for w in t:
  if w[1] == ran:
    ran2.append(w)
  if w[3] == ran:
    ran4.append(w)
f=open('../extracted/tri_slot/ran','wb')
f.write('然2：'+str(len(ran2)))
f.write('，然4：'+str(len(ran4))+'\n')
def insert(t, d, sp=0):
  s = t.strip().split(' ')
  t = ''
  for i in s:
    t += i.split('/')[1][0]
  if sp == 1:
    t = t[0] + ' ' + t[1:]
  if t not in d:
    d[t] = 1
  else:
    d[t] += 1
ch = '然'
for indx in [1,3]:
  arr = []
  exec("arr = ran"+str(indx+1))
  pred = {}
  if indx == 1:
    postd = {}
    alld = {}
  for w in arr:
    if indx == 1:
      pre = w[0]
      post = w[2:]
    else:
      pre = w[:3]
    preTag = ParagraphProcess(pre.encode('utf-8'),c_int(1))
    insert(preTag,pred)
    if indx == 1:
      postTag = ParagraphProcess(post.encode('utf-8'),c_int(1))
      allTag = preTag.strip() + ' ' + postTag.strip()
      insert(postTag,postd)
      insert(allTag,alld,indx)
  f.write(ch+str(indx+1)+':\n')
  def printf(d,sp=0):
    if sp == 1:
      s = sorted(d.iteritems(),key=lambda x:(x[0][0],x[1]),reverse=True)
    else:
      s = sorted(d.iteritems(),key=lambda x:x[1],reverse=True)
    for i in s:
      f.write('\t\t'+str(i[1])+'\t'+i[0]+'\n')
  f.write('\tPRETAG:\n')
  printf(pred)
  if indx == 1:
    f.write('\tPOSTTAG:\n')
    printf(postd)
    f.write('\tFULLTAG:\n')
    printf(alld,indx)
f.close()