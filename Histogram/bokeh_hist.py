from bokeh.charts import Histogram
from bokeh.sampledata.autompg import autompg as df
from bokeh.charts import defaults, vplot, hplot, show, output_file
import math
import numpy

defaults.width =  1000
defaults.height = 600


output_file("histograms.html")





listFiles=["1mm_true.txt","2mm_true.txt","10mm_true.txt"]


x = []
y = []
z= []
u = []
v = []
w = []

count = 0
f = open("1mm_true.txt")
for line in iter(f):
        xa = line.split( )
        x.append(float(xa[0]))
        y.append(float(xa[1]))
        #z.append(float(xa[2]))
        if (float(xa[0]) * float(xa[0]) + float(xa[1]) * float(xa[1]) < 10*10):
            v.append(1)
            u.append(math.sqrt(float(xa[4]) * float(xa[4]) + float(xa[3]) * float(xa[3])))
        #v.append(float(xa[4]))
        #w.append(float(xa[5]))
        count += 1
        if count > 58081:
            break
       # for k in range(100):
       #     next(f)
f.close()


hist = Histogram(u,bins=200, title="Weight")


sum = 0
large = 0
for x in u:
    sum = x*0.1*0.1 + sum
    if x > 1:
        large = large +1
print "Mean is: ",numpy.mean(u)

show(hist)