import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess
#--------------lectura de archivos txt--------------
archi = open('picoEMGalto.txt', 'r')
# limite_MMG2 = float(archi.read())
picoEMGalto = float(archi.read())

#factor = 100 / picoEMGalto

archi.close()

archi = open('limiteEmg.txt', 'r')
# limite_EMG2 = float(archi.read())
limite_EMG2 = int(float(archi.read()))
limite_EMG2 = float(limite_EMG2) / 100
archi.close()

archi = open('limiteEmg_alto.txt', 'r')
# limite_EMG_alto2 = float(archi.read())
limite_EMG_alto2 = int(float(archi.read()))
archi.close()

# limite_EMG2 = 0.16
print('limite_EMG: ', limite_EMG2)


# limite_EMG_alto2 = 0.3177
print('limite EMG alto: ', limite_EMG_alto2)

MMG = []
EMG = []
ax = []
ay = []
az = []
angulo1 = []
angulo2 = []
t = []
print('Esto el es tipo de []: ', type(t))
i = 0.0
archi = open('variables.txt', 'r')
for vv in archi.readlines():
    t.append(i)
    i = i + 0.001
    #print('esto es antes del split: ', len(vv))
    vv = vv.split()  # Correcto
    #print('esto es despues: ', vv)
    ax.append(float(vv[0]))
    ay.append(float(vv[1]))
    az.append(float(vv[2]))
    angulo1.append(float(vv[3]) / 100)
    angulo2.append(float(vv[4]) / 100)
    EMG.append(float(vv[5]))
    MMG.append(float(vv[6]))
    # Solo para prueba
    # ax.append(float(vv[0]))
    # ay.append(float(vv[1]))
    # az.append(float(vv[2]))
    # EMG.append(float(vv[8]))
    # MMG.append(float(vv[9]))
archi.close()
print('Esto es un mensaje diferente: ', len(t))
plt.plot(t, EMG, 'k')
plt.xlabel('Tiempo(s)')
plt.ylabel('Amplitud')
plt.title('Actividad muscular')
plt.figure()
plt.plot(t, MMG, 'r')

#--------------lectura de archivos txt--------------

#--------------creacion de archivos txt--------------
archi = open('new.txt', 'w')
filtered = lowess(EMG, t, is_sorted=True, frac=0.003, it=0, return_sorted=False)
print('Esto es un mensaje diferente: ', filtered[2])
plt.figure()
plt.plot(t, EMG, 'k', t, filtered, 'r')
plt.show()
#--------------creacion de archivos txt--------------
for i in range(len(filtered)):
    archi.write(str(filtered[i]) + '\n')

