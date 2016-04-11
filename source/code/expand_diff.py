#coding:utf-8
import os
out=open('../extracted/expand/gradient','w')
def diff(fn1,fn2):
  f = open(fn1,'rb')
  list1 = f.read().split('\n')
  if list1[-1] == '':
    list1 = list1[:-1]
  f.close()
  f = open(fn2,'rb')
  list2 = f.read().split('\n')
  if list2[-1] == '':
    list2 = list2[:-1]
  f.close()
  set1 = set(list1)
  set2 = set(list2)
  diff1 = sorted(list(set1 - set2))
  diff2 = sorted(list(set2 - set1))
  fn1 = 'd'+fn1.split('/')[-1][1:6]
  fn2 = 'd'+fn2.split('/')[-1][1:6]
  out.write('==== '+fn1+' v.s. '+fn2+' ====\n')
  out.write('-- '+fn1+'('+str(len(diff1))+') --\n')
  for i in diff1:
    out.write(i+'\n')
  out.write('-- '+fn2+'('+str(len(diff2))+') --\n')
  for i in diff2:
    out.write(i+'\n')

for dp, dns, fns in os.walk('../lexDic/1234'):
  for i in range(len(fns)-1):
    for j in range(i+1,len(fns)):
      diff(dp+'/'+fns[i],dp+'/'+fns[j])

out.close()



