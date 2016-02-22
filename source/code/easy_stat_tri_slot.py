#coding:utf-8
path = '../extracted/tri_slot/'
def stat(thres, top):
  if thres == 'all':
    f=open(path+'explicit_result.py')
  else:
    f=open(path+'explicit_result_'+str(thres)+'.py')
  t=f.read().split('\n')
  f.close()
  #d={}
  a=[0,0,0,0]
  c=0
  for l in t:
    if c >= top:
      break
    p=l.split('\t')[0][-1]
    a[int(p)-1] += 1
    c += 1
  return a
def var(arr):
  e = float(sum(arr))/4
  v = sum(map(lambda x:(x-e)*(x-e), arr)) / 3
  return v/e
for i in ['all',10,5,2]:
  for j in [100]:
    arr = stat(i,j)
    print str(i)+"\t"+"\t".join(map(str,arr))+'\t'+str(round(var(arr),2))
