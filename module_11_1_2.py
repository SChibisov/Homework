import numpy as np
import matplotlib.pyplot as plt

# определение поверхности и осей
x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
y = x.copy().T
z = np.cos(x ** 2 + y ** 3)

fig = plt.figure()

# построения графиков 3D графика
ax = plt.axes(projection='3d')

# Построение графиков
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='green')
ax.set_title('Surface plot geeks for geeks')
plt.show()
