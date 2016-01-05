#coding:utf-8

sortTypes = ['1234','1324','1423','2341','2413','3412']

extractPairs = [
  ['12','1234'],
  ['13','1324'],
  ['14','1423'],
  ['23','2341'],
  ['24','2413'],
  ['34','3412'],
  ['123','1234'],
  ['124','1423'],
  ['134','3412'],
  ['234','2341']
]

#mode: eg. '13', '24'
def is_same(w1, w2, mode):
  for i in range(len(mode)):
    if w1[int(mode[i])-1] != w2[int(mode[i])-1]:
      return False
  return True

def make_construction_by_mode(ins, mode):
  for i in [1,2,3,4]:
    if str(i) not in mode:
      if i < 4:
        ins = ins[:i-1] + '…'.decode('utf-8') + ins[i:]
      else:
        ins = ins[:i-1] + '…'.decode('utf-8')
  return ins

#input: a word list file with the mode we want to use to extract
#return: a dict maps constructions to their instance groups
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
        c = make_construction_by_mode(s[0],mode)
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

DROP_PAIRS = [
  ['123', '12'],
  ['123', '23'],
  ['123', '13'],
  ['234', '23'],
  ['234', '34'],
  ['234', '24'],
  ['124', '12'],
  ['124', '24'],
  ['124', '14'],
  ['134', '13'],
  ['134', '14'],
  ['134', '34']
]

def drop_uni_slot_from_bi_slot(dic):
  for pair in DROP_PAIRS:
    for uni_slot_construction in dic[pair[0]]:
      bi_slot_construction = make_construction_by_mode(uni_slot_construction, pair[1])
      if not bi_slot_construction in dic[pair[1]]:
        continue
      trimmed = set(dic[pair[1]][bi_slot_construction]) - set(dic[pair[0]][uni_slot_construction])
      if(len(trimmed) > 1):
        dic[pair[1]][bi_slot_construction] = list(trimmed)
      else:
        del dic[pair[1]][bi_slot_construction]

def print_dict_to_html(dic, filename):
  f = open("../extracted/lex/" + filename, "wb")
  f.write('<html><head><meta charset="utf-8"><link rel="stylesheet" href="table.css"></head><body><table><thead><tr><th width="10%">排序类型</th><th width="10%">构式</th><th width="80%">实例</th></tr></thead><tbody>')
  for i in dic:
    s = sorted(dic[i].iteritems(),key=lambda x:x[0])
    for j in range(len(s)):
      if not j:
        f.write('<tr><td rowspan="'+str(len(s))+'">'+i+'<br>'+str(len(s))+'</td>')
      else:
        f.write('<tr>')
      f.write('<td>'+s[j][0].encode('utf-8')+'</td><td>'+('，'.decode('utf-8').join(s[j][1])).encode('utf-8')+'</td></tr>')
  f.write('</tbody></table></body></html>')
  f.close()

def stat_dict(dic, outFp, print_construction=False, thold=False):
  mode_list = []
  if print_construction:
    construction_list = []
  for mode in dic:
    ls = [mode, 0, []] #ls[1]: construction, ls[2]: instance
    for construction in dic[mode]:
      cnum = len(dic[mode][construction])
      if thold and cnum < thold:
        continue
      ls[1] += 1
      ls[2].append(cnum)
      if print_construction:
        construction_list.append([mode, construction, cnum])
    sorted_amount = sorted(ls[2],reverse=True)
    amount_str = ''
    same_amount = 1
    amount = sorted_amount[0]
    total = 0
    for i in range(1,len(sorted_amount)):
      if sorted_amount[i] == amount:
        same_amount += 1
      else:
        if same_amount > 1:
          amount_str += str(amount) + '×' + str(same_amount) + ' + '
        else:
          amount_str += str(amount) + ' + '
        total += amount * same_amount
        same_amount = 1
        amount = sorted_amount[i]
    total += amount * same_amount
    if same_amount > 1:
      amount_str = str(total) + ' (' + amount_str + str(amount) + '×' + str(same_amount) + ')'
    else:
      amount_str = str(total) + ' (' + amount_str + str(amount) + ')'
    ls[2] = amount_str
    mode_list.append(ls)
  f = open(outFp, 'wb')
  f.write('*'*32+'\n')
  f.write('1. MODE\n')
  f.write('*'*32+'\n')
  f.write('mode\tcnum\tinum\n')
  for i in mode_list:
    f.write(i[0]+'\t'+str(i[1])+'\t'+i[2]+'\n')
  if print_construction:
    construction_list = sorted(construction_list,key=lambda x:x[2], reverse=True)
    f.write('\n'+'*'*32+'\n')
    f.write('2. CONSTRUCTION\n')
    f.write('*'*32+'\n')
    f.write('mode\tcform\t\tinum\n')
    for i in construction_list:
      f.write(i[0]+'\t'+i[1].encode('utf-8')+'\t'+str(i[2])+'\n')
  f.close()

d = extract_construction_by_diff_modes("../lexDic/union/")
print ('start stat full dict ...')
stat_dict(d, '../extracted/lex/full_result_stat.txt')
print ('start drop uni slot ...')
drop_uni_slot_from_bi_slot(d)
print ('start stat trimmed dict ...')
stat_dict(d, '../extracted/lex/trimmed_result_stat.txt')
print ('start stat trimmed dict with threshold ...')
stat_dict(d, '../extracted/lex/trimmed_with_threshold_result_stat.txt', print_construction=True, thold=3)





