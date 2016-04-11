#coding:utf-8
f=open('../lexDic/xiandai.txt')
s=[]
while 1:
  l=f.readline()
  if l=='':
    break
  t=l.split('】')
  if len(t) and len(t[0])==15 and t[0][:3] == '【':
    s.append(t[0][3:])
s=sorted(s)
f.close()
f=open('../lexDic/chineseDict','w')
for i in s:
  f.write(i+'\n')
f.close()