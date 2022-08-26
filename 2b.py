import numpy as np
import math
import matplotlib.pyplot as plt
x = [0.0050, 0.0164, 0.0252, 0.0349, 0.0455, 0.0722]
# xeq=np.array([0.000,0.22])
# yeq=0.624409+0.628250*(pow(xeq,1.5))+0.624409*(np.exp(xeq))
x11 = np.linspace(0.000, 0.22, 100) 
plt.plot(x11, -0.997398-1.493892*(pow(x11,1.5))+0.997398*np.exp(x11),label='Equilibrium Line')
plt.plot(x11, 0.480326*x11 + 0.0120048,label='Optimized Line')
# xeq=xeq.tolist()
# yeq=yeq.tolist()
y = [0.0054, 0.0210, 0.0320, 0.0420, 0.0533, 0.0800]
x1 = 0
x2 = 0.21799
y1 = 0.0120048
y2 = 0.2004799
ex = [x1, x2]
ey = [y1, y2]
m=((y2-y1)/(x2-x1))
c=0.0120048
# print(m)
plt.plot(ex, ey, 'ro-',label='Operating Line')
#plt.plot(xeq, yeq, 'bo-')
p= -0.997398-1.493892*(pow(ex[1],1.5))+0.997398*math.exp(ex[1])
plt.vlines(ex[1],ymin=p,ymax=ey[1],colors='green') # Q(ex[1],ey[1]) se niche A(ex[1],p)
q=(p-c)/m # A(ex[1],p) se left B(q,p)
plt.hlines(y=p,xmin=q,xmax=ex[1],colors='green')
r=-0.997398-1.493892*(pow(q,1.5))+0.997398*math.exp(q) # B(q,p) se niche C(q,r)
plt.vlines(q,ymin=r,ymax=p,colors='green')
s=(r-c)/m # C(q,r) se left D(s,r)
plt.hlines(y=r,xmin=s,xmax=q,colors='green')
t=-0.997398-1.493892*(pow(s,1.5))+0.997398*math.exp(s) # D(s,r) se niche C(s,t)
plt.vlines(s,ymin=t,ymax=r,colors='green')
u=(t-c)/m
plt.hlines(t,xmin=u,xmax=s,colors='green')
v=-0.997398-1.493892*(pow(u,1.5))+0.997398*math.exp(u) # D(s,r) se niche C(s,t)
plt.vlines(u,ymin=v,ymax=t,colors='green')
w=(v-c)/m
plt.hlines(v,xmin=w,xmax=u,colors='green')
x=-0.997398-1.493892*(pow(w,1.5))+0.997398*math.exp(w) # D(s,r) se niche C(s,t)
plt.vlines(w,ymin=x,ymax=v,colors='green')
y=(x-c)/m
plt.hlines(x,xmin=ex[0],xmax=w,colors='green')
plt.legend(loc='upper left')
plt.show()
