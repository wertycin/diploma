import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
plt.rcParams["figure.figsize"] = (8,2)
plt.rcParams["figure.dpi"] = 100
plt.rcParams['axes.grid'] = True
data = np.loadtxt('Карнуп упражнение 3.csv', delimiter=';')
x = data[:, 1]
t = data[:, 0]
import time

for i in range(10):
    plt.close()
    plt.xlim(t[100*i], t[200*i])
    plt.plot(t[100*i:200*i], x[100*i:200*i])
    plt.show()
    time.sleep(1)