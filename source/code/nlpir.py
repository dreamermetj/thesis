# -*- coding: UTF-8 -*-
from ctypes import *

#libFile = '/Users/Dreamer/workspace/thesis/source/code/NLPIR/nlpir/libNLPIR.so'
libFile = 'F:\\thesis\\source\\code\\NLPIR\\nlpir\\NLPIR.dll'
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

if not Init('F:\\thesis\\source\\code\\NLPIR\\',1,''): # 1 for utf-8 code
    print("Initialization failed!")
    exit(-111111)
