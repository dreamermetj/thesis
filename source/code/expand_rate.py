#coding:utf-8
import os
frate=open('../extracted/expand/diff_rate','w')
fnum=open('../extracted/expand/diff_num','w')
for dp, dns, fns in os.walk('../lexDic/1234'):
  frate.write('O\t'+'\t'.join(fns)+'\n')
  fnum.write('O\t'+'\t'.join(fns)+'\n')
  for i in range(len(fns)):
    frate.write(fns[i]+'\t'*(i+1))
    fnum.write(fns[i]+'\t'*(i+1))
    for j in range(i+1,len(fns)):
      set_i=set(open(dp+'/'+fns[i]).read().strip().split('\n'))
      set_j=set(open(dp+'/'+fns[j]).read().strip().split('\n'))
      inter = set_i & set_j
      fnum.write(str(len(inter)))
      frate.write(str(len(inter)*100/len(set_i))+'% ('+str(len(inter)-len(set_i))+')')
      if j < len(fns) - 1:
        fnum.write('\t')
        frate.write('\t')
      else:
        fnum.write('\n')
        frate.write('\n')
frate.close()
fnum.close()
