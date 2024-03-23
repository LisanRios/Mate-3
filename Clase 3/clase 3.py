# import numpy as np
# from IPython.display import Audio, display
# import warnings
# warnings.simplefilter("ignore")

# #cantidad de puntos por segundo
# framerate = 44100

# # Definición ajustada de la función para generar una onda senoidal
# def simple_wave(f, duration, framerate, A = 1):
#     '''
#     Función para crear una onda senoidal.
#     inputs:
#     f = frecuencia en Hz, int
#     duration = duración en segundos, int o float
#     framerate = cantidad de puntos de muestreo por segundo, int
#     A = amplitud de la onda, float o int (opcional)
#     return:
#     wave = onda senoidal, np.array
#     '''
#     t = np.linspace(0, duration, int(framerate*duration))  # Genera el arreglo de tiempo correctamente
#     return A * np.sin(2*np.pi*f*t)  # Usa la amplitud A

# # Ejemplo de generación de onda
# la440 = simple_wave(440, 5, framerate)
# Audio(data=la440, rate=framerate)#Para reproducir audio en Jupyter N.
# import numpy as np
# from IPython.display import Audio, display
# from scipy.fft import fft, fftshift
# import warnings
# warnings.simplefilter("ignore")
# #cantidad de puntos por segundo
# framerate = 44100
# #cinco segundos de audio
# t = np.linspace(0,5,framerate*5)
# f = 440
# data = np.sin(2*np.pi*f*t)
# # data
# def simple_wave(f, t, framerate, A = 1):
#  '''Funcion para crear una onda senoidal
#  inputs:
#  f = frecuencia, int
#  t = tiempo, int
#  A = amplitud, int
#  return:
#  wave = onda senoidal, np.array
#  '''
#  t = np.linspace(0, t, framerate*t)
#  return np.sin(2*np.pi*f*t)
# la440 = simple_wave(440, 5, 44100)
# Audio(data=la440, rate=44100)

########################################
# Ejercicios:
# 1. Crear un arreglo de 10 cincos.
# 2. Generar un número aleatorio entre 0 y 1
# 3. Crear un arreglo con todos los números pares del 10 al 50
# 4. Generar un arreglo de 25 números aleatorioas con una distribución normal.
# 5. Convertir el array anterior en una matriz de 5 x 5.
# import numpy as np

# x = np.full((10,), fill_value = '5')
# print(x)

# v=np.random.randint(low = 0, high = 2, size = 1)
# for elemento in v:
#  print(elemento, end=' ')

# num = np.arange(10, 51, 2, dtype=int)
# print(num)

# v_norm = np.random.randn(25)
# print(v_norm)

# v_norm.shape = (5,5)
# print(v_norm)
# print(v_norm.ndim)

# Ejercicios:
# 1. Generar un array aleatorio de 15 números enteros.
# 2. Agregar el valor 0 en la posición 5
# 3. Generar un array de 4 números enteros y agregalo al array del punto 1
# 4. Generar un array de 20 elementos enteros, une éste con el anterior en un nuevo eje.
# 5. Suma los elementos de ambos arrays.

# import numpy as np

# v1=np.random.randint(low = 0, high = 10, size = 15)
# print(v1)

# v1 = np.insert(v1, 4, 0)
# print(v1)

# v2=np.random.randint(low = 0, high = 10, size = 4)
# new_v = np.append(v1, v2)
# print(v2)
# print(new_v)

# v3=np.random.randint(low = 0, high = 10, size = 20)
# juntos1 = np.stack((new_v, v3), axis=0)
# print(juntos1)

# print("Suma de arrays:\n", new_v + v3)

# Ejercicios:
# 1. Generar una matriz con una distribución normal de 3 por 4.
# 2. Agregar una nueva columna y una fila a la matriz anterior.
# 3. Generar otra matriz con la mismas dimensiones de la anterior y concatena ambas.
# 4. Apilar las matrices horizontalmente.


# import numpy as np

# m1 = np.random.randint(100, size=(3, 4))
# print(m1)

# m1 = np.append(m1, [[400], [800], [260]], axis = 1)
# m1 = np.append(m1, [[50, 60, 70, 70, 70]], axis = 0)
# print(m1)

# m2 = np.random.randint(100, size=(4, 5))
# print(m2)
# print(f"Concatenar a lo largo del primer eje:\n{np.concatenate([m1, m2])}")

# print(f"Mezcla Horizontal:\n {np.hstack((m1, m2))}")

import matplotlib
import matplotlib.pyplot as plt
from nbclient import NotebookClient
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
def update_line(num, data, line):
 line.set_data(data[...,:num])
 return line,
fig1 = plt.figure()
fig1.set_size_inches(5,3)
data = np.random.rand(2, 25)
l, = plt.plot([], [], 'b-')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Animación simple')
line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l), interval=50, blit=True)
plt.show()