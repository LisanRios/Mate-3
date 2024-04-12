# Ejercicios:
# 1. Crear un objeto Serie con 10 elementos aleatorios. Luego, convertir el objeto Series creado, en una lista Python.
# 2. Aplica las operaciones aritméticas básicas sobre 2 objetos Series.
#  serie1 = pd.Series([1, 2, 3, 4, 5])
#  serie2 = pd.Series([9, 8, 7, 6, 5])
# 3. Usa operadores relacionales para comparar los objetos Series creados en el anterior.
# 4. Cambia el tipo de datos de un objeto Series a número.
#  datos = pd.Series(['100', '200', 'python', '300.15', '500.8'])

# import pandas as pd
# import numpy as np

# s = pd.Series(np.random.randn(10))
# print(s)

# serie1 = pd.Series([1, 2, 3, 4, 5])
# serie2 = pd.Series([9, 8, 7, 6, 5])
# ari = serie1 + serie2
# print(ari)

# ari = serie1 == serie2
# print(ari)

# datos = pd.Series(['100', '200', 'python', '300.15', '500.8'])
# datos = pd.to_numeric(datos, errors="coerce")
# print(datos)

# Ejercicio:
# 1. Construir un programa que pregunte al usuario un rango de días -datos de tipo entero- (el usuario
# debe ingresar el día inicial y día final), luego pida las ventas de cada día y por último emita por
# pantalla una serie con los datos de las ventas indexada por los días, antes y después de aplicarles
# un descuento del 10%.

# import pandas as pd
# import numpy as np

# dia_inicial = int(input("Por favor, ingresa el día inicial: "))
# dia_final = int(input("Por favor, ingresa el día final: "))

# datos_ventas = {}

# for dia in range(dia_inicial, dia_final + 1):
#     ventas = float(input(f"Por favor, ingresa las ventas para el día {dia}: "))
#     datos_ventas[dia] = ventas

# serie_ventas = pd.Series(datos_ventas)

# print("Datos de ventas:")
# print(serie_ventas)

# ventas_descuento = serie_ventas * 0.9
# print("Datos de ventas con descuento:")
# print(ventas_descuento)

# Ejercicios:
# 1. Escribir una función que reciba un diccionario con las notas de 5 alumnos de un curso
# y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.
#  notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
# 2. Escribir una función que reciba el diccionario dado en el punto anterior y devuelva una serie
# con las notas de los alumnos aprobados ordenadas de mayor a menor.

# import pandas as pd
# import numpy as np

# notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
# s1 = pd.Series(notas)
# print("Datos de notas:")
# print(s1)
# nota_max = notas.max()

import pandas as pd
import numpy as np

rng = np.random.RandomState(0)
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
 'data1': range(6), 'data2': rng.randint(0, 10, 6)},
 columns = ['key', 'data1', 'data2'])

print(df)

df.groupby('key').aggregate(['min', np.median, max])
print(df)





