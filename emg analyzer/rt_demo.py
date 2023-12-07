# Блок подключаемых библиотек
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np

# Блок настройки визуального отображения графиков
plt.rcParams["figure.figsize"] = (8,2)
plt.rcParams["figure.dpi"] = 100
plt.rcParams['axes.grid'] = True

# Функция анимации
def animation(width=10, shift=1, frames=20, min_y = -1, max_y=1):
    global frames_per_second
    def animate(i):
        data = np.loadtxt('Карнуп упражнение 3 copy.csv', delimiter=';')
        x = data[:, 1]
        t = data[:, 0]
        l.set_data(t[i:i+width+1], x[i:i+width+1])
        ax.set_xlim(t[i], t[i+width])
        ax.set_ylim(min_y, max_y)
    return matplotlib.animation.FuncAnimation(fig, animate, frames=np.arange(frames)*shift, interval = 1000/frames_per_second)

# Блок инициализации данных


# Блок инициализации окна
fig, ax = plt.subplots()
l, = ax.plot([],[])
# Функция интерактивности

def on_key(event):
    global interval
    if event.key == 'left':
        ani.event_source.stop()
    elif event.key == 'right':
        ani.event_source.start()
    elif event.key == 'up':
        interval = max(1, interval - 10)
        ani.event_source.interval = interval
    elif event.key == 'down':
        interval += 10
        ani.event_source.interval = interval

# Обработка событий клавиш
fig.canvas.mpl_connect('key_press_event', on_key)

frames_per_second = 10
interval = 1000/frames_per_second

ani = animation(width=200, shift=5, frames=1000, min_y = 0, max_y=5000)
plt.show()