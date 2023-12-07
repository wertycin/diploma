import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pyautogui

# Инициализация графика
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

# Функция обновления графика
def update(frame):
    line.set_ydata(np.sin(x + frame / 10))
    return line,

# Параметры анимации
frames = 200
interval = 50
blit = True

# Создание анимации
ani = FuncAnimation(fig, update, frames=frames, interval=interval, blit=blit)

# Обработка событий клавиш
def on_key(event):
    if event.name == 'left':
        if ani.running:
            ani.event_source.stop()
    elif event.name == 'right':
        if not ani.running:
            ani.event_source.start()
    elif event.name == 'up':
        ani.event_source.interval = max(1, ani.event_source.interval - 10)
    elif event.name == 'down':
        ani.event_source.interval += 10

# Обработка событий клавиш в реальном времени
pyautogui.on_press(on_key)

# Добавленная строка для отображения окна
plt.show()
