#coding:utf-8

sortTypes = ['1234','1324','1423','2341','2413','3412']

extractPairs = [
  ['123','1234'],
  ['124','1423'],
  ['134','3412'],
  ['234','2341'],
  ['12','1234'],
  ['13','1324'],
  ['14','1423'],
  ['23','2341'],
  ['24','2413'],
  ['34','3412']
]

#mode: eg. '13', '24'
def is_same(w1, w2, mode):
  for i in range(len(mode)):
    if w1[int(mode[i])-1] != w2[int(mode[i])-1]:
      return False
  return True

#input: a word list file with the mode we want to use to extract
#return: a dict maps constructions to their instance groups
#data structure:
# dict(mode)
#  |
#  |- construction 1
#  |       |- instance 1
#  |       |- instance 2
#  |       |- ...
#  |
#  |- construction 2
#  |       |- ...
#  |
#  |- ...
#  |
#  |- construction n
#          |- ...
def extract_construction_with_instances(inf, mode):
  print "processing inf: " + inf + " using mode: " + mode + " ..."
  f = open(inf,"rb")
  ls = f.read().decode("utf-8").split("\n")
  f.close()
  if not ls[-1]:
    ls.pop()
  #d:dict
  d = {}
  #s:instance group
  s = [ls[0]]
  i = 1
  while i <= len(ls):
    if i < len(ls) and is_same(ls[i],s[0],mode):
      s.append(ls[i])
    else:
      if len(s) >= 2:
        #c:construction
        c = s[0]
        for j in [1,2,3,4]:
          if str(j) not in mode:
            if j < 4:
              c = c[:j-1] + '…'.decode('utf-8') + c[j:]
            else:
              c = c[:j-1] + '…'.decode('utf-8')
        d[c] = s
      if i < len(ls):
        s = [ls[i]]
    i += 1
  print "process done, len(d) (number of construction) is " + str(len(d))
  return d

def extract_construction_by_diff_modes(dicPath):
  d = dict()
  for pair in extractPairs:
    mode = pair[0]
    fn = pair[1]
    d[mode] = extract_construction_with_instances(dicPath+fn,mode)
  return d

d = extract_construction_by_diff_modes("../lexDic/union/")
f = open("../extracted/lex/result.html","wb")
f.write('<html><head><link rel="stylesheet" href="table.css"></head><body><table><thead><tr><th width="60px">排序类型</th><th width="60px">构式</th><th width="900px">实例</th></tr></thead><tbody>')
for i in d:
  s = sorted(d[i].iteritems(),key=lambda x:x[0])
  for j in range(len(s)):
    if not j:
      f.write('<tr><td rowspan="'+str(len(s))+'">'+i+'</td>')
    else:
      f.write('<tr>')
    f.write('<td>'+s[j][0].encode('utf-8')+'</td><td>'+('，'.decode('utf-8').join(s[j][1])).encode('utf-8')+'</td></tr>')
f.write('</tbody></table></body></html>')
f.close()




