#coding:utf-8

diff_pair=[['04203','04635'],['04635','12601'],['12601','16948'],['17011','17267'],['17267','30175'],['30175','42198'],['30175','42372'],['30175','46238_sogou'],['30175','49218_pangu'],['30175','54058']]
#diff_pair=[['04635','12601']]
import json,re

f=open('../extracted/json/full_dict')
d=json.loads(f.read())
f.close()

print 'preparing rev dict ...'
rev=dict()
f=open('../extracted/multi_inheritance.txt')
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

def printf(_list):
  print '[',
  for _i in range(len(_list)):
    if type(_list[_i]) != type([]):
      print _list[_i],
    else:
      printf(_list[_i])
    if _i < len(_list) -1 :
      print ',',
    else:
      print ']',

def writef(f,_list):
  f.write('[')
  for _i in range(len(_list)):
    _t = type(_list[_i])
    if _t != type([]):
      try:
        f.write(_list[_i].encode('utf-8'))
      except:
        f.write(str(_list[_i]))
    else:
      writef(f,_list[_i])
    if _i < len(_list) -1 :
      f.write(',')
    else:
      f.write(']')

from nlpir import *
VARSIGN = '…'.decode('utf-8')
out = open('../extracted/expand/auto_diff','w')
for i in diff_pair:
  print 'start processing ' + str(i) + ' ...'
  f=open('../lexDic/1234/c'+i[0]+'.pure')
  less=set(f.read().strip().decode("utf-8").split('\n'))
  f.close()
  f=open('../lexDic/1234/c'+i[1]+'.pure')
  more=set(f.read().strip().decode("utf-8").split('\n'))
  f.close()
  out.write('==== ' + i[0]+' : '+i[1]+ ' ===='+'\n')
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
    #print '    processing ' + w + ' ...'
    sw = ''.join(sorted(w))
    if sw in trd: #全变换等级最高，为0
      rsd.append([w,0,trd[sw]])
      continue
    temp = ParagraphProcess(w.encode('utf-8'),c_int(1)).strip().split(' ')
    if len(temp) == 2:
      rsd.append([w,7])
    else:
      protos = []
      unislot = []
      isUniSlot = False
      if w in rev:
        for c in rev[w]:
          proto = [c,[]]
          mode = ''
          for idx in range(4):
            if c[idx] != VARSIGN:
              mode += str(idx+1)
          for ins in d[mode][c]:
            if ins == w:
              continue
            if ins in inter:
              proto[1].append(ins)
          if proto[1]:
            protos.append(proto)
            if len(mode) == 3:
              isUniSlot = True
              unislot.append(proto)
      if isUniSlot: #单槽次之，等级为1
        rsd.append([w,1,unislot])
      elif w[0] == w[2] or w[1] == w[3]: #叠字对举等级为2
        rsd.append([w,2])
      elif protos:
        alterslot = []
        for proto in protos:
          if (proto[0][0] == VARSIGN and proto[0][2] == VARSIGN) or (proto[0][1] == VARSIGN and proto[0][3] == VARSIGN):
            alterslot.append(proto)
        if alterslot: #格式对举等级为3
          rsd.append([w,3,alterslot])
      else:
        temp = re.split(r'[ ]+',ParagraphProcess(' '.join(w).encode('utf-8'),c_int(1)).strip())
        tags = map(lambda x:x.split('/')[1][0],temp)
        if tags[0] == tags[2] and tags[1] == tags[3]:
          rsd.append([w,4]) #词性对举等级为4
        elif tags[1] == tags[3]:
          biw = w[0]+w[2]
          if len(ParagraphProcess(biw.encode('utf-8'),c_int(1)).split('/')) == 2:
            rsd.append([w,5]) #扩展对举等级为5
            continue
          biw = w[2]+w[0]
          if len(ParagraphProcess(biw.encode('utf-8'),c_int(1)).split('/')) == 2:
            rsd.append([w,5]) #扩展对举等级为5
            continue
        elif tags[0] == tags[2]:
          biw = w[1]+w[3]
          if len(ParagraphProcess(biw.encode('utf-8'),c_int(1)).split('/')) == 2:
            rsd.append([w,5]) #扩展对举等级为5
            continue
          biw = w[3]+w[1]
          if len(ParagraphProcess(biw.encode('utf-8'),c_int(1)).split('/')) == 2:
            rsd.append([w,5]) #扩展对举等级为5
            continue
        else:
          biw1 = w[0]+w[2]
          biw2 = w[1]+w[3]
          biw3 = w[2]+w[0]
          biw4 = w[3]+w[1]
          if len(ParagraphProcess(biw1.encode('utf-8'),c_int(1)).split('/')) + len(ParagraphProcess(biw2.encode('utf-8'),c_int(1)).split('/')) == 4:
            rsd.append([w,5]) #扩展对举等级为5
          elif len(ParagraphProcess(biw3.encode('utf-8'),c_int(1)).split('/')) + len(ParagraphProcess(biw4.encode('utf-8'),c_int(1)).split('/')) == 4:
            rsd.append([w,5]) #扩展对举等级为5
          else:
            rsd.append([w,6]) #啥也没有
  s = sorted(rsd,key=lambda x:x[1])
  count = [0,0,0,0,0,0,0,0]
  for si in s:
    '''
    out.write(si[0].encode('utf-8') + '\t' + str(si[1]))
    if len(si) > 2:
      out.write('\t')
      writef(out,si[2])
    out.write('\n')
    '''
    count[si[1]] += 1
  out.write('********\n')
  for ci in range(8):
    out.write(str(ci)+': '+str(count[ci])+'\n')
  out.write('********\n')
out.close()













