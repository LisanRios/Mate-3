# De 1000 televidentes encuestados se obtiene la siguiente información:
# 
# a)
#     391 ven programas deportivos y los datos se han recolectado en un diccionario: 
#         {"Voleybol": 10, "Hockey": 87,  "Equitacion":23, "Ciclismo":81, "Esqui":11, "Futbol": 45, "Tenis": 37,
#         "Rugby": 9, "Basquetbol": 7, "Boxeo": 6, "Natacion":75}
#     
#     230 ven programas cómicos y los datos se han recolectado en una tupla:
#         (41,29,58,4,45,37,9,7)
#     
#     545 ven programas sobre mundo animal y los datos se han recolectado en una lista:
#         [65,14,25,29,12,1,17,18,45,37,6,41,19,8,2,90,103,13]
# 
# b) 
# Por otra parte, se sabe que:
#     98 ven programas cómicos y deportivos
#     152 ven programas cómicos y de mundo animal
#     88 ven programas deportivos y de mundo animal
#     90 no ven ninguno de esos programas
# 
# c)
# Resolver y responder:
#     1. Cuántos entrevistados ven los 3 tipos de programas?
#     2. Cuántos entrevistados sólo lo ven deportivos y cómicos?
#     3. Cuántos entrevistados ven sólo cómicos y mundo animal?
#     4. Cuántos entrevistados ven sólo deportivos y mundo animal?
#     5. Cuántos entrevistados ven sólo deportes?
#     6. Cuántos entrevistados ven sólo cómicos?
#     7. Cuántos entrevistados ven sólo mundo animal? 
#     8. Cuántos entrevistados ven 2 de las 3 categorías?
# 
# d) Graficar con matplotlib_venn
# 
# Nota: 
# 
# El ejercicio debe resolverse con variables, estructuras, operaciones de conjuntos, funciones propias y del lenguaje, etc. No se admiten valores literales, salvo en el caso de la asignación del valor universal y en las inicializaciones de variables.
from matplotlib import pyplot as plt
from matplotlib_venn import *
from matplotlib.patches import Circle

# Total de entrevistados
total_entrevistados = 1000

# Números individuales de cada categoría
deportivos = 391
comicos = 230
mundo_animal = 545

# Intersecciones de dos categorías
deportivos_comicos = 98
comicos_mundo_animal = 152
deportivos_mundo_animal = 88

# Ninguno de esos programas
ninguno = 90

tres_tipos = total_entrevistados - ninguno - (deportivos + comicos + mundo_animal - deportivos_comicos - deportivos_mundo_animal - comicos_mundo_animal)

from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# Cálculo previo (a completar con el código)
tres_tipos = total_entrevistados - ninguno - (deportivos + comicos + mundo_animal - deportivos_comicos - deportivos_mundo_animal - comicos_mundo_animal)
solo_deportivos_comicos = deportivos_comicos - tres_tipos
solo_comicos_mundo_animal = comicos_mundo_animal - tres_tipos
solo_deportivos_mundo_animal = deportivos_mundo_animal - tres_tipos
solo_deportivos = deportivos - solo_deportivos_comicos - solo_deportivos_mundo_animal - tres_tipos
solo_comicos = comicos - solo_deportivos_comicos - solo_comicos_mundo_animal - tres_tipos
solo_mundo_animal = mundo_animal - solo_comicos_mundo_animal - solo_deportivos_mundo_animal - tres_tipos

# Dibujo del diagrama de Venn
plt.figure(figsize=(7, 7))


venn = venn3(subsets=(solo_deportivos, solo_comicos, solo_deportivos_comicos, solo_mundo_animal, solo_deportivos_mundo_animal, solo_comicos_mundo_animal, tres_tipos),
             set_labels=('Deportivos', 'Cómicos', 'Mundo Animal'))
plt.title("Diagrama de Venn de Preferencias de Programas de Televisión")
plt.show()
