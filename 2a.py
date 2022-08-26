import numpy as np
import matplotlib.pyplot as plt
x = [0.0050, 0.0164, 0.0252, 0.0349, 0.0455, 0.0722]
xeq=np.array([0.000,0.06])
yeq=1.095592*xeq+0.002576
xeq=xeq.tolist()
yeq=yeq.tolist()
y = [0.0054, 0.0210, 0.0320, 0.0420, 0.0533, 0.0800]
x1 = 0
x2 = 0.05050599
y1 = 0.01111
y2 = 0.111107
ex = [x1, x2]
ey = [y1, y2]
plt.plot(ex, ey, 'ro-',label='Operating Line')
plt.plot(xeq, yeq, 'bo-',label='Eqiuilibrium Line')
p=1.095592*ex[1]+0.002576
plt.vlines(ex[1],ymin=p,ymax=ey[1],colors='green') # Q(ex[1],ey[1]) se niche A(ex[1],p)
q=(p-0.01111)/1.9799037698300737 # A(ex[1],p) se left B(q,p)
plt.hlines(y=p,xmin=q,xmax=ex[1],colors='green')
r=1.095592*q+0.002576 # B(q,p) se niche C(q,r)
plt.vlines(q,ymin=r,ymax=p,colors='green')
s=(r-0.01111)/1.9799037698300737 # C(q,r) se left D(s,r)
plt.hlines(y=r,xmin=s,xmax=q,colors='green')
t=1.095592*s+0.002576 # D(s,r) se niche C(s,t)
plt.vlines(s,ymin=t,ymax=r,colors='green')
plt.hlines(t,xmin=ex[0],xmax=s,colors='green')
plt.legend(loc='upper left')
plt.show()
