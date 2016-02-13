#coding:utf-8
from NLPIR.nlpir import *

p='生而是死'
p2='生 而 是死'
print ParagraphProcess(p,c_int(1))
print ParagraphProcess(p2,c_int(1))
Exit()
'''
li = ['之','而','然']
f=open('../lexDic/union/1234')
t=f.read().strip().decode('utf-8').split('\n')
f.close()

def insert(t, d):
  if t not in d:
    d[t] = 1
  else:
    d[t] += 1

pred = {}
postd = {}
for w in t:
  if w[2] != '之':
    continue
  tags = ParagraphProcess(w,c_int(1)).split(' ')
  postTag = tags[-1].split('/')[1]
  insert(postTag,postd)
  preTag = tags[0].split('/')[1]
  if len(tags) == 4:
    preTag += tags[1].split('/')[1]
  insert(preTag,pred)
'''

