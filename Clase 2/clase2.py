import matplotlib.pyplot as plt
fig,ax=plt.subplots()
# type(ax)
# Color de fondo
ax.set_facecolor('lightcoral')
# Color de los bordes:
for axis in ['top', 'bottom', 'left', 'right']:
 ax.spines[axis].set_color('darkviolet')
plt.show()