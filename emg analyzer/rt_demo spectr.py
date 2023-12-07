# Блок подключаемых библиотек
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import scipy.signal as sg
import time
from cycler import cycler
# Блок настройки визуального отображения графиков
plt.rcParams["figure.figsize"] = (8, 2)
plt.rcParams["figure.dpi"] = 100
plt.rcParams['axes.grid'] = False
plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14
#plt.rcParams['axes.prop_cycle'] = cycler('color', ['orange'])
# Функция анимации
def animation(width=10, shift=1, frames=20, min_y = -1, max_y=1, fs = 500, frames_per_second = 10):
    data = np.loadtxt('Карнуп упражнение 4.csv', delimiter=';')
    print('data_loaded')
    def animate(i):
        # data = np.loadtxt('Карнуп упражнение 3 copy.csv', delimiter=';')
        
        x = data[:, 1]
        t = data[:, 0]
        if i+width+1 > len(x):
            return 
        start_time = time.time()
        x_slc = x[i:i+width+1]
        t_slc = t[i:i+width+1]
        l.set_data(t_slc, x_slc)
        ax.set_xlim(t_slc[0], t_slc[width])
        ax.set_ylim(min_y, max_y)
        ax.set_xticks([t_slc[0], t_slc[width]], [t_slc[0], t_slc[width]])
        end_time = time.time()
        n = len(x_slc)
        k = np.arange(n)
        T = n / fs
        frq = k / T  # двусторонний спектр
        frq = frq[:n//2]  # односторонний спектр

        X = np.fft.fft(x_slc)/n  # вычисление комплексных амплитуд
        X = X[:n//2]
        s.set_data(frq, abs(X))
        sx.set_xlim(frq.min(), frq.max())
        sx.set_ylim(0, 200)
        print(f"Время выполнения: {i, start_time-end_time} секунд")
    return matplotlib.animation.FuncAnimation(fig, animate, frames=np.arange(frames)*shift, interval = 1000/frames_per_second)

# Блок инициализации данных


# Блок инициализации окна
plt.style.use('seaborn-v0_8-darkgrid')
fig, (ax, sx) = plt.subplots(2, 1)
plt.subplots_adjust(hspace=0.5)
ax.grid(axis='y', linestyle='--', color='gray')
ax.set_title('ЭМГ сигнал')
ax.set_xlabel('Время')
ax.set_ylabel('Амплитуда')
sx.set_title('Спектр')
sx.set_xlabel('Частота, Гц')
sx.set_ylabel('Амплитуда')
l, = ax.plot([],[])
s, = sx.plot([],[])


ani = animation(width=500, shift=30, frames=1000, min_y = -1000, max_y=4000, fs = 500, frames_per_second=10)
plt.show()