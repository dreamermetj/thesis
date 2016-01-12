# -*- coding: UTF-8 -*-
from ctypes import *

libFile = './nlpir/libNLPIR.so'

dll =  CDLL(libFile)
def loadFun(exportName, restype, argtypes):
    global dll
    f = getattr(dll,exportName)
    f.restype = restype
    f.argtypes = argtypes
    return f

Init = loadFun('NLPIR_Init',c_int, [c_char_p, c_int, c_char_p])
Exit = loadFun('NLPIR_Exit',c_bool, None)
ParagraphProcess = loadFun('NLPIR_ParagraphProcess',c_char_p, [c_char_p, c_int])

if not Init('',1,''): # 1 for utf-8 code
    print("Initialization failed!")
    exit(-111111)

union_path = '../../lexDic/union/'
extract_path = '../../extracted/singlex/'

f = open(union_path+'1234')
t = f.read()
f.close()
lns = t.strip().split('\n')

f1 = open(extract_path+'1234','w')
f2 = open(extract_path+'1234.abandoned','w')
for l in lns:
    seg = ParagraphProcess(l,c_int(1))
    wlen = len(seg.strip().split(' '))
    if wlen in [1,4]:
        f1.write(l+'\n')
    else:
        print seg
        f2.write(l+'\n')
f1.close()
f2.close()










