import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as NP
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



#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.quiver(x, y, z, u, v, w, length = 0.2)
#plt.show()

gridsize=200
PLT.subplot(111)

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(x, y, u)
#plt.show()

PLT.hexbin(x, y, C=u, gridsize=gridsize, cmap=CM.jet, bins=None)
#PLT.axis([X.min(), X.max(), Y.min(), Y.max()])

cb = PLT.colorbar()
cb.set_label('Tesla')

#PLT.savefig('xy_field_2mic.png', format='png', dpi=300)


sum = 0
large = 0
for x in u:
    sum = x*0.1*0.1 + sum
    if x > 1:
        large = large +1
print sum


PLT.show() 
