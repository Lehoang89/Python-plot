
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm as CM
from matplotlib import mlab as ML
import matplotlib.pyplot as PLT
import re
import math

x = []
y = []
z= []
u = []
v = []
w = []
count = 0
f = open("10mm_true.txt")
for line in iter(f):
        xa = line.split( )
        x.append(float(xa[0]))
        y.append(float(xa[1]))
        #z.append(float(xa[2]))
        if (float(xa[0]) * float(xa[0]) + float(xa[1]) * float(xa[1]) < 10*10):
            v.append(1)
            u.append(math.sqrt(float(xa[4]) * float(xa[4]) + float(xa[3]) * float(xa[3])))
        else:
            v.append(0)
            u.append(0)
        #v.append(float(xa[4]))
        #w.append(float(xa[5]))
        count += 1
        if count > 58081:
            break
       # for k in range(100):
       #     next(f)
f.close()






sum = 0
large = 0
for x in u:
    sum = x*0.1*0.1 + sum
    if x > 1:
        large = large +1
print sum


PLT.show() 
