import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

archi = open('picoEMGalto.txt', 'r')
picoEMGalto = float(archi.read())
archi.close()

archi = open('limiteEmg.txt', 'r')
limiteEmg2 = float(archi.read()) /100
archi.close()
print('limiteEmg: ', limiteEmg2)

archi = open('limiteEmg_alto.txt', 'r')
limiteEmg_alto2 = float(archi.read()) /100
archi.close()
print('limiteEmg_alto: ', limiteEmg_alto2)

MMG = []
EMG = []
ax = []
ay = []
az = []
angulo1 = []
angulo2 = []
t = []
print('Esto es el tipo de []: ', type(t))
i = 0.0
archi = open('variables.txt', 'r')

for vv in archi.readlines():
    t.append(i)
    i = i + 0.001
    #print('Esto es antes del split', len(vv))
    vv = vv.split()
    #print('Esto es despues: ', vv)
    #print('Esto es 2do despues: ', float(vv[5]))
    ax.append(float(vv[0]))
    ay.append(float(vv[1]))
    az.append(float(vv[2]))
    angulo1.append(float(vv[3]) / 100)
    angulo2.append(float(vv[4]) / 100)
    EMG.append(float(vv[5]))
    MMG.append(float(vv[6]))


archi.close()
print('Esto es un mensaje diferente: ', len(t))

plt.plot(t, EMG, 'r')
plt.xlabel('Tiempo(s)')
plt.ylabel('Amplitud')
plt.title('Actividad muscular')
plt.figure()
plt.plot(t, MMG, 'b')

#------------lectura de archivos txt--------

#----------------creacion de archivos txt--------

open('new, txt', 'w')
filtered = lowess(EMG, t, is_sorted=True, frac=0.003, it=0)
plt.figure()
plt.plot(t, EMG, 'k', t, filtered, 'r')

plt.show()


