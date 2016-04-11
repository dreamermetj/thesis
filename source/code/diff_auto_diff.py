#coding:utf-8

diff_pair=[['04635','12601'],['12601','16948'],['17011','17267'],['17267','30175']]

import json,re

f=open('../extracted/json/full_dict')
d=json.loads(f.read())
f.close()

rev=dict()
f=open('../extracted/multi_inheritance')
while 1:
  l=f.readline().strip()
  if l == '':
    break
  p=l.decode('utf-8').split('\t')
  if p[1] == '0':
    continue
  ls=re.findall(r'\(([^,]+)',p[2])
  rev[p[0]]=ls
f.close()

for i in diff_pair:
  print 'start processing ' + str(i) + ' ...'
  f=open('../lexDic/1234/c'+i[0]+'.pure')
  less=set(f.read().strip().decode("utf-8").split('\n'))
  f.close()
  f=open('../lexDic/1234/c'+i[1]+'.pure')
  more=set(f.read().strip().decode("utf-8").split('\n'))
  f.close()
  inter=less&more
  #全变换表trd
  trd = dict()
  #临时表tmpd，记录交集的词，便于判断词是否出现在交集中
  tmpd = dict()
  for w in inter:
    tmpd[w]=True
    sw=''.join(sorted(w))
    if sw not in trd:
      trd[sw] = [w]
    else:
      trd[sw].append(w)
  diff=more-less
  #结果表rsd，记录diff中每个词是否在inter中有相应的extends形式
  rsd = []
  for w in diff:
    sw = ''.join(sorted(w))
    if sw in trd: #全变换等级最高，为0
      rsd.append([w,0,trd[sw]])
    #单槽次之，等级为1
    #交替复现再次，等级为2
    #交替双槽再次，等级为3
    #词性对举再次，等级为4







