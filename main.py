# use os.system() commands.getstatusoutput() and popen() to run binarys

import os
from time import sleep
from observable import *
import subprocess
import ctypes

library = ctypes.cdll.LoadLibrary("./GoBinary/library.so")

hello_world = library.helloWorld
hello_world()
###############################################################################3
# os.system() command to run binary
# res = os.system("./GoBinary/main")
# print(res)  
#########################
# subprocess.Popen() command to run binary
# if os.path.exists("./GoBinary/main"):
#     rs,out = subprocess.getstatusoutput("./GoBinary/main")
#     # print(rs)
#     print(out)
# else:
#     print("binary not found")

#########################
# os.popen() command to run binary
# p = os.popen("./GoBinary/main")
# print(p.read())
# p.close()


if __name__ == '__main__':

    pass



