#coding:utf-8

def diff(fn1,fn2,openType,outpath):
  f = open(fn1,'rb')
  list1 = f.read().split('\n')
  if list1[-1] == '':
    list1 = list1[:-1]
  f.close()
  f = open(fn2,openType)
  list2 = f.read().split('\n')
  if list2[-1] == '':
    list2 = list2[:-1]
  f.close()
  set1 = set(list1)
  set2 = set(list2)
  diff1 = sorted(list(set1 - set2))
  diff2 = sorted(list(set2 - set1))
  f = open(outpath,'a')
  f.write(fn1+' versus '+fn2+':\n')
  f.write('  '+fn1+' only (amount:'+str(len(diff1))+'):\n')
  for i in diff1:
    f.write('    '+i+'\n')
  f.write('  '+fn2+' only (amount:'+str(len(diff2))+'):\n')
  for i in diff2:
    f.write('    '+i+'\n')
  f.write('\n'+'*'*8+'\n')
  f.close()

diff('sogou_4','pangu_4','result')



