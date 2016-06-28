import numpy as np
import matplotlib.pyplot as plt
print 'Hello World'
m=np.zeros((10,20))
print m
x=np.linspace(0,2*np.pi,20)
print x
y=np.linspace(0,1,30)
print y
y=np.cos(x)

plt.plot(x,y,'-o')
plt.title('grafico')
plt.show()
