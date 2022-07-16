import matplotlib.pyplot as plt
import numpy as np
#import math

x = [2.5, 1.8, 3.4, -2.5]
y = [0.5, -2, 5.1, 1.8]

x2 = np.arange(-4, 4, 0.001)
y2 = np.sin(x2)
y3 = np.cos(x2)

plt.plot(x, y)
plt.figure()
plt.plot(x, y, 'r--o')
plt.figure()
plt.plot(x2, y2, 'k', x2, y3, '--r')
plt.title('graficas')
plt.xlabel('Tiempo (seg)')
plt.ylabel('Corriente (A)')
plt.legend(['Grafica 1','Grafica 2'])
plt.show()

