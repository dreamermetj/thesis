#coding:utf-8
import os

sortTypes = ['1324','1423','2341','2413','3412','4321']

def c1324(w1, w2):
  if w1[0] > w2[0]:
    return 1
  elif w1[0] < w2[0]:
    return -1
  elif w1[2] > w2[2]:
    return 1
  elif w1[2] < w2[2]:
    return -1
  elif w1[1] > w2[1]:
    return 1
  elif w1[1] < w2[1]:
    return -1
  elif w1[3] > w2[3]:
    return 1
  elif w1[3] < w2[3]:
    return -1
  else:
    return 0

def c4321(w1, w2):
  if w1[3] > w2[3]:
    return 1
  elif w1[3] < w2[3]:
    return -1
  elif w1[2] > w2[2]:
    return 1
  elif w1[2] < w2[2]:
    return -1
  elif w1[1] > w2[1]:
    return 1
  elif w1[1] < w2[1]:
    return -1
  elif w1[0] > w2[0]:
    return 1
  elif w1[0] < w2[0]:
    return -1
  else:
    return 0

def c1423(w1, w2):
  if w1[0] > w2[0]:
    return 1
  elif w1[0] < w2[0]:
    return -1
  elif w1[3] > w2[3]:
    return 1
  elif w1[3] < w2[3]:
    return -1
  elif w1[1] > w2[1]:
    return 1
  elif w1[1] < w2[1]:
    return -1
  elif w1[2] > w2[2]:
    return 1
  elif w1[2] < w2[2]:
    return -1
  else:
    return 0

def c2341(w1, w2):
  if w1[1] > w2[1]:
    return 1
  elif w1[1] < w2[1]:
    return -1
  elif w1[2] > w2[2]:
    return 1
  elif w1[2] < w2[2]:
    return -1
  elif w1[3] > w2[3]:
    return 1
  elif w1[3] < w2[3]:
    return -1
  elif w1[0] > w2[0]:
    return 1
  elif w1[0] < w2[0]:
    return -1
  else:
    return 0

def c2413(w1, w2):
  if w1[1] > w2[1]:
    return 1
  elif w1[1] < w2[1]:
    return -1
  elif w1[3] > w2[3]:
    return 1
  elif w1[3] < w2[3]:
    return -1
  elif w1[0] > w2[0]:
    return 1
  elif w1[0] < w2[0]:
    return -1
  elif w1[2] > w2[2]:
    return 1
  elif w1[2] < w2[2]:
    return -1
  else:
    return 0

def c3412(w1, w2):
  if w1[2] > w2[2]:
    return 1
  elif w1[2] < w2[2]:
    return -1
  elif w1[3] > w2[3]:
    return 1
  elif w1[3] < w2[3]:
    return -1
  elif w1[0] > w2[0]:
    return 1
  elif w1[0] < w2[0]:
    return -1
  elif w1[1] > w2[1]:
    return 1
  elif w1[1] < w2[1]:
    return -1
  else:
    return 0

def sort(ls,outf,sortType):
  print('\tsorting as '+sortType+' ...')
  exec( 'ls = sorted(ls,cmp=' + sortType + ')' )
  f = open(outf,'wb')
  for i in ls:
    f.write(i.encode('utf-8')+'\n')
  f.close()

fn = "../lexDic/1234/c30175.pure"
f = open(fn,'rb')
ls = f.read().strip().decode('utf-8').split('\n')
for sortType in sortTypes:
  sort(ls,'../lexDic/30175/'+sortType,'c'+sortType)
f.close()